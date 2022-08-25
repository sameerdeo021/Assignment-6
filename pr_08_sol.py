# ax2+bx+c=0 is a quadratic equation of two roots 
a=int(input("Enter positive no only "))
b=int(input('Enter any no '))
c=int(input('Enter any no '))

D=b**2-4*a*c
if D>0:
    print('Quadratic Equation has two real and distinct roots ')
elif D==0:
    print('Quadratic Equation has two real and equal roots')
else:
    print('Quadratic Equation has two emaginary roots')

