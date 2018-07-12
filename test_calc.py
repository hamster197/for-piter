import calc
import numpy as np

for i in np.arange(-10, 10, 0.5):
    if (calc.is_even(i) == 1) or (calc.is_even(i) == 0):
        print("Test  is OK " +'rez is_even='+ str(calc.is_even(i))+' numb=' + str(i))
    else:
        print("Test  is Fail " +'rez is_even='+ str(calc.is_even(i))+' numb='+ str((i)))




