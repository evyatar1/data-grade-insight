from fpdf import FPDF


def generate_pdf(data, output_file):
    """
    Generate a PDF report based on the provided data.

    Args:
        data (dict): A dictionary representing the data from the CSV file.
        output_file (str): The path to save the generated PDF file.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for key, value in data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True, align="L")

    pdf.output(output_file)
