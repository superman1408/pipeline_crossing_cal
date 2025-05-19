import math



# ---------------------------------1) Input Data ------------------------------------------------------------
 
Steel_grade = 330
Pipe_Type = "Seamless"
Pipe_Outside_Diameter = 1016 #mm
Pipe_Wall_Thickness = 10 #mm
Specified_Minimum_Yield_Strength = 195 #MPa
Depth_of_Cover = 1.5 #m
Corrosion_Allowance = 0 #mm
Pipe_Wall_Thickness_Including_CA = 10 #mm
Bored_Diameter = 1067 #mm
Soil_Unit_Weight = 18.9 #kN/m3
Soil_Type = "Soft_to_medium_clay" 
Modulus_of_Soil_Reaction = 3.4 #MPa
Resilient_Modulus = 34 #MPa
Operating_Pressure = 0 #bar
Impact_Factor = 1.5
Design_Factor = 0.72
Longitudinal_Joint_Factor = 1
Installation_Temperature = 65
Operating_Temperature = 40
Design_Wheel_Load_From_Single_Axle = 53.4 #kN
Design_Wheel_Load_From_Tandem_Axle = 44.5 #kN
Youngs_Modulus = 210 #GPa
Poissons_Ratio = 0.30
Coefficient_of_Thermal_Expansion = 1.44*10**(-5)  
Applied_Design_Surface_Pressure = 0.478 #MPa
Thickness_to_diameter_ratio = 0.00984 
Ratio_of_bore_diameter_and_pipe_diameter = 1.05
Ratio_of_pipe_dept_and_bore_daimeter = 1.406

# -------------------------------------Calculation ------------------------------------------------------------
Pipe_Wall_Thickness_Including_CA = (Pipe_Wall_Thickness - Corrosion_Allowance)
print("Pipe_Wall_Thickness_Including_CA : " , Pipe_Wall_Thickness_Including_CA , "mm")

Bored_Diameter = (Pipe_Outside_Diameter + 51)
print("Bored_Diameter : " , Bored_Diameter , "mm")

Thickness_to_diameter_ratio = (Pipe_Wall_Thickness_Including_CA / Pipe_Outside_Diameter)
Thickness_to_diameter_ratio = round(Thickness_to_diameter_ratio, 4)
print("Thickness_to_diameter_ratio : " , Thickness_to_diameter_ratio)

Ratio_of_bore_diameter_and_pipe_diameter = (Bored_Diameter / Pipe_Outside_Diameter)
Ratio_of_bore_diameter_and_pipe_diameter = round(Ratio_of_bore_diameter_and_pipe_diameter, 2)
print("Ratio_of_bore_diameter_and_pipe_diameter : " , Ratio_of_bore_diameter_and_pipe_diameter)

Ratio_of_pipe_dept_and_bore_daimeter = (Depth_of_Cover * 1000) / Bored_Diameter
Ratio_of_pipe_dept_and_bore_daimeter = round(Ratio_of_pipe_dept_and_bore_daimeter, 3)
print("Ratio_of_pipe_dept_and_bore_daimeter:", Ratio_of_pipe_dept_and_bore_daimeter)

Applied_Design_Surface_Pressure = round(Design_Wheel_Load_From_Tandem_Axle/0.093)/1000
print("Applied_Design_Surface_Pressure : " , Applied_Design_Surface_Pressure , "MPa")

Borrow_Stress = (Operating_Pressure * (Pipe_Outside_Diameter - Pipe_Wall_Thickness_Including_CA ))/2*Pipe_Wall_Thickness_Including_CA
print("Borrow_Stress : " , Borrow_Stress , "MPa")

F_E_SMYS = (Design_Factor * Longitudinal_Joint_Factor  * Specified_Minimum_Yield_Strength)
print("F_E_SMYS : " , F_E_SMYS , "MPa")

