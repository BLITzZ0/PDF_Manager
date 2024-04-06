from PyPDF2 import PdfReader
import os

def extract_images():
    pdf_path = input("Enter the path of the PDF file to extract images from: ")

    try:
        with open(pdf_path, "rb") as file_obj:
            pdf_reader = PdfReader(file_obj)
            num_pages = len(pdf_reader.pages)

            output_folder = r"C:\Users\ababh\Desktop\ImagesPDF"
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                if '/XObject' in page['/Resources']:
                    xObject = page['/Resources']['/XObject']
                    for obj in xObject:
                        if xObject[obj]['/Subtype'] == '/Image':
                            data = xObject[obj].get_data()
                            mode = ""
                            if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                                mode = "RGB"
                            else:
                                mode = "P"

                            image_path = os.path.join(output_folder, f"page{page_num + 1}_{obj[1:]}.png")
                            with open(image_path, "wb") as image_file:
                                image_file.write(data)

                            print(f"Extracted image {obj} from page {page_num + 1}")

            print("Images extracted successfully.")
    except Exception as e:
        print(f"Error extracting images: {e}")

# Example usage
if __name__ == "__main__":
    extract_images()
