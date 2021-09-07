"""
	Prepared by: MOHD ZULFADZLI BIN AB JALIL
	Omnilytics - Programming Challenge (B)
	This program will read generated text file which contains random alphabetical strings,
	real numbers, integers and alphanumreic. Then, print the type of objects based on classification.
"""
import os
import time

def read_file():
    print("PLease wait...")
    file_check = os.path.exists("./omnilytics.txt")
    if file_check:
        start = time.time()
        f = open("omnilytics.txt", "r")
        data = f.read().split(',')

        for x in range(len(data)):
            d = data[x]
            if d.isalpha() and d.isalnum():
                print(d, "- alphabetical strings")

            elif not (d.isalpha()) and d.isalnum():
                if d.isnumeric():
                    print(d, "- integer")
                else:
                    print(d, "- alphanumeric")

            else:
                try:
                    int(d)
                    print(d, "- integer")
                except:
                    print(d, "- real numbers")
        print("Time taken to execute Challenge B:", time.time() - start, "s")
    else:
        print("File not exists, please run Challenge A script first.")


if __name__ == '__main__':
    read_file()
