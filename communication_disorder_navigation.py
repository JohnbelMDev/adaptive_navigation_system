function navigate_to_park(S, D, A, F):
    current_location = S
    landmarks = get_landmarks_between(S, D, A)
    route_plan = create_route_plan(S, D, landmarks)

    for step in route_plan:
        if validate_step(step, current_location, F):
            move_to_next_step(step)
        else:
            current_location = handle_error(current_location, A, F)
            if current_location == "unknown":
                return "Unable to complete route. Seek assistance."

    if validate_arrival(current_location, D):
        return "Successfully reached the park!"
    else:
        return "Error in final step. Confirm location and retry."
