def calculate_combinations(total, door, window):
    results = {}

    # Only doors
    doors = int(total // door)
    waste = round(total - doors * door, 2)
    results["doors_only"] = {"type": "Only Doors", "doors": doors, "windows": 0, "wastage": waste}

    # Only windows
    windows = int(total // window)
    waste = round(total - windows * window, 2)
    results["windows_only"] = {"type": "Only Windows", "doors": 0, "windows": windows, "wastage": waste}

    # Combo: both doors and windows (prefer more doors)
    best_doors = best_windows = 0
    best_waste = total

    for d in range(doors + 1):
        used_door = d * door
        remaining = total - used_door
        w = int(remaining // window)
        waste = round(remaining - w * window, 2)

        # Condition: both > 0, door > window, and less wastage
        if d > 0 and w > 0 and d > w and waste < best_waste:
            best_doors, best_windows, best_waste = d, w, waste

    if best_doors > 0 and best_windows > 0:
        results["combo"] = {
            "type": "Combo (More Doors)",
            "doors": best_doors,
            "windows": best_windows,
            "wastage": best_waste
        }
    else:
        results["combo"] = {
            "type": "Combo (Not Possible)",
            "doors": 0,
            "windows": 0,
            "wastage": total
        }

    return results
