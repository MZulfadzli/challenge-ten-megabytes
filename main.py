'''
	Prepared by: MOHD ZULFADZLI BIN AB JALIL
	Omnilytics - Programming Challenge
	This is main program to run Challenge A and Challenge B. Run this script and enter the input:
	1 - to run challenge A script
	2 - to run challenge B script
	3 - to exit
	Thank you for your time on reviewing my code. Looking forward to next step.
'''

import challengeA
import challengeB


def main():
    while True:
        val = int(input("Please enter '1' for Challenge A, '2' for Challenge B and '3' for exit: "))

        if val == 1:
            challengeA.to_generate()
        if val == 2:
            challengeB.read_file()
        if val != 1 and val != 2:
            print("Exit")
            return False


if __name__ == '__main__':
    main()
