import re


def replace_comma_with_dot(text):
    # Replace commas between digits with a dot
    return re.sub(r'(?<=\d),(?=\d)', '.', text)


def check_if_only_zero(text):
    get_string = str(text)
    characters = " ".join(get_string).split()

    check = all(char in ("0", ".") for char in characters)
    # print(check)

    return check


def rounding_fractional_part(frac_part):
    if len(frac_part) == 0 or len(frac_part) == 1 or len(frac_part) == 2:
        return frac_part
    else:
        # check third decimal place for rounding the second one
        if int(frac_part[2]) >= 5:
            rounded_frac_part = int(frac_part[1])
            rounded_frac_part = rounded_frac_part + 1

            frac_part_new = frac_part[0] + str(rounded_frac_part)
            return frac_part_new
        else:
            frac_part_new = frac_part[0] + frac_part[1]
            return frac_part_new


def custom_round(value):
    # Convert the value to a string to analyze its structure
    str_value = str(value)

    # Split the value into whole and fractional parts
    if '.' in str_value:
        whole_part, frac_part = str_value.split('.')
    else:
        whole_part, frac_part = str_value, ''

    # Rule 1: If there are 3 or more chars before the ".", return only the whole part
    if len(whole_part) >= 3:
        return whole_part

    # Rule 2: If the float starts with 0. and only Zeros are following, always format as 0.00
    if whole_part.startswith('0') and len(frac_part) == 1 and frac_part[0] == 0:
        return f"{whole_part}.00"

    elif whole_part.startswith('0') and len(frac_part) == 2 and frac_part[0] == 0 and frac_part[1] == 0:
        return f"{whole_part}.00"

    # Rule 3: Otherwise, format according to the number of characters before the dot
    if len(whole_part) == 1:
        # Round to 2 decimal places
        if len(frac_part) >= 2:
            # Check the third character for rounding
            if int(frac_part[2]) >= 5:
                rounded_frac = str(int(frac_part[1]) + 1)
            else:
                rounded_frac = frac_part[1]
            return f"{whole_part}.{rounded_frac}"  # {'0' if len(frac_part) < 2 else ''}
        elif len(frac_part) == 2:
            rounded_frac = frac_part
            return f"{whole_part}.{rounded_frac}"
        elif len(frac_part) == 1:
            rounded_frac = frac_part[0]
            return f"{whole_part}.{rounded_frac}0"
        else:
            return f"{whole_part}.00"

    elif len(whole_part) == 2:
        # Round to 1 decimal place
        if len(frac_part) > 0:
            if int(frac_part[0]) >= 5:
                rounded_whole = str(int(whole_part) + 1)
                return f"{rounded_whole}.0"
            else:
                return f"{whole_part}.{frac_part[0]}"
        else:
            return f"{whole_part}.0"

    return str(value)


print(custom_round(0.0004))
print(custom_round(0.12))
print(custom_round(0.123))
print(custom_round(0.125))
print("_________")
print(custom_round(2.234))
print(custom_round(2.235))
print(custom_round(10.26))
print(custom_round(10.246))

