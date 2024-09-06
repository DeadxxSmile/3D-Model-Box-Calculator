import traceback

def output_results(box_results, lid_results=None, window_results=None):
    try:
        if lid_results is not None and window_results is not None:
            box_width, box_height, box_depth, box_outer_wall, box_inner_wall = box_results
            box_lid_match_depth, lid_width, lid_height, lid_depth, lid_wall = lid_results
            window_corner_measure, window_inner_wall, window_total_width, window_total_height, outer_window_width, inner_window_width = window_results
            print(f"""
                Box Width: {round(box_width, 2)}
                Box Height: {round(box_height, 2)}
                Box Depth: {round(box_depth, 2)}
                Box Outer Wall: {round(box_outer_wall, 2)}
                Box Inner Wall: {round(box_inner_wall, 2)}
                Box Lid Match Depth: {round(box_lid_match_depth, 2)}
                Lid Width: {round(lid_width, 2)}
                Lid Height: {round(lid_height, 2)}
                Lid Depth: {round(lid_depth, 2)}
                Lid Wall: {round(lid_wall, 2)}
                Window Dist. From Corner: {round(window_corner_measure, 2)}
                Window Inner Wall: {round(window_inner_wall, 2)}
                Window Total Width: {round(window_total_width, 2)}
                Window Total Height: {round(window_total_height, 2)}
                Outer Window Width: {round(outer_window_width, 2)}
                Inner Window Width: {round(inner_window_width, 2)}
            """)
        elif lid_results is not None and window_results is None:
            box_width, box_height, box_depth, box_outer_wall, box_inner_wall = box_results
            lid_width, lid_height, lid_depth = lid_results
            print(f"""
                Box Width: {round(box_width, 2)}
                Box Height: {round(box_height, 2)}
                Box Depth: {round(box_depth, 2)}
                Box Outer Wall: {round(box_outer_wall, 2)}
                Box Inner Wall: {round(box_inner_wall, 2)}
                Lid Width: {round(lid_width, 2)}
                Lid Height: {round(lid_height, 2)}
                Lid Depth: {round(lid_depth, 2)}
            """)
        elif lid_results is None and window_results is None:
            box_width, box_height, box_depth, box_outer_wall, box_inner_wall = box_results
            print(f"""
                Box Width: {round(box_width, 2)}
                Box Height: {round(box_height, 2)}
                Box Depth: {round(box_depth, 2)}
                Box Outer Wall: {round(box_outer_wall, 2)}
                Box Inner Wall: {round(box_inner_wall, 2)}
            """)
        else:
            exception = Exception(f"Invalid Results, Please Check Your Inputs.")
            raise exception
    except Exception as e:
        print(f"An Error Occured While Outputting Results: {e}")
        print(f"Error Type: {type(e)}")
        print(f"Traceback: {traceback.format_exc()}")