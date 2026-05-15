import sys

def rush(x, y):
    """
    Display a square pattern based on x (width) and y (height)

    Args:
        x (int): Width of the square
        y (int): Height of the square
    """
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return
    
    for i in range(y):
        if i == 0:
            if x == 1:
                print("o")
            else:
                print("o" + "-" * (x - 2) + "o")
        elif i == y - 1:
            if x == 1:
                print("o")
            else:
                print("o" + "-" * (x - 2) + "o")
        else:
            if x == 1:
                print("|")
            else:
                print("|" + " " * (x - 2) + "|")