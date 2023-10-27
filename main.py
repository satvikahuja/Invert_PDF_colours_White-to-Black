import PyPDF2
from pdf2image import convert_from_path
from PIL import Image, ImageOps
#Enter your file path here
input_pdf_path = "To_convert.pdf"
def invert_pdf_colors(input_pdf_path, output_pdf_path):
    # Convert PDF pages to a list of images
    images = convert_from_path(input_pdf_path)

    # Invert colors of each image
    inverted_images = [ImageOps.invert(img.convert('RGB')) for img in images]

    # Save inverted images back to a single PDF
    inverted_images[0].save(output_pdf_path, save_all=True, append_images=inverted_images[1:])
#enter file name and the name of the file to be converted to
if __name__ == "__main__":
    input_pdf = "To_convert.pdf"
    output_pdf = "Converted.pdf"
    invert_pdf_colors(input_pdf, output_pdf)
