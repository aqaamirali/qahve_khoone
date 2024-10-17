# here, we are going to get familiar with conditional statements such as if, elif, and else.
# also get familiar with round() function.

print("welcome to BMI calculator!")
height = float(input("height(Meters):"))
weight = int(input("weight(Kg):"))
BMI = round(weight / height ** 2)
if BMI < 18.5:
    print("UnderWeight")
elif BMI < 25:
    print("NormalWeight")
elif BMI < 30:
    print("OverWight")
elif BMI < 35:
    print("Obese")
else:
    print("Clinically Obese")

