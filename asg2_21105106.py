# ASSIGNMENT 2                                   -BY HIMANSHU(21105106), ECE
# PLEASE REMOVE (""") SIGNS TO ACCESS A PARTICULAR CODE
# QUESTION 1
"""
# ALL PARTS ARE  DONE IN A SINGLE CODE
GIVEN_INPUT_STRING = 'Python is a case sensitive language'
print("THE GIVEN STRING IS: 'Python is a case sensitive language'")
# PART (a)
print("(a)- THE LENGTH OF THE STRING IS",len(GIVEN_INPUT_STRING))
# PART (b)
print("(b)- STRING AFTER REVERSING ITS ORDER IS-:",GIVEN_INPUT_STRING[ : :-1])
# PART (c)
NEW_STRING = GIVEN_INPUT_STRING[12:26]
print("(c)- A NEW STRING CONTAINING A PART OF GIVEN STRING AS:-", NEW_STRING)
# PART (d)
print("(d)- FOLLOWING GIVEN INSTRUCTIONS NEW STRING WILL BE:- ",GIVEN_INPUT_STRING.replace('a case sensitive','object oriented'))
# PART (e)
print("(e)- THE INDEX OF SUBSTRING 'a' IS",GIVEN_INPUT_STRING.index('a'))
# PART (f)
print("(f)- REMOVING BLANK SPACES FROM STRING :-",GIVEN_INPUT_STRING.replace(' ',''))
# OVER
"""
# OUESTION 2
"""
NAME = str(input('PLEASE ENTER YOUR NAME:\n'))
S_ID = int(input('PLEASE ENTER YOUR SID:\n'))
DEPARTMENT = str(input('PLEASE WRITE YOUR RESPECTIVE DEPARTMENT:\n'))
CGPA = float(input('ENTER YOUR CGPA:\n'))
name_ ='Hey,%s Here!'%(NAME)
s_id_ ='My SID is %d'%(S_ID)
department_cgpa ='I am from %s department and my CGPA is %f'%(DEPARTMENT,CGPA)
print("THE OUTPUT IS:")
print(name_)
print(s_id_)
print(department_cgpa)
# OVER 
"""
# QUESTION 3
"""
a=56 # (111000 IN BINARY)
b=10 # (1010 IN BINARY)
print("(a):- RESULT AFTER USING (&) B/W a AND b is:",a&b)      # PART (a)
print("(b):- RESULT AFTER USING (|) B/W a AND b is:",a|b)      # PART (b)
print("(c):- RESULT AFTER USING (^) B/W a AND b is:",a^b)      # PART (c)
print("(d):- LEFT SHIFTING BOTH a AND b BY 2 bit will be:",'a-',a<<2,'b-',b<<2)      # PART(d)
print("(e):- RIGHT SHIFTING a WITH 2 bits AND b WITH b WITH 4 bits will be:",'a-',a>>2,'b-',b>>4)      # PART(e)
# OVER
"""
# QUESTION 4
"""
NUM_1=int(input('ENTER NUMBER 1:'))
NUM_2=int(input('ENTER NUMBER 2:'))
NUM_3=int(input('ENTER NUMBER 3:'))
if NUM_1>=NUM_2 and NUM_1>=NUM_3 :
    print(" MAXIMUM OF THREE NUMBERS ENTERED BY YOU IS:\n",NUM_1)
elif NUM_2>=NUM_1 and NUM_2>=NUM_3 :
    print(" MAXIMUM OF THREE NUMBERS ENTERED BY YOU IS:\n",NUM_2)
elif NUM_3>=NUM_2 and NUM_3>=NUM_1:
    print(" MAXIMUM OF THREE NUMBERS ENTERED BY YOU IS:\n",NUM_3)
# OVER
"""
# QUESTION 5
"""
print("IF 'name' IS PRESENT IN YOUR STRING OUTPUT WILL BE YES OTHERWISE NO.")
print("PLSS WRITE IN SMALL LETTERS")
your_line = input('KINDLY WRITE THE LINE IN WHICH PRESENCE OF "name" TO BE FOUND\n')
if 'name' in your_line :
    print("YESS, ITS PRESENT")
else:
    print("NOO, ITS NOT PRESENT")
# OVER
"""
# QUESTION 6
"""
print("BY YOUR THREE NUMBERS IF TRIANGLE COULD BE FORMED THEN OUTPUT WILL BE YESS ELSE NO.")
NUMBER_1 = int(input('ENTER FIRST INTEGER \n'))
NUMBER_2 = int(input('ENTER SECOND INTEGER \n'))
NUMBER_3 = int(input('ENTER THIRD INTEGER \n'))
if NUMBER_1 > NUMBER_2+NUMBER_3 :
    print("NO, TRIANGLE CAN'T BE FORMED")
elif NUMBER_2 > NUMBER_1+NUMBER_3 :
    print("NO, TRIANGLE CAN'T BE FORMED")
elif NUMBER_3 > NUMBER_1+NUMBER_2 :
    print("NO, TRIANGLE CAN'T BE FORMED")
else:
    print("YES, TRIANGLE COULD BE FORMED")
# OVER
"""

# ASSIGNMENT 2 COMPLETED                          -BY HIMANSHU(21105106),ECE