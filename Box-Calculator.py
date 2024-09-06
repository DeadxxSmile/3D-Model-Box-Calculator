import traceback
from modules import *


def main():
    # Display the intro block
    intro_block()
    # Get the box type from the user
    box_type = get_box_type()
    # Build the box based on the box type
    build_box(box_type)


if __name__ == "__main__":
    try:
        # Call the main function
        main()
    except Exception as e:
        # If an error occurs in the main function, print the error message and traceback
        print(f"An Error Occurred: {e}")
        print(f"Error Type: {type(e)}")
        print(f"Traceback: {traceback.format_exc()}")
