from PyPDF2 import PdfMerger
from datetime import datetime

def merge_pdfs():
    pdf_list = []
    while True:
        pdf_file = input("Enter the path of the PDF file to merge (or type 'done' to finish): ")
        if pdf_file.lower() == 'done':
            break
        pdf_list.append(pdf_file)

    if not pdf_list:
        print("No PDF files provided. Exiting...")
        return

    output_folder = r"C:\Users\ababh\Desktop\MergedPDF"

    output_file_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".pdf"
    output_path = output_folder + "\\" + output_file_name

    merger = PdfMerger()
    for pdf_file in pdf_list:
        with open(pdf_file, "rb") as file_obj:
            merger.append(file_obj)

    with open(output_path, "wb") as output_file:
        merger.write(output_file)

    merger.close()
    print(f"PDF files merged successfully. Merged PDF saved at: {output_path}")

# Example usage
if __name__ == "__main__":
    merge_pdfs()
