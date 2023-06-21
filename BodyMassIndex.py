def calculateBMI(height, weight):
    print("height = " + str(height))
    print("weight = " + str(weight))
    bmi = weight/(height**2)
    if bmi<18.5:
        print("Your bmi is " + str(bmi) + "and you are under weight")
    elif 18.5 <=bmi<= 25.0:
        print("Your bmi is " + str(bmi) + "and you are normal weight")
    elif bmi > 25.0:
        print("Your bmi is " + str(bmi) + "and you are over weight")
    print("Your bmi is " + str(bmi))

calculateBMI(height=1.73, weight=60)
