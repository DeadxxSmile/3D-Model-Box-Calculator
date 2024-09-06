import re
import traceback


def get_box_type():
    while True:
        box_type = input("Enter the type of box you want to create (1,2 or 3): ").strip()
        if re.match(r"^[1-3]$", box_type):
            return int(box_type)
        else:
            print("Invalid input, please enter a valid number.")


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


def get_user_input(key_list):
    output_list = {}

    try:
        for key, value in key_list.items():
            while True:
                if value["type"] == float:
                    output_list[key] = get_float_input(value["prompt"])
                elif value["type"] == int:
                    output_list[key] = get_int_input(value["prompt"])
                else:
                    raise Exception("Script Error, Invalid Data Type(get_user_input).")

                if not isinstance(output_list[key], (value["type"])):
                    raise Exception(f"Invalid Input, Please Enter a Valid {value["type"]}.")
                else:
                    break

    except ValueError:
        print("Invalid input, please enter a valid number.")

    return output_list


def get_box_settings():
    try:
        key_list = {
            "item_height": {"prompt": "Enter the height of the item: ", "type": float},
            "item_width": {"prompt": "Enter the width of the item: ", "type": float},
            "item_depth": {"prompt": "Enter the depth of the item: ", "type": float},
            "item_slop": {"prompt": "Enter the slop for the item: ", "type": float},
            "item_count": {"prompt": "Enter the number of items: ", "type": int},
            "outer_wall": {"prompt": "Enter the thickness of the outer walls: ", "type": float},
            "inner_wall": {"prompt": "Enter the thickness of the inner walls: ", "type": float}
        }

        print("-" * 50, "\n")
        box_settings = get_user_input(key_list)
        print("")

        return box_settings

    except Exception as e:
        print(f"An Error Occurred While Getting Box Dimensions: {e}")
        print(f"Error Type: {type(e)}")


def get_lid_settings():
    try:
        key_list = {
            "lid_depth": {"prompt": "Enter the depth of the lid: ", "type": float},
            "lid_wall": {"prompt": "Enter the thickness of the lid walls: ", "type": float},
            "lid_separation": {"prompt": "Enter the separation between the lid and the box outer wall: ",
                               "type": float},
            "lid_gap": {"prompt": "Enter the gap between the lid and the box: ", "type": float}
        }

        print("-" * 50, "\n")
        lid_settings = get_user_input(key_list)
        print("")

        return lid_settings

    except Exception as e:
        print(f"An Error Occurred While Getting Lid Settings: {e}")
        print(f"Error Type: {type(e)}")
        print(f"Traceback: {traceback.format_exc()}")


def get_window_settings():
    try:
        key_list = {
            "window_overhang": {"prompt": "Enter the overhang of the window: ", "type": float},
            "window_separator": {"prompt": "Enter the overhang of the window separators: ", "type": float}
        }

        print("-" * 50, "\n")
        window_settings = get_user_input(key_list)
        print("")
        print("-" * 50, "\n")

        return window_settings

    except Exception as e:
        print(f"An Error Occurred While Getting Window Settings: {e}")
        print(f"Error Type: {type(e)}")
        print(f"Traceback: {traceback.format_exc()}")
