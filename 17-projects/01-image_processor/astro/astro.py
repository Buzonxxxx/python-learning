# Pillow https://pypi.org/project/Pillow/

from PIL import Image

astro = Image.open("./astro.jpg")

# get thumbnail
astro.thumbnail((400, 400))
astro.save("./thumbnail.jpg")

# check image info
print(astro.format, astro.size)