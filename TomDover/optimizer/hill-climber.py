import numpy as np
import matplotlib.pyplot as plt
import random as r
import math

def run():
    t = np.arange(0.0, 1.01, 0.01)
    s = np.sin(2*2*np.pi*t)*(np.exp(-5*t))
    plt.plot(t, s, 'r')

    movement = raw_input("Would you like to show movement?(Y/N)...")

    for x in range(input('How many agents would you like to deploy?...')):
        a = r.choice(t)
        b = np.sin(2*2*np.pi*a)*(np.exp(-5*a))
        x = np.sin(2*2*np.pi*(a - 0.01))*(np.exp(-5*(a-0.01)))
        y = np.sin(2*2*np.pi*(a + 0.01))*(np.exp(-5*(a+0.01)))
        while x>b or y>b:
            if x>b:
                a = a - 0.01
                b = np.sin(2*2*np.pi*a)*(np.exp(-5*a))
                x = np.sin(2*2*np.pi*(a - 0.01))*(np.exp(-5*(a-0.01)))
                y = np.sin(2*2*np.pi*(a + 0.01))*(np.exp(-5*(a+0.01)))
                if movement == 'Y':
                    plt.plot(a,b,'go')
                else:
                    pass
            elif y>b:
                a = a + 0.01
                b = np.sin(2*2*np.pi*a)*(np.exp(-5*a))
                x = np.sin(2*2*np.pi*(a - 0.01))*(np.exp(-5*(a-0.01)))
                y = np.sin(2*2*np.pi*(a + 0.01))*(np.exp(-5*(a+0.01)))
                if movement == 'Y':
                    plt.plot(a,b,'ro')
                else:
                    pass
        plt.plot(a,b,'bo')

    plt.grid(True)
    plt.show()

    again = raw_input("Do it again?(Y/N)...")
    if again == 'Y':
        run()
    else:
        print "Okay..."
     
run()                      

