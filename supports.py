# Import the bitmap
# Scan through bitmap several times, depending on slope of walls
    # For each loop
    # Check whether the pixel is white
        # If white, check whether neighbors are the color of the previous step (black for first iteration)
            # If so, set to the color of the current step
# Export new bitmap with "sloped" appended
