def filter_selected_keys(data, selected_keys):
    filtered_data = []

    for obj in data:
        filtered_obj = {}
        for key in selected_keys:
            if key in obj:
                filtered_obj[key] = obj[key]
        filtered_data.append(filtered_obj)

    return filtered_data
