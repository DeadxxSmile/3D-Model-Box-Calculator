import traceback

def calc_box(box_settings):
    try: 
        item_height, item_width, item_depth, item_slop, item_count, outer_wall, inner_wall = box_settings
        box_width = ((item_width + (item_slop * 2)) * item_count) + (outer_wall * 2) + ((item_count - 1) * inner_wall)
        box_height = (item_height + (item_slop * 2)) + (outer_wall * 2)
        box_depth = (item_depth + (item_slop * 2)) + outer_wall
        box_results = (box_width, box_height, box_depth, outer_wall, inner_wall)
        return box_results
    except Exception as e:
        print(f"An Error Occured While Calculating Box Settings: {e}")
        print(f"Error Type: {type(e)}")
        print(f"Traceback: {traceback.format_exc()}")

def calc_lid(box_results, lid_settings):
    try:
        box_width, box_height, box_depth, outer_wall, inner_wall = box_results
        lid_depth, lid_wall, lid_separation, lid_gap = lid_settings
        box_lid_match_depth = box_depth - lid_depth - lid_separation
        lid_width = box_width + (lid_wall * 2) + (lid_gap * 2)
        lid_height = box_height + (lid_wall * 2) + (lid_gap * 2)
        lid_results = (box_lid_match_depth, lid_width, lid_height, lid_depth, lid_wall)
        return lid_results
    except Exception as e:
        print(f"An Error Occured While Calculating Lid Settings: {e}")
        print(f"Error Type: {type(e)}")
        print(f"Traceback: {traceback.format_exc()}")

def calc_window(box_settings, lid_settings, lid_results, window_settings):
    try:
        item_height, item_width, item_depth, item_slop, item_count, outer_wall, inner_wall = box_settings
        lid_depth, lid_wall, lid_separation, lid_gap = lid_settings
        box_lid_match_depth, lid_width, lid_height, lid_depth, lid_wall = lid_results
        window_overhang, separator_overhang = window_settings
        
        window_inset = lid_wall + lid_gap + outer_wall + window_overhang + item_slop
        window_corner_measure = lid_gap + outer_wall + window_overhang
        window_inner_wall = inner_wall + (separator_overhang * 2)
        window_total_height = lid_height - (lid_wall * 2) - (lid_gap * 2) - (outer_wall * 2) - (window_overhang * 2)
        outer_window_width = (item_width + (item_slop * 2)) - window_overhang - separator_overhang
        inner_window_width = (item_width + (item_slop * 2)) - (separator_overhang * 2)
        
        if item_count == 1:
            window_total_width = (item_width + (item_slop * 2)) - (window_overhang * 2)
        elif item_count == 2:
            window_total_width = (outer_window_width * 2) + window_inner_wall
        elif item_count == 3:
            window_total_width = (outer_window_width * 2) + inner_window_width + (window_inner_wall * 2)
        elif item_count > 3:
            window_total_width = (outer_window_width * 2) + (inner_window_width * (item_count - 2))+ (window_inner_wall * (item_count - 1))
            window_width_test = window_total_width + (window_overhang * 2) + (lid_gap * 2) + (lid_wall * 2)
            if window_width_test == lid_width:
                print("Window Width Test Passed.")
            else:
                print(f"Window Width Test Failed: {window_width_test} != {lid_width}")
                print(f"Window Total Width: {window_total_width}")
        else:
            exception = Exception(f"Invalid Item Count, Please Enter a Valid Whole Number Greater Than 0.")
            raise exception
        
        window_results = (window_corner_measure, window_inner_wall, window_total_width, window_total_height, outer_window_width, inner_window_width)
        return window_results
    except Exception as e:
        print(f"An Error Occured While Calculating Window Settings: {e}")
        print(f"Error Type: {type(e)}")
        print(f"Traceback: {traceback.format_exc()}")