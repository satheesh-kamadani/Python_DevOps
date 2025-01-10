# BMI Calculator

weight = float(input("Enter the body weight in kilograms: "))
height = float(input("Enter the height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Your BMI is {:.2f}. You are underweight.".format(bmi))
elif 18.5 <= bmi < 24.9:
    print("Your BMI is {:.2f}. You have a normal weight.".format(bmi))
elif 25 <= bmi < 29.9:
    print("Your BMI is {:.2f}. You are overweight.".format(bmi))
else:
    print("Your BMI is {:.2f}. You are obese.".format(bmi))