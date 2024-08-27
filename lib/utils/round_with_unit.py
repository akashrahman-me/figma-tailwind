import re

def round_with_unit(value):
    if value is None:
        return None

    ignored = ["normal", "inherit", "none"]
    if value in ignored:
        return value

    # Regular expression to separate the number from the unit
    regex = r"^(\d*\.?\d+)([a-z%]*)$"

    # Execute the regular expression
    match = re.match(regex, value)

    if not match:
        raise ValueError(f"Could not parse value: {value}")

    # Extract the number and unit
    number = match.group(1)
    unit = match.group(2)

    # Round the number
    rounded_number = round(float(number))

    # Return the rounded number with the unit
    return f"{rounded_number}{unit}"
