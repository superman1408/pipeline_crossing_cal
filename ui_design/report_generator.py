from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import ParagraphStyle, TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import datetime
import os


LOGO_PATH = os.path.join("Assests", "Ashkam LOGO (300 x 100 px).png")

# Define the ASHKAM brand color
ASHKAM_BRAND_COLOR = colors.HexColor("#0D325C")

def _draw_logo(canvas_obj):
    """Helper function to draw the logo on the canvas."""
    if os.path.exists(LOGO_PATH):
        try:
            logo_image = ImageReader(LOGO_PATH)
            logo_width = 0.95 * inch
            logo_height = 0.55 * inch
            x_position = 0.75 * inch
            y_position = A4[1] - 1.0 * inch # Position at top left
            canvas_obj.drawImage(logo_image, x_position, y_position, width=logo_width, height=logo_height, mask='auto')
        except Exception as e:
            print(f"Warning: Could not draw logo from {LOGO_PATH} on canvas. Error: {e}")
    else:
        print(f"Warning: Logo file not found at {LOGO_PATH}. Skipping logo drawing on canvas.")

def _first_page_header_footer(canvas_obj, doc):
    """
    Function to add the logo, page number, footer text, and a line to the first page.
    """
    canvas_obj.saveState()

    # Draw the horizontal line above the footer
    line_y_position = 1.0 * inch # Position the line 1.0 inch from the bottom
    margin_x = 0.75 * inch
    canvas_obj.setStrokeColor(colors.lightgrey) # Set line color
    canvas_obj.setLineWidth(0.5)
    canvas_obj.line(margin_x, line_y_position, A4[0] - margin_x, line_y_position) # Draw the line

    # Footer: Page number (bottom right)
    page_number_text = f"Page {doc.page}"
    canvas_obj.setFont('Helvetica', 9)
    canvas_obj.setFillColor(colors.black) # Ensure page number is black
    canvas_obj.drawString(A4[0] - inch, 0.75 * inch, page_number_text)

    # Footer: ASHKAM ENERGY PVT. LTD. text (bottom left)
    canvas_obj.setFont('Helvetica', 9)
    canvas_obj.setFillColor(ASHKAM_BRAND_COLOR) # Set color for ASHKAM text
    canvas_obj.drawString(0.75 * inch, 0.75 * inch, "ASHKAM ENERGY PVT. LTD.") # Position at bottom left
    canvas_obj.setFillColor(colors.black) # Reset fill color for other drawings

    # Header: Logo (top left)
    _draw_logo(canvas_obj)

    canvas_obj.restoreState()


def _later_pages_header_footer(canvas_obj, doc):
    """
    Function to add page numbers, footer text, a line, and logo to subsequent pages.
    """
    canvas_obj.saveState()

    # Draw the horizontal line above the footer
    line_y_position = 1.0 * inch
    margin_x = 0.75 * inch
    canvas_obj.setStrokeColor(colors.lightgrey)
    canvas_obj.setLineWidth(0.5)
    canvas_obj.line(margin_x, line_y_position, A4[0] - margin_x, line_y_position)

    # Footer: Page number (bottom right)
    page_number_text = f"Page {doc.page}"
    canvas_obj.setFont('Helvetica', 9)
    canvas_obj.setFillColor(colors.black) # Ensure page number is black
    canvas_obj.drawString(A4[0] - inch, 0.75 * inch, page_number_text)

    # Footer: ASHKAM ENERGY PVT. LTD. text (bottom left)
    canvas_obj.setFont('Helvetica', 9)
    canvas_obj.setFillColor(ASHKAM_BRAND_COLOR) # Set color for ASHKAM text
    canvas_obj.drawString(0.75 * inch, 0.75 * inch, "ASHKAM ENERGY PVT. LTD.") # Position at bottom left
    canvas_obj.setFillColor(colors.black) # Reset fill color

    # Header: Logo (top left) - now on all pages
    _draw_logo(canvas_obj)

    canvas_obj.restoreState()


