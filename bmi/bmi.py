def calculate_body_mass_index(weight, height):
    """
    height -> height in meters.
    kilograms -> weight in kilograms.
    """
    bmi = round((weight/height**2), 2)

    return bmi

def body_mass_index_category(bmi):
    """
    bmi -> Body Mass Index Value.
    """
    if (bmi <= 18.4):
        return "Underweight"
    elif (bmi >= 18.5 and bmi <= 24.9):
        return "Normal"
    elif (bmi >= 25.0 and bmi <= 39.9):
        return "Overweight"
    elif (bmi >= 40.0):
        return "Obese"
        
def needed_weight(weight, height, bmi_want_to):
    """
    height -> height in meters.
    kilograms -> weight in kilograms.
    bmi_want_to -> Body Mass Index You Want to Be.
    """
    bmi = calculate_body_mass_index(weight, height)

    bmi_weight = round((bmi_want_to * height**2), 2)
    weight_needed = round((bmi_weight - weight), 2)

    return [bmi_weight, weight_needed]
