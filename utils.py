import cv2
import os


# function to read the target watermark image
def prepare_watermark(path_mark, inver_style):
	"""
	reads the image in greyscale, create an alpha mask according to the scale
	invert_style determines whether the key info letters/shapes are darker or lighter than the rest
	"""