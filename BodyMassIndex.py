def calculateBMI(height, weight):
    print("height = " + str(height))
    print("weight = " + str(weight))
    bmi = weight/(height**2)
    if bmi<18.5:
        print("Your bmi is " + str(bmi) + "and you are under weight")
        return -1
    elif 18.5 <=bmi<= 25.0:
        print("Your bmi is " + str(bmi) + "and you are normal weight")
        return 0
    elif bmi > 25.0:
        print("Your bmi is " + str(bmi) + "and you are over weight")
        return 1


calculateBMI(height=1.73, weight=60)
