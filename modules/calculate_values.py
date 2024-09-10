import traceback


def calc_box(box_values, shrinkage_factor):
    try:
        box_results = {
            "item_space_width": round((box_values["item_width"] + (box_values["item_gap"] * 2)) * shrinkage_factor, 4),
            "box_height": round(((box_values["item_height"] + (box_values["item_gap"] * 2)) +
                           (box_values["outer_wall"] * 2)) * shrinkage_factor, 4),
            "box_width": round(((box_values["item_width"] + (box_values["item_gap"] * 2)) * box_values["item_count"] +
                          (box_values["outer_wall"] * 2) +
                          ((box_values["item_count"] - 1) * box_values["inner_wall"])) * shrinkage_factor, 4),
            "box_depth": round(((box_values["item_depth"] + box_values["item_gap"]) +
                          box_values["outer_wall"]) * shrinkage_factor, 4),
            "box_inner_width": round(((box_values["item_width"] + (box_values["item_gap"] * 2)) * box_values["item_count"] +
                                ((box_values["item_count"] - 1) * box_values["inner_wall"])) * shrinkage_factor, 4),
            "box_inner_height": round((box_values["item_height"] + (box_values["item_gap"] * 2)) * shrinkage_factor, 4),
            "box_inner_depth": round((box_values["item_depth"] + box_values["item_gap"]) * shrinkage_factor, 4),
            "outer_wall": round(box_values["outer_wall"] * shrinkage_factor, 4),
            "inner_wall": round(box_values["inner_wall"] * shrinkage_factor, 4),
            "item_gap": round(box_values["item_gap"] * shrinkage_factor, 4)
        }
        return box_results
    except Exception as e:
        print(f"An Error Occurred While Calculating Box Settings: {e}")
        print(f"Error Type: {type(e)}")
        print(f"Traceback: {traceback.format_exc()}")


def calc_lid(box_results, lid_settings, shrinkage_factor):
    try:
        lid_results = {
            "box_outer_depth": round((box_results["box_depth"] - lid_settings["lid_depth"] - lid_settings["lid_separation"]) * shrinkage_factor, 4),
            "box_remaining_depth": round((box_results["box_depth"] - lid_settings["lid_depth"]) * shrinkage_factor, 4),
            "lid_height": round((box_results["box_height"] + (lid_settings["lid_wall"] * 2) + (lid_settings["lid_gap"] * 2)) * shrinkage_factor, 4),
            "lid_width": round((box_results["box_width"] + (lid_settings["lid_wall"] * 2) + (lid_settings["lid_gap"] * 2)) * shrinkage_factor, 4),
            "lid_depth": round(lid_settings["lid_depth"] * shrinkage_factor, 4),
            "lid_wall": round(lid_settings["lid_wall"] * shrinkage_factor, 4),
            "lid_inner_height": round((box_results["box_height"] + (lid_settings["lid_gap"] * 2)) * shrinkage_factor, 4),
            "lid_inner_width": round((box_results["box_width"] + (lid_settings["lid_gap"] * 2)) * shrinkage_factor, 4),
            "lid_gap": round(lid_settings["lid_gap"] * shrinkage_factor, 4)
        }

        return lid_results
    except Exception as e:
        print(f"An Error Occurred While Calculating Lid Settings: {e}")
        print(f"Error Type: {type(e)}")
        print(f"Traceback: {traceback.format_exc()}")


def calc_window(box_settings, lid_settings, window_settings, shrinkage_factor):
    try:
        window_results = {
            "window_overhang": round(window_settings["window_overhang"] * shrinkage_factor, 4),
            "window_inset": round((lid_settings["lid_gap"] + box_settings["outer_wall"] +
                             window_settings["window_overhang"]) * shrinkage_factor, 4),
            "window_inner_wall": round((box_settings["inner_wall"] + (window_settings["window_separator"] * 2)) * shrinkage_factor, 4),
            "outer_window_width": round(((box_settings["item_width"] + (box_settings["item_gap"] * 2)) -
                                   window_settings["window_overhang"] - window_settings["window_separator"]) * shrinkage_factor, 4),
            "inner_window_width": round(((box_settings["item_width"] + (box_settings["item_gap"] * 2)) -
                                   (window_settings["window_separator"] * 2)) * shrinkage_factor, 4),
            "window_total_height": round(((box_settings["item_height"] + (box_settings["item_gap"] * 2)) -
                                    (window_settings["window_overhang"] * 2)) * shrinkage_factor, 4),
        }

        if box_settings["item_count"] == 1:
            window_results["window_total_width"] = round(((box_settings["item_width"] + (box_settings["item_gap"] * 2)) -
                                                    (window_settings["window_overhang"] * 2)) * shrinkage_factor, 4)
        elif box_settings["item_count"] == 2:
            window_results["window_total_width"] = round(((window_results["outer_window_width"] * 2) +
                                                    window_results["window_inner_wall"]) * shrinkage_factor, 4)
        elif box_settings["item_count"] == 3:
            window_results["window_total_width"] = round(((window_results["outer_window_width"] * 2) +
                                                    window_results["inner_window_width"] +
                                                    (window_results["window_inner_wall"] * 2)) * shrinkage_factor, 4)
        elif box_settings["item_count"] > 3:
            window_results["window_total_width"] = round(((window_results["outer_window_width"] * 2) +
                                                    (window_results["inner_window_width"] *
                                                     (box_settings["item_count"] - 2)) +
                                                    (window_results["window_inner_wall"] *
                                                     (box_settings["item_count"] - 1))) * shrinkage_factor, 4)
        else:
            exception = Exception(f"Invalid Item Count, Please Enter a Valid Whole Number Greater Than 0.")
            raise exception

        return window_results
    except Exception as e:
        print(f"An Error Occurred While Calculating Window Settings: {e}")
        print(f"Error Type: {type(e)}")
        print(f"Traceback: {traceback.format_exc()}")
