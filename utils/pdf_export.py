from fpdf import FPDF
import os

class PDFExporter:
    """
    Exports resumes as PDF.
    """

    @staticmethod
    def export(content: str, filename: str):

        os.makedirs("exports/pdf", exist_ok=True)

        pdf = FPDF()
        pdf.add_page()

        pdf.set_auto_page_break(True, margin=15)

        pdf.set_font("Helvetica", size=12)

        for line in content.split("\n"):
            pdf.multi_cell(0, 8, line)

        output_path = f"exports/pdf/{filename}.pdf"

        pdf.output(output_path)

        return output_path