import PythonMagick

img = PythonMagick.Image('pdf.bmp')

img.sample('128x128')
img.write('ico.ico')
