


def PossionCheck(marks):
    
    Amarks = 75
    Bmarks = 65
    Cmarks = 55
    Smarks = 35

    if marks >=  Amarks:
        possition = 'A'
    elif marks >= Bmarks:
        possition = 'B'
    elif marks >= Cmarks:
        possition = 'C'
    elif marks >= Smarks:
        possition = 'S'
    else:
        possition = 'F'
    
    return possition



marks = [11,22,33,44,55,66,77,88,99]
total = 0
for i in range(0,9):
    total = total + marks[i]

avg = total/9
print(avg)