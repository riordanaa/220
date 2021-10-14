'''
Name: <Aidan Riordan>
program name: <mean.py>

I Aidan Riordan certify that this is my own work

What will the program do? calculate the geometric mean,
rms mean, and harmonic mean with given input
What will be the inputs and outputs?
The inputs will be number of terms an each terms value.
The outputs will be the three different types of means listed above.
What is a step-by-step list of what the program must do, aka an algorithm?
 (Remember this is in English!)
ask for input and store terms as list and the number of terms as a variable
calculate the three different types of means with given data
output the three different types of means
Implement your code.
Test your program.
Maintain.
'''

import math
def main():
    #get input and make list of terms
    num_terms = int(input("how many terms are there?"))
    terms =[]
    for _ in range(num_terms):
        temp = float(input("enter value"))
        terms.append(temp)
    #get rms avg
    acc = 0
    for term in terms:
        temp = term**2
        acc = acc + temp
    rms_avg = math.sqrt(acc/num_terms)
    print(round(rms_avg,3))
    # calculate harmonic mean
    acc = 0
    for term in terms:
        temp = 1/term
        acc = acc + temp
    harmonic_mean = num_terms/acc
    print(round(harmonic_mean,3))
    # calculate geometric mean
    acc = 1
    for term in terms:
        temp = term
        acc = acc * term
    geometric_mean = acc**(1/num_terms)
    print(round(geometric_mean, 3))

if __name__ == '__main__':
    main()
