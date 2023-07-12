# **Summary**


ImageCraft is a cutting-edge photo editing platform that offers advanced imaging solutions:
    
    
* Developed an interactive, Python-based application for streamlined photo editing
  
* Utilized prominent libraries like PIL, NumPy, and Matplotlib for advanced image manipulation
  
* Implemented colorization features via PIL and NumPy, offering a broader editing palette
  
* Incorporated edge detection capabilities using PyEdgeEval, improving the platform's versatility



# **Core Features**

* Interactive Python-based Application: Enables straightforward navigation and editing process
  
* Advanced Image Manipulation: Using libraries like PIL, NumPy, and Matplotlib, it offers sophisticated photo editing tools
  
* Colorization: Integrates PIL and NumPy to offer diverse colorizing options
  
* Edge Detection: Features edge detection capabilities with the help of PyEdgeEval
  
* Intuitive Menu: Prompts users to input an image and choose from a wide array of edits through a command menu


# **Main Menu**


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

                    
# **Libraries**

*PIL
*NumPy
*Matplotlib
*PyEdgeEval
