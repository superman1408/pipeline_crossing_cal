import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from pipeline_simulation import Ui_MainWindow # Import your generated UI class
from pipeline_calculation import calculate_pipeline_crossing # Import your backend function

class PipelineSimulationApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        
        super().__init__()
        self.setupUi(self) # Set up the UI from pipeline_gui.py

        # Connect the START button to our calculation method
        self.Start.clicked.connect(self.on_start_button_clicked)

        # Initialize output fields to be read-only
        self.make_output_fields_read_only()

        # Set initial values for input fields based on your backend's default inputs
        # This makes the GUI pre-filled and ready for calculation
        self.set_initial_input_values()

    def make_output_fields_read_only(self):
      
        self.lineEdit_6PipeWallThickness_including_CA.setReadOnly(True)
        self.lineEdit_6Boreddiameter.setReadOnly(True)
        self.lineEdit_33barlowStress.setReadOnly(True)
        self.lineEdit_35StressDuetoEarthLoad.setReadOnly(True)
        self.lineEdit_34_CyclicCircumferentialStress.setReadOnly(True)
        self.lineEdit_36CyclicLongitudinalStress.setReadOnly(True)
        self.lineEdit_30radial_stress.setReadOnly(True)
        self.lineEdit_38Circumferential_stress.setReadOnly(True)
        self.lineEdit_39Longitudinal_stress.setReadOnly(True)
        self.lineEdit_40Effective_stresses.setReadOnly(True)

    def set_initial_input_values(self):
        
        # Set default values for combo boxes
        self.comboBox_2_pipe_type.setCurrentText("Seamless")
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
        self.lineEdit_6youngs_modulus.setText("210")
        self.lineEdit_6resilient_modulus.setText("34")
        self.lineEdit_6installation_temperature.setText("65")
        self.lineEdit_6poissons_ratio.setText("0.30")
        self.lineEdit_37Coefficient_Of_Thermal_Expansion.setText("1.44e-5") # Use scientific notation

        # Fixed values from original backend script that are not direct GUI inputs
        # but are used in calculations (these are passed as defaults to the backend function)
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


    def on_start_button_clicked(self):
        
        input_data = {}
        try:
            # --- Read Input Data from GUI ---
            input_data["Steel_grade"] = float(self.comboBox_Streel_grade.currentText().replace("Fe ", "")) # Assuming "Fe 330" -> 330.0
            input_data["Pipe_Type"] = self.comboBox_2_pipe_type.currentText()
            input_data["Pipe_Outside_Diameter"] = float(self.lineEdit_Pipe_outside_diameter.text())
            input_data["Pipe_Wall_Thickness"] = float(self.lineEdit_2_pipe_wall_thickness.text())
            input_data["Specified_Minimum_Yield_Strength"] = float(self.lineEdit_3_SMYS.text())
            input_data["Depth_of_Cover"] = float(self.lineEdit_5_Depth_of_Cover.text())
            input_data["Corrosion_Allowance"] = float(self.lineEdit_4_Corrossion_Allowance.text())
            input_data["Bored_Diameter_Option"] = self.comboBox_5_Bored_Diameter.currentText()
            input_data["Soil_Unit_Weight"] = float(self.lineEdit_6soilunitweight.text())
            input_data["Soil_Type"] = self.comboBox_3_Soil_Type.currentText()
            input_data["Modulus_of_Soil_Reaction"] = float(self.lineEdit_6Modulus_of_soil_reaction.text())
            input_data["Resilient_Modulus"] = float(self.lineEdit_6resilient_modulus.text())
            input_data["Operating_Pressure"] = float(self.lineEdit_6operatingpressure.text())
            input_data["Impact_Factor"] = float(self.lineEdit_6impactfactor.text())
            input_data["Design_Factor"] = float(self.lineEdit_6designfactor.text())
            input_data["Longitudinal_Joint_Factor"] = float(self.lineEdit_6longitudinaljointfactor.text())
            input_data["Installation_Temperature"] = float(self.lineEdit_6installation_temperature.text())
            input_data["Operating_Temperature"] = float(self.lineEdit_6operating_temperature.text())
            input_data["Design_Wheel_Load_From_Single_Axle"] = float(self.lineEdit_6Design_wheel_load_from_single_axle.text())
            input_data["Design_Wheel_Load_From_Tandem_Axle"] = float(self.Design_wheel_load_from_tandem_axle_2.text())
            input_data["Youngs_Modulus"] = float(self.lineEdit_6youngs_modulus.text())
            input_data["Poissons_Ratio"] = float(self.lineEdit_6poissons_ratio.text())
            input_data["Coefficient_of_Thermal_Expansion"] = float(self.lineEdit_37Coefficient_Of_Thermal_Expansion.text())

            # Read fixed values from UI that were previously hardcoded in backend
            input_data["Earth_Load_Stiffness_Factor"] = float(self.lineEdit_21EarthLoadStiffnessFactor.text())
            input_data["Earth_Load_Burial_Factor"] = float(self.lineEdit_22EarthLoadBurialFactor.text())
            input_data["Earth_Load_Excavation_Factor"] = float(self.lineEdit_23EarthLoadExcavationFactor.text())
            input_data["Stiffness_Factor_KHh"] = float(self.lineEdit_27StiffnessFactorKHh.text())
            input_data["Geometry_Factor_GHh"] = float(self.lineEdit_25_GeometryFactorGHh.text())
            input_data["Stiffness_Factor_KLh"] = float(self.lineEdit_29_StifnessFactorKLh.text())
            input_data["Geometry_Factor_GLh"] = float(self.lineEdit_28geometryFactorGLh.text())
            input_data["Road_Axle_Configuration_Factor"] = float(self.lineEdit_26RoadAxleConfigurationFactor.text())
            input_data["Road_Pavement_Type_Factor"] = float(self.lineEdit_24RoadPavementFactor.text())
            input_data["Fatigue_endurance_Limit_of_Girth_yield"] = float(self.lineEdit_31FatigueEnduranceofGirthYield.text())
            input_data["Fatigue_endurance_Limit_of_Longitudinal_Weld"] = float(self.lineEdit_32FatigueEnduranceofLongitudinalWeld.text())


            # --- Perform Calculation ---
            results = calculate_pipeline_crossing(input_data)

            # --- Display Results on GUI ---
            self.lineEdit_6PipeWallThickness_including_CA.setText(f"{results['Pipe_Wall_Thickness_Including_CA']:.3f}")
            self.lineEdit_6Boreddiameter.setText(f"{results['Bored_Diameter']:.3f}")
            self.lineEdit_33barlowStress.setText(f"{results['Barlow_Stress']:.3f}")
            self.lineEdit_35StressDuetoEarthLoad.setText(f"{results['Stress_due_to_Earth_Load']:.3f}")
            self.lineEdit_34_CyclicCircumferentialStress.setText(f"{results['Cyclic_Circumferential_Stress']:.3f}")
            self.lineEdit_36CyclicLongitudinalStress.setText(f"{results['Cyclic_Longitudinal_Stress']:.3f}")
            self.lineEdit_30radial_stress.setText(f"{results['Radial_Stress']:.3f}")
            self.lineEdit_38Circumferential_stress.setText(f"{results['Circumferential_Stress_S1']:.3f}")
            self.lineEdit_39Longitudinal_stress.setText(f"{results['Longitudinal_Stress_S2']:.3f}")
            self.lineEdit_40Effective_stresses.setText(f"{results['Effective_Stress_Seff']:.3f}")

            # --- Update Radio Buttons for Criteria Checks ---
            self.update_radio_button_status(self.radioButton_7_safe, self.radioButton_8_not_safe, results['Barlow_Stress_Check'])
            self.update_radio_button_status(self.radioButton_5_safe, self.radioButton_6_not_safe, results['Principle_Stress_Check'])
            self.update_radio_button_status(self.radioButton_safe, self.radioButton_2_not_safe, results['Girth_Weld_Criteria_Check'])
            self.update_radio_button_status(self.radioButton_3_safe, self.radioButton_4_not_safe, results['Longitudinal_Weld_Criteria_Check'])

            QtWidgets.QMessageBox.information(self, "Calculation Complete", "Pipeline crossing calculations finished successfully!")

        except ValueError as e:
            QtWidgets.QMessageBox.critical(self, "Input Error", f"Please ensure all input fields contain valid numbers. Error: {e}")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Calculation Error", f"An unexpected error occurred during calculation: {e}")

    def update_radio_button_status(self, safe_rb, not_safe_rb, status):
       
        if status == "Allowable":
            safe_rb.setChecked(True)
            not_safe_rb.setChecked(False)
        else:
            safe_rb.setChecked(False)
            not_safe_rb.setChecked(True)

# --- Main execution block ---
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PipelineSimulationApp()
    window.show()
    sys.exit(app.exec_())
