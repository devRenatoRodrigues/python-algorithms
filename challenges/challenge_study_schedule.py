def study_schedule(permanence_period, target_time):
    if target_time is None or target_time <= 0:
        return None

    total_time_hours = {}

    for login, logout in permanence_period:
        is_string = isinstance(login, str) or isinstance(logout, str)
        is_none = login is None or logout is None
        if is_none or is_string:
            return None
        for hour in range(login, logout + 1):
            total_time_hours[hour] = total_time_hours.get(hour, 0) + 1

    new_target_time = target_time - 1
    study_schedule(permanence_period, new_target_time)
    return total_time_hours.get(target_time, 0)
