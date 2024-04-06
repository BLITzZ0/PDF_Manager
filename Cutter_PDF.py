from PyPDF2 import PdfWriter, PdfReader
import os
from datetime import datetime

def Cutter_PDF():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    output_folder = os.path.join(desktop_path, "PDF_CUTTER")
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    while True:
        pdf_path = input("Enter the path of the PDF file to merge (or type 'done' to finish): ")
        if pdf_path.lower() == 'done':
            break

        try:
            pdf_writer = PdfWriter()
            with open(pdf_path, "rb") as file_obj:
                pdf_reader = PdfReader(file_obj)
                page_numbers = input("Enter the page numbers to merge (e.g., '1,5,8') or type 'done' to finish with this PDF: ")
                if page_numbers.lower() == 'done':
                    continue
                page_numbers = map(int, page_numbers.split(","))
                for page_num in page_numbers:
                    pdf_writer.add_page(pdf_reader.pages[page_num - 1])

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            output_file_name = f"merged_{os.path.splitext(os.path.basename(pdf_path))[0]}_{timestamp}.pdf"
            output_path = os.path.join(output_folder, output_file_name)
            with open(output_path, "wb") as output_file:
                pdf_writer.write(output_file)
            print(f"PDFs merged successfully. Merged PDF saved at: {output_path}")
        except Exception as e:
            print(f"Error processing PDF file: {e}")

    print("No pages merged. Exiting...")

# Example usage
if __name__ == "__main__":
    Cutter_PDF()
