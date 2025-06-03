import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import json
import csv 
from pipeline_simulation import Ui_MainWindow 
from pipeline_calculation import calculate_pipeline_crossing, calculate_bored_diameter_value 
import traceback

class PipelineSimulationApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # Set up the UI from pipeline_gui.py

        self.current_file_path = None # To store the path of the current project file for Save/Open

        # Define lists of input widgets for easy iteration during saving/loading
        self._line_edit_inputs = [
            'lineEdit_Pipe_outside_diameter', 'lineEdit_2_pipe_wall_thickness',
            'lineEdit_3_SMYS', 'lineEdit_5_Depth_of_Cover', 'lineEdit_4_Corrossion_Allowance',
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
        self._combo_box_inputs = [
            'comboBox_2_pipe_type', 'comboBox_3_Soil_Type', 'comboBox_5_Bored_Diameter',
            'comboBox_Streel_grade', 'comboBox_4_Codes_and_standards',
        ]
        # Connect the START button to our calculation method
        self.Start.clicked.connect(self.on_start_button_clicked)

        # Connect menu actions
        self.actionExit.triggered.connect(self.close)
        self.actionNew.triggered.connect(self.handle_new)
        self.actionOpen.triggered.connect(self.handle_open)
        self.actionSave_As.triggered.connect(self.handle_save_as) 
        self.actionReset.triggered.connect(self.handle_reset)
        self.actionGenerate_Report.triggered.connect(self.handle_generate_report)
        self.actionWhat_s_New.triggered.connect(self.handle_whats_new)
        self.actionDocumentation.triggered.connect(self.handle_documentation)

        # Initialize output fields to be read-only and have page background color
        self.setup_output_fields_style()

        self.set_initial_input_values()

        # Connect signals for immediate Bored Diameter update
        self.comboBox_5_Bored_Diameter.currentIndexChanged.connect(self.update_bored_diameter_display)
        self.lineEdit_Pipe_outside_diameter.textChanged.connect(self.update_bored_diameter_display)

        self.update_bored_diameter_display()


    def setup_output_fields_style(self):
        output_fields = [
            self.lineEdit_6PipeWallThickness_including_CA,
            self.lineEdit_6Boreddiameter,
            self.lineEdit_33barlowStress,
            self.lineEdit_35StressDuetoEarthLoad,
            self.lineEdit_34_CyclicCircumferentialStress,
            self.lineEdit_36CyclicLongitudinalStress,
            self.lineEdit_30radial_stress,
            self.lineEdit_38Circumferential_stress,
            self.lineEdit_39Longitudinal_stress,
            self.lineEdit_40Effective_stresses,
        ]
        for field in output_fields:
            field.setReadOnly(True)
            field.setStyleSheet("")
    def set_initial_input_values(self):
        # Set default values for combo boxes
        self.comboBox_2_pipe_type.setCurrentText("SMLS")
        self.comboBox_3_Soil_Type.setCurrentText("Soft to medium clay")
        self.comboBox_5_Bored_Diameter.setCurrentText("Considered")
        self.comboBox_Streel_grade.setCurrentText("Fe 330")
        self.comboBox_4_Codes_and_standards.setCurrentText("API 1102")

        # Set default values for LineEdits
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
        self.lineEdit_37Coefficient_Of_Thermal_Expansion.setText("1.44e-5") # Use scientific notation

        # Fixed values from original backend script that are not direct GUI inputs
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

        # Apply white background to all input fields
        self.reset_input_field_styles_to_white()

    def reset_input_field_styles_to_white(self):
        for name in self._line_edit_inputs:
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
            pipe_outside_diameter = float(pipe_outside_diameter_text)
            self.lineEdit_Pipe_outside_diameter.setStyleSheet("background-color: white; border: 1px solid gray;")
            bored_diameter_option = self.comboBox_5_Bored_Diameter.currentText()

            calculated_bored_diameter = calculate_bored_diameter_value(pipe_outside_diameter, bored_diameter_option)
            self.lineEdit_6Boreddiameter.setText(f"{calculated_bored_diameter:.3f}")
            self.lineEdit_6Boreddiameter.setStyleSheet("")
        except ValueError:
            self.lineEdit_Pipe_outside_diameter.setStyleSheet("background-color: white; border: 2px solid red;")
            self.lineEdit_6Boreddiameter.clear() 
            self.lineEdit_6Boreddiameter.setStyleSheet("") 
        except Exception as e:
            print(f"Error updating bored diameter: {e}")
            self.lineEdit_Pipe_outside_diameter.setStyleSheet("background-color: white; border: 2px solid red;")
            self.lineEdit_6Boreddiameter.clear() 
            self.lineEdit_6Boreddiameter.setStyleSheet("") 


    def on_start_button_clicked(self):
        self.reset_input_field_styles_to_white() 
        self.reset_results() 
        input_data = {}
        has_overall_error = [False] 

        print("\n--- Reading Input Values from GUI ---")

        # --- Read Input Data from GUI with Validation ---
        try:
            steel_grade_text = self.comboBox_Streel_grade.currentText()
            input_data["Steel_grade"] = float(steel_grade_text.replace("Fe ", "")) if "Fe" in steel_grade_text else float(steel_grade_text)
            print(f"Steel Grade: {input_data['Steel_grade']}")
        except ValueError:
            print(f"Error converting Steel Grade from '{steel_grade_text}': Please select a valid option.")
            has_overall_error[0] = True

        input_data["Pipe_Type"] = self.comboBox_2_pipe_type.currentText()
        print(f"Pipe Type: {input_data['Pipe_Type']}")

        input_data["Bored_Diameter_Option"] = self.comboBox_5_Bored_Diameter.currentText()
        print(f"Bored Diameter Option: {input_data['Bored_Diameter_Option']}")

        input_data["Soil_Type"] = self.comboBox_3_Soil_Type.currentText()
        print(f"Soil Type: {input_data['Soil_Type']}")

        # Numeric input fields with validation
        self._validate_and_get_float_input(self.lineEdit_Pipe_outside_diameter, "Pipe_Outside_Diameter", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_2_pipe_wall_thickness, "Pipe_Wall_Thickness", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_3_SMYS, "Specified_Minimum_Yield_Strength", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_5_Depth_of_Cover, "Depth_of_Cover", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_4_Corrossion_Allowance, "Corrosion_Allowance", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_6operatingpressure, "Operating_Pressure", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_6operating_temperature, "Operating_Temperature", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_6impactfactor, "Impact_Factor", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_6Design_wheel_load_from_single_axle, "Design_Wheel_Load_From_Single_Axle", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_6soilunitweight, "Soil_Unit_Weight", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_6designfactor, "Design_Factor", input_data, has_overall_error)
        self._validate_and_get_float_input(self.Design_wheel_load_from_tandem_axle_2, "Design_Wheel_Load_From_Tandem_Axle", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_6Modulus_of_soil_reaction, "Modulus_of_Soil_Reaction", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_6longitudinaljointfactor, "Longitudinal_Joint_Factor", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_6youngs_modulus, "Youngs_Modulus", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_6resilient_modulus, "Resilient_Modulus", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_6installation_temperature, "Installation_Temperature", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_6poissons_ratio, "Poissons_Ratio", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_37Coefficient_Of_Thermal_Expansion, "Coefficient_of_Thermal_Expansion", input_data, has_overall_error)

        self._validate_and_get_float_input(self.lineEdit_21EarthLoadStiffnessFactor, "Earth_Load_Stiffness_Factor", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_22EarthLoadBurialFactor, "Earth_Load_Burial_Factor", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_23EarthLoadExcavationFactor, "Earth_Load_Excavation_Factor", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_27StiffnessFactorKHh, "Stiffness_Factor_KHh", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_25_GeometryFactorGHh, "Geometry_Factor_GHh", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_29_StifnessFactorKLh, "Stiffness_Factor_KLh", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_28geometryFactorGLh, "Geometry_Factor_GLh", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_26RoadAxleConfigurationFactor, "Road_Axle_Configuration_Factor", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_24RoadPavementFactor, "Road_Pavement_Type_Factor", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_31FatigueEnduranceofGirthYield, "Fatigue_endurance_Limit_of_Girth_yield", input_data, has_overall_error)
        self._validate_and_get_float_input(self.lineEdit_32FatigueEnduranceofLongitudinalWeld, "Fatigue_endurance_Limit_of_Longitudinal_Weld", input_data, has_overall_error)
        print("--- Input Reading Complete ---")

        # If any validation failed, show an error message and stop
        if has_overall_error[0]:
            QtWidgets.QMessageBox.critical(self, "Input Error", "Please correct the highlighted fields with valid numeric inputs.")
            return

        # --- Perform Calculation ---
        try:
            results = calculate_pipeline_crossing(input_data)
            print("\n--- Calculation Results ---")
            for key, value in results.items():
                if "Check" in key or key in ["Barlow_Stress", "Stress_due_to_Earth_Load",
                                           "Cyclic_Circumferential_Stress", "Cyclic_Longitudinal_Stress",
                                           "Circumferential_Stress_S1", "Longitudinal_Stress_S2",
                                           "Effective_Stress_Seff", "Radial_Stress",
                                           "Pipe_Wall_Thickness_Including_CA", "Bored_Diameter"]:
                    print(f"{key}: {value}")
            print("--------------------------")

            # --- Display Results on GUI ---
            self.lineEdit_6PipeWallThickness_including_CA.setText(f"{results['Pipe_Wall_Thickness_Including_CA']:.3f}")
            self.lineEdit_6PipeWallThickness_including_CA.setStyleSheet("") 

            # Explicitly update Bored Diameter from main calculation results
            self.lineEdit_6Boreddiameter.setText(f"{results['Bored_Diameter']:.3f}")
            self.lineEdit_6Boreddiameter.setStyleSheet("") 

            self.lineEdit_33barlowStress.setText(f"{results['Barlow_Stress']:.3f}")
            self.lineEdit_33barlowStress.setStyleSheet("") 
            self.lineEdit_35StressDuetoEarthLoad.setText(f"{results['Stress_due_to_Earth_Load']:.3f}")
            self.lineEdit_35StressDuetoEarthLoad.setStyleSheet("") 
            self.lineEdit_34_CyclicCircumferentialStress.setText(f"{results['Cyclic_Circumferential_Stress']:.3f}")
            self.lineEdit_34_CyclicCircumferentialStress.setStyleSheet("") 
            self.lineEdit_36CyclicLongitudinalStress.setText(f"{results['Cyclic_Longitudinal_Stress']:.3f}")
            self.lineEdit_36CyclicLongitudinalStress.setStyleSheet("") 
            self.lineEdit_30radial_stress.setText(f"{results['Radial_Stress']:.3f}")
            self.lineEdit_30radial_stress.setStyleSheet("") 
            self.lineEdit_38Circumferential_stress.setText(f"{results['Circumferential_Stress_S1']:.3f}")
            self.lineEdit_38Circumferential_stress.setStyleSheet("") 
            self.lineEdit_39Longitudinal_stress.setText(f"{results['Longitudinal_Stress_S2']:.3f}")
            self.lineEdit_39Longitudinal_stress.setStyleSheet("") 
            self.lineEdit_40Effective_stresses.setText(f"{results['Effective_Stress_Seff']:.3f}")
            self.lineEdit_40Effective_stresses.setStyleSheet("") 
            # --- Update Radio Buttons for Criteria Checks ---
            # Barlow Stress Check
            self.update_radio_button_status(self.radioButton_7_safe, self.radioButton_8_not_safe, results['Barlow_Stress_Check'])
            # Principle Stress Check
            self.update_radio_button_status(self.radioButton_6_safe, self.radioButton_5_not_safe, results['Principle_Stress_Check'])
            # Girth Weld Criteria Check
            self.update_radio_button_status(self.radioButton_safe, self.radioButton_2_not_safe, results['Girth_Weld_Criteria_Check'])
            # Longitudinal Weld Criteria Check
            self.update_radio_button_status(self.radioButton_3_safe, self.radioButton_4_not_safe, results['Longitudinal_Weld_Criteria_Check'])

            QtWidgets.QMessageBox.information(self, "Calculation Complete", "Pipeline crossing calculations finished successfully!")

        except ZeroDivisionError:
            user_friendly_message = (
                "A calculation error occurred:"
                "Please check the 'Pipe Wall Thickness', 'Corrosion Allowance', and 'Pipe Outside Diameter' fields. "
            )
            QtWidgets.QMessageBox.critical(self, "Calculation Error", user_friendly_message)
            traceback.print_exc() 
            self.reset_results() 
        except Exception as e:
            # Catch any other unexpected errors
            QtWidgets.QMessageBox.critical(self, "Calculation Error", f"An unexpected error occurred during calculation: {e}")
            print(f"An unexpected error occurred during calculation: {e}") # Log the error message to the console
            traceback.print_exc() # Print full traceback to console for developer
            self.reset_results() # Reset results on error

    def update_radio_button_status(self, safe_rb, not_safe_rb, status):
        if status == "Allowable":
            safe_rb.setChecked(True)
            not_safe_rb.setChecked(False)
        else:
            safe_rb.setChecked(False)
            not_safe_rb.setChecked(True)

    def reset_results(self):
        output_fields_to_clear = [
            self.lineEdit_6PipeWallThickness_including_CA,
            self.lineEdit_33barlowStress,
            self.lineEdit_35StressDuetoEarthLoad,
            self.lineEdit_34_CyclicCircumferentialStress,
            self.lineEdit_36CyclicLongitudinalStress,
            self.lineEdit_30radial_stress,
            self.lineEdit_38Circumferential_stress,
            self.lineEdit_39Longitudinal_stress,
            self.lineEdit_40Effective_stresses,
        ]
        for field in output_fields_to_clear:
            field.clear()
            field.setStyleSheet("") # Ensure they have page background
        # Clear radio button selections
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
        data = {}
        for name in self._line_edit_inputs:
            widget = getattr(self, name)
            data[name] = widget.text()
        for name in self._combo_box_inputs:
            widget = getattr(self, name)
            data[name] = widget.currentText()
        return data
    def set_all_input_values(self, data):
        self.handle_new() 
        for name in self._line_edit_inputs:
            widget = getattr(self, name)
            if name in data:
                widget.setText(data[name])
                widget.setStyleSheet("background-color: white; border: 1px solid gray;")
            else:
                widget.setStyleSheet("background-color: white; border: 1px solid gray;")
                print(f"Warning: LineEdit '{name}' not found in loaded data. Resetting to default.")

        for name in self._combo_box_inputs:
            widget = getattr(self, name)
            if name in data:
                index = widget.findText(data[name])
                if index != -1:
                    widget.setCurrentIndex(index)
                else:
                    widget.setCurrentIndex(0) # Fallback to first item if text not found
                    print(f"Warning: Value '{data[name]}' not found in ComboBox '{name}'. Resetting to default.")
            else:
                widget.setCurrentIndex(0) # Fallback to first item if key not found
                print(f"Warning: ComboBox '{name}' not found in loaded data. Resetting to default.")
        
        self.update_bored_diameter_display()
    def handle_new(self):
        print("Action: New - Clearing all inputs and results.")
        self.set_initial_input_values()
        self.reset_results()
        self.update_bored_diameter_display()
        self.current_file_path = None # Clear current file path as it's a new project

    def handle_open(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open Project", "", "CSV Files (*.csv);;All Files (*)" 
        )
        if file_path:
            try:
                with open(file_path, 'r', newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    loaded_data = next(reader)
                self.set_all_input_values(loaded_data) 
                self.current_file_path = file_path 
                QtWidgets.QMessageBox.information(self, "Open Project", f"Project data loaded successfully from:\n{file_path}")
            except FileNotFoundError:
                QtWidgets.QMessageBox.critical(self, "Open Error", f"File not found: {file_path}")
            except StopIteration:
                QtWidgets.QMessageBox.critical(self, "Open Error", f"CSV file is empty or has no data rows: {file_path}")
            except csv.Error as e: # Catch specific CSV errors
                QtWidgets.QMessageBox.critical(self, "Open Error", f"Error reading CSV file: {file_path}\nDetails: {e}")
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Open Error", f"An unexpected error occurred while opening file:\n{e}")
                print(f"Error opening file: {traceback.format_exc()}")

    def handle_save_as(self):
        """Saves current GUI input data to a new project file (CSV)."""
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save Project As", "pipeline_project.csv", # Default file name and extension
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

                self.current_file_path = file_path # Set the current file path
                QtWidgets.QMessageBox.information(self, "Save Project As", f"Project data saved successfully to:\n{file_path}")
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Save Error", f"An error occurred while saving file:\n{e}")
                print(f"Error saving file: {traceback.format_exc()}")

    def handle_reset(self):
        print("Action: Reset - Clearing all inputs and results.")
        for name in self._line_edit_inputs:
            field = getattr(self, name)
            field.clear()
            field.setStyleSheet("background-color: white; border: 1px solid gray;")
        for name in self._combo_box_inputs:
            combo_box = getattr(self, name)
            if combo_box.count() > 0:
                combo_box.setCurrentIndex(0) 
        self.reset_results() 
        self.update_bored_diameter_display() 
        self.current_file_path = None # Clear current file path as it's a fresh start
    def handle_generate_report(self):
        print("Action: Generate Report - Functionality not yet implemented.")
        QtWidgets.QMessageBox.information(self, "Report", "Generating report functionality to be implemented.")

    def handle_whats_new(self):
        print("Action: What's New? - Functionality not yet implemented.")
        QtWidgets.QMessageBox.information(self, "What's New?",  "Beta Version 1.0.0 (Released: June , 2025")

    def handle_documentation(self):
        """
        Displays a summary of the application's use case in a QMessageBox.
        Attempts to make the message box more square.
        """
        documentation_text = """
        <p><b>Pipeline Crossing Design Application</b></p>
        <p>This application is designed to assist engineers in the preliminary design and analysis of pipeline crossings, particularly under roads or other infrastructure.</p>
        <p><b>Use Cases:</b></p>
        <ul>
            <li><b>Preliminary Design:</b> Input various pipeline and soil parameters to quickly estimate critical stresses and ensure design compliance with industry standards (e.g., API 1102).</li>
            <li><b>Feasibility Studies:</b> Evaluate different pipe materials, sizes, and installation conditions to determine the most suitable and safe crossing method.</li>
            <li><b>Stress Analysis:</b> Calculate key stresses such as Barlow Stress, Earth Load Stress, Cyclic Circumferential Stress, Cyclic Longitudinal Stress, and Effective Stress.</li>
            <li><b>Criteria Checks:</b> Automatically perform checks against specified minimum yield strength (SMYS) and fatigue endurance limits for girth and longitudinal welds to ensure the design is "Allowable" or "Not Allowable".</li>
            <li><b>Parameter Sensitivity:</b> Understand how changes in input parameters (e.g., depth of cover, soil type, operating pressure) impact the overall pipeline integrity and design criteria.</li>
            <li><b>Data Management:</b> Save and load project input data using CSV files for easy sharing, revision, and record-keeping.</li>
        </ul>
        <p>This tool provides a quick and efficient way to perform essential calculations, helping to identify potential design issues early in the project lifecycle.</p>
        """
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Application Documentation")
        msg_box.setTextFormat(QtCore.Qt.RichText) 
        msg_box.setText(documentation_text)
        msg_box.setMinimumSize(700, 700) # Set minimum width and height
        msg_box.setMaximumSize(700, 700) # Set maximum width and height
        msg_box.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        msg_box.exec_()
# --- Main execution block ---
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PipelineSimulationApp()
    window.showMaximized()
    sys.exit(app.exec_())
