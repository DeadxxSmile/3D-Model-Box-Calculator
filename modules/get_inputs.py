import traceback

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid input, please enter a valid number.")
            
def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Invalid input, please enter a valid number.")

def get_box_dimensions():
    try:
        item_height = get_float_input("Enter the height of the item: ")
        item_width = get_float_input("Enter the width of the item: ")
        item_depth = get_float_input("Enter the depth of the item: ")
        item_slop = get_float_input("Enter the slop for the item: ")
        item_count = get_int_input("Enter the number of items: ")
        outer_walls = get_float_input("Enter the thickness of the outer walls: ")
        inner_walls = get_float_input("Enter the thickness of the inner walls: ")
        
        print("-" * 50)
        
        box_settings = (item_height, item_width, item_depth, item_slop, item_count, outer_walls, inner_walls)
        
        for entry in box_settings:
            if not isinstance(entry, (float, int)):
                raise Exception("Invalid Input, Please Enter a Valid Number for all settings.")
        
        return box_settings
    except Exception as e:
        print(f"An Error Occurred While Getting Box Dimensions: {e}")
        print(f"Error Type: {type(e)}")

def get_lid_settings():
    try:
        lid_depth = get_float_input("Enter the depth of the lid: ")
        lid_wall = get_float_input("Enter the thickness of the lid walls: ")
        lid_separation = get_float_input("Enter the separation between the lid and the box outer wall: ")
        lid_gap = get_float_input("Enter the gap between the lid and the box: ")
        print("-" * 50)
        lid_settings = (lid_depth, lid_wall, lid_separation, lid_gap)
        for entry in lid_settings:
            if not isinstance(entry, (float, int)):
                exception = Exception(f"Invalid Input, Please Enter a Valid Number for all settings.")
                raise exception
        return lid_settings
    except Exception as e:
        print(f"An Error Occured While Getting Lid Settings: {e}")
        print(f"Error Type: {type(e)}")
        print(f"Traceback: {traceback.format_exc()}")

def get_window_settings():
    try:
        window_overhang = get_float_input("Enter the overhang of the window: ")
        window_separator = get_float_input("Enter the overhang of the window separators: ")
        print("-" * 50)
        window_settings = (window_overhang, window_separator)
        for entry in window_settings:
            if not isinstance(entry, (float, int)):
                exception = Exception(f"Invalid Input, Please Enter a Valid Number for all settings.")
                raise exception
        return window_settings
    except Exception as e:
        print(f"An Error Occured While Getting Window Settings: {e}")
        print(f"Error Type: {type(e)}")
        print(f"Traceback: {traceback.format_exc()}")