#Use a for statement to print 10 random numbers.-------------------------------------------------------------------------------
import random

for i in range(10):
    num = random.randrange(1,11)
    print(num)

#Repeat the above exercise but this time print 10 random numbers between 25 and 35, inclusive.--------------------------------
import random

for i in range(10):
    num = random.randrange(25,36)
    print(num)

#Write a program to calculate the hypotenuse of a right triangle.--------------------------------------------------------------
import math

x = 5
y = 2

hyp = math.hypot(x,y)
print(hyp)

#Way to calculate an approximation for pi.-----------------------------------------------------------------------------------
import math

def leibniz_pi(n_terms):
    num = 0
    for i in range(n_terms):
        num += (-1)**i / (2*i + 1)
    return 4 * num

n_terms = 1000000
approx_pi = leibniz_pi(n_terms)
print("Approximation of pi with Leibniz formula using", n_terms, "terms:", approx_pi)
print("math.pi:", math.pi)
