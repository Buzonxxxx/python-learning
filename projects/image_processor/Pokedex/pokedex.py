# Pillow https://pypi.org/project/Pillow/

from PIL import Image, ImageFilter

bulbasaur = Image.open("./original/bulbasaur.jpg")
pikachu = Image.open("./original/pikachu.jpg")

# sharpen image
sharpen_bulbasaur = bulbasaur.filter(ImageFilter.SHARPEN)
sharpen_bulbasaur.save("./edited/sharpen_bulbasaur.png", "png")

# turn grey
grey_pikachu = pikachu.convert('L')
grey_pikachu.save("./edited/grey_pikachu.png", "png")

# rotate 180 degree
crooked_pikachu = pikachu.rotate(180)
crooked_pikachu.save("./edited/crooked_pikachu.png", "png")

# resize
resize_pikachu = pikachu.resize((300, 300))
resize_pikachu.save("./edited/resize_pikachu.png", "png")

# crop
box = (100, 100, 400, 400)
cropped_pikachu = pikachu.crop(box)
cropped_pikachu.save("./edited/cropped_pikachu.png", "png")
# cropped_pikachu.show()

# check image info
print(bulbasaur.format, bulbasaur.size, bulbasaur.mode)
# print(dir(bulbasaur))