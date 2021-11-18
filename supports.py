from PIL import Image

def neighbors(x, y, width, height):
    # Check for boundaries (top, left, right, bottom)
    left = False
    right = False
    top = False
    bottom = False
    if (x == 0):
        left = True
    if (x == width - 1):
        right = True
    if (y == 0):
        top = True
    if (y == height - 1):
        bottom = True

filename = input("What is the filename with extension?\n")

# Import the bitmap
img = Image.open(filename)
pixels = img.load()
im_width, im_height = img.size

# Scan through bitmap several times, depending on slope of walls
for x in range(im_width):
    for y in range(3):
        print(x, y, im_width, im_height)
        neighbors(x, y, im_width, im_height)
    # For each loop
    # Check whether the pixel is white
        # If white, check whether neighbors are the color of the previous step (black for first iteration)
            # If so, set to the color of the current step
# Export new bitmap with "sloped" appended
