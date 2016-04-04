sel1 = raw_input('Enter your score : ')
marks = float(sel1)
def cGrade(marks):
    if marks>=90 and marks<=100:
        grade='A'
    elif marks>=80 and marks<90:
        grade='B'
    elif marks>=70 and marks<80:
        grade='C'
    elif marks>=60 and marks<70:
        grade='D'
    elif marks<60 :
        grade='F'
    else:
        grade='Wrong'

    return grade

grade=cGrade(marks)
print "Your score is '{0:.1f}', so your grade is '{1:2s}'".format(marks,grade)
