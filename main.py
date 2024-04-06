from merge_pdfs import merge_pdfs
from extract_image import extract_images
from Cutter_PDF import Cutter_PDF

def main():
    print("Welcome to the PDF Manager Application!")

    while True:
        print("\nWhat is your Purpose: ")
        print("1. Merge PDFs")
        print("2. Extract Images from PDF")
        print("3. Merge PDFs by Pages")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            merge_pdfs()
        elif choice == '2':
            extract_images()
        elif choice == '3':
            Cutter_PDF()
        elif choice == '4':
            print("Thank you for using the PDF Merger Application!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
