weight = float(input("Enter your weight: "))
unit = input("Kilogram or Pounds? (K or L): ")
if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "L":
    weight = weight / 2.205
    unit = "kgs."
else:
    print(f"Your weight is: {round(weight, 1)} {unit}")
