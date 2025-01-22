#2Write function bmi that calculates body mass index (bmi = weight / height2).

#if bmi <= 18.5 return "Underweight"

#if bmi <= 25.0 return "Normal"

#if bmi <= 30.0 return "Overweight"

#if bmi > 30 return "Obese"(https://www.codewars.com/kata/57a429e253ba3381850000fb/train/python)

def bmi(weight, height):
    bmi_value = weight / (height ** 2)
    if bmi_value <= 18.5:
        return "Underweight"
    if bmi_value <= 25.0:
        return "Normal"
    if bmi_value <= 30.0:
        return "Overweight"
    else:
        return "Obese"
    