import os
from PIL import Image

def convert_image_to_pdf(image_path, output_dir):
    image = Image.open(image_path)
    pdf_path = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(image_path))[0]}.pdf")
    image.convert('RGB').save(pdf_path)
    print(f"Image '{os.path.basename(image_path)}' converted to PDF: {pdf_path}")

def convert_folder_to_pdf(source_dir, output_dir):
    for file in os.listdir(source_dir):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(source_dir, file)
            convert_image_to_pdf(image_path, output_dir)

if __name__ == "__main__":
    user_choice = input("Enter '1' to convert a single image or '2' to convert images in a folder: ")

    if user_choice == '1':
        image_name = input("Enter the image file name (with extension, e.g., 'example.jpg'): ")
        image_path = os.path.join('./', image_name)
        if os.path.exists(image_path):
            convert_image_to_pdf(image_path, './PDFs')
        else:
            print("Image not found.")

    elif user_choice == '2':
        source_dir = input("Enter the folder path containing images: ")
        output_dir = input("Enter the output folder path for PDFs: ")
        if os.path.exists(source_dir):
            convert_folder_to_pdf(source_dir, output_dir)
        else:
            print("Folder not found.")
    else:
        print("Invalid choice. Please enter '1' or '2'.")
