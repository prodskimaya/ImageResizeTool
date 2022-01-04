import os
import pathlib
import sys
from PIL import Image

# Fetches absolute file path
dest_path = pathlib.Path().resolve()

# Checks if Program is opened with an image
if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):

        # Opens an image from ARGV list
        image = Image.open(sys.argv[i])
        print("current image size: ", image.size)

        width, height = image.size
        # Multiply image width and height by 10
        resized_image = image.resize((width * 10, height * 10), Image.ANTIALIAS)
        print("new image size: ", resized_image.size)

        # Saves image to user's current working directory
        resized_image.save(os.path.join(dest_path, image.filename))

        image.close()
        resized_image.close()

else:
    print("ERROR: Please open this tool with an image")
    os.system("pause")


print("Done!")
os.system("pause")
