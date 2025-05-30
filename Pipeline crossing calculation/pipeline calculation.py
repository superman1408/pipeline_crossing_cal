import math



# ---------------------------------1) Input Data -----------------------------------------------------------------------------------------------------------------------------------------------------
 
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
Youngs_Modulus = 210 #MPa
Poissons_Ratio = 0.30
Coefficient_of_Thermal_Expansion = 1.44*10**(-5)  
Applied_Design_Surface_Pressure = 0.478 #MPa
Thickness_to_diameter_ratio = 0.00984 
Ratio_of_bore_diameter_and_pipe_diameter = 1.05
Ratio_of_pipe_dept_and_bore_diameter = 1.406
Barlow_Stress = 0 #MPa
# -------------------------------------Circumferential Stress due to Earth Load--------------------------------------------------------------------------------------------------------------
Earth_Load_Stiffness_Factor = 6330
Earth_Load_Burial_Factor = 0.47
Earth_Load_Excavation_Factor = 0.91
Stress_due_to_Earth_Load = 51.987 #MPa
# -------------------------------------C)Cyclic Stresses-------------------------------------------------------------------------------------------------------------------------------------

Stiffness_Factor_KHh = 19.8
Geometry_Factor_GHh = 0.70
Road_Pavement_Type_Factor = 1
Road_Axle_Configuration_Factor = 1
Cyclic_Circumferential_Stress = 9.948
Stiffness_Factor_KLh = 14.8
Geometry_Factor_GLh = 0.64
Cyclic_Longitudinal_Stress = 6.798 #MPa

# -------------------------------------Calculation ----------------------------------------------------------------------------------------------------------------------------------------------

Pipe_Wall_Thickness_Including_CA = (Pipe_Wall_Thickness - Corrosion_Allowance)
print("Pipe_Wall_Thickness_Including_CA : " , Pipe_Wall_Thickness_Including_CA , "mm")

user_input = input("Consider bored diameter? (yes/no): ").strip().lower()
consider_bored_diameter = user_input == "yes"

Pipe_Outside_Diameter = 1016 #mm  

if consider_bored_diameter:
    Bored_Diameter = Pipe_Outside_Diameter + 51
else:
    Bored_Diameter = Pipe_Outside_Diameter

print("Bored_Diameter:", Bored_Diameter, "mm")


# Bored_Diameter = (Pipe_Outside_Diameter + 51)
# print("Bored_Diameter : " , Bored_Diameter , "mm")

Thickness_to_diameter_ratio = (Pipe_Wall_Thickness_Including_CA / Pipe_Outside_Diameter)
Thickness_to_diameter_ratio = round(Thickness_to_diameter_ratio, 5)
print("Thickness_to_diameter_ratio : " , Thickness_to_diameter_ratio)

Ratio_of_bore_diameter_and_pipe_diameter = (Bored_Diameter / Pipe_Outside_Diameter)
Ratio_of_bore_diameter_and_pipe_diameter = round(Ratio_of_bore_diameter_and_pipe_diameter, 2)
print("Ratio_of_bore_diameter_and_pipe_diameter : " , Ratio_of_bore_diameter_and_pipe_diameter)

Ratio_of_pipe_dept_and_bore_diameter = (Depth_of_Cover * 1000) / Bored_Diameter
Ratio_of_pipe_dept_and_bore_diameter = round(Ratio_of_pipe_dept_and_bore_diameter, 3)
print("Ratio_of_pipe_dept_and_bore_diameter:", Ratio_of_pipe_dept_and_bore_diameter)

Applied_Design_Surface_Pressure = round(Design_Wheel_Load_From_Tandem_Axle/0.093)/1000
print("Applied_Design_Surface_Pressure : " , Applied_Design_Surface_Pressure , "MPa")

Barlow_Stress = (Operating_Pressure * (Pipe_Outside_Diameter - Pipe_Wall_Thickness_Including_CA ))/2*Pipe_Wall_Thickness_Including_CA
print("Borrow_Stress : " , Barlow_Stress , "MPa")