def generate_pipeline_report(filename, input_data, calculation_results, username="N/A", project_title="Untitled Project"):
    doc = SimpleDocTemplate(filename, pagesize=A4)
    # ----------- Styles -----------
    style_title = ParagraphStyle(
        name='Title',
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        alignment=TA_CENTER,
        spaceAfter=20,
        textColor=colors.HexColor("#0D325c")
    )
    style_section = ParagraphStyle(
        name='Section',
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        alignment=TA_LEFT,
        spaceBefore=12,
        spaceAfter=6,
        textColor=colors.HexColor("#111827")
    )
    style_subsection = ParagraphStyle(
        name='Subsection',
        fontName='Helvetica-BoldOblique',
        fontSize=12,
        leading=16,
        alignment=TA_LEFT,
        spaceBefore=10,
        spaceAfter=5,
        textColor=colors.HexColor("#111827")
    )
    style_text = ParagraphStyle(
        name='Text',
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        alignment=TA_LEFT,
        spaceAfter=4
    )
    style_colored_text_green = ParagraphStyle(name='ColoredTextGreen', parent=style_text, textColor=colors.green, alignment=TA_CENTER)
    style_colored_text_red = ParagraphStyle(name='ColoredTextRed', parent=style_text, textColor=colors.red, alignment=TA_CENTER)
    style_colored_text_black = ParagraphStyle(name='ColoredTextBlack', parent=style_text, textColor=colors.black, alignment=TA_CENTER)

    story = []

    # ----------- Title & Project Details Box -----------
    story.append(Paragraph("Pipeline Crossing Simulation Report", style_title))
    story.append(Spacer(1, 0.2 * inch))

    # Project Details Table (replacing individual paragraphs for box effect)
    project_title_display = project_title if project_title else "Untitled Project"
    username_display = username if username else "N/A"

    project_details_data = [
        [Paragraph("<b>Project Title:</b>", style_text), Paragraph(project_title_display, style_text)],
        [Paragraph("<b>Report Date:</b>", style_text), Paragraph(datetime.datetime.now().strftime('%B %d, %Y %H:%M:%S'), style_text)],
        [Paragraph("<b>Generated By:</b>", style_text), Paragraph(username_display, style_text)],
        [Paragraph("<b>Verified By:</b>", style_text), Paragraph("_" * 30, style_text)], # Blank line for manual filling
    ]

    # Calculate width of the project details table
    table_width = A4[0] - (2 * 0.75 * inch) # Page width minus left/right margins

    project_details_table = Table(
        project_details_data,
        colWidths=[0.3 * table_width, 0.7 * table_width]
    )
    project_details_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('BACKGROUND', (0,0), (-1,0), colors.white),
    ]))
    story.append(project_details_table)
    story.append(Spacer(1, 0.2 * inch))

    # ----------- Input Parameters -----------
    story.append(Paragraph("1. Input Parameters", style_section))
    input_data_for_report = [["Parameter", "Value", "Unit"]]
    input_units = {
        "Pipe_Outside_Diameter": "mm",
        "Pipe_Wall_Thickness": "mm",
        "Specified_Minimum_Yield_Strength": "MPa",
        "Depth_of_Cover": "m",
        "Corrosion_Allowance": "mm",
        "Operating_Pressure": "MPa",
        "Operating_Temperature": "°C",
        "Impact_Factor": "-", # Dimensionless
        "Design_Wheel_Load_From_Single_Axle": "kN",
        "Soil_Unit_Weight": "kN/m³",
        "Design_Factor": "-", # Dimensionless
        "Design_Wheel_Load_From_Tandem_Axle": "kN",
        "Modulus_of_Soil_Reaction": "MPa",
        "Longitudinal_Joint_Factor": "-", # Dimensionless
        "Youngs_Modulus": "MPa",
        "Resilient_Modulus": "MPa",
        "Installation_Temperature": "°C",
        "Poissons_Ratio": "-", # Dimensionless
        "Coefficient_of_Thermal_Expansion": "/°C",
        "Earth_Load_Stiffness_Factor": "-", # Dimensionless
        "Earth_Load_Burial_Factor": "-", # Dimensionless
        "Earth_Load_Excavation_Factor": "-", # Dimensionless
        "Stiffness_Factor_KHh": "-", # Dimensionless
        "Geometry_Factor_GHh": "-", # Dimensionless
        "Stiffness_Factor_KLh": "-", # Dimensionless
        "Geometry_Factor_GLh": "-", # Dimensionless
        "Road_Axle_Configuration_Factor": "-", # Dimensionless
        "Road_Pavement_Type_Factor": "-", # Dimensionless
        "Fatigue_endurance_Limit_of_Girth_yield": "MPa",
        "Fatigue_endurance_Limit_of_Longitudinal_Weld": "MPa",
        "Pipe_Type": "-", # Categorical, no unit
        "Bored_Diameter_Option": "-", # Categorical, no unit
        "Soil_Type": "-", # Categorical, no unit
        "Steel_grade": "-", # Categorical, no unit
        "Codes_and_standards": "-", # Categorical, no unit
    }
    input_display_names = {
        "Pipe_Outside_Diameter": "Pipe Outside Diameter   D",
        "Pipe_Wall_Thickness": "Pipe Wall Thickness   t",
        "Specified_Minimum_Yield_Strength": "Specified Minimum Yield Strength   SMYS",
        "Depth_of_Cover": "Depth of Cover   H",
        "Corrosion_Allowance": "Corrosion Allowance   CA",
        "Operating_Pressure": "Operating Pressure   p",
        "Operating_Temperature": "Operating Temperature   T2",
        "Impact_Factor": "Impact Factor   Fi",
        "Design_Wheel_Load_From_Single_Axle": "Design Wheel Load (Single Axle)   Ps",
        "Soil_Unit_Weight": "Soil Unit Weight   γ",
        "Design_Factor": "Design Factor   F",
        "Design_Wheel_Load_From_Tandem_Axle": "Design Wheel Load (Tandem Axle)   Pt",
        "Modulus_of_Soil_Reaction": "Modulus of Soil Reaction   E'",
        "Longitudinal_Joint_Factor": "Longitudinal Joint Factor   E",
        "Youngs_Modulus": "Young's Modulus   Es",
        "Resilient_Modulus": "Resilient Modulus   Er",
        "Installation_Temperature": "Installation Temperature   T1",
        "Poissons_Ratio": "Poisson's Ratio   μ",
        "Coefficient_of_Thermal_Expansion": "Coeff. of Thermal Expansion   αT",
        "Earth_Load_Stiffness_Factor": "Earth Load Stiffness Factor   KHe",
        "Earth_Load_Burial_Factor": "Earth Load Burial Factor   Be",
        "Earth_Load_Excavation_Factor": "Earth Load Excavation Factor   Ee",
        "Stiffness_Factor_KHh": "Stiffness Factor   KHh",
        "Geometry_Factor_GHh": "Geometry Factor   GHh",
        "Stiffness_Factor_KLh": "Stiffness Factor   KLh",
        "Geometry_Factor_GLh": "Geometry Factor   GLh",
        "Road_Axle_Configuration_Factor": "Road Axle Configuration Factor   L",
        "Road_Pavement_Type_Factor": "Road Pavement Type Factor   R",
        "Fatigue_endurance_Limit_of_Girth_yield": "Fatigue Endurance (Girth weld)   SFG",
        "Fatigue_endurance_Limit_of_Longitudinal_Weld": "Fatigue Endurance (Long. Weld)   SFL",
        "Pipe_Type": "Pipe Type",
        "Bored_Diameter_Option": "Bored Diameter Option",
        "Soil_Type": "Soil Type",
        "Steel_grade": "Steel Grade",
        "Codes_and_standards": "Codes & Standards",
    }
    for key, display_name in input_display_names.items():
        val = input_data.get(key, "N/A")
        unit = input_units.get(key, "-")
        input_data_for_report.append([display_name, str(val), unit])
    table1 = Table(input_data_for_report, colWidths=[2.5 * inch, 2.0 * inch, 1.5 * inch])
    table1.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ]))
    story.append(table1)
    story.append(Spacer(1, 0.2 * inch))

    # ----------- 2. Calculation Results (Modified to exclude checks) -----------
    story.append(Paragraph("2. Calculation Results", style_section))
    output_data_for_report = [["Output Parameter", "Value", "Unit"]]
    output_units = {
        "Pipe_Wall_Thickness_Including_CA": "mm",
        "Bored_Diameter": "mm",
        "Barlow_Stress": "MPa",
        "Stress_due_to_Earth_Load": "MPa",
        "Cyclic_Circumferential_Stress": "MPa",
        "Cyclic_Longitudinal_Stress": "MPa",
        "Radial_Stress": "MPa",
        "Circumferential_Stress_S1": "MPa",
        "Longitudinal_Stress_S2": "MPa",
        "Effective_Stress_Seff": "MPa",
    }
    output_display_names = {
        "Pipe_Wall_Thickness_Including_CA": "Pipe Wall Thickness (incl. CA)   tw",
        "Bored_Diameter": "Bored Diameter   Bd",
        "Barlow_Stress": "Barlow Stress   SHi",
        "Stress_due_to_Earth_Load": "Stress due to Earth Load   SHe",
        "Cyclic_Circumferential_Stress": "Cyclic Circumferential Stress   ΔSHh",
        "Cyclic_Longitudinal_Stress": "Cyclic Longitudinal Stress   ΔSLh",
        "Radial_Stress": "Radial Stress   S3",
        "Circumferential_Stress_S1": "Circumferential Stress   S1",
        "Longitudinal_Stress_S2": "Longitudinal Stress   S2",
        "Effective_Stress_Seff": "Effective Stress   Seff",
    }
    for key, display_name in output_display_names.items():
        actual_value = calculation_results.get(key, "N/A")
        unit = output_units.get(key, "-")

        if isinstance(actual_value, (int, float)):
            val_to_display = f"{actual_value:.3f}"
        else:
            val_to_display = str(actual_value)

        output_data_for_report.append([display_name, val_to_display, unit])
    table2 = Table(output_data_for_report, colWidths=[2.5 * inch, 2.0 * inch, 1.5 * inch])
    table2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ]))
    story.append(table2)
    story.append(Spacer(1, 0.2 * inch))

    # ----------- 3. Ratio Check -----------
    story.append(Paragraph("3. Ratio Check", style_section))

    # 3.1 Barlow Stress Check Table
    story.append(Paragraph("Barlow Stress Check", style_subsection))
    barlow_stress = calculation_results.get("Barlow_Stress", "N/A")
    F_E_SMYS = calculation_results.get("F_E_SMYS", "N/A")
    barlow_stress_ratio = calculation_results.get("Barlow_Stress_Ratio", "N/A")
    barlow_check_result = calculation_results.get("Barlow_Stress_Check", "N/A")

    if barlow_check_result == "Allowable":
        barlow_result_para = Paragraph(barlow_check_result, style_colored_text_green)
    elif barlow_check_result == "Not Allowable!":
        barlow_result_para = Paragraph(barlow_check_result, style_colored_text_red) 
    else:
        barlow_result_para = Paragraph(str(barlow_check_result), style_colored_text_black)

    barlow_table_data = [
        ["Barlow Stress   SHi", "F.E. SMYS", "Ratio < 1", "Result"],
        [f"{barlow_stress:.3f}" if isinstance(barlow_stress, (int, float)) else str(barlow_stress),
         f"{F_E_SMYS:.3f}" if isinstance(F_E_SMYS, (int, float)) else str(F_E_SMYS),
         f"{barlow_stress_ratio:.3f}" if isinstance(barlow_stress_ratio, (int, float)) else str(barlow_stress_ratio),
         barlow_result_para]
    ]
    barlow_table = Table(barlow_table_data, colWidths=[1.5 * inch, 1.5 * inch, 1.5 * inch, 1.5 * inch])
    barlow_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
    ]))
    story.append(barlow_table)
    story.append(Spacer(1, 0.2 * inch))

    # 3.2 Principal Stress Criteria Check Table
    story.append(Paragraph("Principal Stress Criteria Check", style_subsection))
    effective_stress = calculation_results.get("Effective_Stress_Seff", "N/A")
    SMYS_DF = calculation_results.get("SMYS_x_Design_Factor", "N/A")
    principal_stress_ratio = calculation_results.get("Principal_Stress_Ratio", "N/A")
    principal_check_result = calculation_results.get("Principal_Stress_Check", "N/A")

    if principal_check_result == "Allowable":
        principal_result_para = Paragraph(principal_check_result, style_colored_text_green)
    elif principal_check_result == "Not Allowable!":
        principal_result_para = Paragraph(principal_check_result, style_colored_text_red)
    else:
        principal_result_para = Paragraph(str(principal_check_result), style_colored_text_black)

    principal_table_data = [
        ["Effective Stress   Seff", "SMYS * D.F.", "Ratio < 1", "Result"],
        [f"{effective_stress:.3f}" if isinstance(effective_stress, (int, float)) else str(effective_stress),
         f"{SMYS_DF:.3f}" if isinstance(SMYS_DF, (int, float)) else str(SMYS_DF),
         f"{principal_stress_ratio:.3f}" if isinstance(principal_stress_ratio, (int, float)) else str(principal_stress_ratio),
         principal_result_para]
    ]
    principal_table = Table(principal_table_data, colWidths=[1.5 * inch, 1.5 * inch, 1.5 * inch, 1.5 * inch])
    principal_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
    ]))
    story.append(principal_table)
    story.append(Spacer(1, 0.2 * inch))

    # ----------- Add a PageBreak before Fatigue Check -----------
    story.append(PageBreak())

    # ----------- Fatigue Check -----------
    story.append(Paragraph("Fatigue Check", style_section))

    # 3.3 Girth Weld Criteria Check Table
    story.append(Paragraph("Girth Weld Criteria Check", style_subsection))
    cyclic_longitudinal_stress = calculation_results.get("Cyclic_Longitudinal_Stress", "N/A")
    Fatigue_Girth_DF = calculation_results.get("Fatigue_Girth_x_Design_Factor", "N/A")
    girth_ratio = calculation_results.get("Girth_Weld_Ratio", "N/A")
    girth_check_result = calculation_results.get("Girth_Weld_Criteria_Check", "N/A")

    if girth_check_result == "Allowable":
        girth_result_para = Paragraph(girth_check_result, style_colored_text_green)
    elif girth_check_result == "Not Allowable!":
        girth_result_para = Paragraph(girth_check_result, style_colored_text_red)
    else:
        girth_result_para = Paragraph(str(girth_check_result), style_colored_text_black)

    girth_table_data = [
        ["Cyclic Long. Stress   ΔSLh", "Fatigue Girth x D.F.", "Ratio < 1", "Result"],
        [f"{cyclic_longitudinal_stress:.3f}" if isinstance(cyclic_longitudinal_stress, (int, float)) else str(cyclic_longitudinal_stress),
         f"{Fatigue_Girth_DF:.3f}" if isinstance(Fatigue_Girth_DF, (int, float)) else str(Fatigue_Girth_DF),
         f"{girth_ratio:.3f}" if isinstance(girth_ratio, (int, float)) else str(girth_ratio),
         girth_result_para]
    ]
    girth_table = Table(girth_table_data, colWidths=[1.6 * inch, 1.6 * inch, 1.4 * inch, 1.4 * inch])
    girth_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
    ]))
    story.append(girth_table)
    story.append(Spacer(1, 0.2 * inch))

    # 3.4 Longitudinal Weld Criteria Check Table
    story.append(Paragraph("Longitudinal Weld Criteria Check", style_subsection))
    cyclic_circumferential_stress = calculation_results.get("Cyclic_Circumferential_Stress", "N/A")
    Fatigue_Long_DF = calculation_results.get("Fatigue_Long_x_Design_Factor", "N/A")
    longitudinal_ratio = calculation_results.get("Longitudinal_Weld_Ratio", "N/A")
    longitudinal_check_result = calculation_results.get("Longitudinal_Weld_Criteria_Check", "N/A")

    if longitudinal_check_result == "Allowable":
        longitudinal_result_para = Paragraph(longitudinal_check_result, style_colored_text_green)
    elif longitudinal_check_result == "Not Allowable!":
        longitudinal_result_para = Paragraph(longitudinal_check_result, style_colored_text_red)
    else:
        longitudinal_result_para = Paragraph(str(longitudinal_check_result), style_colored_text_black)

    longitudinal_table_data = [
        ["Cyclic Circ. Stress   ΔSHh", "Fatigue Long x D.F.", "Ratio < 1", "Result"],
        [f"{cyclic_circumferential_stress:.3f}" if isinstance(cyclic_circumferential_stress, (int, float)) else str(cyclic_circumferential_stress),
         f"{Fatigue_Long_DF:.3f}" if isinstance(Fatigue_Long_DF, (int, float)) else str(Fatigue_Long_DF),
         f"{longitudinal_ratio:.3f}" if isinstance(longitudinal_ratio, (int, float)) else str(longitudinal_ratio),
         longitudinal_result_para]
    ]
    longitudinal_table = Table(longitudinal_table_data, colWidths=[1.6 * inch, 1.6 * inch, 1.4 * inch, 1.4 * inch])
    longitudinal_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
    ]))
    story.append(longitudinal_table)
    story.append(Spacer(1, 0.2 * inch))


    try:
        doc.build(story, onFirstPage=_first_page_header_footer, onLaterPages=_later_pages_header_footer)
    except Exception as e:
        raise Exception(f"PDF generation failed: {e}")