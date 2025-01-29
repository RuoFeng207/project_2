import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def create_pdf(text):
    # Maak de map aan als deze nog niet bestaat
    directory = "PDF_INVOICE"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Definieer de bestandsnaam en het pad
    pdf_file_path = os.path.join(directory, "output.pdf")

    # Maak een canvas voor de PDF
    c = canvas.Canvas(pdf_file_path, pagesize=A4)
    width, height = A4

    # Voeg de tekst toe aan de PDF
    c.drawString(100, height - 100, text)

    # Sla de PDF op
    c.save()
    print(f"PDF is opgeslagen als: {pdf_file_path}")

if __name__ == "__main__":
    # Vraag de gebruiker om input
    user_input = input("Voer de tekst in die je in de PDF wilt weergeven: ")
    create_pdf(user_input)