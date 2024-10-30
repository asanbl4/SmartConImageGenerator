from pdf2image import convert_from_path


def convert_pdf_to_jpg(pdf_path, output_path):
    images = convert_from_path(pdf_path)
    image_paths = []

    for i, image in enumerate(images):
        cropped_image = image.crop((160, 0, 1460, 680))  # 880 lower crop bound
        cropped_image.save(output_path, 'PNG')
        image_paths.append(output_path)
        print(f"Saved page {i + 1} as PNG at {output_path}")


if __name__ == '__main__':
    convert_pdf_to_jpg("IMG1.pdf", "IMG1.png")