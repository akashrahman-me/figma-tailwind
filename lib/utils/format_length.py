import re

def format_length(length_string, max_length = 2):
    if length_string is None:
        return None
    
    ignored = ["normal", "inherit", "none"]
    if length_string in ignored:
        return length_string

    # Parse the length value from the input string
    match = re.match(r'(-?\d+(\.\d+)?)([a-zA-Z]*)', f"{length_string}")
    if match:
        length_value, _, units = match.groups()
        length_value = float(length_value)

        # Check if the length value has decimal places
        has_decimal_places = length_value % 1 != 0

        # Format the length value without decimal places if necessary
        formatted_length = '{:.{}f}'.format(length_value, max_length).rstrip('0').rstrip(
            '.') if has_decimal_places else str(int(length_value))

        # Return the formatted length value with the original units
        return formatted_length + units
    else:
        return length_string
