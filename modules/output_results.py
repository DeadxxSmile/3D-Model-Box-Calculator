import traceback


def print_results(results_data):
    try:
        for entry in results_data:
            value_name_parts = entry.split("_")
            value_name = " ".join(value_name_parts).capitalize()
            print(f"  {value_name}: {round(results_data[entry], 2)}")
    except Exception as e:
        print(f"An Error Occurred While Printing Results: {e}")
        print(f"Error Type: {type(e)}")
        print(f"Traceback: {traceback.format_exc()}")


def output_results(
    shrinkage_factor, box_results, lid_results=None, window_results=None
):
    try:
        if box_results is not None:
            sep = " " + "-" * 32
            print(sep)
            print("|", "Main Body Measurements".center(30), "|")
            print(sep, "\n")
            print_results(box_results)
            print("")
        else:
            exception = Exception(f"Invalid Results, Please Check Your Inputs.")
            raise exception
        if lid_results is not None:
            print(sep)
            print("|", "Lid Measurements".center(30), "|")
            print(sep, "\n")
            print_results(lid_results)
            print("")
        if window_results is not None:
            print(sep)
            print("|", "Lid Window Measurements".center(30), "|")
            print(sep, "\n")
            print_results(window_results)
        print("\n\n")
    except Exception as e:
        print(f"An Error Occurred While Outputting Results: {e}")
        print(f"Error Type: {type(e)}")
        print(f"Traceback: {traceback.format_exc()}")
