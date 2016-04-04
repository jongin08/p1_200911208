marksTmp = raw_input('Enter your marks (0~100): ')
marks = float(marksTmp)
def Grade(marks):
    if marks>=90 and marks<=100:
        grade='A'
        
    elif marks>=80 and marks<90:
        grade='B'
        
    elif marks>=70 and marks<80:
        grade='C'
        
    elif marks>=60 and marks<70:
        grade='D'
        
    else:
        grade='F'
        
    return grade

grade=Grade(marks)
print "Your mark is '{0:.1f}' and your grade is '{1:2s}'".format(marks,grade)
