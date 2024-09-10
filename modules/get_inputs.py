import re
import traceback


def get_box_type():
    while True:
        box_type = input(" Enter Box Type Option(1,2 or 3): ").strip()
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
            
def get_percentage_input(prompt):
    while True:
        try:
            # Get user input and strip leading/trailing spaces
            user_input = input(prompt).strip()
            # Check if input contains the "%" sign
            if "%" in user_input:
                # Remove the "%" sign and convert to float, then divide by 100 to get the decimal form
                return float(user_input.replace("%", "").strip()) / 100
            else:
                # If no "%" sign, just convert directly to float
                return float(user_input)
        except ValueError:
            print("Invalid input, please enter a valid number or percentage (e.g., '5%' or '0.05').")


def get_user_input(key_list):
    output_list = {}

    try:
        for key, value in key_list.items():
            while True:
                if value["type"] == float:
                    output_list[key] = get_float_input(value["prompt"])
                elif value["type"] == int:
                    output_list[key] = get_int_input(value["prompt"])
                elif key == "shrinkage_factor":
                    output_list[key] = get_percentage_input(value["prompt"])
                else:
                    raise Exception("Script Error, Invalid Data Type(get_user_input).")

                if not isinstance(output_list[key], (value["type"])):
                    raise Exception(f"Invalid Input, Please Enter a Valid {value["type"]}.")
                else:
                    break

    except ValueError:
        print("Invalid input, please enter a valid number.")

    return output_list

def get_shrinkage_factor():
    # Dictionary to hold common shrinkage factors for different filaments
    filament_shrinkage = {
        "PLA": 0.997,  # ~0.3% shrinkage
        "ABS": 0.993,  # ~0.7% shrinkage
        "PETG": 0.995,  # ~0.5% shrinkage
        "Nylon": 0.980,  # ~2.0% shrinkage
        "TPU": 0.990,  # ~1.0% shrinkage
        "Polycarbonate": 0.990,  # ~1.0% shrinkage
        "HIPS": 0.995   # ~0.5% shrinkage
    }

    # Prompt the user to select a filament type
    print("\n  ", "-" * 48, "\n")
    print(" Select the filament type being used:")
    for i, filament in enumerate(filament_shrinkage.keys(), start = 1):
        print(f"    ({i}) {filament}")
    print("    (0) Enter Custom Shrinkage Factor\n")

    try:
        filament_choice = int(input(" Enter the number corresponding to your filament type: ").strip())

        if filament_choice == 0:
            shrinkage_prompt = " Enter the custom shrinkage factor: "
            shrinkage = get_percentage_input(shrinkage_prompt)
        elif 1 <= filament_choice <= len(filament_shrinkage):
            # Select the corresponding shrinkage factor
            filament = list(filament_shrinkage.keys())[filament_choice - 1]
            shrinkage = filament_shrinkage[filament]
            print(f" Using shrinkage factor {shrinkage} for {filament}.")
        else:
            raise ValueError("Invalid choice")
        print("")
        shrinkage += 1
        return shrinkage

    except ValueError:
        print("Invalid input, please enter a valid number.")
        return get_shrinkage_factor()  # Recursively ask again if there's an error

def get_box_settings():
    try:
        key_list = {
            "item_height": {"prompt": " Enter the height of the item: ", "type": float},
            "item_width": {"prompt": " Enter the width of the item: ", "type": float},
            "item_depth": {"prompt": " Enter the depth of the item: ", "type": float},
            "item_gap": {"prompt": " Enter the gap for the item: ", "type": float},
            "item_count": {"prompt": " Enter the number of items: ", "type": int},
            "outer_wall": {"prompt": " Enter the thickness of the outer walls: ", "type": float},
            "inner_wall": {"prompt": " Enter the thickness of the inner walls: ", "type": float}
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
            "lid_depth": {"prompt": " Enter the depth of the lid: ", "type": float},
            "lid_wall": {"prompt": " Enter the thickness of the lid walls: ", "type": float},
            "lid_separation": {"prompt": " Enter the separation between the lid and the box outer wall: ", "type": float},
            "lid_gap": {"prompt": " Enter the gap between the lid and the box: ", "type": float}
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
            "window_overhang": {"prompt": " Enter the overhang of the window: ", "type": float},
            "window_separator": {"prompt": " Enter the overhang of the window separators: ", "type": float}
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
