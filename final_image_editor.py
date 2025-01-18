from PIL import Image, ImageFilter

# Resize Image Function
def resize_image(input_path, output_path, width, height):
    try:
        with Image.open(input_path) as img:
            # Resize the image
            resized_img = img.resize((width, height))
            resized_img.save(output_path)
            print(f"Image successfully resized to {width}x{height} and saved to {output_path}")
    except Exception as e:
        print(f"Error resizing image: {e}")

# Crop Image Function
def crop_image(input_path, output_path, left, top, right, bottom):
    try:
        with Image.open(input_path) as img:
            # Crop the image based on coordinates (left, top, right, bottom)
            cropped_img = img.crop((left, top, right, bottom))
            cropped_img.save(output_path)
            print(f"Image successfully cropped and saved to {output_path}")
    except Exception as e:
        print(f"Error cropping image: {e}")

# Apply Filter Function
def apply_filter(input_path, output_path, filter_type):
    try:
        with Image.open(input_path) as img:
            # Apply different filters
            if filter_type == "BLUR":
                filtered_img = img.filter(ImageFilter.BLUR)
            elif filter_type == "CONTOUR":
                filtered_img = img.filter(ImageFilter.CONTOUR)
            elif filter_type == "DETAIL":
                filtered_img = img.filter(ImageFilter.DETAIL)
            else:
                print("Invalid filter type. Choose 'BLUR', 'CONTOUR', or 'DETAIL'.")
                return
            
            # Save the image with the applied filter
            filtered_img.save(output_path)
            print(f"Filter '{filter_type}' applied and saved to {output_path}")
    except Exception as e:
        print(f"Error applying filter: {e}")

# Rotate Image Function
def rotate_image(input_path, output_path, angle):
    try:
        with Image.open(input_path) as img:
            # Rotate the image by the specified angle
            rotated_img = img.rotate(angle, expand=True)
            rotated_img.save(output_path)
            print(f"Image successfully rotated by {angle} degrees and saved to {output_path}")
    except Exception as e:
        print(f"Error rotating image: {e}")

# Flip Image Function
def flip_image(input_path, output_path, flip_type):
    try:
        with Image.open(input_path) as img:
            if flip_type == "HORIZONTAL":
                flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
            elif flip_type == "VERTICAL":
                flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM)
            else:
                print("Invalid flip type. Choose 'HORIZONTAL' or 'VERTICAL'.")
                return
            
            flipped_img.save(output_path)
            print(f"Image successfully flipped ({flip_type}) and saved to {output_path}")
    except Exception as e:
        print(f"Error flipping image: {e}")
        
        
print("~~~~~~~~~~~WELCOME TO THE IMAGE EDITOR~~~~~~~~~~~~~~~~~~~~")
print('''
      
      You can perform the following operations on your image: 
        1. Resize
        2. Crop
        3. Apply filter ( blur, contour, detail)
        4. Rotate the image
        5. Flip the image
      
      ''')

while True:
    input_image = input("Enter the path to input the image: ")
    print("Which operation do you want to perform on the image?")
    ch = int(input("Enter it here: "))
    #resizing image
    if ch == 1:
        try:
            output_image_resized = input("Enter the path where the resized image should be stored: ")
            width = int(input("Enter the width of the image: "))
            height = int(input("Enter height of the image: "))
            resize_image(input_image, output_image_resized, width, height)
        
        except ValueError:
            print("Invalid entry! Width and Height must be integers!")
    #cropping image       
    elif ch == 2:
        try: 
            output_image_cropped = input("Enter the path where the cropped image should be stored: ")
            left = int(input("Enter the left coordinate: "))
            upper = int(input("Enter the upper coordinate: "))
            right = int(input("Enter the right coordinate: "))
            lower = int(input("Enter the lower coordinate: "))
            crop_image(input_image, output_image_cropped, left, upper, right, lower)
        
        except ValueError:
            print("Invalid entry! Values must be integers!")
    #applying filters to the image        
    elif ch == 3:
        output_image_filtered = input("Enter the path where the filtered image should be stored: ")
        filter_image = input("Enter the filter (BLUR / CONTOUR / DETAIL): ").upper()
        apply_filter(input_image, output_image_filtered, filter_image)
        
    #rotating the image    
    elif ch == 4:
        try:
            output_image_rotated = input("Enter the path where the rotated image should be stored: ")
            degree = float(input("Enter the degree by which you want to rotate it: "))
            rotate_image(input_image, output_image_rotated, degree) 
        
        except ValueError:
            print("Invalid entry! Degree should be an integer!")
    #flipping the image        
    elif ch == 5:
        output_image_flipped = input("Enter the path where the flipped image should be stored: ")
        flip = input("Do you want to flip the image vertically or horizontally  (enter VERTICAL / HORIZONTAL) ? ").upper()
        flip_image(input_image, output_image_flipped, flip)
        
          
    else:
        print("Invalid Choice!!")
    
    # Ask user if they want to continue and validate input
    while True:
        continue_choice = input("Do you want to perform another operation? (y/n): ").lower()
        if continue_choice == "n":
            print("Exiting the program. Goodbye!")
            break  # Exit the program
        elif continue_choice == "y":
            break  # Continue the loop for the next operation
        else:
            print("Invalid input! Please enter 'y' or 'n'!")
    
    if continue_choice == "n":
        break  # Exit the outer loop
    
        
      



