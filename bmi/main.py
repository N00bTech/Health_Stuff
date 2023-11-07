import bmi
import os

if __name__ == "__main__":
    os.system('cls')
    print("Welcome to BMI Adjuster.\n")

    weight = float(input("Enter your Weight in Kilograms: "))
    height = float(input("Enter your Height in Meters: "))

    print(f"Your BMI is {bmi.calculate_body_mass_index(weight, height)}. Your BMI is in {bmi.body_mass_index_category(bmi.calculate_body_mass_index(weight, height))} Range.\n")

    bmi_want_to = float(input("Enter your Desired BMI: "))
    bmi_weight, weight_needed = bmi.needed_weight(weight, height, bmi_want_to)

    if weight_needed > 0:
        print(f"Based from the BMI, {bmi_want_to}, you want, you need to gain {weight_needed} kgs for a total weight of {bmi_weight} kgs.\n")   
    elif weight_needed < 0:
        print(f"Based from the BMI, {bmi_want_to}, you want, you need to lose {weight_needed} kgs for a total weight of {bmi_weight} kgs.\n")   

    input("Press ENTER to exit.")
    os.system('cls')
    exit