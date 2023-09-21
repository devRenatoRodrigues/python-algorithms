def study_schedule(permanence_period, target_time):
    if target_time is None or target_time <= 0:
        return None

    total_online = 0

    for login, logout in permanence_period:
        is_string = isinstance(login, str) or isinstance(logout, str)
        is_none = login is None or logout is None
        if is_none or is_string:
            return None
        if login <= target_time <= logout:
            total_online += 1
    return total_online
