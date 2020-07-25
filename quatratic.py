# This program is my first program on phython and I thought it should not
# be the hello world program. 
#I am going to take to simple quadratic equation and going to solve it 

#ax2 + bx + c = 0, where
#a, b and c are real numbers and
#a ≠ 0

import cmath
a=1
b=5
c=6

#calculate the descrimnant
d=(b**2)-(4*a*c)

#find solutions using quadaratic formula 
# 
print(cmath.sqrt(d)) 

sol1= (-b+cmath.sqrt(d))/(2*a)
sol2= (-b-cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))
