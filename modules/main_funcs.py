import traceback
from .calculate_values import *
from .get_inputs import *
from .output_results import *


def intro_block():
    sep = "  " + "-" * 48
    print(sep)
    print("|", "3D Model Box Calculator".center(48), "|")
    print(sep, "\n")

    print(
        "This script will calculate the values for a box to",
        "\nbe created using a 3D printer. You will be prompted",
        "\nto enter the dimensions of the box, lid, and windows.\n",
    )
    print(sep, "\n")

    print("First, pick the type of box you want to create.")
    print("    (1) Box without Lid or Windows")
    print("    (2) Box with Lid")
    print("    (3) Box with Lid and Windows\n")


def build_box(box_type):
    try:
        # Get shrinkage factor from user or based on filament type
        shrinkage_factor = get_shrinkage_factor()
        
        # Get box dimensions and calculate box results
        box_settings = get_box_settings()
        box_results = calc_box(box_settings, shrinkage_factor)

        if box_type == 3:
            # Get lid settings and calculate lid results
            lid_settings = get_lid_settings()
            lid_results = calc_lid(box_results, lid_settings, shrinkage_factor)

            # Get window settings and calculate window results
            window_settings = get_window_settings()
            window_results = calc_window(
                box_settings, lid_settings, window_settings, shrinkage_factor
            )

            # Output all the results
            output_results(shrinkage_factor, box_results, lid_results, window_results)

        elif box_type == 2:
            # Get lid settings and calculate lid results
            lid_settings = get_lid_settings()
            lid_results = calc_lid(box_results, lid_settings, shrinkage_factor)

            # Output box and lid results
            output_results(shrinkage_factor, box_results, lid_results)

        elif box_type == 1:
            # Output box results
            output_results(shrinkage_factor, box_results)

        else:
            # If the user entered invalid input, raise an exception
            exception = Exception(
                f"Invalid Input, Please Enter 1 or 2 For Each Option."
            )
            raise exception

    except Exception as e:
        # If an error occurs during the calculations, print the error message and traceback
        print(f"An Error Occurred While Generating Box Values: {e}")
        print(f"Error Type: {type(e)}")
        print(f"Traceback: {traceback.format_exc()}")
