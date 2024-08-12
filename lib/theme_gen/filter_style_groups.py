def filter_style_groups(styles_str, required_properties):
    # Split the styles string into groups
    groups = styles_str.split("\n\n")

    # Filter the groups
    filtered_groups = [group for group in groups
                       if all(prop in group for prop in required_properties)]

    # Join the filtered groups back into a string
    return '\n\n'.join(filtered_groups)
