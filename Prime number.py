'''
Problem: To determine prime numbers
Target User:Me
Interface: Command-line
Functional Requirements: Must print out the value
Must state whether its a prme or non-prime number
Must Exit automatically if number is not prime
testing:
'''
import math
PRIME=int(input('ENTER A NUMBER GREATER THAN 2:'))
PRIME2=math.sqrt(PRIME)
if PRIME%PRIME2!=0:
    print(PRIME,'is a prime number.')
else:
    exit(0)
