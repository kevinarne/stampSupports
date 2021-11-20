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
img_width, img_height = img.size

# Scan through bitmap several times, depending on slope of walls
steps = int(input("How many pixels deep should the layers be?\n"))
step_inc = 255//steps
detect_color = (0, 0, 0, 255)
shift_color = (0, 0, 0, 255 - step_inc)
print(step_inc)
print(shift_color)
for s in range(steps):
    for x in range(img_width):
        for y in range(img_height):
            pix = img.getpixel((x, y))
            # Check whether the pixel is black
            if (pix == detect_color):
                # If black, check whether neighbors are the color of the previous step (white for first iteration)
                neigh = neighbors(x, y, img_width, img_height)
                correct_color = False
                for n in neigh:
                    if img.getpixel(n) == (0, 0, 0, 0):
                        correct_color = True
                # If so, set to the color of the current step
                if correct_color:
                    pixels[x,y] = shift_color
                # Set new target color and shift color
                detect_color = shift_color
                shift_color = (0, 0, 0, shift_color[3]-step_inc)
                print(shift_color)

# Export new bitmap with "sloped" appended
img.save(filename[:len(filename)-4] + "sloped.png", format="png")
