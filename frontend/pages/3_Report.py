import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

st.title("📄 Download Report")

def generate_pdf():
    doc = SimpleDocTemplate("report.pdf", pagesize=letter)
    styles = getSampleStyleSheet()

    content = []
    content.append(Paragraph("Visa AI Report", styles["Title"]))
    content.append(Paragraph("Prediction Summary & Insights", styles["Normal"]))

    doc.build(content)

    with open("report.pdf", "rb") as f:
        return f.read()

if st.button("Generate Report"):
    pdf = generate_pdf()
    st.download_button("Download PDF", pdf, file_name="visa_report.pdf")