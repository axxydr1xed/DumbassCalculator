import random
import time

numA = input("Input a number. ")
numB = input("Input a second number. ")
print("Calculating... Please wait 3 seconds.")
time.sleep(3)
print(random.randint(0, 100))
print("Press the X button or the red circle in the corner of this window to close. Otherwise, I will close by myself in 10 seconds.")
time.sleep(10)
exit