import sys
import math
import time # Import time module for sleep

from PyQt5 import QtCore, QtGui, QtWidgets

# --- UI_MainWindow (from PipelineCrossingSimulation.py) ---
# This class defines the main application window's UI.
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1307, 793)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.028, y1:0.0455909, x2:0.841, y2:0.966364, stop:0 rgba(169, 237, 255, 107), stop:0.994318 rgba(253, 255, 218, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.Header = QtWidgets.QFrame(self.centralwidget)
        self.Header.setStyleSheet("background-color: rgb(11, 119, 130);")
        self.Header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Header.setObjectName("Header")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.Header)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.AshkamLogo = QtWidgets.QLabel(self.Header)
        self.AshkamLogo.setStyleSheet("background-color: rgb(11, 119, 130);")
        self.AshkamLogo.setText("")
        # Placeholder for image path. Ensure 'ashkam.jpg' is accessible or remove this line.
        self.AshkamLogo.setPixmap(QtGui.QPixmap("ashkam.png"))
        self.AshkamLogo.setObjectName("AshkamLogo")
        self.gridLayout_18.addWidget(self.AshkamLogo, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_18.addItem(spacerItem, 0, 3, 1, 1)
        self.PipelineCrossingCalulation = QtWidgets.QLabel(self.Header)
        self.PipelineCrossingCalulation.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Cambria\";\n"
"background-color: rgb(11, 120, 130);")
        self.PipelineCrossingCalulation.setObjectName("PipelineCrossingCalulation")
        self.gridLayout_18.addWidget(self.PipelineCrossingCalulation, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_18.addItem(spacerItem1, 0, 1, 1, 1)
        self.gridLayout_17.addWidget(self.Header, 0, 0, 1, 1)
        self.StringInputs = QtWidgets.QHBoxLayout()
        self.StringInputs.setObjectName("StringInputs")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Pipe_Type = QtWidgets.QLabel(self.centralwidget)
        self.Pipe_Type.setStyleSheet("font: 8pt \"Cambria\";")
        self.Pipe_Type.setObjectName("Pipe_Type")
        self.horizontalLayout_2.addWidget(self.Pipe_Type)
        self.PipeType_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.PipeType_combobox.setObjectName("PipeType_combobox")
        self.PipeType_combobox.addItem("")
        self.PipeType_combobox.addItem("")
        self.PipeType_combobox.addItem("")
        self.horizontalLayout_2.addWidget(self.PipeType_combobox)
        self.StringInputs.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(13, 19, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.StringInputs.addItem(spacerItem2)
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.StringInputs.addWidget(self.line_11)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Soil_Type = QtWidgets.QLabel(self.centralwidget)
        self.Soil_Type.setStyleSheet("font: 8pt \"Cambria\";")
        self.Soil_Type.setObjectName("Soil_Type")
        self.horizontalLayout_3.addWidget(self.Soil_Type)
        self.SoilType_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.SoilType_combobox.setObjectName("SoilType_combobox")
        self.SoilType_combobox.addItem("")
        self.horizontalLayout_3.addWidget(self.SoilType_combobox)
        self.StringInputs.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(13, 19, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.StringInputs.addItem(spacerItem3)
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.StringInputs.addWidget(self.line_10)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.Codes_and_standards_2 = QtWidgets.QLabel(self.centralwidget)
        self.Codes_and_standards_2.setStyleSheet("font: 8pt \"Cambria\";")
        self.Codes_and_standards_2.setObjectName("Codes_and_standards_2")
        self.horizontalLayout_17.addWidget(self.Codes_and_standards_2)
        self.BoredDiameter_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.BoredDiameter_combobox.setObjectName("BoredDiameter_combobox")
        self.BoredDiameter_combobox.addItem("")
        self.BoredDiameter_combobox.addItem("")
        self.horizontalLayout_17.addWidget(self.BoredDiameter_combobox)
        self.StringInputs.addLayout(self.horizontalLayout_17)
        spacerItem4 = QtWidgets.QSpacerItem(13, 19, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.StringInputs.addItem(spacerItem4)
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.StringInputs.addWidget(self.line_12)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Streel_grade = QtWidgets.QLabel(self.centralwidget)
        self.Streel_grade.setStyleSheet("font: 8pt \"Cambria\";")
        self.Streel_grade.setObjectName("Streel_grade")
        self.horizontalLayout_4.addWidget(self.Streel_grade)
        self.SteelGrade_Combobox = QtWidgets.QComboBox(self.centralwidget)
        self.SteelGrade_Combobox.setObjectName("SteelGrade_Combobox")
        self.SteelGrade_Combobox.addItem("")
        self.SteelGrade_Combobox.addItem("")
        self.SteelGrade_Combobox.addItem("")
        self.SteelGrade_Combobox.addItem("")
        self.SteelGrade_Combobox.addItem("")
        self.SteelGrade_Combobox.addItem("")
        self.SteelGrade_Combobox.addItem("")
        self.SteelGrade_Combobox.addItem("")
        self.SteelGrade_Combobox.addItem("")
        self.SteelGrade_Combobox.addItem("")
        self.SteelGrade_Combobox.addItem("")
        self.SteelGrade_Combobox.addItem("")
        self.horizontalLayout_4.addWidget(self.SteelGrade_Combobox)
        self.StringInputs.addLayout(self.horizontalLayout_4)
        spacerItem5 = QtWidgets.QSpacerItem(13, 19, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.StringInputs.addItem(spacerItem5)
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.StringInputs.addWidget(self.line_13)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Codes_and_standards = QtWidgets.QLabel(self.centralwidget)
        self.Codes_and_standards.setStyleSheet("font: 8pt \"Cambria\";")
        self.Codes_and_standards.setObjectName("Codes_and_standards")
        self.horizontalLayout_5.addWidget(self.Codes_and_standards)
        self.CodesAndStandards_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.CodesAndStandards_combobox.setObjectName("CodesAndStandards_combobox")
        self.CodesAndStandards_combobox.addItem("")
        self.CodesAndStandards_combobox.addItem("")
        self.CodesAndStandards_combobox.addItem("")
        self.horizontalLayout_5.addWidget(self.CodesAndStandards_combobox)
        self.StringInputs.addLayout(self.horizontalLayout_5)
        self.gridLayout_17.addLayout(self.StringInputs, 1, 0, 1, 1)
        self.mainInputs = QtWidgets.QFrame(self.centralwidget)
        self.mainInputs.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainInputs.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainInputs.setObjectName("mainInputs")
        self.gridLayout = QtWidgets.QGridLayout(self.mainInputs)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.PipeWallThicknessIncluding_CA = QtWidgets.QLabel(self.mainInputs)
        self.PipeWallThicknessIncluding_CA.setStyleSheet("font: 8pt \"Cambria\";")
        self.PipeWallThicknessIncluding_CA.setObjectName("PipeWallThicknessIncluding_CA")
        self.verticalLayout_4.addWidget(self.PipeWallThicknessIncluding_CA)
        self.BoredDiameter = QtWidgets.QLabel(self.mainInputs)
        self.BoredDiameter.setObjectName("BoredDiameter")
        self.verticalLayout_4.addWidget(self.BoredDiameter)
        self.SoilunitWeight = QtWidgets.QLabel(self.mainInputs)
        self.SoilunitWeight.setStyleSheet("font: 8pt \"Cambria\";")
        self.SoilunitWeight.setObjectName("SoilunitWeight")
        self.verticalLayout_4.addWidget(self.SoilunitWeight)
        self.ModulusofSoilReaction = QtWidgets.QLabel(self.mainInputs)
        self.ModulusofSoilReaction.setStyleSheet("font: 8pt \"Cambria\";")
        self.ModulusofSoilReaction.setObjectName("ModulusofSoilReaction")
        self.verticalLayout_4.addWidget(self.ModulusofSoilReaction)
        self.ResilientModulus = QtWidgets.QLabel(self.mainInputs)
        self.ResilientModulus.setStyleSheet("font: 8pt \"Cambria\";")
        self.ResilientModulus.setObjectName("ResilientModulus")
        self.verticalLayout_4.addWidget(self.ResilientModulus)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 5, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_26 = QtWidgets.QLabel(self.mainInputs)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_6.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(self.mainInputs)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_6.addWidget(self.label_27)
        self.label_29 = QtWidgets.QLabel(self.mainInputs)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_6.addWidget(self.label_29)
        self.label_30 = QtWidgets.QLabel(self.mainInputs)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_6.addWidget(self.label_30)
        self.label_31 = QtWidgets.QLabel(self.mainInputs)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_6.addWidget(self.label_31)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 7, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.OperatingPressure = QtWidgets.QLabel(self.mainInputs)
        self.OperatingPressure.setStyleSheet("font: 8pt \"Cambria\";")
        self.OperatingPressure.setObjectName("OperatingPressure")
        self.verticalLayout_8.addWidget(self.OperatingPressure)
        self.ImpactFactor = QtWidgets.QLabel(self.mainInputs)
        self.ImpactFactor.setStyleSheet("font: 8pt \"Cambria\";")
        self.ImpactFactor.setObjectName("ImpactFactor")
        self.verticalLayout_8.addWidget(self.ImpactFactor)
        self.DesignFactor = QtWidgets.QLabel(self.mainInputs)
        self.DesignFactor.setStyleSheet("font: 8pt \"Cambria\";")
        self.DesignFactor.setObjectName("DesignFactor")
        self.verticalLayout_8.addWidget(self.DesignFactor)
        self.LongitudinalJointFactor = QtWidgets.QLabel(self.mainInputs)
        self.LongitudinalJointFactor.setStyleSheet("font: 8pt \"Cambria\";")
        self.LongitudinalJointFactor.setObjectName("LongitudinalJointFactor")
        self.verticalLayout_8.addWidget(self.LongitudinalJointFactor)
        self.InstallationTemperature = QtWidgets.QLabel(self.mainInputs)
        self.InstallationTemperature.setStyleSheet("font: 8pt \"Cambria\";")
        self.InstallationTemperature.setObjectName("InstallationTemperature")
        self.verticalLayout_8.addWidget(self.InstallationTemperature)
        self.gridLayout.addLayout(self.verticalLayout_8, 0, 10, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.OutsideDiameter = QtWidgets.QLabel(self.mainInputs)
        self.OutsideDiameter.setStyleSheet("font: 8pt \"Cambria\";")
        self.OutsideDiameter.setObjectName("OutsideDiameter")
        self.verticalLayout.addWidget(self.OutsideDiameter)
        self.PipeWallThickness_2 = QtWidgets.QLabel(self.mainInputs)
        self.PipeWallThickness_2.setStyleSheet("font: 8pt \"Cambria\";")
        self.PipeWallThickness_2.setObjectName("PipeWallThickness_2")
        self.verticalLayout.addWidget(self.PipeWallThickness_2)
        self.SpecifiedMinimumYieldStrength = QtWidgets.QLabel(self.mainInputs)
        self.SpecifiedMinimumYieldStrength.setStyleSheet("font: 8pt \"Cambria\";")
        self.SpecifiedMinimumYieldStrength.setObjectName("SpecifiedMinimumYieldStrength")
        self.verticalLayout.addWidget(self.SpecifiedMinimumYieldStrength)
        self.DepthOfCover = QtWidgets.QLabel(self.mainInputs)
        self.DepthOfCover.setStyleSheet("font: 8pt \"Cambria\";")
        self.DepthOfCover.setObjectName("DepthOfCover")
        self.verticalLayout.addWidget(self.DepthOfCover)
        self.CorrosionAllowence = QtWidgets.QLabel(self.mainInputs)
        self.CorrosionAllowence.setStyleSheet("font: 8pt \"Cambria\";")
        self.CorrosionAllowence.setObjectName("CorrosionAllowence")
        self.verticalLayout.addWidget(self.CorrosionAllowence)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.mainInputs)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.mainInputs)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.mainInputs)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.mainInputs)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_3.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.mainInputs)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_3.addWidget(self.label_15)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 12, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.PipeOutsideDiameter_box = QtWidgets.QLineEdit(self.mainInputs)
        self.PipeOutsideDiameter_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PipeOutsideDiameter_box.setObjectName("PipeOutsideDiameter_box")
        self.verticalLayout_2.addWidget(self.PipeOutsideDiameter_box)
        self.PipeWallThickness_box = QtWidgets.QLineEdit(self.mainInputs)
        self.PipeWallThickness_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PipeWallThickness_box.setObjectName("PipeWallThickness_box")
        self.verticalLayout_2.addWidget(self.PipeWallThickness_box)
        self.SpecifiedMinimumYieldStrength_box = QtWidgets.QLineEdit(self.mainInputs)
        self.SpecifiedMinimumYieldStrength_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SpecifiedMinimumYieldStrength_box.setObjectName("SpecifiedMinimumYieldStrength_box")
        self.verticalLayout_2.addWidget(self.SpecifiedMinimumYieldStrength_box)
        self.DepthOfCover_box = QtWidgets.QLineEdit(self.mainInputs)
        self.DepthOfCover_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DepthOfCover_box.setObjectName("DepthOfCover_box")
        self.verticalLayout_2.addWidget(self.DepthOfCover_box)
        self.CorrossionAllowence_box = QtWidgets.QLineEdit(self.mainInputs)
        self.CorrossionAllowence_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CorrossionAllowence_box.setObjectName("CorrossionAllowence_box")
        self.verticalLayout_2.addWidget(self.CorrossionAllowence_box)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.mainInputs)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 0, 13, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 0, 3, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.PipeWallThicknessIncludingCA_box = QtWidgets.QLineEdit(self.mainInputs)
        self.PipeWallThicknessIncludingCA_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PipeWallThicknessIncludingCA_box.setText("")
        self.PipeWallThicknessIncludingCA_box.setObjectName("PipeWallThicknessIncludingCA_box")
        self.verticalLayout_5.addWidget(self.PipeWallThicknessIncludingCA_box)
        self.BoredDiameter_box = QtWidgets.QLineEdit(self.mainInputs)
        self.BoredDiameter_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BoredDiameter_box.setText("")
        self.BoredDiameter_box.setObjectName("BoredDiameter_box")
        self.verticalLayout_5.addWidget(self.BoredDiameter_box)
        self.SoilUnitWeight_box = QtWidgets.QLineEdit(self.mainInputs)
        self.SoilUnitWeight_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SoilUnitWeight_box.setObjectName("SoilUnitWeight_box")
        self.verticalLayout_5.addWidget(self.SoilUnitWeight_box)
        self.ModulusOfSoilReaction_box = QtWidgets.QLineEdit(self.mainInputs)
        self.ModulusOfSoilReaction_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ModulusOfSoilReaction_box.setObjectName("ModulusOfSoilReaction_box")
        self.verticalLayout_5.addWidget(self.ModulusOfSoilReaction_box)
        self.ResilientModulus_box = QtWidgets.QLineEdit(self.mainInputs)
        self.ResilientModulus_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ResilientModulus_box.setObjectName("ResilientModulus_box")
        self.verticalLayout_5.addWidget(self.ResilientModulus_box)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 6, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 0, 8, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.mainInputs)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 9, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.OperatingPressure_box = QtWidgets.QLineEdit(self.mainInputs)
        self.OperatingPressure_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.OperatingPressure_box.setObjectName("OperatingPressure_box")
        self.horizontalLayout_7.addWidget(self.OperatingPressure_box)
        self.bar = QtWidgets.QLabel(self.mainInputs)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.bar.setFont(font)
        self.bar.setObjectName("bar")
        self.horizontalLayout_7.addWidget(self.bar)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.impactFactor_box = QtWidgets.QLineEdit(self.mainInputs)
        self.impactFactor_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.impactFactor_box.setObjectName("impactFactor_box")
        self.verticalLayout_7.addWidget(self.impactFactor_box)
        self.designFactor_box = QtWidgets.QLineEdit(self.mainInputs)
        self.designFactor_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.designFactor_box.setObjectName("designFactor_box")
        self.verticalLayout_7.addWidget(self.designFactor_box)
        self.LongitudinalJointFactor_box = QtWidgets.QLineEdit(self.mainInputs)
        self.LongitudinalJointFactor_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LongitudinalJointFactor_box.setObjectName("LongitudinalJointFactor_box")
        self.verticalLayout_7.addWidget(self.LongitudinalJointFactor_box)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.InstallationTemperature_box = QtWidgets.QLineEdit(self.mainInputs)
        self.InstallationTemperature_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InstallationTemperature_box.setObjectName("InstallationTemperature_box")
        self.horizontalLayout_8.addWidget(self.InstallationTemperature_box)
        self.centigrade = QtWidgets.QLabel(self.mainInputs)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.centigrade.setFont(font)
        self.centigrade.setObjectName("centigrade")
        self.horizontalLayout_8.addWidget(self.centigrade)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.gridLayout.addLayout(self.verticalLayout_7, 0, 11, 1, 1)
        self.line = QtWidgets.QFrame(self.mainInputs)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 4, 1, 1)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.OperatingTemperature = QtWidgets.QLabel(self.mainInputs)
        self.OperatingTemperature.setStyleSheet("font: 8pt \"Cambria\";")
        self.OperatingTemperature.setObjectName("OperatingTemperature")
        self.verticalLayout_9.addWidget(self.OperatingTemperature)
        self.DesignWheelLoadFromSingleAxle = QtWidgets.QLabel(self.mainInputs)
        self.DesignWheelLoadFromSingleAxle.setStyleSheet("font: 8pt \"Cambria\";")
        self.DesignWheelLoadFromSingleAxle.setObjectName("DesignWheelLoadFromSingleAxle")
        self.verticalLayout_9.addWidget(self.DesignWheelLoadFromSingleAxle)
        self.DesignWheelLoadFromTandemAxle = QtWidgets.QLabel(self.mainInputs)
        self.DesignWheelLoadFromTandemAxle.setStyleSheet("font: 8pt \"Cambria\";")
        self.DesignWheelLoadFromTandemAxle.setObjectName("DesignWheelLoadFromTandemAxle")
        self.verticalLayout_9.addWidget(self.DesignWheelLoadFromTandemAxle)
        self.YoungsModulus = QtWidgets.QLabel(self.mainInputs)
        self.YoungsModulus.setStyleSheet("font: 8pt \"Cambria\";")
        self.YoungsModulus.setObjectName("YoungsModulus")
        self.verticalLayout_9.addWidget(self.YoungsModulus)
        self.PoissonsRatio = QtWidgets.QLabel(self.mainInputs)
        self.PoissonsRatio.setStyleSheet("font: 8pt \"Cambria\";")
        self.PoissonsRatio.setObjectName("PoissonsRatio")
        self.verticalLayout_9.addWidget(self.PoissonsRatio)
        self.gridLayout.addLayout(self.verticalLayout_9, 0, 14, 1, 1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.OperatingTemperature_box = QtWidgets.QLineEdit(self.mainInputs)
        self.OperatingTemperature_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.OperatingTemperature_box.setObjectName("OperatingTemperature_box")
        self.horizontalLayout_9.addWidget(self.OperatingTemperature_box)
        self.label_39 = QtWidgets.QLabel(self.mainInputs)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_9.addWidget(self.label_39)
        self.verticalLayout_10.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.DesignWheelLoadFromSingleAxle_box = QtWidgets.QLineEdit(self.mainInputs)
        self.DesignWheelLoadFromSingleAxle_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DesignWheelLoadFromSingleAxle_box.setObjectName("DesignWheelLoadFromSingleAxle_box")
        self.horizontalLayout_10.addWidget(self.DesignWheelLoadFromSingleAxle_box)
        self.label_40 = QtWidgets.QLabel(self.mainInputs)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_10.addWidget(self.label_40)
        self.verticalLayout_10.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.DesignWheelLoadFromtandemAxle_box = QtWidgets.QLineEdit(self.mainInputs)
        self.DesignWheelLoadFromtandemAxle_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DesignWheelLoadFromtandemAxle_box.setObjectName("DesignWheelLoadFromtandemAxle_box")
        self.horizontalLayout_11.addWidget(self.DesignWheelLoadFromtandemAxle_box)
        self.label_41 = QtWidgets.QLabel(self.mainInputs)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.horizontalLayout_11.addWidget(self.label_41)
        self.verticalLayout_10.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.YongsModulus_box = QtWidgets.QLineEdit(self.mainInputs)
        self.YongsModulus_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.YongsModulus_box.setObjectName("YongsModulus_box")
        self.horizontalLayout_12.addWidget(self.YongsModulus_box)
        self.label_42 = QtWidgets.QLabel(self.mainInputs)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.horizontalLayout_12.addWidget(self.label_42)
        self.verticalLayout_10.addLayout(self.horizontalLayout_12)
        self.PoissonsRatio_box = QtWidgets.QLineEdit(self.mainInputs)
        self.PoissonsRatio_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PoissonsRatio_box.setObjectName("PoissonsRatio_box")
        self.verticalLayout_10.addWidget(self.PoissonsRatio_box)
        self.gridLayout.addLayout(self.verticalLayout_10, 0, 15, 1, 1)
        self.gridLayout_17.addWidget(self.mainInputs, 2, 0, 1, 1)
        self.CoefficientOfThermalExpansion = QtWidgets.QFrame(self.centralwidget)
        self.CoefficientOfThermalExpansion.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CoefficientOfThermalExpansion.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CoefficientOfThermalExpansion.setObjectName("CoefficientOfThermalExpansion")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.CoefficientOfThermalExpansion)
        self.gridLayout_20.setObjectName("gridLayout_20")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem9, 0, 4, 1, 1)
        self.CoefficientOfThermalExpansion_box = QtWidgets.QLineEdit(self.CoefficientOfThermalExpansion)
        self.CoefficientOfThermalExpansion_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CoefficientOfThermalExpansion_box.setObjectName("CoefficientOfThermalExpansion_box")
        self.gridLayout_20.addWidget(self.CoefficientOfThermalExpansion_box, 0, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem10, 0, 3, 1, 1)
        self.Coefficient_Of_Thermal_Expansion = QtWidgets.QLabel(self.CoefficientOfThermalExpansion)
        self.Coefficient_Of_Thermal_Expansion.setStyleSheet("font: 75 10pt \"Cambria\";")
        self.Coefficient_Of_Thermal_Expansion.setObjectName("Coefficient_Of_Thermal_Expansion")
        self.gridLayout_20.addWidget(self.Coefficient_Of_Thermal_Expansion, 0, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem11, 0, 6, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem12, 0, 5, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem13, 0, 7, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem14, 0, 8, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.CoefficientOfThermalExpansion)
        self.label_6.setStyleSheet("font: 8pt \"Cambria\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout_20.addWidget(self.label_6, 0, 2, 1, 1)
        self.gridLayout_17.addWidget(self.CoefficientOfThermalExpansion, 3, 0, 1, 1)
        self.StressInputs = QtWidgets.QFrame(self.centralwidget)
        self.StressInputs.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.StressInputs.setFrameShadow(QtWidgets.QFrame.Raised)
        self.StressInputs.setObjectName("StressInputs")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.StressInputs)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.EarthLoadStiffnessFactor = QtWidgets.QLabel(self.StressInputs)
        self.EarthLoadStiffnessFactor.setStyleSheet("font: 8pt \"Cambria\";")
        self.EarthLoadStiffnessFactor.setObjectName("EarthLoadStiffnessFactor")
        self.verticalLayout_11.addWidget(self.EarthLoadStiffnessFactor)
        self.EarthLoadBurialFactor = QtWidgets.QLabel(self.StressInputs)
        self.EarthLoadBurialFactor.setStyleSheet("font: 8pt \"Cambria\";")
        self.EarthLoadBurialFactor.setObjectName("EarthLoadBurialFactor")
        self.verticalLayout_11.addWidget(self.EarthLoadBurialFactor)
        self.EarthLoadExcavationFactor = QtWidgets.QLabel(self.StressInputs)
        self.EarthLoadExcavationFactor.setStyleSheet("font: 8pt \"Cambria\";")
        self.EarthLoadExcavationFactor.setObjectName("EarthLoadExcavationFactor")
        self.verticalLayout_11.addWidget(self.EarthLoadExcavationFactor)
        self.gridLayout_2.addLayout(self.verticalLayout_11, 2, 0, 1, 1)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.EarthLoadStiffnessFactor_box = QtWidgets.QLineEdit(self.StressInputs)
        self.EarthLoadStiffnessFactor_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.EarthLoadStiffnessFactor_box.setObjectName("EarthLoadStiffnessFactor_box")
        self.verticalLayout_12.addWidget(self.EarthLoadStiffnessFactor_box)
        self.earthLoadBurialFactor_box = QtWidgets.QLineEdit(self.StressInputs)
        self.earthLoadBurialFactor_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.earthLoadBurialFactor_box.setObjectName("earthLoadBurialFactor_box")
        self.verticalLayout_12.addWidget(self.earthLoadBurialFactor_box)
        self.EarthLoadExcavationFactor_box = QtWidgets.QLineEdit(self.StressInputs)
        self.EarthLoadExcavationFactor_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.EarthLoadExcavationFactor_box.setObjectName("EarthLoadExcavationFactor_box")
        self.verticalLayout_12.addWidget(self.EarthLoadExcavationFactor_box)
        self.gridLayout_2.addLayout(self.verticalLayout_12, 2, 1, 1, 1)
        self.CircumferencialStressDuetoEarthLoad = QtWidgets.QLabel(self.StressInputs)
        self.CircumferencialStressDuetoEarthLoad.setObjectName("CircumferencialStressDuetoEarthLoad")
        self.gridLayout_2.addWidget(self.CircumferencialStressDuetoEarthLoad, 0, 0, 1, 2)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem15, 1, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem16, 0, 1, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.StressInputs)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_7.addWidget(self.line_4, 0, 2, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.FatigurCheckInput = QtWidgets.QLabel(self.StressInputs)
        self.FatigurCheckInput.setObjectName("FatigurCheckInput")
        self.gridLayout_6.addWidget(self.FatigurCheckInput, 0, 0, 1, 2)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_20 = QtWidgets.QLabel(self.StressInputs)
        self.label_20.setStyleSheet("font: 8pt \"Cambria\";")
        self.label_20.setObjectName("label_20")
        self.verticalLayout_20.addWidget(self.label_20)
        self.label_19 = QtWidgets.QLabel(self.StressInputs)
        self.label_19.setStyleSheet("font: 8pt \"Cambria\";")
        self.label_19.setObjectName("label_19")
        self.verticalLayout_20.addWidget(self.label_19)
        self.gridLayout_6.addLayout(self.verticalLayout_20, 2, 2, 1, 1)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.FatigueEnduranceofGirthYield_box = QtWidgets.QLineEdit(self.StressInputs)
        self.FatigueEnduranceofGirthYield_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.FatigueEnduranceofGirthYield_box.setObjectName("FatigueEnduranceofGirthYield_box")
        self.verticalLayout_19.addWidget(self.FatigueEnduranceofGirthYield_box)
        self.FatigueEnduranceofLongitudinalWeld_box = QtWidgets.QLineEdit(self.StressInputs)
        self.FatigueEnduranceofLongitudinalWeld_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.FatigueEnduranceofLongitudinalWeld_box.setObjectName("FatigueEnduranceofLongitudinalWeld_box")
        self.verticalLayout_19.addWidget(self.FatigueEnduranceofLongitudinalWeld_box)
        self.gridLayout_6.addLayout(self.verticalLayout_19, 2, 1, 1, 1)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.FatigueEnduranceofGirthYield = QtWidgets.QLabel(self.StressInputs)
        self.FatigueEnduranceofGirthYield.setStyleSheet("font: 8pt \"Cambria\";")
        self.FatigueEnduranceofGirthYield.setObjectName("FatigueEnduranceofGirthYield")
        self.verticalLayout_18.addWidget(self.FatigueEnduranceofGirthYield)
        self.FatigueEnduranceofLongitudinalWeld = QtWidgets.QLabel(self.StressInputs)
        self.FatigueEnduranceofLongitudinalWeld.setStyleSheet("font: 8pt \"Cambria\";")
        self.FatigueEnduranceofLongitudinalWeld.setObjectName("FatigueEnduranceofLongitudinalWeld")
        self.verticalLayout_18.addWidget(self.FatigueEnduranceofLongitudinalWeld)
        self.gridLayout_6.addLayout(self.verticalLayout_18, 2, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem17, 1, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 9, 1, 1)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.CyclicStressInput = QtWidgets.QLabel(self.StressInputs)
        self.CyclicStressInput.setObjectName("CyclicStressInput")
        self.verticalLayout_17.addWidget(self.CyclicStressInput)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_17.addItem(spacerItem18)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.StiffnessFactorKhh = QtWidgets.QLabel(self.StressInputs)
        self.StiffnessFactorKhh.setStyleSheet("font: 8pt \"Cambria\";")
        self.StiffnessFactorKhh.setObjectName("StiffnessFactorKhh")
        self.verticalLayout_13.addWidget(self.StiffnessFactorKhh)
        self.GeometryFactorGHh = QtWidgets.QLabel(self.StressInputs)
        self.GeometryFactorGHh.setStyleSheet("font: 8pt \"Cambria\";")
        self.GeometryFactorGHh.setObjectName("GeometryFactorGHh")
        self.verticalLayout_13.addWidget(self.GeometryFactorGHh)
        self.gridLayout_3.addLayout(self.verticalLayout_13, 0, 0, 1, 1)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.StiffnessFactorKhh_box = QtWidgets.QLineEdit(self.StressInputs)
        self.StiffnessFactorKhh_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.StiffnessFactorKhh_box.setObjectName("StiffnessFactorKhh_box")
        self.verticalLayout_14.addWidget(self.StiffnessFactorKhh_box)
        self.GeometryFactorGHh_box = QtWidgets.QLineEdit(self.StressInputs)
        self.GeometryFactorGHh_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.GeometryFactorGHh_box.setObjectName("GeometryFactorGHh_box")
        self.verticalLayout_14.addWidget(self.GeometryFactorGHh_box)
        self.gridLayout_3.addLayout(self.verticalLayout_14, 0, 1, 1, 1)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.StifnessFactorKLh = QtWidgets.QLabel(self.StressInputs)
        self.StifnessFactorKLh.setStyleSheet("font: 8pt \"Cambria\";")
        self.StifnessFactorKLh.setObjectName("StifnessFactorKLh")
        self.verticalLayout_15.addWidget(self.StifnessFactorKLh)
        self.geometryFactorGLh = QtWidgets.QLabel(self.StressInputs)
        self.geometryFactorGLh.setStyleSheet("font: 8pt \"Cambria\";")
        self.geometryFactorGLh.setObjectName("geometryFactorGLh")
        self.verticalLayout_15.addWidget(self.geometryFactorGLh)
        self.gridLayout_3.addLayout(self.verticalLayout_15, 0, 2, 1, 1)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.StifnessFactorKLh_box = QtWidgets.QLineEdit(self.StressInputs)
        self.StifnessFactorKLh_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.StifnessFactorKLh_box.setObjectName("StifnessFactorKLh_box")
        self.verticalLayout_16.addWidget(self.StifnessFactorKLh_box)
        self.geometryFactorGLh_box = QtWidgets.QLineEdit(self.StressInputs)
        self.geometryFactorGLh_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.geometryFactorGLh_box.setObjectName("geometryFactorGLh_box")
        self.verticalLayout_16.addWidget(self.geometryFactorGLh_box)
        self.gridLayout_3.addLayout(self.verticalLayout_16, 0, 3, 1, 1)
        self.verticalLayout_17.addLayout(self.gridLayout_3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.RoadPavementFactor = QtWidgets.QLabel(self.StressInputs)
        self.RoadPavementFactor.setStyleSheet("font: 8pt \"Cambria\";")
        self.RoadPavementFactor.setObjectName("RoadPavementFactor")
        self.gridLayout_4.addWidget(self.RoadPavementFactor, 1, 0, 1, 1)
        self.RoadAxleConfigurationFactor_box = QtWidgets.QLineEdit(self.StressInputs)
        self.RoadAxleConfigurationFactor_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.RoadAxleConfigurationFactor_box.setObjectName("RoadAxleConfigurationFactor_box")
        self.gridLayout_4.addWidget(self.RoadAxleConfigurationFactor_box, 0, 1, 1, 1)
        self.RoadPavementFactor_box = QtWidgets.QLineEdit(self.StressInputs)
        self.RoadPavementFactor_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.RoadPavementFactor_box.setObjectName("RoadPavementFactor_box")
        self.gridLayout_4.addWidget(self.RoadPavementFactor_box, 1, 1, 1, 1)
        self.RoadAxleConfigurationFactor = QtWidgets.QLabel(self.StressInputs)
        self.RoadAxleConfigurationFactor.setStyleSheet("font: 8pt \"Cambria\";")
        self.RoadAxleConfigurationFactor.setObjectName("RoadAxleConfigurationFactor")
        self.gridLayout_4.addWidget(self.RoadAxleConfigurationFactor, 0, 0, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem19, 1, 2, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem20, 0, 2, 1, 1)
        self.verticalLayout_17.addLayout(self.gridLayout_4)
        self.gridLayout_7.addLayout(self.verticalLayout_17, 0, 3, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.StressInputs)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_7.addWidget(self.line_5, 0, 5, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.PrincipleStressInput = QtWidgets.QLabel(self.StressInputs)
        self.PrincipleStressInput.setObjectName("PrincipleStressInput")
        self.gridLayout_5.addWidget(self.PrincipleStressInput, 0, 0, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.RadialStress = QtWidgets.QLabel(self.StressInputs)
        self.RadialStress.setStyleSheet("font: 8pt \"Cambria\";")
        self.RadialStress.setObjectName("RadialStress")
        self.horizontalLayout_13.addWidget(self.RadialStress)
        self.RadialStress_box = QtWidgets.QLineEdit(self.StressInputs)
        self.RadialStress_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.RadialStress_box.setObjectName("RadialStress_box")
        self.horizontalLayout_13.addWidget(self.RadialStress_box)
        self.label_18 = QtWidgets.QLabel(self.StressInputs)
        self.label_18.setStyleSheet("font: 8pt \"Cambria\";")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_13.addWidget(self.label_18)
        self.gridLayout_5.addLayout(self.horizontalLayout_13, 2, 0, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem21, 1, 0, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem22, 3, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_5, 0, 6, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem23, 0, 4, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem24, 0, 7, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.StressInputs)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_7.addWidget(self.line_6, 0, 8, 1, 1)
        self.gridLayout_17.addWidget(self.StressInputs, 4, 0, 1, 1)
        self.CalculationFrame = QtWidgets.QFrame(self.centralwidget)
        self.CalculationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CalculationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CalculationFrame.setObjectName("CalculationFrame")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.CalculationFrame)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.Calculation = QtWidgets.QLabel(self.CalculationFrame)
        self.Calculation.setStyleSheet("font: 75 10pt \"Cambria\";")
        self.Calculation.setObjectName("Calculation")
        self.gridLayout_12.addWidget(self.Calculation, 0, 0, 1, 1)
        self.gridLayout_17.addWidget(self.CalculationFrame, 5, 0, 1, 1)
        self.cal1Frame = QtWidgets.QFrame(self.centralwidget)
        self.cal1Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cal1Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cal1Frame.setObjectName("cal1Frame")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.cal1Frame)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.BarlowStress_2 = QtWidgets.QLabel(self.cal1Frame)
        self.BarlowStress_2.setObjectName("BarlowStress_2")
        self.gridLayout_8.addWidget(self.BarlowStress_2, 0, 0, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.barlowStress = QtWidgets.QLabel(self.cal1Frame)
        self.barlowStress.setStyleSheet("font: 8pt \"Cambria\";")
        self.barlowStress.setObjectName("barlowStress")
        self.horizontalLayout_14.addWidget(self.barlowStress)
        self.barlowStress_box = QtWidgets.QLineEdit(self.cal1Frame)
        self.barlowStress_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.barlowStress_box.setObjectName("barlowStress_box")
        self.horizontalLayout_14.addWidget(self.barlowStress_box)
        self.label_21 = QtWidgets.QLabel(self.cal1Frame)
        self.label_21.setStyleSheet("font: 8pt \"Cambria\";")
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_14.addWidget(self.label_21)
        self.gridLayout_8.addLayout(self.horizontalLayout_14, 1, 0, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.CircumferentialStressDuetoEarthLoad_2 = QtWidgets.QLabel(self.cal1Frame)
        self.CircumferentialStressDuetoEarthLoad_2.setObjectName("CircumferentialStressDuetoEarthLoad_2")
        self.gridLayout_11.addWidget(self.CircumferentialStressDuetoEarthLoad_2, 0, 0, 1, 4)
        self.StressDuetoEarthLoad = QtWidgets.QLabel(self.cal1Frame)
        self.StressDuetoEarthLoad.setStyleSheet("font: 8pt \"Cambria\";")
        self.StressDuetoEarthLoad.setObjectName("StressDuetoEarthLoad")
        self.gridLayout_11.addWidget(self.StressDuetoEarthLoad, 1, 0, 1, 1)
        self.StressDuetoEarthLoad_box = QtWidgets.QLineEdit(self.cal1Frame)
        self.StressDuetoEarthLoad_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.StressDuetoEarthLoad_box.setObjectName("StressDuetoEarthLoad_box")
        self.gridLayout_11.addWidget(self.StressDuetoEarthLoad_box, 1, 1, 1, 1)
        self.label_66 = QtWidgets.QLabel(self.cal1Frame)
        self.label_66.setStyleSheet("font: 8pt \"Cambria\";")
        self.label_66.setObjectName("label_66")
        self.gridLayout_11.addWidget(self.label_66, 1, 2, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout_11, 0, 3, 1, 2)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_67 = QtWidgets.QLabel(self.cal1Frame)
        self.label_67.setObjectName("label_67")
        self.gridLayout_9.addWidget(self.label_67, 0, 0, 1, 1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.CyclicCircumferentialStress = QtWidgets.QLabel(self.cal1Frame)
        self.CyclicCircumferentialStress.setStyleSheet("font: 8pt \"Cambria\";")
        self.CyclicCircumferentialStress.setObjectName("CyclicCircumferentialStress")
        self.horizontalLayout_15.addWidget(self.CyclicCircumferentialStress)
        self.CyclicCircumferentialStress_box = QtWidgets.QLineEdit(self.cal1Frame)
        self.CyclicCircumferentialStress_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CyclicCircumferentialStress_box.setObjectName("CyclicCircumferentialStress_box")
        self.horizontalLayout_15.addWidget(self.CyclicCircumferentialStress_box)
        self.label_68 = QtWidgets.QLabel(self.cal1Frame)
        self.label_68.setStyleSheet("font: 8pt \"Cambria\";")
        self.label_68.setObjectName("label_68")
        self.horizontalLayout_15.addWidget(self.label_68)
        self.CyclicLongitudinalStress = QtWidgets.QLabel(self.cal1Frame)
        self.CyclicLongitudinalStress.setStyleSheet("font: 8pt \"Cambria\";")
        self.CyclicLongitudinalStress.setObjectName("CyclicLongitudinalStress")
        self.horizontalLayout_15.addWidget(self.CyclicLongitudinalStress)
        self.CyclicLongitudinalStress_box = QtWidgets.QLineEdit(self.cal1Frame)
        self.CyclicLongitudinalStress_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CyclicLongitudinalStress_box.setObjectName("CyclicLongitudinalStress_box")
        self.horizontalLayout_15.addWidget(self.CyclicLongitudinalStress_box)
        self.label_69 = QtWidgets.QLabel(self.cal1Frame)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.label_69.setFont(font)
        self.label_69.setObjectName("label_69")
        self.horizontalLayout_15.addWidget(self.label_69)
        self.gridLayout_9.addLayout(self.horizontalLayout_15, 1, 0, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout_9, 0, 7, 1, 2)
        self.line_7 = QtWidgets.QFrame(self.cal1Frame)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_14.addWidget(self.line_7, 0, 2, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem25, 0, 1, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem26, 0, 5, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.cal1Frame)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_14.addWidget(self.line_8, 0, 6, 1, 1)
        self.gridLayout_17.addWidget(self.cal1Frame, 6, 0, 1, 1)
        self.Cal2Frame = QtWidgets.QFrame(self.centralwidget)
        self.Cal2Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Cal2Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Cal2Frame.setObjectName("Cal2Frame")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.Cal2Frame)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.line_9 = QtWidgets.QFrame(self.Cal2Frame)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_16.addWidget(self.line_9, 0, 2, 1, 1)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.Circumferential_stress = QtWidgets.QLabel(self.Cal2Frame)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.Circumferential_stress.setFont(font)
        self.Circumferential_stress.setObjectName("Circumferential_stress")
        self.gridLayout_13.addWidget(self.Circumferential_stress, 1, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.Cal2Frame)
        self.label_22.setStyleSheet("font: 8pt \"Cambria\";")
        self.label_22.setObjectName("label_22")
        self.gridLayout_13.addWidget(self.label_22, 1, 2, 1, 1)
        self.Longitudinal_Stress_box = QtWidgets.QLineEdit(self.Cal2Frame)
        self.Longitudinal_Stress_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Longitudinal_Stress_box.setObjectName("Longitudinal_Stress_box")
        self.gridLayout_13.addWidget(self.Longitudinal_Stress_box, 1, 4, 1, 1)
        self.Longitudinal_Stress = QtWidgets.QLabel(self.Cal2Frame)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.Longitudinal_Stress.setFont(font)
        self.Longitudinal_Stress.setObjectName("Longitudinal_Stress")
        self.gridLayout_13.addWidget(self.Longitudinal_Stress, 1, 3, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.Cal2Frame)
        self.label_23.setStyleSheet("font: 8pt \"Cambria\";")
        self.label_23.setObjectName("label_23")
        self.gridLayout_13.addWidget(self.label_23, 1, 5, 1, 1)
        self.Circumferential_stress_box = QtWidgets.QLineEdit(self.Cal2Frame)
        self.Circumferential_stress_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Circumferential_stress_box.setObjectName("Circumferential_stress_box")
        self.gridLayout_13.addWidget(self.Circumferential_stress_box, 1, 1, 1, 1)
        self.CircumferentialStressDueToInternalPressurization = QtWidgets.QLabel(self.Cal2Frame)
        self.CircumferentialStressDueToInternalPressurization.setObjectName("CircumferentialStressDueToInternalPressurization")
        self.gridLayout_13.addWidget(self.CircumferentialStressDueToInternalPressurization, 0, 0, 1, 6)
        self.gridLayout_16.addLayout(self.gridLayout_13, 0, 0, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem27, 0, 1, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.PrincipleStress_3 = QtWidgets.QLabel(self.Cal2Frame)
        self.PrincipleStress_3.setObjectName("PrincipleStress_3")
        self.gridLayout_10.addWidget(self.PrincipleStress_3, 0, 0, 1, 1)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.Effective_stress = QtWidgets.QLabel(self.Cal2Frame)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.Effective_stress.setFont(font)
        self.Effective_stress.setObjectName("Effective_stress")
        self.horizontalLayout_16.addWidget(self.Effective_stress)
        self.Effective_stress_box = QtWidgets.QLineEdit(self.Cal2Frame)
        self.Effective_stress_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Effective_stress_box.setObjectName("Effective_stress_box")
        self.horizontalLayout_16.addWidget(self.Effective_stress_box)
        self.label_24 = QtWidgets.QLabel(self.Cal2Frame)
        self.label_24.setStyleSheet("font: 8pt \"Cambria\";")
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_16.addWidget(self.label_24)
        self.gridLayout_10.addLayout(self.horizontalLayout_16, 1, 0, 1, 1)
        self.gridLayout_16.addLayout(self.gridLayout_10, 0, 3, 1, 1)
        self.gridLayout_17.addWidget(self.Cal2Frame, 7, 0, 1, 1)
        self.ResultFrame = QtWidgets.QFrame(self.centralwidget)
        self.ResultFrame.setStyleSheet("background-color: rgb(11, 119, 130);\n"
"color: rgb(255, 255, 255);")
        self.ResultFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ResultFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ResultFrame.setObjectName("ResultFrame")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.ResultFrame)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.line_17 = QtWidgets.QFrame(self.ResultFrame)
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.gridLayout_19.addWidget(self.line_17, 1, 2, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.ResultFrame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.Submit = QtWidgets.QPushButton(self.frame_4)
        self.Submit.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.869, y1:0.943318, x2:0.0285909, y2:0.0515913, stop:0 rgba(247, 255, 204, 107), stop:1 rgba(199, 255, 254, 255));\n"
"font: 75 8pt \"Cambria\";\n"
"color: rgb(0, 0, 0);")
        self.Submit.setObjectName("Submit")
        self.gridLayout_15.addWidget(self.Submit, 1, 0, 1, 2)
        spacerItem28 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_15.addItem(spacerItem28, 0, 0, 1, 1)
        self.gridLayout_19.addWidget(self.frame_4, 1, 6, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_19.addItem(spacerItem29, 1, 7, 1, 1)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_19.addItem(spacerItem30, 1, 4, 1, 1)
        self.line_16 = QtWidgets.QFrame(self.ResultFrame)
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.gridLayout_19.addWidget(self.line_16, 1, 5, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.ResulWindow = QtWidgets.QLabel(self.ResultFrame)
        self.ResulWindow.setStyleSheet("font: 75 10pt \"Cambria\";")
        self.ResulWindow.setObjectName("ResulWindow")
        self.horizontalLayout_22.addWidget(self.ResulWindow)
        self.horizontalLayout.addLayout(self.horizontalLayout_22)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem31)
        self.line_15 = QtWidgets.QFrame(self.ResultFrame)
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.horizontalLayout.addWidget(self.line_15)
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.BarlowStress_Result = QtWidgets.QLabel(self.ResultFrame)
        self.BarlowStress_Result.setObjectName("BarlowStress_Result")
        self.verticalLayout_26.addWidget(self.BarlowStress_Result)
        self.barlowStress_criteriacheck = QtWidgets.QLabel(self.ResultFrame)
        self.barlowStress_criteriacheck.setStyleSheet("font: 8pt \"Cambria\";")
        self.barlowStress_criteriacheck.setObjectName("barlowStress_criteriacheck")
        self.verticalLayout_26.addWidget(self.barlowStress_criteriacheck)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.BarlowSafe_radioButton = QtWidgets.QRadioButton(self.ResultFrame)
        self.BarlowSafe_radioButton.setObjectName("BarlowSafe_radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.BarlowSafe_radioButton)
        self.horizontalLayout_20.addWidget(self.BarlowSafe_radioButton)
        self.BarlowNotSafe_radioButton = QtWidgets.QRadioButton(self.ResultFrame)
        self.BarlowNotSafe_radioButton.setObjectName("BarlowNotSafe_radioButton")
        self.buttonGroup.addButton(self.BarlowNotSafe_radioButton)
        self.horizontalLayout_20.addWidget(self.BarlowNotSafe_radioButton)
        self.verticalLayout_26.addLayout(self.horizontalLayout_20)
        self.horizontalLayout.addLayout(self.verticalLayout_26)
        self.line_14 = QtWidgets.QFrame(self.ResultFrame)
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.horizontalLayout.addWidget(self.line_14)
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.PrincipleStress_Result = QtWidgets.QLabel(self.ResultFrame)
        self.PrincipleStress_Result.setObjectName("PrincipleStress_Result")
        self.verticalLayout_25.addWidget(self.PrincipleStress_Result)
        self.PrincipleStress_CriteriaCheck = QtWidgets.QLabel(self.ResultFrame)
        self.PrincipleStress_CriteriaCheck.setStyleSheet("font: 8pt \"Cambria\";")
        self.PrincipleStress_CriteriaCheck.setObjectName("PrincipleStress_CriteriaCheck")
        self.verticalLayout_25.addWidget(self.PrincipleStress_CriteriaCheck)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.PrincipleSafe_radioButton = QtWidgets.QRadioButton(self.ResultFrame)
        self.PrincipleSafe_radioButton.setObjectName("PrincipleSafe_radioButton")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.PrincipleSafe_radioButton)
        self.horizontalLayout_19.addWidget(self.PrincipleSafe_radioButton)
        self.PrincipleNotSafe_raadioButton = QtWidgets.QRadioButton(self.ResultFrame)
        self.PrincipleNotSafe_raadioButton.setObjectName("PrincipleNotSafe_raadioButton")
        self.buttonGroup_2.addButton(self.PrincipleNotSafe_raadioButton)
        self.horizontalLayout_19.addWidget(self.PrincipleNotSafe_raadioButton)
        self.verticalLayout_25.addLayout(self.horizontalLayout_19)
        self.horizontalLayout.addLayout(self.verticalLayout_25)
        self.gridLayout_19.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.Fatigue_Check_Result = QtWidgets.QLabel(self.ResultFrame)
        self.Fatigue_Check_Result.setObjectName("Fatigue_Check_Result")
        self.verticalLayout_27.addWidget(self.Fatigue_Check_Result)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.GirthWeldCriteriaCheck = QtWidgets.QLabel(self.ResultFrame)
        self.GirthWeldCriteriaCheck.setStyleSheet("font: 8pt \"Cambria\";")
        self.GirthWeldCriteriaCheck.setObjectName("GirthWeldCriteriaCheck")
        self.verticalLayout_23.addWidget(self.GirthWeldCriteriaCheck)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.FatigueSafe_radioButton = QtWidgets.QRadioButton(self.ResultFrame)
        self.FatigueSafe_radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.FatigueSafe_radioButton.setObjectName("FatigueSafe_radioButton")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.FatigueSafe_radioButton)
        self.horizontalLayout_18.addWidget(self.FatigueSafe_radioButton)
        self.FatigueNotSafeGirthWeld_radiButton = QtWidgets.QRadioButton(self.ResultFrame)
        self.FatigueNotSafeGirthWeld_radiButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.FatigueNotSafeGirthWeld_radiButton.setObjectName("FatigueNotSafeGirthWeld_radiButton")
        self.buttonGroup_3.addButton(self.FatigueNotSafeGirthWeld_radiButton)
        self.horizontalLayout_18.addWidget(self.FatigueNotSafeGirthWeld_radiButton)
        self.verticalLayout_21.addLayout(self.horizontalLayout_18)
        self.verticalLayout_23.addLayout(self.verticalLayout_21)
        self.horizontalLayout_21.addLayout(self.verticalLayout_23)
        self.line_18 = QtWidgets.QFrame(self.ResultFrame)
        self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.horizontalLayout_21.addWidget(self.line_18)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.LongitudinalYieldsCriteriaCheck = QtWidgets.QLabel(self.ResultFrame)
        self.LongitudinalYieldsCriteriaCheck.setStyleSheet("font: 8pt \"Cambria\";")
        self.LongitudinalYieldsCriteriaCheck.setObjectName("LongitudinalYieldsCriteriaCheck")
        self.verticalLayout_24.addWidget(self.LongitudinalYieldsCriteriaCheck)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.FatigueCheckLongitudinalYields_Safe = QtWidgets.QRadioButton(self.ResultFrame)
        self.FatigueCheckLongitudinalYields_Safe.setStyleSheet("color: rgb(255, 255, 255);")
        self.FatigueCheckLongitudinalYields_Safe.setObjectName("FatigueCheckLongitudinalYields_Safe")
        self.buttonGroup_4 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_4.setObjectName("buttonGroup_4")
        self.buttonGroup_4.addButton(self.FatigueCheckLongitudinalYields_Safe)
        self.horizontalLayout_23.addWidget(self.FatigueCheckLongitudinalYields_Safe)
        self.FatigueCheckLongitudinalYields_NotSafe = QtWidgets.QRadioButton(self.ResultFrame)
        self.FatigueCheckLongitudinalYields_NotSafe.setStyleSheet("color: rgb(255, 255, 255);")
        self.FatigueCheckLongitudinalYields_NotSafe.setObjectName("FatigueCheckLongitudinalYields_NotSafe")
        self.buttonGroup_4.addButton(self.FatigueCheckLongitudinalYields_NotSafe)
        self.horizontalLayout_23.addWidget(self.FatigueCheckLongitudinalYields_NotSafe)
        self.verticalLayout_22.addLayout(self.horizontalLayout_23)
        self.verticalLayout_24.addLayout(self.verticalLayout_22)
        self.horizontalLayout_21.addLayout(self.verticalLayout_24)
        self.verticalLayout_27.addLayout(self.horizontalLayout_21)
        self.gridLayout_19.addLayout(self.verticalLayout_27, 1, 3, 1, 1)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_19.addItem(spacerItem32, 1, 1, 1, 1)
        self.gridLayout_17.addWidget(self.ResultFrame, 8, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1307, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuReport = QtWidgets.QMenu(self.menubar)
        self.menuReport.setObjectName("menuReport")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.New = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/new.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.New.setIcon(icon)
        self.New.setObjectName("New")
        self.Open = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/open.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Open.setIcon(icon1)
        self.Open.setObjectName("Open")
        self.SaveAs = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/save_as_dis.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SaveAs.setIcon(icon2)
        self.SaveAs.setObjectName("SaveAs")
        self.Exit = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/close.png.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Exit.setIcon(icon3)
        self.Exit.setObjectName("Exit")
        self.actionReset = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/page_setup.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReset.setIcon(icon4)
        self.actionReset.setObjectName("actionReset")
        self.actionGenerate_Report = QtWidgets.QAction(MainWindow)
        self.actionGenerate_Report.setObjectName("actionGenerate_Report")
        self.actionWhat_s_New = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/help_dis.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionWhat_s_New.setIcon(icon5)
        self.actionWhat_s_New.setObjectName("actionWhat_s_New")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.menuFile.addAction(self.New)
        self.menuFile.addAction(self.Open)
        self.menuFile.addAction(self.SaveAs)
        self.menuFile.addAction(self.Exit)
        self.menuEdit.addAction(self.actionReset)
        self.menuReport.addAction(self.actionGenerate_Report)
        self.menuHelp.addAction(self.actionWhat_s_New)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuReport.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pipeline Crossing Simulation"))
        self.PipelineCrossingCalulation.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline; color:#ffffff;\">Pipeline Crossing Simulation</span></p></body></html>"))
        self.Pipe_Type.setText(_translate("MainWindow", "Pipe Type:"))
        self.PipeType_combobox.setItemText(0, _translate("MainWindow", "Seamless"))
        self.PipeType_combobox.setItemText(1, _translate("MainWindow", "SAW"))
        self.PipeType_combobox.setItemText(2, _translate("MainWindow", "ERW"))
        self.Soil_Type.setText(_translate("MainWindow", "Soil Type:"))
        self.SoilType_combobox.setItemText(0, _translate("MainWindow", "Soft To Medium Clay"))
        self.Codes_and_standards_2.setText(_translate("MainWindow", "Bored Diametrer:"))
        self.BoredDiameter_combobox.setItemText(0, _translate("MainWindow", "Considered"))
        self.BoredDiameter_combobox.setItemText(1, _translate("MainWindow", "Not Considered"))
        self.Streel_grade.setText(_translate("MainWindow", "Steel Grade:"))
        self.SteelGrade_Combobox.setItemText(0, _translate("MainWindow", "Fe 330"))
        self.SteelGrade_Combobox.setItemText(1, _translate("MainWindow", "A25"))
        self.SteelGrade_Combobox.setItemText(2, _translate("MainWindow", "A"))
        self.SteelGrade_Combobox.setItemText(3, _translate("MainWindow", "B"))
        self.SteelGrade_Combobox.setItemText(4, _translate("MainWindow", "X42"))
        self.SteelGrade_Combobox.setItemText(5, _translate("MainWindow", "X46"))
        self.SteelGrade_Combobox.setItemText(6, _translate("MainWindow", "X52"))
        self.SteelGrade_Combobox.setItemText(7, _translate("MainWindow", "X56"))
        self.SteelGrade_Combobox.setItemText(8, _translate("MainWindow", "X60"))
        self.SteelGrade_Combobox.setItemText(9, _translate("MainWindow", "X65"))
        self.SteelGrade_Combobox.setItemText(10, _translate("MainWindow", "X70"))
        self.SteelGrade_Combobox.setItemText(11, _translate("MainWindow", "X80"))
        self.Codes_and_standards.setText(_translate("MainWindow", "Codes & Standards:"))
        self.CodesAndStandards_combobox.setItemText(0, _translate("MainWindow", "API 1102"))
        self.CodesAndStandards_combobox.setItemText(1, _translate("MainWindow", "ISO"))
        self.CodesAndStandards_combobox.setItemText(2, _translate("MainWindow", "IS"))
        self.PipeWallThicknessIncluding_CA.setText(_translate("MainWindow", "<html><head/><body><p>Pipe Wall Thickness including CA_(t<span style=\" vertical-align:sub;\">w</span>):</p></body></html>"))
        self.BoredDiameter.setText(_translate("MainWindow", "<html><head/><body><p>Bored Diameter_(B<span style=\" vertical-align:sub;\">d</span>):</p></body></html>"))
        self.SoilunitWeight.setText(_translate("MainWindow", "Soil Unit Weight_(γ):"))
        self.ModulusofSoilReaction.setText(_translate("MainWindow", "Modulus of Soil Reaction_(E\'):"))
        self.ResilientModulus.setText(_translate("MainWindow", "<html><head/><body><p>Resilient Modulus_(E<span style=\" vertical-align:sub;\">r</span>):</p></body></html>"))
        self.label_26.setText(_translate("MainWindow", "mm"))
        self.label_27.setText(_translate("MainWindow", "mm"))
        self.label_29.setText(_translate("MainWindow", "kN/m³"))
        self.label_30.setText(_translate("MainWindow", "MPa"))
        self.label_31.setText(_translate("MainWindow", "MPa"))
        self.OperatingPressure.setText(_translate("MainWindow", "Operating Pressure:_(p)"))
        self.ImpactFactor.setText(_translate("MainWindow", "<html><head/><body><p>Impact Factor(F<span style=\" vertical-align:sub;\">i</span>):</p></body></html>"))
        self.DesignFactor.setText(_translate("MainWindow", "Design Factor_(F):"))
        self.LongitudinalJointFactor.setText(_translate("MainWindow", "Longitudinal Joint Factor_(E):"))
        self.InstallationTemperature.setText(_translate("MainWindow", "<html><head/><body><p>Installation Temperature_(T<span style=\" vertical-align:sub;\">1</span>):</p></body></html>"))
        self.OutsideDiameter.setText(_translate("MainWindow", "Pipe Outside Diameter_(D):"))
        self.PipeWallThickness_2.setText(_translate("MainWindow", "Pipe Wall Thickness_(t):"))
        self.SpecifiedMinimumYieldStrength.setText(_translate("MainWindow", "Specified Minimum Yield Strength_(SMYS):"))
        self.DepthOfCover.setText(_translate("MainWindow", "Depth Of Cover_(H):"))
        self.CorrosionAllowence.setText(_translate("MainWindow", "Corrossion Allowence(CA):"))
        self.label_11.setText(_translate("MainWindow", "mm"))
        self.label_12.setText(_translate("MainWindow", "mm"))
        self.label_13.setText(_translate("MainWindow", "MPa"))
        self.label_14.setText(_translate("MainWindow", "m"))
        self.label_15.setText(_translate("MainWindow", "mm"))
        self.bar.setText(_translate("MainWindow", "bar"))
        self.centigrade.setText(_translate("MainWindow", "°C"))
        self.OperatingTemperature.setText(_translate("MainWindow", "<html><head/><body><p>Operating Temperature_(T<span style=\" vertical-align:sub;\">2</span>):</p></body></html>"))
        self.DesignWheelLoadFromSingleAxle.setText(_translate("MainWindow", "<html><head/><body><p>Design Wheel load from Single Axle_(P<span style=\" vertical-align:sub;\">s</span>):</p></body></html>"))
        self.DesignWheelLoadFromTandemAxle.setText(_translate("MainWindow", "<html><head/><body><p>Design Wheel load from Tandem Axle(P<span style=\" vertical-align:sub;\">t</span>):</p></body></html>"))
        self.YoungsModulus.setText(_translate("MainWindow", "<html><head/><body><p>Young\'s Modulus_(E<span style=\" vertical-align:sub;\">s</span>):</p></body></html>"))
        self.PoissonsRatio.setText(_translate("MainWindow", "Poisson\'s Ratio_(μ):"))
        self.label_39.setText(_translate("MainWindow", "°C"))
        self.label_40.setText(_translate("MainWindow", "kN"))
        self.label_41.setText(_translate("MainWindow", "kN"))
        self.label_42.setText(_translate("MainWindow", "MPa"))
        self.Coefficient_Of_Thermal_Expansion.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:600; text-decoration: underline;\">COEFFECIENT OF THERMAL EXPANSION_(</span>α<span style=\" vertical-align:sub;\">T</span>)</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">1/°C</span></p></body></html>"))
        self.EarthLoadStiffnessFactor.setText(_translate("MainWindow", "<html><head/><body><p>Earth Load Stiffness Factor_(K<span style=\" vertical-align:sub;\">He</span>):</p></body></html>"))
        self.EarthLoadBurialFactor.setText(_translate("MainWindow", "<html><head/><body><p>Earth Load Burial Factor_(B<span style=\" vertical-align:sub;\">e</span>):</p></body></html>"))
        self.EarthLoadExcavationFactor.setText(_translate("MainWindow", "<html><head/><body><p>Earth Load Excavation Factor_(E<span style=\" vertical-align:sub;\">e</span>):</p></body></html>"))
        self.CircumferencialStressDuetoEarthLoad.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Circumferencial Stress Due to Earth Load:</span></p></body></html>"))
        self.FatigurCheckInput.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Fatigue Check:</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "MPa"))
        self.label_19.setText(_translate("MainWindow", "MPa"))
        self.FatigueEnduranceofGirthYield.setText(_translate("MainWindow", "<html><head/><body><p>Fatigue Endurance Limit Of Girth Yield_(S<span style=\" vertical-align:sub;\">FG</span>):</p></body></html>"))
        self.FatigueEnduranceofLongitudinalWeld.setText(_translate("MainWindow", "<html><head/><body><p>Fatigue Endurance Limit Of Longitudinal Weld_(S<span style=\" vertical-align:sub;\">FL</span>):</p></body></html>"))
        self.CyclicStressInput.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Cyclic Stress:</span></p></body></html>"))
        self.StiffnessFactorKhh.setText(_translate("MainWindow", "<html><head/><body><p>Stifness Factor_(K<span style=\" vertical-align:sub;\">Hh</span>):</p></body></html>"))
        self.GeometryFactorGHh.setText(_translate("MainWindow", "<html><head/><body><p>Geometry Factor_(G<span style=\" vertical-align:sub;\">Hh)</span>:</p></body></html>"))
        self.StifnessFactorKLh.setText(_translate("MainWindow", "<html><head/><body><p>Stifness Factor_(K<span style=\" vertical-align:sub;\">Lh</span>):</p></body></html>"))
        self.geometryFactorGLh.setText(_translate("MainWindow", "<html><head/><body><p>Geometry Factor_(G<span style=\" vertical-align:sub;\">Lh</span>):</p></body></html>"))
        self.RoadPavementFactor.setText(_translate("MainWindow", "<html><head/><body><p>Road Pavement Type Factor_(R):</p></body></html>"))
        self.RoadAxleConfigurationFactor.setText(_translate("MainWindow", "<html><head/><body><p>Road Axle Configuration Factor_(L):</p></body></html>"))
        self.PrincipleStressInput.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Principle Stress:</span></p></body></html>"))
        self.RadialStress.setText(_translate("MainWindow", "<html><head/><body><p>Radial Stress_(S<span style=\" vertical-align:sub;\">3</span>) :</p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "MPa"))
        self.Calculation.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">CALCULATION:</span></p></body></html>"))
        self.BarlowStress_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">(A) BARLOW STRESS:</span></p></body></html>"))
        self.barlowStress.setText(_translate("MainWindow", "<html><head/><body><p>Barlow Stress_(S<span style=\" vertical-align:sub;\">Hi</span>):</p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "MPa"))
        self.CircumferentialStressDuetoEarthLoad_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">(B) CIRCUMFERENTIAL STRESS DUE TO EARTH LOAD:</span></p></body></html>"))
        self.StressDuetoEarthLoad.setText(_translate("MainWindow", "<html><head/><body><p>Stress Due to Earth Load_(S<span style=\" vertical-align:sub;\">He</span>):</p></body></html>"))
        self.label_66.setText(_translate("MainWindow", "MPa"))
        self.label_67.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">(C) CYCLIC STRESS:</span></p></body></html>"))
        self.CyclicCircumferentialStress.setText(_translate("MainWindow", "<html><head/><body><p>Cyclic Circumferential Stress_(ΔS<span style=\" vertical-align:sub;\">Hh</span>):</p></body></html>"))
        self.label_68.setText(_translate("MainWindow", "MPa"))
        self.CyclicLongitudinalStress.setText(_translate("MainWindow", "<html><head/><body><p>Cyclic Longitudinal Stress_(ΔS<span style=\" vertical-align:sub;\">Lh</span>):</p></body></html>"))
        self.label_69.setText(_translate("MainWindow", "MPa"))
        self.Circumferential_stress.setText(_translate("MainWindow", "<html><head/><body><p>Circumferential Stress_(S<span style=\" vertical-align:sub;\">1</span>):</p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "MPa"))
        self.Longitudinal_Stress.setText(_translate("MainWindow", "<html><head/><body><p>Longitudinal Stress_(S<span style=\" vertical-align:sub;\">2)</span>:</p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "MPa"))
        self.CircumferentialStressDueToInternalPressurization.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">(D)CIRCUMFERENTIAL STRESS DUE TO INTERNAL PRESSURIZATION:</span></p></body></html>"))
        self.PrincipleStress_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">(E)PRINCIPLE STRESSES:</span></p></body></html>"))
        self.Effective_stress.setText(_translate("MainWindow", "<html><head/><body><p>Effective Stresses_(S<span style=\" vertical-align:sub;\">eff</span>):</p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "MPa"))
        self.Submit.setText(_translate("MainWindow", "SUBMIT"))
        self.ResulWindow.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline; color:#ffffff;\">RESULT WINDOW:</span></p></body></html>"))
        self.BarlowStress_Result.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">(A) BARLOW STRESS:</span></p></body></html>"))
        self.barlowStress_criteriacheck.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Criteria Check:</span></p></body></html>"))
        self.BarlowSafe_radioButton.setText(_translate("MainWindow", "SAFE"))
        self.BarlowNotSafe_radioButton.setText(_translate("MainWindow", "NOT SAFE"))
        self.PrincipleStress_Result.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">(B) PRINCIPLE STRESSES:</span></p></body></html>"))
        self.PrincipleStress_CriteriaCheck.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Criteria Check:</span></p></body></html>"))
        self.PrincipleSafe_radioButton.setText(_translate("MainWindow", "SAFE"))
        self.PrincipleNotSafe_raadioButton.setText(_translate("MainWindow", "NOT SAFE"))
        self.Fatigue_Check_Result.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">(C) FATIGUE CHECK:</span></p></body></html>"))
        self.GirthWeldCriteriaCheck.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Girth Weld Criteria Check:</span></p></body></html>"))
        self.FatigueSafe_radioButton.setText(_translate("MainWindow", "SAFE"))
        self.FatigueNotSafeGirthWeld_radiButton.setText(_translate("MainWindow", "NOT SAFE"))
        self.LongitudinalYieldsCriteriaCheck.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Longitudinal Yields Criteria Check:</span></p></body></html>"))
        self.FatigueCheckLongitudinalYields_Safe.setText(_translate("MainWindow", "SAFE"))
        self.FatigueCheckLongitudinalYields_NotSafe.setText(_translate("MainWindow", "NOT SAFE"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuReport.setTitle(_translate("MainWindow", "Report"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.New.setText(_translate("MainWindow", "New"))
        self.New.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.Open.setText(_translate("MainWindow", "Open"))
        self.Open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.SaveAs.setText(_translate("MainWindow", "Save As"))
        self.SaveAs.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.Exit.setText(_translate("MainWindow", "Exit"))
        self.Exit.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionReset.setText(_translate("MainWindow", "Reset"))
        self.actionReset.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionGenerate_Report.setText(_translate("MainWindow", "Generate Report"))
        self.actionGenerate_Report.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.actionWhat_s_New.setText(_translate("MainWindow", "What\'s New?"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionDocumentation.setShortcut(_translate("MainWindow", "F1"))


# --- Ui_Dialog (from loadingbox.py) ---
# This class defines the loading dialog's UI.
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(373, 288)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 46, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(54, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.AshkamLogo = QtWidgets.QLabel(self.frame)
        self.AshkamLogo.setText("")
        # Placeholder for image path. Ensure 'ashkam.jpg' is accessible or remove this line.
        self.AshkamLogo.setPixmap(QtGui.QPixmap("ashkam.png"))
        self.AshkamLogo.setObjectName("AshkamLogo")
        self.gridLayout.addWidget(self.AshkamLogo, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.PipelineCrossingSimulation = QtWidgets.QLabel(Dialog)
        self.PipelineCrossingSimulation.setStyleSheet("font: 18pt \"Cambria\";")
        self.PipelineCrossingSimulation.setObjectName("PipelineCrossingSimulation")
        self.verticalLayout.addWidget(self.PipelineCrossingSimulation)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.Loading = QtWidgets.QLabel(Dialog)
        self.Loading.setStyleSheet("font: 10pt \"Cambria\";")
        self.Loading.setObjectName("Loading")
        self.verticalLayout.addWidget(self.Loading)

        # Add QProgressBar here, below the Loading label
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setValue(0) # Initial value
        self.verticalLayout.addWidget(self.progressBar) # Add to the vertical layout

        self.gridLayout_2.addLayout(self.verticalLayout, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(53, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 1, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 45, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem7, 2, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Loading...")) # Changed window title
        self.PipelineCrossingSimulation.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">Pipeline Crossing Simulation</span></p></body></html>"))
        self.Loading.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Loading.....</p></body></html>"))


# --- LoadingScreen Class ---
class LoadingScreen(QtWidgets.QDialog):
    """
    A custom loading screen dialog with a progress bar.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.SplashScreen | QtCore.Qt.FramelessWindowHint) # Make it a splash screen
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose) # Ensure it's deleted when closed

        self.progress_timer = QtCore.QTimer(self)
        self.progress_timer.timeout.connect(self.update_progress)
        self.current_progress = 0
        self.duration = 5000 # 5 seconds in milliseconds
        self.interval = 50 # Update every 50 ms
        self.steps = self.duration // self.interval

    def start_loading(self):
        """Starts the progress bar animation."""
        self.progress_timer.start(self.interval)

    def update_progress(self):
        """Updates the progress bar value."""
        self.current_progress += 1
        if self.current_progress <= self.steps:
            progress_value = int((self.current_progress / self.steps) * 100)
            self.ui.progressBar.setValue(progress_value)
        else:
            self.progress_timer.stop()
            self.accept() # Close the dialog


# Worker Thread for Calculations
class CalculationWorker(QtCore.QThread):
    """
    A QThread subclass to perform calculations in a separate thread,
    preventing the UI from freezing.
    """
    calculation_finished = QtCore.pyqtSignal(dict) # Signal to emit results back to main thread
    calculation_error = QtCore.pyqtSignal(str) # Signal to emit error messages

    def __init__(self, inputs, parent=None):
        super().__init__(parent)
        self.inputs = inputs

    def run(self):
        """
        Performs the pipeline stress calculations.
        Includes a simulated delay.
        """
        try:
            # Unpack inputs
            pipe_outside_diameter = self.inputs['pipe_outside_diameter']
            pipe_wall_thickness = self.inputs['pipe_wall_thickness']
            specified_minimum_yield_strength = self.inputs['specified_minimum_yield_strength']
            depth_of_cover = self.inputs['depth_of_cover']
            corrosion_allowance = self.inputs['corrosion_allowance']
            consider_bored_diameter_in_calc = self.inputs['consider_bored_diameter_in_calc']
            soil_unit_weight = self.inputs['soil_unit_weight']
            modulus_of_soil_reaction = self.inputs['modulus_of_soil_reaction']
            resilient_modulus = self.inputs['resilient_modulus']
            operating_pressure = self.inputs['operating_pressure']
            impact_factor = self.inputs['impact_factor']
            design_factor = self.inputs['design_factor']
            longitudinal_joint_factor = self.inputs['longitudinal_joint_factor']
            installation_temperature = self.inputs['installation_temperature']
            operating_temperature = self.inputs['operating_temperature']
            design_wheel_load_single_axle = self.inputs['design_wheel_load_single_axle']
            design_wheel_load_tandem_axle = self.inputs['design_wheel_load_tandem_axle']
            youngs_modulus = self.inputs['youngs_modulus']
            poissons_ratio = self.inputs['poissons_ratio']
            coefficient_of_thermal_expansion = self.inputs['coefficient_of_thermal_expansion']
            earth_load_stiffness_factor = self.inputs['earth_load_stiffness_factor']
            earth_load_burial_factor = self.inputs['earth_load_burial_factor']
            earth_load_excavation_factor = self.inputs['earth_load_excavation_factor']
            stiffness_factor_khh = self.inputs['stiffness_factor_khh']
            geometry_factor_ghh = self.inputs['geometry_factor_ghh']
            stiffness_factor_klh = self.inputs['stiffness_factor_klh']
            geometry_factor_glh = self.inputs['geometry_factor_glh']
            road_pavement_type_factor = self.inputs['road_pavement_type_factor']
            road_axle_configuration_factor = self.inputs['road_axle_configuration_factor']
            radial_stress = self.inputs['radial_stress']
            fatigue_endurance_girth_yield = self.inputs['fatigue_endurance_girth_yield']
            fatigue_endurance_longitudinal_weld = self.inputs['fatigue_endurance_longitudinal_weld']

            # Simulate a time-consuming calculation
            time.sleep(5) # 5-second delay as requested

            # Perform calculations
            pipe_wall_thickness_including_ca = (pipe_wall_thickness - corrosion_allowance)

            bored_diameter = 0
            if consider_bored_diameter_in_calc:
                bored_diameter = pipe_outside_diameter + 51
            else:
                bored_diameter = pipe_outside_diameter

            thickness_to_diameter_ratio = (pipe_wall_thickness_including_ca / pipe_outside_diameter)
            thickness_to_diameter_ratio = round(thickness_to_diameter_ratio, 5)

            ratio_of_bore_diameter_and_pipe_diameter = (bored_diameter / pipe_outside_diameter)
            ratio_of_bore_diameter_and_pipe_diameter = round(ratio_of_bore_diameter_and_pipe_diameter, 2)

            ratio_of_pipe_dept_and_bore_diameter = (depth_of_cover * 1000) / bored_diameter
            ratio_of_pipe_dept_and_bore_diameter = round(ratio_of_pipe_dept_and_bore_diameter, 3)

            applied_design_surface_pressure = round(design_wheel_load_tandem_axle / 0.093) / 1000

            barlow_stress = 0
            if pipe_wall_thickness_including_ca != 0:
                barlow_stress = (operating_pressure * (pipe_outside_diameter - pipe_wall_thickness_including_ca)) / (2 * pipe_wall_thickness_including_ca)
            # No else needed, as it defaults to 0 if division by zero would occur
            barlow_stress = round(barlow_stress, 3)

            f_e_smys = (design_factor * longitudinal_joint_factor * specified_minimum_yield_strength)

            stress_due_to_earth_load = (earth_load_stiffness_factor * earth_load_burial_factor * earth_load_excavation_factor * soil_unit_weight * pipe_outside_diameter) / 1_000_000
            stress_due_to_earth_load = round(stress_due_to_earth_load, 3)

            cyclic_circumferential_stress = (stiffness_factor_khh * geometry_factor_ghh * road_pavement_type_factor * road_axle_configuration_factor * impact_factor * applied_design_surface_pressure)
            cyclic_circumferential_stress = round(cyclic_circumferential_stress, 3)

            cyclic_longitudinal_stress = (stiffness_factor_klh * geometry_factor_glh * road_pavement_type_factor * road_axle_configuration_factor * impact_factor * applied_design_surface_pressure)
            cyclic_longitudinal_stress = round(cyclic_longitudinal_stress, 3)

            circumferential_stress_s1 = stress_due_to_earth_load + cyclic_circumferential_stress + barlow_stress
            longitudinal_stress_s2 = cyclic_longitudinal_stress - youngs_modulus * coefficient_of_thermal_expansion * (operating_temperature - installation_temperature) + poissons_ratio * (stress_due_to_earth_load + barlow_stress)

            effective_stress = math.sqrt(1/2*((circumferential_stress_s1 - longitudinal_stress_s2)**2 + \
                                             (longitudinal_stress_s2 - radial_stress)**2 + \
                                             (radial_stress - circumferential_stress_s1)**2))
            effective_stress = round(effective_stress, 3)

            # Prepare results to be sent back
            results = {
                'pipe_wall_thickness_including_ca': pipe_wall_thickness_including_ca,
                'bored_diameter': bored_diameter,
                'barlow_stress': barlow_stress,
                'f_e_smys': f_e_smys,
                'stress_due_to_earth_load': stress_due_to_earth_load,
                'cyclic_circumferential_stress': cyclic_circumferential_stress,
                'cyclic_longitudinal_stress': cyclic_longitudinal_stress,
                'circumferential_stress_s1': circumferential_stress_s1,
                'longitudinal_stress_s2': longitudinal_stress_s2,
                'effective_stress': effective_stress,
                'specified_minimum_yield_strength': specified_minimum_yield_strength,
                'design_factor': design_factor,
                'fatigue_endurance_girth_yield': fatigue_endurance_girth_yield,
                'fatigue_endurance_longitudinal_weld': fatigue_endurance_longitudinal_weld
            }
            self.calculation_finished.emit(results)

        except ValueError as e:
            self.calculation_error.emit(f"Calculation Error: Invalid numerical input. {e}")
        except Exception as e:
            self.calculation_error.emit(f"An unexpected error occurred during calculation: {e}")


# Main Application Logic
class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Instance variables to hold selected combobox values or flags
        self.selected_pipe_type = "Seamless"
        self.selected_soil_type = "Soft To Medium Clay"
        self.consider_bored_diameter_in_calc = True # Default based on "Considered"
        self.steel_grade_smys = 195 # Default SMYS for Fe 330 (initial value)
        self.selected_codes_standards = "API 1102"

        self.calculation_worker = None # To hold the worker thread instance
        self.loading_dialog = None # To hold the loading dialog instance

        self.connect_signals_slots()
        self.initialize_default_input_values()

    def connect_signals_slots(self):
        """Connects UI signals to their corresponding slot methods."""
        # Combobox signals
        self.ui.PipeType_combobox.currentIndexChanged.connect(self.on_pipe_type_changed)
        self.ui.SoilType_combobox.currentIndexChanged.connect(self.on_soil_type_changed)
        self.ui.BoredDiameter_combobox.currentIndexChanged.connect(self.on_bored_diameter_changed)
        self.ui.SteelGrade_Combobox.currentIndexChanged.connect(self.on_steel_grade_changed)
        self.ui.CodesAndStandards_combobox.currentIndexChanged.connect(self.on_codes_standards_changed)

        # Button and Action signals
        self.ui.Submit.clicked.connect(self.start_calculation_thread) # Connect to start_calculation_thread
        self.ui.New.triggered.connect(self.new_file)
        self.ui.Open.triggered.connect(self.open_file)
        self.ui.SaveAs.triggered.connect(self.save_file_as)
        self.ui.Exit.triggered.connect(self.close) # Built-in close method
        self.ui.actionReset.triggered.connect(self.reset_all_inputs)
        self.ui.actionGenerate_Report.triggered.connect(self.generate_report)
        self.ui.actionWhat_s_New.triggered.connect(self.show_whats_new)
        self.ui.actionDocumentation.triggered.connect(self.show_documentation)

        # Trigger initial combobox handlers to set default instance variables
        self.on_pipe_type_changed(self.ui.PipeType_combobox.currentIndex())
        self.on_soil_type_changed(self.ui.SoilType_combobox.currentIndex())
        self.on_bored_diameter_changed(self.ui.BoredDiameter_combobox.currentIndex())
        self.on_steel_grade_changed(self.ui.SteelGrade_Combobox.currentIndex())
        self.on_codes_standards_changed(self.ui.CodesAndStandards_combobox.currentIndex())


    def initialize_default_input_values(self):
        """Sets default numerical values in the QLineEdit fields."""
        # Clear all numerical input fields
        self.ui.PipeOutsideDiameter_box.clear()
        self.ui.PipeWallThickness_box.clear()
        # SMYS will be set by the combobox handler, so clear it initially
        self.ui.SpecifiedMinimumYieldStrength_box.clear()
        self.ui.DepthOfCover_box.clear()
        self.ui.CorrossionAllowence_box.clear()
        self.ui.SoilUnitWeight_box.clear()
        self.ui.ModulusOfSoilReaction_box.clear()
        self.ui.ResilientModulus_box.clear()
        self.ui.OperatingPressure_box.clear()
        self.ui.impactFactor_box.clear()
        self.ui.designFactor_box.clear()
        self.ui.LongitudinalJointFactor_box.clear()
        self.ui.InstallationTemperature_box.clear()
        self.ui.OperatingTemperature_box.clear()
        self.ui.DesignWheelLoadFromSingleAxle_box.clear()
        self.ui.DesignWheelLoadFromtandemAxle_box.clear()
        self.ui.YongsModulus_box.clear()
        self.ui.PoissonsRatio_box.clear()
        self.ui.CoefficientOfThermalExpansion_box.clear()

        self.ui.EarthLoadStiffnessFactor_box.clear()
        self.ui.earthLoadBurialFactor_box.clear()
        self.ui.EarthLoadExcavationFactor_box.clear()
        self.ui.StiffnessFactorKhh_box.clear()
        self.ui.GeometryFactorGHh_box.clear()
        self.ui.StifnessFactorKLh_box.clear()
        self.ui.geometryFactorGLh_box.clear()
        self.ui.RoadPavementFactor_box.clear()
        self.ui.RoadAxleConfigurationFactor_box.clear()
        self.ui.RadialStress_box.clear()
        self.ui.FatigueEnduranceofGirthYield_box.clear()
        self.ui.FatigueEnduranceofLongitudinalWeld_box.clear()

        # Clear output fields initially
        self.ui.PipeWallThicknessIncludingCA_box.clear()
        self.ui.BoredDiameter_box.clear()
        self.ui.barlowStress_box.clear()
        self.ui.StressDuetoEarthLoad_box.clear()
        self.ui.CyclicCircumferentialStress_box.clear()
        self.ui.CyclicLongitudinalStress_box.clear()
        self.ui.Circumferential_stress_box.clear()
        self.ui.Longitudinal_Stress_box.clear()
        self.ui.Effective_stress_box.clear()

        # Uncheck all result radio buttons
        self._uncheck_all_radio_buttons()


    def _uncheck_all_radio_buttons(self):
        """Helper to uncheck all radio buttons in the result section."""
        # Temporarily set exclusive to False to allow unchecking all
        self.ui.buttonGroup.setExclusive(False)
        self.ui.BarlowSafe_radioButton.setChecked(False)
        self.ui.BarlowNotSafe_radioButton.setChecked(False)
        self.ui.buttonGroup.setExclusive(True) # Restore exclusivity

        self.ui.buttonGroup_2.setExclusive(False)
        self.ui.PrincipleSafe_radioButton.setChecked(False)
        self.ui.PrincipleNotSafe_raadioButton.setChecked(False)
        self.ui.buttonGroup_2.setExclusive(True)

        self.ui.buttonGroup_3.setExclusive(False)
        self.ui.FatigueSafe_radioButton.setChecked(False)
        self.ui.FatigueNotSafeGirthWeld_radiButton.setChecked(False)
        self.ui.buttonGroup_3.setExclusive(True)

        self.ui.buttonGroup_4.setExclusive(False)
        self.ui.FatigueCheckLongitudinalYields_Safe.setChecked(False)
        self.ui.FatigueCheckLongitudinalYields_NotSafe.setChecked(False)
        self.ui.buttonGroup_4.setExclusive(True)


    # --- Combobox Handlers (using match case) ---
    def on_pipe_type_changed(self, index):
        """Handles changes in the Pipe Type combobox."""
        self.selected_pipe_type = self.ui.PipeType_combobox.currentText()
        match self.selected_pipe_type:
            case "Seamless":
                print(f"Pipe Type selected: {self.selected_pipe_type}")
                # Add specific logic for Seamless pipes if needed
            case "SAW":
                print(f"Pipe Type selected: {self.selected_pipe_type}")
                # Add specific logic for SAW pipes if needed
            case "ERW":
                print(f"Pipe Type selected: {self.selected_pipe_type}")
                # Add specific logic for ERW pipes if needed
            case _:
                print(f"Unknown Pipe Type selected: {self.selected_pipe_type}")

    def on_soil_type_changed(self, index):
        """Handles changes in the Soil Type combobox."""
        self.selected_soil_type = self.ui.SoilType_combobox.currentText()
        match self.selected_soil_type:
            case "Soft To Medium Clay":
                print(f"Soil Type selected: {self.selected_soil_type}")
                # Adjust properties like Modulus of Soil Reaction or Resilient Modulus if they vary by soil type
            case _:
                print(f"Unknown Soil Type selected: {self.selected_soil_type}")

    def on_bored_diameter_changed(self, index):
        """Handles changes in the Bored Diameter combobox."""
        bored_diameter_option = self.ui.BoredDiameter_combobox.currentText()
        match bored_diameter_option:
            case "Considered":
                self.consider_bored_diameter_in_calc = True
                print(f"Bored Diameter option selected: {bored_diameter_option} (will be considered in calculation)")
            case "Not Considered":
                self.consider_bored_diameter_in_calc = False
                print(f"Bored Diameter option selected: {bored_diameter_option} (will NOT be considered in calculation)")
            case _:
                print(f"Unknown Bored Diameter option selected: {bored_diameter_option}")
                self.consider_bored_diameter_in_calc = False # Default to not considered for safety

    def on_steel_grade_changed(self, index):
        """Handles changes in the Steel Grade combobox and updates SMYS."""
        steel_grade_text = self.ui.SteelGrade_Combobox.currentText()
        # Mapping steel grade text to a specified minimum yield strength (SMYS) in MPa
        # These values are examples; ensure they match your engineering standards.
        match steel_grade_text:
            case "Fe 330": self.steel_grade_smys = 330
            case "A25": self.steel_grade_smys = 172
            case "A": self.steel_grade_smys = 241
            case "B": self.steel_grade_smys = 290
            case "X42": self.steel_grade_smys = 290
            case "X46": self.steel_grade_smys = 317
            case "X52": self.steel_grade_smys = 358
            case "X56": self.steel_grade_smys = 386
            case "X60": self.steel_grade_smys = 413
            case "X65": self.steel_grade_smys = 448
            case "X70": self.steel_grade_smys = 482
            case "X80": self.steel_grade_smys = 552
            case _:
                self.steel_grade_smys = 0 # Default or error value
                QtWidgets.QMessageBox.warning(self, "Input Warning", f"Unknown Steel Grade: {steel_grade_text}. SMYS set to 0.")
        print(f"Steel Grade selected: {steel_grade_text}, SMYS set to: {self.steel_grade_smys} MPa")
        # Update the SMYS input box to reflect the selected value
        self.ui.SpecifiedMinimumYieldStrength_box.setText(str(self.steel_grade_smys))


    def on_codes_standards_changed(self, index):
        """Handles changes in the Codes & Standards combobox."""
        self.selected_codes_standards = self.ui.CodesAndStandards_combobox.currentText()
        match self.selected_codes_standards:
            case "API 1102":
                print(f"Codes & Standards selected: {self.selected_codes_standards}")
                # Adjust design factors or calculation methodologies if required by this code
            case "ISO":
                print(f"Codes & Standards selected: {self.selected_codes_standards}")
            case "IS":
                print(f"Codes & Standards selected: {self.selected_codes_standards}")
            case _:
                print(f"Unknown Codes & Standards selected: {self.selected_codes_standards}")

    # --- Action Button Handlers ---
    def new_file(self):
        """Resets all inputs for a new simulation."""
        print("Action: New File")
        self.reset_all_inputs()
        QtWidgets.QMessageBox.information(self, "New File", "All inputs have been reset for a new simulation.")

    def open_file(self):
        """Opens an existing simulation file."""
        print("Action: Open File")
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Simulation", "", "Simulation Files (*.sim);;All Files (*)")
        if file_path:
            print(f"Opening file: {file_path}")
            QtWidgets.QMessageBox.information(self, "Open File", f"Attempting to open: {file_path}\n(File loading logic not implemented yet)")
            # TODO: Implement actual file loading logic here.
            # You would read the content of the file (e.g., JSON or CSV)
            # and populate the UI fields accordingly.
        else:
            print("File open cancelled.")

    def save_file_as(self):
        """Saves the current simulation data to a new file."""
        print("Action: Save File As")
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Simulation As", "", "Simulation Files (*.sim);;All Files (*)")
        if file_path:
            print(f"Saving file as: {file_path}")
            QtWidgets.QMessageBox.information(self, "Save File As", f"Attempting to save to: {file_path}\n(File saving logic not implemented yet)")
            # TODO: Implement actual file saving logic here.
            # You would gather all current input and output values from the UI
            # and write them to the specified file (e.g., in JSON format).
        else:
            print("File save cancelled.")

    def generate_report(self):
        """Generates a detailed report of the simulation."""
        print("Action: Generate Report")
        QtWidgets.QMessageBox.information(self, "Generate Report", "Generating simulation report... (Placeholder)")
        # TODO: Implement report generation. This would typically involve:
        # 1. Re-running calculations to ensure results are fresh.
        # 2. Formatting all inputs and outputs into a printable format (e.g., PDF, HTML).
        # 3. Saving or displaying the report.

    def show_whats_new(self):
        """Displays information about new features."""
        print("Action: What's New?")
        QtWidgets.QMessageBox.information(self, "What's New?",
                                       "Version 1.0.1\n\n"
                                       "- Implemented combobox selection logic.\n"
                                       "- Added action button functionality.\n"
                                       "- Console output for all inputs.\n"
                                       "- Corrected Barlow Stress calculation formula.\n"
                                       "- Added threading for calculations with a 'Calculating...' dialog.")

    def show_documentation(self):
        """Displays application documentation."""
        print("Action: Documentation")
        QtWidgets.QMessageBox.information(self, "Documentation",
                                       "Detailed documentation will be available here.\n"
                                       "For now, please refer to the input labels for guidance. (Placeholder)")
        # You could open a local PDF/HTML file or an online link here
        # Example: QtGui.QDesktopServices.openUrl(QtCore.QUrl("file:///path/to/your/documentation.pdf"))

    def reset_all_inputs(self):
        """Resets all input fields, comboboxes, and radio buttons to their default states."""
        print("Resetting all inputs...")
        # Clear all line edits
        for line_edit in self.findChildren(QtWidgets.QLineEdit):
            line_edit.clear()

        # Reset comboboxes to default index (0)
        for combo_box in self.findChildren(QtWidgets.QComboBox):
            combo_box.setCurrentIndex(0)

        # Uncheck all radio buttons
        self._uncheck_all_radio_buttons()

        # Re-initialize default numerical values (which now clears them)
        self.initialize_default_input_values()
        print("All inputs have been reset.")


    def print_all_inputs_to_console(self):
        """Prints all current input values from the UI to the console."""
        print("\n--- Current Input Values from UI ---")
        # String Inputs (Comboboxes)
        print(f"Pipe Type: {self.ui.PipeType_combobox.currentText()}")
        print(f"Soil Type: {self.ui.SoilType_combobox.currentText()}")
        print(f"Bored Diameter Option: {self.ui.BoredDiameter_combobox.currentText()}")
        print(f"Steel Grade: {self.ui.SteelGrade_Combobox.currentText()} (SMYS: {self.steel_grade_smys} MPa)")
        print(f"Codes & Standards: {self.ui.CodesAndStandards_combobox.currentText()}")

        # Main Inputs (Line Edits)
        print(f"Pipe Outside Diameter (D): {self.ui.PipeOutsideDiameter_box.text()} mm")
        print(f"Pipe Wall Thickness (t): {self.ui.PipeWallThickness_box.text()} mm")
        print(f"Depth Of Cover (H): {self.ui.DepthOfCover_box.text()} m")
        print(f"Corrosion Allowance (CA): {self.ui.CorrossionAllowence_box.text()} mm")
        print(f"Soil Unit Weight (γ): {self.ui.SoilUnitWeight_box.text()} kN/m³")
        print(f"Modulus of Soil Reaction (E'): {self.ui.ModulusOfSoilReaction_box.text()} MPa")
        print(f"Resilient Modulus (Er): {self.ui.ResilientModulus_box.text()} MPa")
        print(f"Operating Pressure (p): {self.ui.OperatingPressure_box.text()} bar")
        print(f"Impact Factor (Fi): {self.ui.impactFactor_box.text()}")
        print(f"Design Factor (F): {self.ui.designFactor_box.text()}")
        print(f"Longitudinal Joint Factor (E): {self.ui.LongitudinalJointFactor_box.text()}")
        print(f"Installation Temperature (T1): {self.ui.InstallationTemperature_box.text()} °C")
        print(f"Operating Temperature (T2): {self.ui.OperatingTemperature_box.text()} °C")
        print(f"Design Wheel load from Single Axle (Ps): {self.ui.DesignWheelLoadFromSingleAxle_box.text()} kN")
        print(f"Design Wheel load from Tandem Axle (Pt): {self.ui.DesignWheelLoadFromtandemAxle_box.text()} kN")
        print(f"Young's Modulus (Es): {self.ui.YongsModulus_box.text()} MPa")
        print(f"Poisson's Ratio (μ): {self.ui.PoissonsRatio_box.text()}")
        print(f"Coefficient Of Thermal Expansion (αT): {self.ui.CoefficientOfThermalExpansion_box.text()}")

        # Stress Inputs
        print(f"Earth Load Stiffness Factor (KHe): {self.ui.EarthLoadStiffnessFactor_box.text()}")
        print(f"Earth Load Burial Factor (Be): {self.ui.earthLoadBurialFactor_box.text()}")
        print(f"Earth Load Excavation Factor (Ee): {self.ui.EarthLoadExcavationFactor_box.text()}")
        print(f"Stiffness Factor (KHh): {self.ui.StiffnessFactorKhh_box.text()}")
        print(f"Geometry Factor (GHh): {self.ui.GeometryFactorGHh_box.text()}")
        print(f"Stiffness Factor (KLh): {self.ui.StifnessFactorKLh_box.text()}")
        print(f"Geometry Factor (GLh): {self.ui.geometryFactorGLh_box.text()}")
        print(f"Road Pavement Type Factor (R): {self.ui.RoadPavementFactor_box.text()}")
        print(f"Road Axle Configuration Factor (L): {self.ui.RoadAxleConfigurationFactor_box.text()}")
        print(f"Radial Stress (S3): {self.ui.RadialStress_box.text()} MPa")
        print(f"Fatigue Endurance Limit Of Girth Yield (SFG): {self.ui.FatigueEnduranceofGirthYield_box.text()} MPa")
        print(f"Fatigue Endurance Limit Of Longitudinal Weld (SFL): {self.ui.FatigueEnduranceofLongitudinalWeld_box.text()} MPa")
        print("-----------------------------------\n")


    def start_calculation_thread(self):
        """
        Initiates the calculation in a separate thread and shows a loading dialog.
        """
        print("\n--- Starting Calculation Thread ---")
        # 1. Read all input values from UI
        inputs = {}
        try:
            inputs['pipe_outside_diameter'] = float(self.ui.PipeOutsideDiameter_box.text())
            inputs['pipe_wall_thickness'] = float(self.ui.PipeWallThickness_box.text())
            inputs['specified_minimum_yield_strength'] = self.steel_grade_smys # From combobox
            inputs['depth_of_cover'] = float(self.ui.DepthOfCover_box.text())
            inputs['corrosion_allowance'] = float(self.ui.CorrossionAllowence_box.text())
            inputs['consider_bored_diameter_in_calc'] = self.consider_bored_diameter_in_calc # From combobox

            inputs['soil_unit_weight'] = float(self.ui.SoilUnitWeight_box.text())
            inputs['modulus_of_soil_reaction'] = float(self.ui.ModulusOfSoilReaction_box.text())
            inputs['resilient_modulus'] = float(self.ui.ResilientModulus_box.text())
            inputs['operating_pressure'] = float(self.ui.OperatingPressure_box.text())
            inputs['impact_factor'] = float(self.ui.impactFactor_box.text())
            inputs['design_factor'] = float(self.ui.designFactor_box.text())
            inputs['longitudinal_joint_factor'] = float(self.ui.LongitudinalJointFactor_box.text())
            inputs['installation_temperature'] = float(self.ui.InstallationTemperature_box.text())
            inputs['operating_temperature'] = float(self.ui.OperatingTemperature_box.text())
            inputs['design_wheel_load_single_axle'] = float(self.ui.DesignWheelLoadFromSingleAxle_box.text())
            inputs['design_wheel_load_tandem_axle'] = float(self.ui.DesignWheelLoadFromtandemAxle_box.text())
            inputs['youngs_modulus'] = float(self.ui.YongsModulus_box.text())
            inputs['poissons_ratio'] = float(self.ui.PoissonsRatio_box.text())
            inputs['coefficient_of_thermal_expansion'] = float(self.ui.CoefficientOfThermalExpansion_box.text())

            inputs['earth_load_stiffness_factor'] = float(self.ui.EarthLoadStiffnessFactor_box.text())
            inputs['earth_load_burial_factor'] = float(self.ui.earthLoadBurialFactor_box.text())
            inputs['earth_load_excavation_factor'] = float(self.ui.EarthLoadExcavationFactor_box.text())
            inputs['stiffness_factor_khh'] = float(self.ui.StiffnessFactorKhh_box.text())
            inputs['geometry_factor_ghh'] = float(self.ui.GeometryFactorGHh_box.text())
            inputs['stiffness_factor_klh'] = float(self.ui.StifnessFactorKLh_box.text())
            inputs['geometry_factor_glh'] = float(self.ui.geometryFactorGLh_box.text())
            inputs['road_pavement_type_factor'] = float(self.ui.RoadPavementFactor_box.text())
            inputs['road_axle_configuration_factor'] = float(self.ui.RoadAxleConfigurationFactor_box.text())
            inputs['radial_stress'] = float(self.ui.RadialStress_box.text())
            inputs['fatigue_endurance_girth_yield'] = float(self.ui.FatigueEnduranceofGirthYield_box.text())
            inputs['fatigue_endurance_longitudinal_weld'] = float(self.ui.FatigueEnduranceofLongitudinalWeld_box.text())

        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Input Error", f"Please ensure all numerical input fields are filled with valid numbers. Error: {e}")
            return
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Unexpected Error", f"An unexpected error occurred while preparing inputs: {e}")
            return

        # Show loading dialog
        self.loading_dialog = QtWidgets.QDialog(self)
        self.loading_dialog.setWindowTitle("Calculating...")
        self.loading_dialog.setModal(True) # Make it modal to block interaction with main window
        layout = QtWidgets.QVBoxLayout()
        label = QtWidgets.QLabel("Calculating, please wait for 5 seconds...") # Updated text
        label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(label)
        self.loading_dialog.setLayout(layout)
        self.loading_dialog.setFixedSize(300, 100) # Fixed size for the dialog
        self.loading_dialog.show() # Show non-blocking

        # Create and start the worker thread
        self.calculation_worker = CalculationWorker(inputs)
        self.calculation_worker.calculation_finished.connect(self.handle_calculation_finished)
        self.calculation_worker.calculation_error.connect(self.handle_calculation_error)
        self.calculation_worker.start() # Start the thread

    def handle_calculation_finished(self, results):
        """
        Slot to receive results from the worker thread and update the UI.
        """
        print("Calculation finished in thread. Updating UI...")
        # Hide loading dialog
        if self.loading_dialog:
            self.loading_dialog.accept() # Close the dialog
            self.loading_dialog = None

        # Update UI with results
        self.ui.PipeWallThicknessIncludingCA_box.setText(str(round(results['pipe_wall_thickness_including_ca'], 3)))
        self.ui.BoredDiameter_box.setText(str(round(results['bored_diameter'], 3)))
        self.ui.barlowStress_box.setText(str(results['barlow_stress']))
        self.ui.StressDuetoEarthLoad_box.setText(str(results['stress_due_to_earth_load']))
        self.ui.CyclicCircumferentialStress_box.setText(str(results['cyclic_circumferential_stress']))
        self.ui.CyclicLongitudinalStress_box.setText(str(results['cyclic_longitudinal_stress']))
        self.ui.Circumferential_stress_box.setText(str(round(results['circumferential_stress_s1'], 3)))
        self.ui.Longitudinal_Stress_box.setText(str(round(results['longitudinal_stress_s2'], 3)))
        self.ui.Effective_stress_box.setText(str(results['effective_stress']))

        # Update Radio Buttons
        self._uncheck_all_radio_buttons() # Clear previous checks

        if results['barlow_stress'] <= results['f_e_smys']:
            self.ui.BarlowSafe_radioButton.setChecked(True)
        else:
            self.ui.BarlowNotSafe_radioButton.setChecked(True)

        if results['effective_stress'] <= results['specified_minimum_yield_strength'] * results['design_factor']:
            self.ui.PrincipleSafe_radioButton.setChecked(True)
        else:
            self.ui.PrincipleNotSafe_raadioButton.setChecked(True)

        if results['cyclic_longitudinal_stress'] <= results['fatigue_endurance_girth_yield'] * results['design_factor']:
            self.ui.FatigueSafe_radioButton.setChecked(True)
        else:
            self.ui.FatigueNotSafeGirthWeld_radiButton.setChecked(True)

        if results['cyclic_circumferential_stress'] <= results['fatigue_endurance_longitudinal_weld'] * results['design_factor']:
            self.ui.FatigueCheckLongitudinalYields_Safe.setChecked(True)
        else:
            self.ui.FatigueCheckLongitudinalYields_NotSafe.setChecked(True)

        self.print_all_inputs_to_console() # Print inputs after successful calculation
        print("--- Calculation and UI Update Complete ---")

    def handle_calculation_error(self, error_message):
        """
        Slot to receive error messages from the worker thread and display them.
        """
        print(f"Calculation Error: {error_message}")
        # Hide loading dialog
        if self.loading_dialog:
            self.loading_dialog.accept() # Close the dialog
            self.loading_dialog = None
        QtWidgets.QMessageBox.critical(self, "Calculation Error", error_message)


# Main execution block
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Show the loading screen first
    loading_screen = LoadingScreen()
    loading_screen.show()
    loading_screen.start_loading() # Start the progress bar animation

    # Use a QTimer to open the main window after the loading screen duration
    # This timer is separate from the progress bar timer to ensure the main window
    # opens only after the full 5 seconds, regardless of how fast the progress bar fills.
    main_window_timer = QtCore.QTimer()
    main_window_timer.setSingleShot(True) # Ensure it only runs once
    main_window_timer.timeout.connect(lambda: main_window.show())
    main_window_timer.timeout.connect(lambda: loading_screen.close()) # Close loading screen when main window opens

    # Start the timer to open the main window after 5 seconds
    main_window_timer.start(5000) # 5000 milliseconds = 5 seconds

    # Initialize the main window, but don't show it yet
    main_window = MyMainWindow()

    sys.exit(app.exec_())
