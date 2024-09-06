import traceback
from modules import *

def main():
    boxLid = get_int_input("Type (1) for a box with a lid, or (2) for a box without a lid: ")
    boxDispaly = get_int_input("Type (1) for a box with windows, or (2) for a box without windows: ")
    print("-" * 50)
    try:
        if boxLid == 1 and boxDispaly == 1:
            boxSettings = get_box_dimensions()
            boxResults = calc_box(boxSettings) 
            lidSettings = get_lid_settings()
            lidResults = calc_lid(boxResults, lidSettings)
            windowSettings = get_window_settings()
            windowResults = calc_window(boxSettings, lidSettings, lidResults, windowSettings)
            output_results(boxResults, lidResults, windowResults)
        elif boxLid == 1 and boxDispaly == 2:
            boxSettings = get_box_dimensions()
            boxResults = calc_box(boxSettings) 
            lidSettings = get_lid_settings()
            lidResults = calc_lid(boxResults, lidSettings)
            output_results(boxResults, lidResults)
        elif boxLid == 2 and boxDispaly == 2:
            boxSettings = get_box_dimensions()
            boxResults = calc_box(boxSettings)
            output_results(boxResults)
        else:
            exception = Exception(f"Invalid Input, Please Enter 1 or 2 For Each Option.")
            raise exception
    except Exception as e:
        print(f"An Error Occured While Generating Box Values: {e}")
        print(f"Error Type: {type(e)}")
        print(f"Traceback: {traceback.format_exc()}")
        
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An Error Occured: {e}")
        print(f"Error Type: {type(e)}")
        print(f"Traceback: {traceback.format_exc()}")