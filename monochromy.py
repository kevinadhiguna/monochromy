from PIL import Image

image_file = Image.open('test.jpg')

image_file = image_file.convert('L')

image_file.save('monochrome.png')
