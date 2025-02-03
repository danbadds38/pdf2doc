import os
import glob
from pdf2docx import Converter


def convert_all_pdfs(input_folder, output_folder):
    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)

    # Get a list of all PDF files in the input folder
    pdf_files = glob.glob(os.path.join(input_folder, '*.pdf'))
    if not pdf_files:
        print(f"No PDF files found in '{input_folder}'")
        return

    # Process each PDF file found
    for pdf_file in pdf_files:
        # Generate the DOCX file path by replacing the PDF extension
        base_filename = os.path.splitext(os.path.basename(pdf_file))[0]
        output_docx = os.path.join(output_folder, base_filename + '.docx')

        print(f"Converting '{pdf_file}' to '{output_docx}'...")
        # Initialize the converter for the current PDF file
        cv = Converter(pdf_file)
        cv.convert(output_docx, start=0, end=None)
        cv.close()
        print(f"Conversion complete for '{pdf_file}'")

    print("All conversions complete.")


if __name__ == '__main__':
    # Define the input and output directories (relative to the project root)
    input_folder = 'intput'
    output_folder = 'output'

    convert_all_pdfs(input_folder, output_folder)
