import traceback
from .calculate_values import calc_box, calc_lid, calc_window
from .get_inputs import get_box_settings, get_lid_settings, get_window_settings
from .output_results import output_results


def intro_block():
    sep = "-" * 50
    print(" ", sep, " ")
    print("|", "3D Model Box Calculator".center(50), "|")
    print(" ", sep, " \n")

    print("This script will calculate the values for a box to be created using a 3D printer.")
    print("You will be prompted to enter the dimensions of the box, lid, and windows.")
    print(sep, "\n")

    print("First, pick the type of box you want to create.")
    print("Options: (1) Box without Lid or Windows, (2) Box with Lid, (3) Box with Lid and Windows\n")


def build_box(box_type):
    try:
        # Get box dimensions and calculate box results
        box_settings = get_box_settings()
        box_results = calc_box(box_settings)

        if box_type == 3:
            # Get lid settings and calculate lid results
            lid_settings = get_lid_settings()
            lid_results = calc_lid(box_results, lid_settings)

            # Get window settings and calculate window results
            window_settings = get_window_settings()
            window_results = calc_window(box_settings, lid_settings, window_settings)

            # Output all the results
            output_results(box_results, lid_results, window_results)

        elif box_type == 2:
            # Get lid settings and calculate lid results
            lid_settings = get_lid_settings()
            lid_results = calc_lid(box_results, lid_settings)

            # Output box and lid results
            output_results(box_results, lid_results)

        elif box_type == 1:
            # Output box results
            output_results(box_results)

        else:
            # If the user entered invalid input, raise an exception
            exception = Exception(f"Invalid Input, Please Enter 1 or 2 For Each Option.")
            raise exception

    except Exception as e:
        # If an error occurs during the calculations, print the error message and traceback
        print(f"An Error Occurred While Generating Box Values: {e}")
        print(f"Error Type: {type(e)}")
        print(f"Traceback: {traceback.format_exc()}")
