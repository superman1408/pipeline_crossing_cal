import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import csv
from pipeline_simulation import Ui_MainWindow
from pipeline_calculation import calculate_pipeline_crossing, calculate_bored_diameter_value
import traceback
import os
from report_generator import generate_pipeline_report 

global_app_info = {
    "username": "Guest User", # Default until launcher populates it
    "project_name": "Untitled Project (Initial)", # Default until launcher populates it
}

class PipelineSimulationApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.current_file_path = None
        
        # --- Initialize dynamic User and Project Info from global_app_info ---
        self._logged_in_username = global_app_info.get("username", "Guest User")
        self._current_project_title = global_app_info.get("project_name", "Untitled Project (Initial)")
        self.setWindowTitle(f"Pipeline Crossing Simulation - {self._current_project_title}")
        
        self.steel_grade_smys = 0
        # Output fields (to be cleared by 'new' and 'reset', and are read-only)
        self._output_field_names = [
            "lineEdit_6PipeWallThickness_including_CA",
            "lineEdit_6Boreddiameter",
            "lineEdit_33barlowStress",                   
            "lineEdit_35StressDuetoEarthLoad",          
            "lineEdit_34_CyclicCircumferentialStress",  
            "lineEdit_36CyclicLongitudinalStress",      
            "lineEdit_30radial_stress",                 
            "lineEdit_38Circumferential_stress",        
            "lineEdit_39Longitudinal_stress",           
            "lineEdit_40Effective_stresses",            
        ]

        # These are the fields whose values are reset to defaults by 'reset'
        self._input_line_edit_names = [
            'lineEdit_Pipe_outside_diameter', 'lineEdit_2_pipe_wall_thickness',
            'lineEdit_3_SMYS',
            'lineEdit_5_Depth_of_Cover', 'lineEdit_4_Corrossion_Allowance',
            'lineEdit_6operatingpressure', 'lineEdit_6operating_temperature',
            'lineEdit_6impactfactor', 'lineEdit_6Design_wheel_load_from_single_axle',
            'lineEdit_6soilunitweight', 'lineEdit_6designfactor',
            'Design_wheel_load_from_tandem_axle_2', 'lineEdit_6Modulus_of_soil_reaction',
            'lineEdit_6longitudinaljointfactor', 'lineEdit_6youngs_modulus',
            'lineEdit_6resilient_modulus', 'lineEdit_6installation_temperature',
            'lineEdit_6poissons_ratio', 'lineEdit_37Coefficient_Of_Thermal_Expansion',
            'lineEdit_21EarthLoadStiffnessFactor', 'lineEdit_22EarthLoadBurialFactor',
            'lineEdit_23EarthLoadExcavationFactor',
            'lineEdit_27StiffnessFactorKHh', 'lineEdit_25_GeometryFactorGHh',
            'lineEdit_29_StifnessFactorKLh', 'lineEdit_28geometryFactorGLh',
            'lineEdit_26RoadAxleConfigurationFactor', 'lineEdit_24RoadPavementFactor',
            'lineEdit_31FatigueEnduranceofGirthYield', 'lineEdit_32FatigueEnduranceofLongitudinalWeld',
        ]
        self._input_combo_box_names = [
            'comboBox_2_pipe_type', 'comboBox_3_Soil_Type', 'comboBox_5_Bored_Diameter',
            'comboBox_Streel_grade', 'comboBox_4_Codes_and_standards',
        ]

        # Connect signals
        self.Start.clicked.connect(self.on_start_button_clicked)
        self.actionExit.triggered.connect(self.close)
        self.actionNew.triggered.connect(self.handle_new)
        self.actionOpen.triggered.connect(self.handle_open)
        self.actionSave_As.triggered.connect(self.handle_save_as)
        self.actionReset.triggered.connect(self.handle_reset)
        self.actionGenerate_Report.triggered.connect(self.handle_generate_report)
        self.actionWhat_s_New.triggered.connect(self.handle_whats_new)
        self.actionDocumentation.triggered.connect(self.handle_documentation)

        self.setup_output_fields_style()
        self.set_initial_input_values() # Populates initial values for input fields
        
        # Connect signals for dynamic updates
        self.comboBox_5_Bored_Diameter.currentIndexChanged.connect(self.update_bored_diameter_display)
        self.lineEdit_Pipe_outside_diameter.textChanged.connect(self.update_bored_diameter_display)
        self.comboBox_Streel_grade.currentIndexChanged.connect(self.on_steel_grade_changed)
        
        # Initial updates
        self.update_bored_diameter_display()
        self.on_steel_grade_changed(self.comboBox_Streel_grade.currentIndex()) 
        
        self.last_calculation_results = {}
        self.last_input_data = {}

    def setup_output_fields_style(self):
        """Sets output fields to read-only and clears any explicit background style."""
        for name in self._output_field_names:
            field = getattr(self, name)
            field.setReadOnly(True)
            field.setStyleSheet("") 


    def set_initial_input_values(self):
        """Sets the default initial values for all input fields."""
        self.comboBox_2_pipe_type.setCurrentText("SMLS")
        self.comboBox_3_Soil_Type.setCurrentText("Soft to medium clay")
        self.comboBox_5_Bored_Diameter.setCurrentText("Considered")
        self.comboBox_Streel_grade.setCurrentText("Fe 330") 
        self.comboBox_4_Codes_and_standards.setCurrentText("API 1102")
        self.lineEdit_Pipe_outside_diameter.setText("1016")
        self.lineEdit_2_pipe_wall_thickness.setText("10")
        self.lineEdit_3_SMYS.setText("195") 
        self.lineEdit_5_Depth_of_Cover.setText("1.5")
        self.lineEdit_4_Corrossion_Allowance.setText("0")
        self.lineEdit_6operatingpressure.setText("0")
        self.lineEdit_6operating_temperature.setText("40")
        self.lineEdit_6impactfactor.setText("1.5")
        self.lineEdit_6Design_wheel_load_from_single_axle.setText("53.4")
        self.lineEdit_6soilunitweight.setText("18.9")
        self.lineEdit_6designfactor.setText("0.72")
        self.Design_wheel_load_from_tandem_axle_2.setText("44.5")
        self.lineEdit_6Modulus_of_soil_reaction.setText("3.4")
        self.lineEdit_6longitudinaljointfactor.setText("1")
        self.lineEdit_6youngs_modulus.setText("210000")
        self.lineEdit_6resilient_modulus.setText("34")
        self.lineEdit_6installation_temperature.setText("65")
        self.lineEdit_6poissons_ratio.setText("0.30")
        self.lineEdit_37Coefficient_Of_Thermal_Expansion.setText("1.44e-5")
        self.lineEdit_21EarthLoadStiffnessFactor.setText("6330")
        self.lineEdit_22EarthLoadBurialFactor.setText("0.47")
        self.lineEdit_23EarthLoadExcavationFactor.setText("0.91")
        self.lineEdit_27StiffnessFactorKHh.setText("19.8")
        self.lineEdit_25_GeometryFactorGHh.setText("0.70")
        self.lineEdit_29_StifnessFactorKLh.setText("14.8")
        self.lineEdit_28geometryFactorGLh.setText("0.64")
        self.lineEdit_26RoadAxleConfigurationFactor.setText("1")
        self.lineEdit_24RoadPavementFactor.setText("1")
        self.lineEdit_31FatigueEnduranceofGirthYield.setText("82.737")
        self.lineEdit_32FatigueEnduranceofLongitudinalWeld.setText("158.57")
        
        # Ensure all input fields have white background and default border
        self.reset_input_field_styles_to_white() 


    def reset_input_field_styles_to_white(self):
        """Sets the background style for all input LineEdit widgets to white."""
        for name in self._input_line_edit_names:
            field = getattr(self, name)
            field.setStyleSheet("background-color: white; border: 1px solid gray;")


    def _validate_and_get_float_input(self, line_edit_widget, input_data_key, input_data_dict, has_error_flag_list):
        text = line_edit_widget.text()
        try:
            value = float(text)
            input_data_dict[input_data_key] = value
            line_edit_widget.setStyleSheet("background-color: white; border: 1px solid gray;")
            return False
        except ValueError:
            line_edit_widget.setStyleSheet("background-color: white; border: 2px solid red;")
            has_error_flag_list[0] = True
            return True


    def update_bored_diameter_display(self):
        try:
            pipe_outside_diameter_text = self.lineEdit_Pipe_outside_diameter.text()
            if not pipe_outside_diameter_text: # Handle empty input gracefully
                self.lineEdit_6Boreddiameter.clear()
                self.lineEdit_6Boreddiameter.setStyleSheet("")
                self.lineEdit_Pipe_outside_diameter.setStyleSheet("background-color: white; border: 1px solid gray;") # Clear error if it was there
                return

            pipe_outside_diameter = float(pipe_outside_diameter_text)
            self.lineEdit_Pipe_outside_diameter.setStyleSheet("background-color: white; border: 1px solid gray;")
            bored_diameter_option = self.comboBox_5_Bored_Diameter.currentText()
            calculated_bored_diameter = calculate_bored_diameter_value(pipe_outside_diameter, bored_diameter_option)
            self.lineEdit_6Boreddiameter.setText(f"{calculated_bored_diameter:.3f}")
            # Ensure output field does not have white background
            self.lineEdit_6Boreddiameter.setStyleSheet("") 
        except ValueError:
            self.lineEdit_Pipe_outside_diameter.setStyleSheet("background-color: white; border: 2px solid red;")
            self.lineEdit_6Boreddiameter.clear()
            self.lineEdit_6Boreddiameter.setStyleSheet("") # Clear any error style
        except Exception as e:
            print(f"Error updating bored diameter: {e}")
            self.lineEdit_Pipe_outside_diameter.setStyleSheet("background-color: white; border: 2px solid red;")
            self.lineEdit_6Boreddiameter.clear()
            self.lineEdit_6Boreddiameter.setStyleSheet("")


    def on_steel_grade_changed(self, index):
        steel_grade_text = self.comboBox_Streel_grade.currentText()
        smys_values = {
            "Fe 330": 195, "A25": 172.3689, "A": 206.8427, "B": 241.3165,
            "X42": 289.5798, "X46": 317.1588, "X52": 358.5274, "X56": 386.1064,
            "X60": 413.6854, "X65": 448.1592, "X70": 482.633, "X80": 551.5806,
        }
        self.steel_grade_smys = smys_values.get(steel_grade_text, 0)
        if self.steel_grade_smys != 0:
            self.lineEdit_3_SMYS.setText(str(self.steel_grade_smys))
        elif steel_grade_text not in smys_values: # Unknown steel grade but SMYS is 0
            self.lineEdit_3_SMYS.setText("") # Ensure it's blank if unknown
            QtWidgets.QMessageBox.warning(self, "Input Warning", f"Unknown Steel Grade: {steel_grade_text}. SMYS will be blank.")
            self.lineEdit_3_SMYS.setStyleSheet("background-color: white; border: 2px solid orange;")
        else: # SMYS is 0 for a known grade, or it's the default "Fe 330" when clearing
            self.lineEdit_3_SMYS.setText("") # Set to blank as requested

        # Apply normal styling if not an unknown steel grade causing a warning
        if self.steel_grade_smys != 0 or steel_grade_text in smys_values:
            self.lineEdit_3_SMYS.setStyleSheet("background-color: white; border: 1px solid gray;")
        
        print(f"Steel Grade selected: {steel_grade_text}, SMYS set to: {self.steel_grade_smys} MPa")


    def on_start_button_clicked(self):
        self.reset_input_field_styles_to_white()
        self.clear_output_fields() # Use the specific output clearing function
        self.clear_radio_buttons() # Clear radio buttons specifically

        input_data = {}
        has_overall_error = [False]
        print("\n--- Reading Input Values from GUI ---")
        try:
            # For combo boxes, ensure we get the text even if it's the default or cleared state
            input_data["Steel_grade"] = self.comboBox_Streel_grade.currentText()
        except Exception as e:
            print(f"Error getting Steel Grade text: {e}")
            has_overall_error[0] = True
            self.comboBox_Streel_grade.setStyleSheet("border: 2px solid red;")
        
        # Populate input_data for calculation from all input fields
        for name in self._input_combo_box_names:
            if name != "comboBox_Streel_grade": 
                # Convert objectName to a suitable key name for calculation function
                input_data[name.replace('comboBox_', '').replace('_', ' ').title().replace(' ', '_')] = getattr(self, name).currentText()

        for name in self._input_line_edit_names:
            field_widget = getattr(self, name)
            if not field_widget.text(): # If field is blank, treat as missing/invalid for calculation
                field_widget.setStyleSheet("background-color: white; border: 2px solid red;")
                has_overall_error[0] = True
                print(f"Error: Input field '{name}' is blank. Please enter a value.")
                continue 
            # If not blank, proceed with validation and conversion
            if name == 'lineEdit_Pipe_outside_diameter': self._validate_and_get_float_input(field_widget, "Pipe_Outside_Diameter", input_data, has_overall_error)
            elif name == 'lineEdit_2_pipe_wall_thickness': self._validate_and_get_float_input(field_widget, "Pipe_Wall_Thickness", input_data, has_overall_error)
            elif name == 'lineEdit_3_SMYS': self._validate_and_get_float_input(field_widget, "Specified_Minimum_Yield_Strength", input_data, has_overall_error)
            elif name == 'lineEdit_5_Depth_of_Cover': self._validate_and_get_float_input(field_widget, "Depth_of_Cover", input_data, has_overall_error)
            elif name == 'lineEdit_4_Corrossion_Allowance': self._validate_and_get_float_input(field_widget, "Corrosion_Allowance", input_data, has_overall_error)
            elif name == 'lineEdit_6operatingpressure': self._validate_and_get_float_input(field_widget, "Operating_Pressure", input_data, has_overall_error)
            elif name == 'lineEdit_6operating_temperature': self._validate_and_get_float_input(field_widget, "Operating_Temperature", input_data, has_overall_error)
            elif name == 'lineEdit_6impactfactor': self._validate_and_get_float_input(field_widget, "Impact_Factor", input_data, has_overall_error)
            elif name == 'lineEdit_6Design_wheel_load_from_single_axle': self._validate_and_get_float_input(field_widget, "Design_Wheel_Load_From_Single_Axle", input_data, has_overall_error)
            elif name == 'lineEdit_6soilunitweight': self._validate_and_get_float_input(field_widget, "Soil_Unit_Weight", input_data, has_overall_error)
            elif name == 'lineEdit_6designfactor': self._validate_and_get_float_input(field_widget, "Design_Factor", input_data, has_overall_error)
            elif name == 'Design_wheel_load_from_tandem_axle_2': self._validate_and_get_float_input(field_widget, "Design_Wheel_Load_From_Tandem_Axle", input_data, has_overall_error)
            elif name == 'lineEdit_6Modulus_of_soil_reaction': self._validate_and_get_float_input(field_widget, "Modulus_of_Soil_Reaction", input_data, has_overall_error)
            elif name == 'lineEdit_6longitudinaljointfactor': self._validate_and_get_float_input(field_widget, "Longitudinal_Joint_Factor", input_data, has_overall_error)
            elif name == 'lineEdit_6youngs_modulus': self._validate_and_get_float_input(field_widget, "Youngs_Modulus", input_data, has_overall_error)
            elif name == 'lineEdit_6resilient_modulus': self._validate_and_get_float_input(field_widget, "Resilient_Modulus", input_data, has_overall_error)
            elif name == 'lineEdit_6installation_temperature': self._validate_and_get_float_input(field_widget, "Installation_Temperature", input_data, has_overall_error)
            elif name == 'lineEdit_6poissons_ratio': self._validate_and_get_float_input(field_widget, "Poissons_Ratio", input_data, has_overall_error)
            elif name == 'lineEdit_37Coefficient_Of_Thermal_Expansion': self._validate_and_get_float_input(field_widget, "Coefficient_of_Thermal_Expansion", input_data, has_overall_error)
            elif name == 'lineEdit_21EarthLoadStiffnessFactor': self._validate_and_get_float_input(field_widget, "Earth_Load_Stiffness_Factor", input_data, has_overall_error)
            elif name == 'lineEdit_22EarthLoadBurialFactor': self._validate_and_get_float_input(field_widget, "Earth_Load_Burial_Factor", input_data, has_overall_error)
            elif name == 'lineEdit_23EarthLoadExcavationFactor': self._validate_and_get_float_input(field_widget, "Earth_Load_Excavation_Factor", input_data, has_overall_error)
            elif name == 'lineEdit_27StiffnessFactorKHh': self._validate_and_get_float_input(field_widget, "Stiffness_Factor_KHh", input_data, has_overall_error)
            elif name == 'lineEdit_25_GeometryFactorGHh': self._validate_and_get_float_input(field_widget, "Geometry_Factor_GHh", input_data, has_overall_error)
            elif name == 'lineEdit_29_StifnessFactorKLh': self._validate_and_get_float_input(field_widget, "Stiffness_Factor_KLh", input_data, has_overall_error)
            elif name == 'lineEdit_28geometryFactorGLh': self._validate_and_get_float_input(field_widget, "Geometry_Factor_GLh", input_data, has_overall_error)
            elif name == 'lineEdit_26RoadAxleConfigurationFactor': self._validate_and_get_float_input(field_widget, "Road_Axle_Configuration_Factor", input_data, has_overall_error)
            elif name == 'lineEdit_24RoadPavementFactor': self._validate_and_get_float_input(field_widget, "Road_Pavement_Type_Factor", input_data, has_overall_error)
            elif name == 'lineEdit_31FatigueEnduranceofGirthYield': self._validate_and_get_float_input(field_widget, "Fatigue_endurance_Limit_of_Girth_yield", input_data, has_overall_error)
            elif name == 'lineEdit_32FatigueEnduranceofLongitudinalWeld': self._validate_and_get_float_input(field_widget, "Fatigue_endurance_Limit_of_Longitudinal_Weld", input_data, has_overall_error)

        self.last_input_data = input_data.copy()
        
        print("\n--- Input Values ---")
        for key, value in input_data.items():
            print(f"{key}: {value}")
        print("--------------------")
        
        print(f"DEBUG: Current User (before calc): {self._logged_in_username}")
        print(f"DEBUG: Current Project Title (before calc): {self._current_project_title}")

        if has_overall_error[0]:
            QtWidgets.QMessageBox.critical(self, "Input Error", "Please correct the highlighted fields and ensure no required fields are blank with valid numeric inputs.")
            return

        try:
            results = calculate_pipeline_crossing(input_data)
            print("\n--- Calculation Results ---")
            for key, value in results.items():
                if "Check" in key or key in [
                    "Barlow_Stress", "Stress_due_to_Earth_Load",
                    "Cyclic_Circumferential_Stress", "Cyclic_Longitudinal_Stress",
                    "Circumferential_Stress_S1", "Longitudinal_Stress_S2",
                    "Effective_Stress_Seff", "Radial_Stress",
                    "Pipe_Wall_Thickness_Including_CA", "Bored_Diameter"
                ]:
                    print(f"{key}: {value}")
            print("\n--- Criteria Checks ---")
            print(f"Barlow Stress Check: {results.get('Barlow_Stress_Check', 'N/A')}")
            print(f"Principal Stress Check: {results.get('Principal_Stress_Check', 'N/A')}")
            print(f"Girth Weld Criteria Check: {results.get('Girth_Weld_Criteria_Check', 'N/A')}")
            print(f"Longitudinal Weld Criteria Check: {results.get('Longitudinal_Weld_Criteria_Check', 'N/A')}")
            print("-----------------------")
            
            self.last_calculation_results = results.copy()
            
            # Update output fields with calculated results using the correct objectNames
            self.lineEdit_6PipeWallThickness_including_CA.setText(f"{results['Pipe_Wall_Thickness_Including_CA']:.3f}")
            self.lineEdit_6Boreddiameter.setText(f"{results['Bored_Diameter']:.3f}")
            self.lineEdit_30radial_stress.setText(f"{results['Radial_Stress']:.3f}") 
            self.lineEdit_33barlowStress.setText(f"{results['Barlow_Stress']:.3f}") 
            self.lineEdit_35StressDuetoEarthLoad.setText(f"{results['Stress_due_to_Earth_Load']:.3f}") 
            self.lineEdit_34_CyclicCircumferentialStress.setText(f"{results['Cyclic_Circumferential_Stress']:.3f}") 
            self.lineEdit_36CyclicLongitudinalStress.setText(f"{results['Cyclic_Longitudinal_Stress']:.3f}") 
            self.lineEdit_38Circumferential_stress.setText(f"{results['Circumferential_Stress_S1']:.3f}") 
            self.lineEdit_39Longitudinal_stress.setText(f"{results['Longitudinal_Stress_S2']:.3f}") 
            self.lineEdit_40Effective_stresses.setText(f"{results['Effective_Stress_Seff']:.3f}") 

            for name in self._output_field_names:
                getattr(self, name).setStyleSheet("")

            # Update radio button statuses
            self.update_radio_button_status(self.radioButton_7_safe, self.radioButton_8_not_safe, results['Barlow_Stress_Check'])
            self.update_radio_button_status(self.radioButton_6_safe, self.radioButton_5_not_safe, results['Principal_Stress_Check'])
            self.update_radio_button_status(self.radioButton_safe, self.radioButton_2_not_safe, results['Girth_Weld_Criteria_Check'])
            self.update_radio_button_status(self.radioButton_3_safe, self.radioButton_4_not_safe, results['Longitudinal_Weld_Criteria_Check'])
            
            QtWidgets.QMessageBox.information(self, "Calculation Complete", "Pipeline crossing calculations finished successfully!")
        
        except ZeroDivisionError:
            user_friendly_message = (
                "A calculation error occurred: "
                "Please check the 'Pipe Wall Thickness', 'Corrosion Allowance', and 'Pipe Outside Diameter' fields. "
            )
            QtWidgets.QMessageBox.critical(self, "Calculation Error", user_friendly_message)
            traceback.print_exc()
            self.clear_output_fields() # Clear outputs on error
            self.clear_radio_buttons()
            self.last_calculation_results = {}
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Calculation Error", f"An unexpected error occurred during calculation: {e}")
            print(f"An unexpected error occurred during calculation: {e}")
            traceback.print_exc()
            self.clear_output_fields() # Clear outputs on error
            self.clear_radio_buttons()
            self.last_calculation_results = {}


    def update_radio_button_status(self, safe_rb, not_safe_rb, status):
        """Sets the appropriate radio button based on the 'status' (Allowable/Not Allowable)."""
        if status == "Allowable":
            safe_rb.setChecked(True)
            not_safe_rb.setChecked(False)
        else:
            safe_rb.setChecked(False)
            not_safe_rb.setChecked(True)


    def clear_output_fields(self):
        """Clears all LineEdits that are identified as output fields."""
        for name in self._output_field_names:
            field = getattr(self, name)
            field.clear()
            field.setStyleSheet("") 
        self.clear_radio_buttons() # Also clear radio buttons when outputs are cleared
        self.last_calculation_results = {} # Clear results on output clear
    

    def clear_radio_buttons(self):
        """Clears all radio button selections."""
        # Temporarily make button groups non-exclusive to clear all
        self.buttonGroup.setExclusive(False)
        self.radioButton_safe.setChecked(False)
        self.radioButton_2_not_safe.setChecked(False)
        self.buttonGroup.setExclusive(True) 

        self.buttonGroup_2.setExclusive(False)
        self.radioButton_3_safe.setChecked(False)
        self.radioButton_4_not_safe.setChecked(False)
        self.buttonGroup_2.setExclusive(True)

        self.buttonGroup_3.setExclusive(False)
        self.radioButton_6_safe.setChecked(False)
        self.radioButton_5_not_safe.setChecked(False)
        self.buttonGroup_3.setExclusive(True)

        self.buttonGroup_4.setExclusive(False)
        self.radioButton_7_safe.setChecked(False)
        self.radioButton_8_not_safe.setChecked(False)
        self.buttonGroup_4.setExclusive(True)


    def get_all_input_values(self):
        """Retrieves current values from all input fields (LineEdits and ComboBoxes)."""
        data = {}
        for name in self._input_line_edit_names:
            widget = getattr(self, name)
            data[name] = widget.text()
        for name in self._input_combo_box_names:
            widget = getattr(self, name)
            data[name] = widget.currentText()
        return data
    

    def set_all_input_values(self, data):
        """Sets input field values from a dictionary, typically after loading a file."""
        self.clear_output_fields() # Always clear outputs when loading new inputs
        self.clear_input_fields_completely() # Clear all input fields before setting new ones

        for name in self._input_line_edit_names:
            widget = getattr(self, name)
            if name in data:
                widget.setText(data[name])
                widget.setStyleSheet("background-color: white; border: 1px solid gray;")
            else:
                widget.clear() # Clear if not found in data
                widget.setStyleSheet("background-color: white; border: 1px solid gray;")
                print(f"Warning: LineEdit '{name}' not found in loaded data. Clearing field.")
        
        for name in self._input_combo_box_names:
            widget = getattr(self, name)
            if name in data:
                index = widget.findText(data[name])
                if index != -1:
                    widget.setCurrentIndex(index)
                else:
                    widget.setCurrentIndex(0) # Fallback to first item if text not found
                    print(f"Warning: Value '{data[name]}' not found in ComboBox '{name}'. Resetting to first item.")
            else:
                widget.setCurrentIndex(0) # Clear/reset to first item if not found
                print(f"Warning: ComboBox '{name}' not found in loaded data. Resetting to first item.")
        
        self.update_bored_diameter_display() # Update dependent outputs
        # self.on_steel_grade_changed(self.comboBox_Streel_grade.currentIndex()) # Removed to prevent SMYS auto-population on load if not needed


    def clear_input_fields_completely(self):
        """Clears all input fields (LineEdits and ComboBoxes) without setting defaults."""
        for name in self._input_line_edit_names:
            field = getattr(self, name)
            field.clear()
            field.setStyleSheet("background-color: white; border: 1px solid gray;")
        for name in self._input_combo_box_names:
            field = getattr(self, name)
            field.setCurrentIndex(0) 


    def handle_new(self):
        """
        Clears all output fields AND all input fields, leaving inputs blank.
        Resets project title.
        """
        print("Action: New - Clearing all fields (outputs and inputs).")
        self.clear_output_fields() # Clear outputs and radio buttons
        self.clear_input_fields_completely() # This clears inputs to blank
        for name in self._input_combo_box_names:
            combo_box = getattr(self, name)
            combo_box.setCurrentIndex(0) # This will trigger signals if connected
        self.update_bored_diameter_display() 
        self.lineEdit_3_SMYS.clear() 
        self.lineEdit_3_SMYS.setStyleSheet("background-color: white; border: 1px solid gray;") # Clear any special styling


        self.current_file_path = None
        self._current_project_title = global_app_info.get("project_name", "Untitled Project (Initial)")
        self.setWindowTitle(f"Pipeline Crossing Simulation - {self._current_project_title}")
        QtWidgets.QMessageBox.information(self, "New Project", "All output and input fields cleared and left blank.")


    def handle_open(self):
        """Handles opening a project from a CSV file."""
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open Project", "", "CSV Files (*.csv);;All Files (*)"
        )
        if file_path:
            try:
                with open(file_path, 'r', newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    loaded_data = next(reader)
                self.set_all_input_values(loaded_data) # This will also clear outputs
                self.current_file_path = file_path
                self._current_project_title = self.get_project_name_from_path(file_path)
                self.setWindowTitle(f"Pipeline Crossing Simulation - {self._current_project_title}")
                QtWidgets.QMessageBox.information(self, "Open Project", f"Project data loaded successfully from:\n{file_path}")
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Open Error", f"File not found: {file_path}")
            except StopIteration:
                QtWidgets.QMessageBox.critical(self, "Open Error", f"CSV file is empty or has no data rows: {file_path}")
            except csv.Error as e:
                QtWidgets.QMessageBox.critical(self, "Open Error", f"Error reading CSV file: {file_path}\nDetails: {e}")
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Open Error", f"An unexpected error occurred while opening file:\n{e}")
                print(f"Error opening file: {traceback.format_exc()}")


    def handle_save_as(self):
        """Handles saving the current input data to a new CSV file."""
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save Project As", "pipeline_project.csv",
            "CSV Files (*.csv);;All Files (*)"
        )
        if file_path:
            if not file_path.lower().endswith('.csv'):
                file_path += '.csv'

            data_to_save = self.get_all_input_values()
            try:
                with open(file_path, 'w', newline='') as csvfile:
                    fieldnames = list(data_to_save.keys())
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerow(data_to_save)
                self.current_file_path = file_path
                self._current_project_title = self.get_project_name_from_path(file_path)
                self.setWindowTitle(f"Pipeline Crossing Simulation - {self._current_project_title}")
                QtWidgets.QMessageBox.information(self, "Save Project As", f"Project data saved successfully to:\n{file_path}")
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Save Error", f"An error occurred while saving file:\n{e}")
                print(f"Error saving file: {traceback.format_exc()}")



    def handle_reset(self):
        """
        Clears all input and output fields, then sets input fields to their default initial values.
        Resets project title.
        """
        print("Action: Reset - Clearing all fields and resetting inputs to defaults.")
        self.set_initial_input_values() # Sets default values for inputs
        self.clear_output_fields() # Clears outputs and radio buttons
        self.update_bored_diameter_display() # Update bored diameter based on new default input pipe diameter
        self.current_file_path = None
        self._current_project_title = global_app_info.get("project_name", "Untitled Project (Initial)")
        self.setWindowTitle(f"Pipeline Crossing Simulation - {self._current_project_title}")
        QtWidgets.QMessageBox.information(self, "Reset All", "All fields cleared and input fields reset to default values.")


    def handle_generate_report(self):
        """Handles the generation of a PDF report."""
        print("Action: Generate Report initiated.")
        if not self.last_calculation_results or not self.last_input_data:
            QtWidgets.QMessageBox.warning(self, "Report Generation Failed",
                                          "No calculation results available to generate a report. "
                                          "Please run a calculation first.")
            return
        
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save Report", "pipeline_report.pdf",
            "PDF Files (*.pdf);;All Files (*)"
        )
        if file_path:
            if not file_path.lower().endswith('.pdf'):
                file_path += '.pdf'
            try:
                username_for_report = self._logged_in_username
                project_title_for_report = self._current_project_title

                generate_pipeline_report(
                    file_path,
                    self.last_input_data,
                    self.last_calculation_results,
                    username=username_for_report,
                    project_title=project_title_for_report,
                )
                QtWidgets.QMessageBox.information(self, "Report Generated", f"Report saved successfully to:\n{file_path}")
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Report Error", f"An error occurred while generating the report:\n{e}")
                print(f"Error generating report: {traceback.format_exc()}")


    def handle_whats_new(self):
        """Displays information about new features/version."""
        print("Action: What's New? - Functionality not yet implemented.")
        QtWidgets.QMessageBox.information(self, "What's New?", "Beta Version 1.0.0 (Released: June , 2025)")


    def handle_documentation(self):
        """Displays application documentation."""
        documentation_text = """
        <p><b>Pipeline Crossing Simulation Application</b></p>
        <p>This application is designed to assist engineers in the preliminary design and analysis of pipeline crossings, particularly under roads or other infrastructure.</p>
        <p><b>Use Cases:</b></p>
        <ul>
            <li><b>Preliminary Design:</b> Quickly evaluate different pipe parameters and soil conditions.</li>
            <li><b>Stress Analysis:</b> Calculate and check various stresses (Barlow, Earth Load, Cyclic, Principal, Effective) against allowable limits.</li>
            <li><b>Code Compliance:</b> Perform checks based on selected industry codes and standards (e.g., API 1102).</li>
            <li><b>Report Generation:</b> Generate detailed PDF reports of inputs, outputs, and compliance checks.</li>
            <li><b>Project Management:</b> Save and load project data for future use.</li>
        </ul>
        <p>This is a beta version. For detailed methodology and limitations, please refer to relevant engineering standards.</p>
        """
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setWindowTitle("Documentation")
        msg_box.setTextFormat(QtCore.Qt.RichText)
        msg_box.setText(documentation_text)
        msg_box.setMinimumWidth(500)
        msg_box.exec_()
        print("Action: Documentation.")


    def get_project_name_from_path(self, file_path):
        """Extracts a project name from a file path."""
        if file_path:
            base_name = os.path.basename(file_path)
            project_name = os.path.splitext(base_name)[0]
            project_name = project_name.replace('_', ' ').strip()
            return project_name.title()
        return "Untitled Project"
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = PipelineSimulationApp()
    window.show()
    sys.exit(app.exec_())