import tesserocr
from PIL import Image


result = tesserocr.file_to_text('Code.jpg')
print(result)