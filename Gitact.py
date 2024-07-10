def print_pyramid(levels):
    for i in range(1, levels + 1):
        # Print leading spaces
        for j in range(levels - i):
            print(" ", end="")
        # Print pyramid stars
        for k in range(2 * i - 1):
            print("*", end="")
        # Move to the next line after each level
        print()

# Specify the number of levels for the pyramid
levels = 5
print_pyramid(levels)