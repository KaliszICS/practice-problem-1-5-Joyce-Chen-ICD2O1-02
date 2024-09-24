'''
    Lesson: Typecasting
    Author: Joyce Chen
    Date Creatd: Sept 23, 2024
    Date Last Modified: Sept 23, 2024
'''

def q1():
  num = input("Input an integer: ")
  num = int(num) + 3
  print(num)

def q2():
  num2 = str(input("Input a number: "))
  num2 = float(num2 + "4") + 2
  print(num2)

def q3():
  rad = input("Input a radius: ")
  rad = float(rad)
  print(3.14*rad*rad)

def q4():
  num3 = input("Input a number: ")
  num3 = int(float(num3)*12)
  print(num3)

def q5():
  num4 = input("Input an integer: ")
  num4 = str(int(num4) + 5)
  print(f"Your number + 5 is {num4}")

#Comment this code out when running tests
#Do not comment this out when running your program normally

# q1()
# q2()
# q3()
# q4()
# q5()
