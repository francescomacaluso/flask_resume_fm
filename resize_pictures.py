from PIL import Image
import os
import PIL
import glob

folder = 'static/assets/img/'
picture_name = 'dbt-logo.png'

file_path = folder + picture_name

image = Image.open(file_path)

resized_image = image.resize((42,42))

resized_image.save(file_path)