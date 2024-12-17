import os
from pdf2image import convert_from_path
from pptx import Presentation
from pptx.util import Inches

def pdf_to_pptx(pdf_path, pptx_output_path):
    """
    Converts a PDF file into a PowerPoint presentation (PPTX).
    Each page of the PDF will be added as an image to the PPTX.

    Args:
        pdf_path (str): Path to the input PDF file.
        pptx_output_path (str): Path to save the output PPTX file.
    """
    # Convert PDF to a list of images
    print("Converting PDF pages to images...")
    images = convert_from_path(pdf_path)

    # Initialize a PowerPoint Presentation
    print("Creating PowerPoint presentation...")
    presentation = Presentation()

    # Add each image as a slide
    for idx, image in enumerate(images):
        print(f"Adding page {idx + 1} to presentation...")
        slide = presentation.slides.add_slide(presentation.slide_layouts[5])  # Blank slide layout
        image_path = f"temp_image_{idx}.png"
        image.save(image_path, "PNG")

        # Add image to slide
        left = Inches(0)
        top = Inches(0)
        height = Inches(7.5)  # Default height for the slide
        slide.shapes.add_picture(image_path, left, top, height=height)

        # Clean up temporary images
        os.remove(image_path)

    # Save the PowerPoint presentation
    print("Saving the presentation...")
    presentation.save(pptx_output_path)
    print(f"Presentation saved as {pptx_output_path}")

# Example Usage
if __name__ == "__main__":
    pdf_path = "input.pdf"  # Replace with your PDF file path
    pptx_output_path = "output.pptx"  # Replace with your desired output PPTX file path
    pdf_to_pptx(pdf_path, pptx_output_path)

