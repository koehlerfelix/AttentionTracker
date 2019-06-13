import os
import tempfile
# settings -> project interpreter -> '+* seach for 'pdf2image' and install
from pdf2image import convert_from_path
from PIL import Image


class PdfConverter:

    def convert(self, input_dir):
        head, tail = os.path.split(input_dir)
        output_dir = os.path.join(os.getcwd(), 'static', 'img', os.path.splitext(tail)[0])

        # pdf has not been read yet (based on name)
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
            return convert_from_path(input_dir, output_folder=output_dir, fmt='jpeg')

        # pdf has been process, retrieve images
        else:
            images = []
            for img in os.listdir(output_dir):
                images.append(Image.open(os.path.join(output_dir, img)))
            return images
