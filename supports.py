from PIL import Image

def neighbors(x, y, width, height):
    neigh = []
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

    # Top left
    if (not top and not left):
        neigh.append((x - 1, y - 1))
    # Top middle
    if (not top):
        neigh.append((x, y - 1))
    # Top right
    if (not top and not right):
        neigh.append((x + 1, y - 1))
    # Left
    if (not left):
        neigh.append((x - 1, y))
    # Right
    if (not right):
        neigh.append((x + 1, y))
    # Bottom left
    if (not bottom and not left):
        neigh.append((x - 1, y + 1))
    # Bottom middle
    if (not bottom):
        neigh.append((x, y + 1))
    # Bottom right
    if (not bottom and not right):
        neigh.append((x + 1, y + 1))

    return neigh

filename = input("What is the filename with extension?\n")

# Import the bitmap
img = Image.open(filename)
pixels = img.load()
im_width, im_height = img.size

# Scan through bitmap several times, depending on slope of walls
for x in range(im_width):
    for y in range(1):
        print(x, y)
        n = neighbors(x, y, im_width, im_height)
        print(n)
    # For each loop
    # Check whether the pixel is white
        # If white, check whether neighbors are the color of the previous step (black for first iteration)
            # If so, set to the color of the current step
# Export new bitmap with "sloped" appended
