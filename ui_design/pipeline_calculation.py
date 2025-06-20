import math

def calculate_bored_diameter_value(Pipe_Outside_Diameter, Bored_Diameter_Option):
    if Bored_Diameter_Option == "Considered":
        return Pipe_Outside_Diameter + 51
    else:
        return Pipe_Outside_Diameter

def calculate_pipeline_crossing(input_data):

    # --- 1) Input Data     ---
    Steel_grade = input_data.get("Steel_grade")
    Pipe_Type = input_data.get("Pipe_Type")
    Pipe_Outside_Diameter = input_data.get("Pipe_Outside_Diameter")
    Pipe_Wall_Thickness = input_data.get("Pipe_Wall_Thickness")
    Specified_Minimum_Yield_Strength = input_data.get("Specified_Minimum_Yield_Strength")
    Depth_of_Cover = input_data.get("Depth_of_Cover")
    Corrosion_Allowance = input_data.get("Corrosion_Allowance")
    Bored_Diameter_Option = input_data.get("Bored_Diameter_Option") # "Considered" or "Not considered"
    Soil_Unit_Weight = input_data.get("Soil_Unit_Weight")
    Soil_Type = input_data.get("Soil_Type")
    Modulus_of_Soil_Reaction = input_data.get("Modulus_of_Soil_Reaction")
    Resilient_Modulus = input_data.get("Resilient_Modulus")
    Operating_Pressure = input_data.get("Operating_Pressure")
    Impact_Factor = input_data.get("Impact_Factor")
    Design_Factor = input_data.get("Design_Factor")
    Longitudinal_Joint_Factor = input_data.get("Longitudinal_Joint_Factor")
    Installation_Temperature = input_data.get("Installation_Temperature")
    Operating_Temperature = input_data.get("Operating_Temperature")
    Design_Wheel_Load_From_Single_Axle = input_data.get("Design_Wheel_Load_From_Single_Axle")
    Design_Wheel_Load_From_Tandem_Axle = input_data.get("Design_Wheel_Load_From_Tandem_Axle")
    Youngs_Modulus = input_data.get("Youngs_Modulus")
    Poissons_Ratio = input_data.get("Poissons_Ratio")
    Coefficient_of_Thermal_Expansion = input_data.get("Coefficient_of_Thermal_Expansion")

    # Fixed values from original script that are not exposed as GUI inputs
    Earth_Load_Stiffness_Factor = input_data.get("Earth_Load_Stiffness_Factor", 6330)
    Earth_Load_Burial_Factor = input_data.get("Earth_Load_Burial_Factor", 0.47)
    Earth_Load_Excavation_Factor = input_data.get("Earth_Load_Excavation_Factor", 0.91)
    Stiffness_Factor_KHh = input_data.get("Stiffness_Factor_KHh", 19.8)
    Geometry_Factor_GHh = input_data.get("Geometry_Factor_GHh", 0.70)
    Road_Pavement_Type_Factor = input_data.get("Road_Pavement_Type_Factor", 1)
    Road_Axle_Configuration_Factor = input_data.get("Road_Axle_Configuration_Factor", 1)
    Stiffness_Factor_KLh = input_data.get("Stiffness_Factor_KLh", 14.8)
    Geometry_Factor_GLh = input_data.get("Geometry_Factor_GLh", 0.64)
    Fatigue_endurance_Limit_of_Girth_yield = input_data.get("Fatigue_endurance_Limit_of_Girth_yield", 82.737)
    Fatigue_endurance_Limit_of_Longitudinal_Weld = input_data.get("Fatigue_endurance_Limit_of_Longitudinal_Weld", 158.57)

    # --- Calculations (from original script) ---

    # Pipe Wall Thickness Including CA
    Pipe_Wall_Thickness_Including_CA = (Pipe_Wall_Thickness - Corrosion_Allowance)

    # --- Use the helper function here for Bored Diameter ---
    Bored_Diameter = calculate_bored_diameter_value(Pipe_Outside_Diameter, Bored_Diameter_Option)


    # Thickness to diameter ratio
    Thickness_to_diameter_ratio = (Pipe_Wall_Thickness_Including_CA / Pipe_Outside_Diameter)
    Thickness_to_diameter_ratio = round(Thickness_to_diameter_ratio, 5)

    # Ratio of bore diameter and pipe diameter
    Ratio_of_bore_diameter_and_pipe_diameter = (Bored_Diameter / Pipe_Outside_Diameter)
    Ratio_of_bore_diameter_and_pipe_diameter = round(Ratio_of_bore_diameter_and_pipe_diameter, 2)

    # Ratio of pipe depth and bore diameter
    Ratio_of_pipe_dept_and_bore_diameter = (Depth_of_Cover * 1000) / Bored_Diameter
    Ratio_of_pipe_dept_and_bore_diameter = round(Ratio_of_pipe_dept_and_bore_diameter, 3)

    # Applied Design Surface Pressure
    Applied_Design_Surface_Pressure = round(Design_Wheel_Load_From_Tandem_Axle / 0.093) / 1000

    # Barlow Stress (Corrected division for clarity: A / (2*B) instead of (A/2)*B)
    Barlow_Stress = (Operating_Pressure * (Pipe_Outside_Diameter - Pipe_Wall_Thickness_Including_CA)) / (2 * Pipe_Wall_Thickness_Including_CA)

    # F_E_SMYS
    F_E_SMYS = (Design_Factor * Longitudinal_Joint_Factor * Specified_Minimum_Yield_Strength)

    # --- 2) Criteria Checks and Stress Calculations ---

    # A) Barlow Stress Check
    barlow_stress_ratio = Barlow_Stress / F_E_SMYS
    Barlow_Stress_Check = "Allowable" if barlow_stress_ratio < 1 else "Not Allowable!" # Added "!" for consistency
    print("Barlow Stress Criteria Met:", barlow_stress_ratio)

    # B) Circumferential Stress due to Earth Load
    Stress_due_to_Earth_Load = (Earth_Load_Stiffness_Factor * Earth_Load_Burial_Factor * Earth_Load_Excavation_Factor * Soil_Unit_Weight * Pipe_Outside_Diameter) / 1_000_000
    Stress_due_to_Earth_Load = round(Stress_due_to_Earth_Load, 3)

    # C) Cyclic Stresses
    Cyclic_Circumferential_Stress = (Stiffness_Factor_KHh * Geometry_Factor_GHh * Road_Pavement_Type_Factor * Road_Axle_Configuration_Factor * Impact_Factor * Applied_Design_Surface_Pressure)
    Cyclic_Circumferential_Stress = round(Cyclic_Circumferential_Stress, 3)

    Cyclic_Longitudinal_Stress = (Stiffness_Factor_KLh * Geometry_Factor_GLh * Road_Pavement_Type_Factor * Road_Axle_Configuration_Factor * Impact_Factor * Applied_Design_Surface_Pressure)
    Cyclic_Longitudinal_Stress = round(Cyclic_Longitudinal_Stress, 3)

    # D) Circumferential Stress due to Internal Pressurization
    Radial_Stress = 0
    Circumferential = Stress_due_to_Earth_Load + Cyclic_Circumferential_Stress + Barlow_Stress
    Longitudinal = Cyclic_Longitudinal_Stress - Youngs_Modulus * Coefficient_of_Thermal_Expansion * (Operating_Temperature - Installation_Temperature) + Poissons_Ratio * (Stress_due_to_Earth_Load + Barlow_Stress)

    # E) Principal Stress
    effective_stress = math.sqrt(1/2 * ((Circumferential - Longitudinal)**2 + (Longitudinal - Radial_Stress)**2 + (Radial_Stress - Circumferential)**2))

    #SMYS_DF
    SMYS_DF = Specified_Minimum_Yield_Strength * Design_Factor

    # Principal Stress Criteria Check
    principal_stress_ratio = (effective_stress / SMYS_DF) 
    Principal_Stress_Check = "Allowable" if principal_stress_ratio < 1 else "Not Allowable!"
    print("Principal Stress Criteria Met:", principal_stress_ratio)

    #Fatigue_Girth_DF
    Fatigue_Girth_DF = Fatigue_endurance_Limit_of_Girth_yield * Design_Factor

    #Fatigue_Long_DF
    Fatigue_Long_DF = Fatigue_endurance_Limit_of_Longitudinal_Weld * Design_Factor

    # F) Fatigue Check
    # Girth Weld Criteria Check
    girth_ratio = (Cyclic_Longitudinal_Stress / Fatigue_Girth_DF) 
    Girth_Weld_Criteria_Check = "Allowable" if girth_ratio < 1 else "Not Allowable!"
    print("Girth Weld Criteria Met:", girth_ratio)

    # Longitudinal Weld Criteria Check
    longitudinal_ratio = (Cyclic_Circumferential_Stress / Fatigue_Long_DF) 
    Longitudinal_Weld_Criteria_Check = "Allowable" if longitudinal_ratio < 1 else "Not Allowable!"
    print("Longitudinal Weld Criteria Met:", longitudinal_ratio)

    # Prepare results for return
    results = {
        "Pipe_Wall_Thickness_Including_CA": Pipe_Wall_Thickness_Including_CA,
        "Bored_Diameter": Bored_Diameter,
        "Thickness_to_diameter_ratio": Thickness_to_diameter_ratio,
        "Ratio_of_bore_diameter_and_pipe_diameter": Ratio_of_bore_diameter_and_pipe_diameter,
        "Ratio_of_pipe_dept_and_bore_diameter": Ratio_of_pipe_dept_and_bore_diameter,
        "Applied_Design_Surface_Pressure": Applied_Design_Surface_Pressure,
        "Barlow_Stress": Barlow_Stress,
        "F_E_SMYS": F_E_SMYS,
        "Barlow_Stress_Ratio": barlow_stress_ratio, 
        "Barlow_Stress_Check": Barlow_Stress_Check,
        "Stress_due_to_Earth_Load": Stress_due_to_Earth_Load,
        "Cyclic_Circumferential_Stress": Cyclic_Circumferential_Stress,
        "Cyclic_Longitudinal_Stress": Cyclic_Longitudinal_Stress,
        "Circumferential_Stress_S1": Circumferential,
        "Longitudinal_Stress_S2": Longitudinal,
        "Effective_Stress_Seff": effective_stress,
        "SMYS_x_Design_Factor": SMYS_DF, 
        "Principal_Stress_Ratio": principal_stress_ratio,  
        "Principal_Stress_Check": Principal_Stress_Check,
        "Fatigue_Girth_x_Design_Factor": Fatigue_Girth_DF, 
        "Girth_Weld_Ratio": girth_ratio, 
        "Girth_Weld_Criteria_Check": Girth_Weld_Criteria_Check,
        "Fatigue_Long_x_Design_Factor": Fatigue_Long_DF, 
        "Longitudinal_Weld_Ratio": longitudinal_ratio, 
        "Longitudinal_Weld_Criteria_Check": Longitudinal_Weld_Criteria_Check,
        "Radial_Stress": Radial_Stress
    }
    return results