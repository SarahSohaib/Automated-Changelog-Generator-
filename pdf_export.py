from fpdf import FPDF
import io


def export_pdf(changelog_text):

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in changelog_text.split("\n"):
        pdf.multi_cell(0, 8, line)

    # return PDF as bytes
    pdf_bytes = pdf.output(dest="S").encode("latin-1")

    return pdf_bytes