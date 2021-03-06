import sys
from PIL import Image


ASCII_CHARS = [ '#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']

def scale_image(image, new_width=100):
    """Resizes an image preserving the aspect ratio.
    """
    (original_width, original_height) = image.size
    aspect_ratio = original_width/float(original_height)
    new_height = int(aspect_ratio * new_width)

    new_image = image.resize((new_width, new_width))
    return new_image

def convert_to_grayscale(image):
    return image.convert('L')

def map_pixels_to_ascii_chars(image, range_width=100):
    """Maps each pixel to an ascii char based on the range
    in which it lies.

    0-255 is divided into 11 ranges of 25 pixels each.
    """

    pixels_in_image = list(image.getdata())
    pixels_to_chars = [ASCII_CHARS[pixel_value/range_width] for pixel_value in
            pixels_in_image]

    return "".join(pixels_to_chars)

def convert_image_to_ascii(image):
    image = scale_image(image)
    image = convert_to_grayscale(image)
    (original_width, original_height) = image.size

    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_pixels_to_chars = len(pixels_to_chars)

    image_ascii = [pixels_to_chars[index: index + original_width] for index in
            xrange(0, len_pixels_to_chars, original_width)]

    return "\n".join(image_ascii)

import urllib, cStringIO

def handle_image_conversion(image_filepath):
    image = None
    try:
        file = cStringIO.StringIO(urllib.urlopen(image_filepath).read())
        image = Image.open(file)
    except Exception, e:
        print "Unable to open image file {image_filepath}.".format(image_filepath=image_filepath)
        print e
        return

    image_ascii = convert_image_to_ascii(image)
    return image_ascii

