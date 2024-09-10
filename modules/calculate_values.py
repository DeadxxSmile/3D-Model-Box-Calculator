import traceback

def calc_box(box_values):
    try:
        box_results = {
            "item_space_width": (box_values["item_width"] + (box_values["item_gap"] * 2)),
            "box_height": ((box_values["item_height"] + (box_values["item_gap"] * 2)) +
                           (box_values["outer_wall"] * 2)),
            "box_width": ((box_values["item_width"] + (box_values["item_gap"] * 2)) * box_values["item_count"] +
                          (box_values["outer_wall"] * 2) +
                          ((box_values["item_count"] - 1) * box_values["inner_wall"])),
            "box_depth": ((box_values["item_depth"] + box_values["item_gap"]) +
                          box_values["outer_wall"]),
            "box_inner_width": ((box_values["item_width"] + (box_values["item_gap"] * 2)) * box_values["item_count"] +
                                ((box_values["item_count"] - 1) * box_values["inner_wall"])),
            "box_inner_height": (box_values["item_height"] + (box_values["item_gap"] * 2)),
            "box_inner_depth": (box_values["item_depth"] + box_values["item_gap"]),
            "outer_wall": box_values["outer_wall"],
            "inner_wall": box_values["inner_wall"],
            "item_gap": box_values["item_gap"]
        }
        return box_results
    except Exception as e:
        print(f"An Error Occurred While Calculating Box Settings: {e}")
        print(f"Error Type: {type(e)}")
        print(f"Traceback: {traceback.format_exc()}")

def calc_lid(box_results, lid_settings):
    try:
        lid_results = {
            "box_outer_depth": box_results["box_depth"] - lid_settings["lid_depth"] - lid_settings["lid_separation"],
            "box_remaining_depth": box_results["box_depth"] - lid_settings["lid_depth"],
            "box_outer_width": lid_settings["lid_wall"] + lid_settings["lid_gap"],
            "lid_height": box_results["box_height"] + (lid_settings["lid_wall"] * 2) + (lid_settings["lid_gap"] * 2),
            "lid_width": box_results["box_width"] + (lid_settings["lid_wall"] * 2) + (lid_settings["lid_gap"] * 2),
            "lid_depth": lid_settings["lid_depth"],
            "lid_wall": lid_settings["lid_wall"],
            "lid_inner_height": (box_results["box_height"] + (lid_settings["lid_gap"] * 2)),
            "lid_inner_width": (box_results["box_width"] + (lid_settings["lid_gap"] * 2)),
            "lid_gap": lid_settings["lid_gap"]
        }

        return lid_results
    except Exception as e:
        print(f"An Error Occurred While Calculating Lid Settings: {e}")
        print(f"Error Type: {type(e)}")
        print(f"Traceback: {traceback.format_exc()}")

def calc_window(box_settings, lid_settings, window_settings):
    try:
        window_results = {
            "window_overhang": window_settings["window_overhang"],
            "window_inset": (lid_settings["lid_gap"] + box_settings["outer_wall"] +
                             window_settings["window_overhang"]),
            "window_inner_wall": (box_settings["inner_wall"] + (window_settings["window_separator"] * 2)),
            "outer_window_width": ((box_settings["item_width"] + (box_settings["item_gap"] * 2)) -
                                   window_settings["window_overhang"] - window_settings["window_separator"]),
            "inner_window_width": ((box_settings["item_width"] + (box_settings["item_gap"] * 2)) -
                                   (window_settings["window_separator"] * 2)),
            "window_total_height": ((box_settings["item_height"] + (box_settings["item_gap"] * 2)) -
                                    (window_settings["window_overhang"] * 2)),
        }

        if box_settings["item_count"] == 1:
            window_results["window_total_width"] = ((box_settings["item_width"] + (box_settings["item_gap"] * 2)) -
                                                    (window_settings["window_overhang"] * 2))
        elif box_settings["item_count"] == 2:
            window_results["window_total_width"] = ((window_results["outer_window_width"] * 2) +
                                                    window_results["window_inner_wall"])
        elif box_settings["item_count"] == 3:
            window_results["window_total_width"] = ((window_results["outer_window_width"] * 2) +
                                                    window_results["inner_window_width"] +
                                                    (window_results["window_inner_wall"] * 2))
        elif box_settings["item_count"] > 3:
            window_results["window_total_width"] = ((window_results["outer_window_width"] * 2) +
                                                    (window_results["inner_window_width"] *
                                                     (box_settings["item_count"] - 2)) +
                                                    (window_results["window_inner_wall"] *
                                                     (box_settings["item_count"] - 1)))
        else:
            exception = Exception(f"Invalid Item Count, Please Enter a Valid Whole Number Greater Than 0.")
            raise exception

        return window_results
    except Exception as e:
        print(f"An Error Occurred While Calculating Window Settings: {e}")
        print(f"Error Type: {type(e)}")
        print(f"Traceback: {traceback.format_exc()}")
