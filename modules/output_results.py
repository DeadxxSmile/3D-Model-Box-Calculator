import traceback


def print_results(results_data):
    try:
        for entry in results_data:
            value_name_parts = entry.split("_")
            value_name = " ".join(value_name_parts).capitalize()
            print(f"    {value_name}: {round(results_data[entry], 2)}")
    except Exception as e:
        print(f"An Error Occurred While Printing Results: {e}")
        print(f"Error Type: {type(e)}")
        print(f"Traceback: {traceback.format_exc()}")


def output_results(box_results, lid_results=None, window_results=None):
    try:
        if box_results is not None:
            print_results(box_results)
            print("  ", "-" * 30)
        else:
            exception = Exception(f"Invalid Results, Please Check Your Inputs.")
            raise exception
        if lid_results is not None:
            print_results(lid_results)
            print("  ", "-" * 30)
        if window_results is not None:
            print_results(window_results)
        print("\n\n")
    except Exception as e:
        print(f"An Error Occurred While Outputting Results: {e}")
        print(f"Error Type: {type(e)}")
        print(f"Traceback: {traceback.format_exc()}")