F_E_SMYS = (Design_Factor * Longitudinal_Joint_Factor  * Specified_Minimum_Yield_Strength)
print("F_E_SMYS : " , F_E_SMYS , "MPa")

# -------------------------------------2) Calculation ---------------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------A) Barlow Stress -------------------------------------------------------------------------------------------------------------------------------------

if Barlow_Stress <= F_E_SMYS:
    Barlow_Stress_Check = "Allowable"
else:
    Barlow_Stress_Check = "Not Allowable"
print("Barlow_Stress_Check : " , Barlow_Stress_Check)

# -------------------------------------B)Circumferential Stress due to Earth Load------------------------------------------------------------------------------------------------------------

Stress_due_to_Earth_Load = (Earth_Load_Stiffness_Factor * Earth_Load_Burial_Factor * Earth_Load_Excavation_Factor * Soil_Unit_Weight * Pipe_Outside_Diameter) / 1_000_000
Stress_due_to_Earth_Load = round(Stress_due_to_Earth_Load, 3)
print("Stress_due_to_Earth_Load :", Stress_due_to_Earth_Load, "MPa")

# -------------------------------------C)Cyclic Stresses--------------------------------------------------------------------------------------------------------------------------------------

Cyclic_Circumferential_Stress = (Stiffness_Factor_KHh * Geometry_Factor_GHh * Road_Pavement_Type_Factor * Road_Axle_Configuration_Factor * Impact_Factor * Applied_Design_Surface_Pressure)
Cyclic_Circumferential_Stress = round(Cyclic_Circumferential_Stress, 3) 
print("Cyclic_Circumferential_Stress :", Cyclic_Circumferential_Stress, "MPa")

Cyclic_Longitudinal_Stress = (Stiffness_Factor_KLh * Geometry_Factor_GLh * Road_Pavement_Type_Factor * Road_Axle_Configuration_Factor * Impact_Factor * Applied_Design_Surface_Pressure)
Cyclic_Longitudinal_Stress = round(Cyclic_Longitudinal_Stress, 3) 
print("Cyclic_Longitudinal_Stress :", Cyclic_Longitudinal_Stress, "MPa")

# ----------------------------The below calculation and formula are taken from file cal_2 and which is edited by Tanisha-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------D) Circumferential Stress due to Internal Pressurization


Circumferential = Stress_due_to_Earth_Load + Cyclic_Circumferential_Stress + Barlow_Stress
Longitudinal = Cyclic_Longitudinal_Stress - Youngs_Modulus*Coefficient_of_Thermal_Expansion*(Operating_Temperature - Installation_Temperature)+Poissons_Ratio*(Stress_due_to_Earth_Load+Barlow_Stress)
Radial_Stress = 0
print("Circumferential Stress:",Circumferential,"MPa")
print("Longitudinal Stress:",Longitudinal,"MPa")

#---------------E) Principle Stress


effective_stress = math.sqrt(1/2*((Circumferential-Longitudinal)**2+(Longitudinal-Radial_Stress)**2+(Radial_Stress-Circumferential)**2))
print("Effective Stress:",effective_stress,"MPa")

#Criteria Check
if effective_stress<=Specified_Minimum_Yield_Strength*Design_Factor:
    print("Allowable")
else:
    print("Not Allowable!")

#-----------------F) Fatigue Check
Fatigue_endurance_Limit_of_Girth_yield = 82.737 #in MPa
print("Girth Welds criteria:")
if Cyclic_Longitudinal_Stress<=Fatigue_endurance_Limit_of_Girth_yield*Design_Factor:
    print("Allowable")
else:
    print("Not Allowable!")

Fatigue_endurance_Limit_of_Longitudinal_Weld = 158.57
print("Longitudinal Welds check:")
if Cyclic_Circumferential_Stress<=Fatigue_endurance_Limit_of_Longitudinal_Weld*Design_Factor:
    print("Allowable")
else:
    print("Not Allowable!")