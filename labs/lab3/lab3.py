"""
Name: <your name goes here – first and last>
<ProgramName>.py

lab3.py

Aidan Riordan
"""

def average():
    sum = 0
    denominator = eval(input("how many grades would you like to input?"))
    for i in range (0,denominator):
        print("Enter your grade on HW", i+1)
        grade = eval(input(""))


        sum = sum + grade
    avg = sum/denominator
    print("your average grade is", avg)


# hw = i +1
# print ()
#acc = acc/2 or acc = 0 acc = acc + grade/2
#Enter the grade for HW" + str(i+1)



# tip for loop 5
#accumulator

def tip_jar():
    total = 0
    for i in range(0,5,1):
        donation = eval(input("The jar was passed to you. How much are you donating"))
        total = total + donation
    print("The total is", total)

def newton():
    x = eval(input("What is the number x?"))
    times = eval(input("how many times to improve the aproximation?"))
    aprox = x/2
    for i in range (0,times):
        if times == 1:
            break
        aprox = (aprox + x/aprox)/2
    print("The approximation of the square root of", x, "=", aprox)

def sequence():
    num_terms = eval(input("How many terms are there in the series"))
    for i in range (0,num_terms):
        z = i +1
        num=1+(z//2*2)
        print(num)

def pi():
    n = eval(input("What is the number of terms in the series"))
    mult_num=1
    mult_den=1
    for i in range(1,n+1):

        num = 2 + ((i-1) // 2 * 2)
        mult_num = mult_num * num
        den = 1+(i//2*2)
        mult_den=mult_den*den
    approx = (mult_num/mult_den)*2
    print("The approximation of the value of pi with", n, "number of terms in the series is", approx)






pi()
sequence()
newton()
average()
tip_jar()
