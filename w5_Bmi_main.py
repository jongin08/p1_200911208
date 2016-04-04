weight = float(input('Enter weight in kg: '))
height = float(input('Enter height in m: '))
def Bmi():
    if weight <= 0 or weight > 300:
        print 'Weight cannot be less than 0 or greater than 300'

    elif height <= 0:
        print 'Height cannot be less than 0'
    else:
        bmi = (weight / (height * height))
        print 'Your BMI is %.2f' % bmi
        if bmi <= 18.5:
            print 'Your weight status is Underweight'
        elif bmi >= 18.5 and bmi < 25:
              print 'Your weight status is Normal weight'
        elif bmi >= 25 and bmi < 30:
              print 'Your weight status is Overweight'
        elif bmi >= 30:
              print 'Your weight status is Obese'

Bmi()
