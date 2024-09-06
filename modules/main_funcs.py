import traceback
from .calculate_values import calc_box, calc_lid, calc_window
from .get_inputs import get_box_settings, get_lid_settings, get_window_settings
from .output_results import output_results

def intro_block():
    print(" ", "-" * 50, " ")
    print("|", "3D Model Box Calculator".center(50), "|")
    print(" ", "-" * 50, " \n")
    
    print("This script will calculate the values for a box to be created using a 3D printer.")
    print("You will be prompted to enter the dimensions of the box, lid, and windows.")
    print("-" * 50, "\n")
    print("First, pick the type of box you want to create.")
    print("Options: (1) Box without Lid or Windows, (2) Box with Lid, (3) Box with Lid and Windows\n")
    
def build_box(box_type):
    boxSettings, boxResults, lidSettings, lidResults, windowSettings,windowResults= {}, {}, {}, {}, {}, {}
    try:
        # Get box dimensions and calculate box results
        boxSettings = get_box_settings()
        boxResults = calc_box(boxSettings)
        
        if box_type == 3:
            # Get lid settings and calculate lid results
            lidSettings = get_lid_settings()
            lidResults = calc_lid(boxResults, lidSettings)
            
            # Get window settings and calculate window results
            windowSettings = get_window_settings()
            windowResults = calc_window(boxSettings, lidSettings, windowSettings)
            
            # Output all the results
            output_results(boxResults, lidResults, windowResults)

        elif box_type == 2:
            # Get lid settings and calculate lid results
            lidSettings = get_lid_settings()
            lidResults = calc_lid(boxResults, lidSettings)
            
            # Output box and lid results
            output_results(boxResults, lidResults)
            
        elif box_type == 1:
            # Output box results
            output_results(boxResults)
            
        else:
            # If the user entered invalid input, raise an exception
            exception = Exception(f"Invalid Input, Please Enter 1 or 2 For Each Option.")
            raise exception
            
    except Exception as e:
        # If an error occurs during the calculations, print the error message and traceback
        print(f"An Error Occured While Generating Box Values: {e}")
        print(f"Error Type: {type(e)}")
        print(f"Traceback: {traceback.format_exc()}")