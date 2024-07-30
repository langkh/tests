import cv2
import numpy as np
import tempfile
import os
import time






# Function to create and delete a temporary image file
def create_and_delete_temp_image():
    # Create a black image
    image = np.zeros((100, 100, 3), np.uint8)

    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp_file:
        temp_filename = tmp_file.name
        # Save the image to the temporary file
        cv2.imwrite(temp_filename, image)
        img = cv2.imread(temp_filename)
        #time.sleep(5)
        #cv2.imshow(temp_filename,img)
        #cv2.waitKey(10000)
        #cv2.destroyAllWindows()
    os.unlink(temp_filename)






    print(f"Temporary file created: {temp_filename}")

    # Check if the file exists
    if os.path.exists(temp_filename):
        print(f"File {temp_filename} exists, now attempting to delete it.")
        # Remove the file using os.unlink()
        os.unlink(temp_filename)
        print(f"File {temp_filename} has been deleted.")
    else:
        print(f"File {temp_filename} does not exist.")

    # Verify deletion
    if not os.path.exists(temp_filename):
        print(f"File {temp_filename} was successfully deleted.")
    else:
        print(f"Failed to delete file {temp_filename}.")

# Main loop

create_and_delete_temp_image()
    #time.sleep(1)  # Wait for 1 second before creating the next image
