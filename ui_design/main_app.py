import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from pipeline_simulation import Ui_MainWindow 
from pipeline_calculation import calculate_pipeline_crossing, calculate_bored_diameter_value 
import traceback 

class PipelineSimulationApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self) # Set up the UI from pipeline_simulation.py

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

        # Set initial values for input fields based on your backend's default inputs
        self.set_initial_input_values()

        # Connect signals for immediate Bored Diameter update
        self.comboBox_5_Bored_Diameter.currentIndexChanged.connect(self.update_bored_diameter_display)
        self.lineEdit_Pipe_outside_diameter.textChanged.connect(self.update_bored_diameter_display)

        # Call it once to set the initial bored diameter and handle its styling
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
            # Setting stylesheet to empty string allows it to inherit parent's background (page color)
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
        input_fields = [
            self.lineEdit_Pipe_outside_diameter,
            self.lineEdit_2_pipe_wall_thickness,
            self.lineEdit_3_SMYS,
            self.lineEdit_5_Depth_of_Cover,
            self.lineEdit_4_Corrossion_Allowance,
            self.lineEdit_6operatingpressure,
            self.lineEdit_6operating_temperature,
            self.lineEdit_6impactfactor,
            self.lineEdit_6Design_wheel_load_from_single_axle,
            self.lineEdit_6soilunitweight,
            self.lineEdit_6designfactor,
            self.Design_wheel_load_from_tandem_axle_2,
            self.lineEdit_6Modulus_of_soil_reaction,
            self.lineEdit_6longitudinaljointfactor,
            self.lineEdit_6youngs_modulus,
            self.lineEdit_6resilient_modulus,
            self.lineEdit_6installation_temperature,
            self.lineEdit_6poissons_ratio,
            self.lineEdit_37Coefficient_Of_Thermal_Expansion,
            self.lineEdit_21EarthLoadStiffnessFactor,
            self.lineEdit_22EarthLoadBurialFactor,
            self.lineEdit_23EarthLoadExcavationFactor,
            self.lineEdit_27StiffnessFactorKHh,
            self.lineEdit_25_GeometryFactorGHh,
            self.lineEdit_29_StifnessFactorKLh,
            self.lineEdit_28geometryFactorGLh,
            self.lineEdit_26RoadAxleConfigurationFactor,
            self.lineEdit_24RoadPavementFactor,
            self.lineEdit_31FatigueEnduranceofGirthYield,
            self.lineEdit_32FatigueEnduranceofLongitudinalWeld,
        ]
        for field in input_fields:
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
            # Ensure the input field still shows red border if this higher-level error is from bad input
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
            # Catch specific ZeroDivisionError and provide user-friendly message
            user_friendly_message = (
                "A calculation error occurred: "
                "Ensure that Pipe Wall Thickness is greater than Corrosion Allowance, and Pipe Outside Diameter is not zero."
            )
            QtWidgets.QMessageBox.critical(self, "Calculation Error", user_friendly_message)
            traceback.print_exc() 
            self.reset_results() 
        except Exception as e:
            # Catch any other unexpected errors
            QtWidgets.QMessageBox.critical(self, "Calculation Error", f"An unexpected error occurred during calculation: {e}")
            print(f"An unexpected error occurred during calculation: {e}") 
            traceback.print_exc() # Print full traceback to console for developer
            self.reset_results() 

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
            field.setStyleSheet("")
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

    def handle_new(self):
        print("Action: New - Clearing all inputs and results.")
        for line_edit_name in dir(self):
            if isinstance(getattr(self, line_edit_name), QtWidgets.QLineEdit) and \
               (line_edit_name.startswith('lineEdit_') or line_edit_name == 'Design_wheel_load_from_tandem_axle_2') and \
               line_edit_name not in ["lineEdit_6PipeWallThickness_including_CA", "lineEdit_6Boreddiameter",
                                       "lineEdit_33barlowStress", "lineEdit_35StressDuetoEarthLoad",
                                       "lineEdit_34_CyclicCircumferentialStress", "lineEdit_36CyclicLongitudinalStress",
                                       "lineEdit_30radial_stress", "lineEdit_38Circumferential_stress",
                                       "lineEdit_39Longitudinal_stress", "lineEdit_40Effective_stresses"]:
                getattr(self, line_edit_name).clear()

        # Reset ComboBoxes to default index 
        for combo_box_name in dir(self):
            if isinstance(getattr(self, combo_box_name), QtWidgets.QComboBox):
                getattr(self, combo_box_name).setCurrentIndex(0)

        self.reset_results() 
        self.reset_input_field_styles_to_white() 
        self.set_initial_input_values() 
        self.update_bored_diameter_display() 

    def handle_open(self):
        print("Action: Open - Functionality not yet implemented.")
        QtWidgets.QMessageBox.information(self, "Open", "Open file functionality is not yet implemented.")

    def handle_save_as(self):
        print("Action: Save As - Functionality not yet implemented.")
        QtWidgets.QMessageBox.information(self, "Save As", "Save As functionality is not yet implemented.")

    def handle_reset(self):
        print("Action: Reset - Re-setting all inputs and results to initial values.")
        self.handle_new() 

    def handle_generate_report(self):
        print("Action: Generate Report - Functionality not yet implemented.")
        QtWidgets.QMessageBox.information(self, "Report", "Generating report functionality to be implemented.")

    def handle_whats_new(self):
        print("Action: What's New? - Functionality not yet implemented.")
        QtWidgets.QMessageBox.information(self, "What's New?", "This is a placeholder for 'What's New?' information.")

    def handle_documentation(self):
        print("Action: Documentation - Functionality not yet implemented.")
        QtWidgets.QMessageBox.information(self, "Documentation", "Opening documentation functionality to be implemented.")
# --- Main execution block ---
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PipelineSimulationApp()
    window.showMaximized()
    sys.exit(app.exec_())