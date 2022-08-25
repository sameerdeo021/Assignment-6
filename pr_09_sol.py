year=int(input('Enter the year you want to check '))

if (year%4==0 and year%100!=0) or (year%400==0):
  
    print(" The year is a yeap year ")
else:
    print("year is not a yeap year ")
    