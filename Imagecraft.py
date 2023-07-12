"""Video link: https://drive.google.com/file/d/1cAACuRGXl1jxAqIsjjGkXbTNUoV7D6_2/view?usp=sharing"""


import sys
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageOps

def truncate(val):
    ''' returns 0 if val<0 and 255 if val > 255 and otherwise, returns val '''
    return min(255, max(0, val))

def truncate3(r, g, b):
    ''' returns a tuple with the truncate values of r, g, and b which represents a pixel '''
    return (truncate(r), truncate(g), truncate(b))

def negative(img):
    """Creates a negative version of the image by inverting the colors.
    
    Args:
        img: The input image.
    
    Returns:
        A new image with inverted colors.
    """
    inverted_image = ImageOps.invert(img)
    return inverted_image

def black_and_white(img, cutoff):
    new_img = img.copy()
    pixels = new_img.load()
    
    for i in range(new_img.size[0]):
        for j in range(new_img.size[1]):
            r, g, b = pixels[i, j]
            m = (r + g + b) // 3
            
            if m >= cutoff:
                pixels[i, j] = (255, 255, 255)
            else:
                pixels[i, j] = (0, 0, 0)
                
    return new_img

def brighten(img, val):
    new_img = img.copy()
    pixels = new_img.load()
    
    for i in range(new_img.size[0]):
        for j in range(new_img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = truncate3(r + val, g + val, b + val)
            
    return new_img

def colorize(img, alpha):
    new_img = img.copy()
    pixels = new_img.load()
    
    for i in range(new_img.size[0]):
        for j in range(new_img.size[1]):
            r, g, b = pixels[i, j]
            m = (r + g + b) // 3
            
            new_r = r * (1 - alpha) + 255 * alpha if r > m else r * (1 - alpha)
            new_g = g * (1 - alpha) + 255 * alpha if g > m else g * (1 - alpha)
            new_b = b * (1 - alpha) + 255 * alpha if b > m else b * (1 - alpha)
            
            pixels[i, j] = truncate3(new_r, new_g, new_b)
            
    return new_img

def red_green_colorblindness(img):
    new_img = img.copy()
    pixels = new_img.load()
    
    for i in range(new_img.size[0]):
        for j in range(new_img.size[1]):
            r, g, b = pixels[i, j]
            rg = (r // 2) + (g // 2)
            pixels[i, j] = (rg, rg, b)
            
    return new_img

def edge_detect(img, val):
    new_img = img.copy()
    pixels = new_img.load()
    
    for i in range(new_img.size[0] - 1):
        for j in range(new_img.size[1] - 1):
            r, g, b = pixels[i, j]
            r_right, g_right, b_right = pixels[i + 1, j]
            r_below, g_below, b_below = pixels[i, j + 1]
            
            diff_right = abs(r - r_right) + abs(g - g_right) + abs(b - b_right)
            diff_below = abs(r - r_below) + abs(g - g_below) + abs(b - b_below)
            
            if diff_right > val or diff_below > val:
                pixels[i, j] = (255, 255, 255)
            else:
                pixels[i, j] = (0, 0, 0)
                
    return new_img

def main():
    current_image = None

    while True:
        command = input("Enter a command: ").strip().upper()
        
        if command == 'M':
            print("M - print this menu")
            print("L - ask for a name of an image file and load it into the system")
            print("V - view the current image (use pyplot.imshow)")
            print("I - print Info about the image including its size")
            print("F - scale down the image by an integer factor k (and ask the user for that factor)")
            print("Z - zoom in on a range of the image (ask the user for the bounds)")
            print("B - brighten the image by a specified value (ask the user for the value)")
            print("E - run edge detection on the image with a specified difference value")
            print("C - colorize the image with the factor alpha (ask the user for alpha)")
            print("R - run the red-green-color blindness filter on the image")
            print("S - save the image in a file (ask the user for the file name)")
            print("Q - quit the program")
            print("N - create a negative version of the image")
        elif command == 'L':
            file_name = input("Enter the image file name: ")
            current_image = Image.open(file_name)
        elif command == 'V':
            if current_image:
                plt.imshow(current_image)
                plt.show()
            else:
                print("No image loaded.")
        elif command == 'I':
            if current_image:
                print(f"Image size: {current_image.size}")
            else:
                print("No image loaded.")
        elif command == 'F':
            if current_image:
                factor = int(input("Enter the scale down factor: "))
                current_image = current_image.resize((current_image.size[0] // factor, current_image.size[1] // factor))
            else:
                print("No image loaded.")
        elif command == 'Z':
            if current_image:
                left = int(input("Enter left boundary: "))
                upper = int(input("Enter upper boundary: "))
                right = int(input("Enter right boundary: "))
                lower = int(input("Enter lower boundary: "))
                current_image = current_image.crop((left, upper, right, lower))
            else:
                print("No image loaded.")
        elif command == 'B':
            if current_image:
                val = int(input("Enter the brightness value: "))
                current_image = brighten(current_image, val)
            else:
                print("No image loaded.")
        elif command == 'E':
            if current_image:
                val = int(input("Enter the edge detection difference value: "))
                current_image = edge_detect(current_image, val)
            else:
                print("No image loaded.")
        elif command == 'C':
            if current_image:
                alpha = float(input("Enter the colorize alpha value: "))
                current_image = colorize(current_image, alpha)
            else:
                print("No image loaded.")
        elif command == 'R':
            if current_image:
                current_image = red_green_colorblindness(current_image)
            else:
                print("No image loaded.")
        elif command == 'S':
            if current_image:
                file_name = input("Enter the output file name: ")
                current_image.save(file_name)
            else:
                print("No image loaded.")
        elif command == "N":
            current_image = negative(current_image)
            print("Negative version of the image created.")
        elif command == 'Q':
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
