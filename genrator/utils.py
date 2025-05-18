# utils.py
import os
from datetime import datetime
from django.conf import settings
from django.template.loader import render_to_string
from xhtml2pdf.pisa import CreatePDF as pisa_CreatePdf

def generate_resume_pdf_to_file(resume_data, filename=None):
    html = render_to_string('genrator/resume_template.html', {'resume_data': resume_data})

    # Ensure the directory exists
    resume_dir = os.path.join(settings.MEDIA_ROOT, 'resumes')
    os.makedirs(resume_dir, exist_ok=True)

    # Generate unique filename if not provided
    if not filename:
        filename = f'resume_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
    
    file_path = os.path.join(resume_dir, filename)

    with open(file_path, 'wb') as pdf_file:
        pisa_status = pisa_CreatePdf(html, dest=pdf_file)

    if pisa_status.err:
        return None  # or raise an error

    return file_path  # Return path to saved file
