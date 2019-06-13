import os
import tempfile
# settings -> project interpreter -> '+* seach for 'pdf2image' and install
from pdf2image import convert_from_path

class PdfConverter:

    def convert(self, input_dir):
        output_dir = os.path.join('src', 'static', 'img')
        images = []
        with tempfile.TemporaryDirectory() as path:
            print('path: ', path)
            images = convert_from_path(input_dir, output_folder=output_dir, fmt='jpeg')
        return images
