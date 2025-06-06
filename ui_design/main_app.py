import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import csv
from pipeline_simulation import Ui_MainWindow
from pipeline_calculation import calculate_pipeline_crossing, calculate_bored_diameter_value
import traceback
import os
from report_generator import generate_pipeline_report 
print("Python Executable:", sys.executable)
print("Python Version:", sys.version)
print("sys.path:", sys.path)
try:
    from reportlab.lib.styles import getSampleStyleSheet
    styles = getSampleStyleSheet()
    print("ReportLab H1 style found:", 'H1' in styles.byName)
    if 'H1' in styles.byName:
        print("ReportLab styles loaded successfully.")
    else:
        print("ReportLab styles loaded, but H1 is missing. This is unexpected.")
except ImportError:
    print("ReportLab module not found!")
except Exception as e:
    print(f"Error loading ReportLab styles: {e}")
global_app_info = {
    "username": "Guest User", # Default until launcher populates it
    "project_name": "Untitled Project (Initial)", # Default until launcher populates it
}
class PipelineSimulationApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.current_file_path = None
        # --- MODIFIED: Initialize dynamic User and Project Info from global_app_info ---
        self._logged_in_username = global_app_info.get("username", "Guest User")
        self._current_project_title = global_app_info.get("project_name", "Untitled Project (Initial)")
        # Set the initial window title
        self.setWindowTitle(f"Pipeline Crossing Simulation - {self._current_project_title}")
        self.steel_grade_smys = 0
        self._line_edit_inputs = [
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
        self._combo_box_inputs = [
            'comboBox_2_pipe_type', 'comboBox_3_Soil_Type', 'comboBox_5_Bored_Diameter',
            'comboBox_Streel_grade', 'comboBox_4_Codes_and_standards',
        ]
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
        self.set_initial_input_values()
        self.comboBox_5_Bored_Diameter.currentIndexChanged.connect(self.update_bored_diameter_display)
        self.lineEdit_Pipe_outside_diameter.textChanged.connect(self.update_bored_diameter_display)
        self.comboBox_Streel_grade.currentIndexChanged.connect(self.on_steel_grade_changed)
        self.update_bored_diameter_display()
        self.on_steel_grade_changed(self.comboBox_Streel_grade.currentIndex())
        self.last_calculation_results = {}
        self.last_input_data = {}
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
        self.comboBox_2_pipe_type.setCurrentText("SMLS")
        self.comboBox_3_Soil_Type.setCurrentText("Soft to medium clay")
        self.comboBox_5_Bored_Diameter.setCurrentText("Considered")
        self.comboBox_Streel_grade.setCurrentText("Fe 330")
        self.comboBox_4_Codes_and_standards.setCurrentText("API 1102")
        self.lineEdit_Pipe_outside_diameter.setText("1016")
        self.lineEdit_2_pipe_wall_thickness.setText("10")
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
    def on_steel_grade_changed(self, index):
        steel_grade_text = self.comboBox_Streel_grade.currentText()
        smys_values = {
            "Fe 330": 195, "A25": 172.3689, "A": 206.8427, "B": 241.3165,
            "X42": 289.5798, "X46": 317.1588, "X52": 358.5274, "X56": 386.1064,
            "X60": 413.6854, "X65": 448.1592, "X70": 482.633, "X80": 551.5806,
        }
        self.steel_grade_smys = smys_values.get(steel_grade_text, 0)
        
        if self.steel_grade_smys == 0 and steel_grade_text not in smys_values:
            QtWidgets.QMessageBox.warning(self, "Input Warning", f"Unknown Steel Grade: {steel_grade_text}. SMYS set to 0.")
            self.lineEdit_3_SMYS.setStyleSheet("background-color: white; border: 2px solid orange;")
        else:
            self.lineEdit_3_SMYS.setStyleSheet("background-color: white; border: 1px solid gray;")
        print(f"Steel Grade selected: {steel_grade_text}, SMYS set to: {self.steel_grade_smys} MPa")
        self.lineEdit_3_SMYS.setText(str(self.steel_grade_smys))
    def on_start_button_clicked(self):
        self.reset_input_field_styles_to_white()
        self.reset_results()
        input_data = {}
        has_overall_error = [False]
        print("\n--- Reading Input Values from GUI ---")
        try:
            input_data["Steel_grade"] = self.comboBox_Streel_grade.currentText()
        except Exception as e:
            print(f"Error getting Steel Grade text: {e}")
            has_overall_error[0] = True
            self.comboBox_Streel_grade.setStyleSheet("border: 2px solid red;")
        input_data["Pipe_Type"] = self.comboBox_2_pipe_type.currentText()
        input_data["Bored_Diameter_Option"] = self.comboBox_5_Bored_Diameter.currentText()
        input_data["Soil_Type"] = self.comboBox_3_Soil_Type.currentText()
        input_data["Codes_and_standards"] = self.comboBox_4_Codes_and_standards.currentText()
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
        self.last_input_data = input_data.copy()
        print("\n--- Input Values ---")
        for key, value in input_data.items():
            print(f"{key}: {value}")
        print("--------------------")
        print(f"DEBUG: Current User (before calc): {self._logged_in_username}")
        print(f"DEBUG: Current Project Title (before calc): {self._current_project_title}")
        if has_overall_error[0]:
            QtWidgets.QMessageBox.critical(self, "Input Error", "Please correct the highlighted fields with valid numeric inputs.")
            return

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
            print("\n--- Criteria Checks ---")
            print(f"Barlow Stress Check: {results.get('Barlow_Stress_Check', 'N/A')}")
            print(f"Principle Stress Check: {results.get('Principle_Stress_Check', 'N/A')}")
            print(f"Girth Weld Criteria Check: {results.get('Girth_Weld_Criteria_Check', 'N/A')}")
            print(f"Longitudinal Weld Criteria Check: {results.get('Longitudinal_Weld_Criteria_Check', 'N/A')}")
            print("-----------------------")
            self.last_calculation_results = results.copy()
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
            self.update_radio_button_status(self.radioButton_7_safe, self.radioButton_8_not_safe, results['Barlow_Stress_Check'])
            self.update_radio_button_status(self.radioButton_6_safe, self.radioButton_5_not_safe, results['Principle_Stress_Check'])
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
            self.reset_results()
            self.last_calculation_results = {}
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Calculation Error", f"An unexpected error occurred during calculation: {e}")
            print(f"An unexpected error occurred during calculation: {e}")
            traceback.print_exc()
            self.reset_results()
            self.last_calculation_results = {}


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
            self.lineEdit_6Boreddiameter,
            self.lineEdit_Pipe_outside_diameter,
        ]
        for field in output_fields_to_clear:
            field.clear()
            field.setStyleSheet("")
    
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
        self.last_calculation_results = {}
        self.last_input_data = {}
        self._current_project_title = global_app_info.get("project_name", "Untitled Project (Initial)")
        self.setWindowTitle(f"Pipeline Crossing Simulation - {self._current_project_title}")


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
                    widget.setCurrentIndex(0)
                    print(f"Warning: Value '{data[name]}' not found in ComboBox '{name}'. Resetting to default.")
            else:
                widget.setCurrentIndex(0)
                print(f"Warning: ComboBox '{name}' not found in loaded data. Resetting to default.")
        self.update_bored_diameter_display()
        self.on_steel_grade_changed(self.comboBox_Streel_grade.currentIndex())


    def handle_new(self):
        print("Action: New - Clearing all inputs and results.")
        self.set_initial_input_values()
        self.reset_results()
        self.update_bored_diameter_display()
        self.current_file_path = None
        self.on_steel_grade_changed(self.comboBox_Streel_grade.currentIndex())
        # When starting a new project, reset to the initial project name from global info
        self._current_project_title = global_app_info.get("project_name", "Untitled Project (Initial)")
        self.setWindowTitle(f"Pipeline Crossing Simulation - {self._current_project_title}")

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
        print("Action: Reset - Clearing all inputs and results.")
        self.set_initial_input_values()
        self.reset_results()
        self.update_bored_diameter_display()
        self.current_file_path = None
        self.on_steel_grade_changed(self.comboBox_Streel_grade.currentIndex())
        self._current_project_title = global_app_info.get("project_name", "Untitled Project (Initial)")
        self.setWindowTitle(f"Pipeline Crossing Simulation - {self._current_project_title}")


    def handle_generate_report(self):
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
        print("Action: What's New? - Functionality not yet implemented.")
        QtWidgets.QMessageBox.information(self, "What's New?", "Beta Version 1.0.0 (Released: June , 2025)")
    def handle_documentation(self):
        documentation_text = """
        <p><b>Pipeline Crossing Design Application</b></p>
        <p>This application is designed to assist engineers in the preliminary design and analysis of pipeline crossings, particularly under roads or other infrastructure.</p>
        <p><b>Use Cases:</b></p>
        <ul>
            <li><b>Preliminary Design:</b> Quickly evaluate different pipe parameters and soil conditions.</li>
            <li><b>Stress Analysis:</b> Calculate and check various stresses (Barlow, Earth Load, Cyclic, Principle, Effective) against allowable limits.</li>
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