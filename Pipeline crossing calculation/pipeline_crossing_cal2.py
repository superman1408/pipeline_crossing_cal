import math
#1)Input

Steel_Grade = 300
Pipe_type = "Seamless"
Pipe_OD = 1016 #in mm
Pipe_wall_thickness = 10 #in mm
smys = 195 #in MPa
Depth_of_cover = 1.5 #in m
Corrosion_Allowence = 0 #in mm
Pipe_wall_thickness_inc_CA = 10 #in mm
Bored_Diameter = 1067 #in mm
Soil_unit_Weight = 18.9 #kN/mcu.
Soil_type = "Soft to Medium Clay"
Mod_of_Soil_reaction = 3.4 #in MPa
Resilient_Modulus = 34 #MPa
Operating_pressure = 0 #bar
Impact_factor = 1.5
Design_factor = 0.72
Longitudnal_Joint_factor = 1
installation_temp = 65 #in centigrade
operating_temp = 40 #in centigrade
Design_wheel_load_from_single_axle = 53.4 #kN
Design_wheel_load_from_tandem_axle = 44.5 #kN
Youngs_mod = 210 #GPa
Poissons_rat = 0.30
Coefficient_of_thermal_expansion = 1.44 * 10**-5

#2) Formulae Calculation
Applied_Design_Surface_Pressure = ((Design_wheel_load_from_tandem_axle)/0.093)/1000
print("Applied Design surface Pressure:",round(Applied_Design_Surface_Pressure,3),"MPa")

thickness_to_diameter_ratio = (Pipe_wall_thickness)/Pipe_OD
print("Thickness to Diameter Ratio:",round(thickness_to_diameter_ratio,6))

Ratio_of_bore_diameter_and_pipe_diameter = Bored_Diameter/Pipe_OD
print("ratio of Bored Diameter and pipe Diameter:",round(Ratio_of_bore_diameter_and_pipe_diameter,2))

Ratio_of_pipe_depth_and_bored_diameter = (Depth_of_cover*1000)/Bored_Diameter
print("Ratio of Pipe Depth and Bored Diameter:",round(Ratio_of_pipe_depth_and_bored_diameter,3))

S_Hi = (Operating_pressure*(Pipe_OD - Pipe_wall_thickness_inc_CA))/2*Pipe_wall_thickness_inc_CA

#3) CALCULATION
#------------d) Circumferential Stress due to Internal Pressurization
Stresses_due_to_Earth_load = 51.987 #S_He
Cyclic_Circumferential_Stress = 9.948 #S_Hh
Cyclic_Longitudinal_Stress = 6.798 #S_Lh
E_s =Youngs_mod*1000 #unit conversion of Young's Mod

S1 = Stresses_due_to_Earth_load + Cyclic_Circumferential_Stress + S_Hi
S2 = Cyclic_Longitudinal_Stress - E_s*Coefficient_of_thermal_expansion*(operating_temp - installation_temp)+Poissons_rat*(Stresses_due_to_Earth_load+S_Hi)
print("Circumferencial Stress:",S1,"MPa")
print("Longitudnal Stress:",S2,"MPa")

#---------------e) Pricipal Stress
Radial_stress = 0

effective_stress = math.sqrt(1/2*((S1-S2)**2+(S2-Radial_stress)**2+(Radial_stress-S1)**2))
print("Effective Stress:",effective_stress,"MPa")

#Criteria Check
if effective_stress<=smys*Design_factor:
    print("Allowable")
else:
    print("Not Allowable!")

#-----------------f) Fatigue Check
Fatigue_endurance_Limit_of_Girth_yield = 82.737 #in MPa
print("Girth Welds criteria:")
if Cyclic_Longitudinal_Stress<=Fatigue_endurance_Limit_of_Girth_yield*Design_factor:
    print("Allowable")
else:
    print("Not Allowable!")

Fatigue_endurance_Limit_of_Longitudinal_Weld = 158.57
print("Longitutnal Welds check:")
if Cyclic_Circumferential_Stress<=Fatigue_endurance_Limit_of_Longitudinal_Weld*Design_factor:
    print("Allowable")
else:
    print("Not Allowable!")

#end
