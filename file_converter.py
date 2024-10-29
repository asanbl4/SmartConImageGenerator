from pdf2image import convert_from_path


def convert_pdf_to_jpg(pdf_path, output_path):
    images = convert_from_path(pdf_path)
    image_paths = []

    for i, image in enumerate(images):
        cropped_image = image.crop((0, 0, image.width, image.height - 1600))
        cropped_image.save(output_path, 'JPEG')
        image_paths.append(output_path)
        print(f"Saved page {i + 1} as JPEG at {output_path}")

    return image_paths
