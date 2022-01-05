import os
import pathlib
import sys
from PIL import ImageFilter
from PIL import Image

dest_path = pathlib.Path().resolve()
successful = False

if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        
        # Fetch image from ARGV list
        image = Image.open(sys.argv[i])
        print("current image size: ", image.size)

        width, height = image.size

        resized_image = image.resize((width * 10, height * 10), Image.ANTIALIAS)
        print("new image size: ", resized_image.size)
        resized_image.filter(ImageFilter.SHARPEN)
        print("Sharpened")
        
        # Save image to user's current working directory
        resized_image.save(os.path.join(dest_path, image.filename))

        image.close()
        resized_image.close()
        isSuccessful = True

else:
    print("ERROR: Please open this tool with an image")
    os.system("pause")

if successful:
    print("Done!")
    os.system("pause")
