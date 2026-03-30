import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import datetime

st.title("📄 Generate Report")

def generate_pdf(data):
    file_name = "visa_report.pdf"

    doc = SimpleDocTemplate(file_name, pagesize=letter)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("Visa AI Report", styles["Title"]))
    content.append(Spacer(1, 10))

    content.append(Paragraph(f"Generated on: {datetime.datetime.now()}", styles["Normal"]))
    content.append(Spacer(1, 10))

    content.append(Paragraph("User Input:", styles["Heading2"]))
    content.append(Paragraph(f"Visa Type: {data['visa_type']}", styles["Normal"]))
    content.append(Paragraph(f"Visa Status: {data['visa_status']}", styles["Normal"]))
    content.append(Paragraph(f"City: {data['city']}", styles["Normal"]))
    content.append(Spacer(1, 10))

    content.append(Paragraph("Prediction:", styles["Heading2"]))
    content.append(Paragraph(f"Processing Days: {data['days']}", styles["Normal"]))
    content.append(Paragraph(f"Confidence Range: {data['range']}", styles["Normal"]))

    doc.build(content)

    return file_name


if "last_result" in st.session_state:

    data = st.session_state["last_result"]

    if st.button("📥 Download Report"):
        file = generate_pdf(data)

        with open(file, "rb") as f:
            st.download_button("Download PDF", f, file_name="visa_report.pdf")

else:
    st.warning("⚠️ First make a prediction to generate report")