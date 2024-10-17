# this is a BMI calculator, health is gift, dont waste it.
weight = input("enter your weight(Kg):\n")
height = input("enter your height(Meters):\n")
# here i used "**", this exactly performs the power operation in mathematics.
BMI = float(weight) / float(height) ** 2
# also as you can see i changed the type of my inputs.
print(int(BMI))
