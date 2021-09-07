'''	Prepared by: MOHD ZULFADZLI BIN AB JALIL
	Omnilytics - Programming Challenge (A)
	This program will generate a text file with 10 MB size (targerted file size)
	which contains random alphabetical strings, real numbers, integers and alphanumreic.
'''

import random
import sys
import string
import time

init_file_size = 0.1                                         # initialize 0.1 MB
multiplier = 10
targeted_file_size = 10                                      # 10 MB (edit here for file size)
bytes_conversion = 2 ** 20                                   # To Bytes (1MB = 2^20 B)
init_file_size = round(init_file_size * bytes_conversion)    # to find range of object represent 0.1 MB


class RandomGenerator:

    def gen_alphabetical_string():
        k = random.randint(1, 17)
        alpha = ''.join(random.choices(string.ascii_letters, k=k))
        return alpha

    def gen_real_number():
        re_num = random.uniform(0, 32767)                               # assuming positive value
        return re_num

    def gen_integers():
        int_num = random.randint(0, 32767)                              # assuming positive value
        return int_num

    def gen_alphanumerics():
        k = random.randint(1, 17)
        num = str(''.join(random.choices(string.digits, k=10)))
        alpnum = ''.join(random.choices(string.ascii_letters + num, k=k))
        return alpnum


def gen_random(file_size):
    data = []
    for x in range(file_size):
        data.append(random.choice((RandomGenerator.gen_alphabetical_string(), RandomGenerator.gen_real_number(),
                                   RandomGenerator.gen_integers(), RandomGenerator.gen_alphanumerics())))
    return data


def checking_size_two(checking, file_size):
    new_range = round((file_size ** 2) / checking)
    return new_range


def to_generate():
    print("Please Wait...")
    start = time.time()
    data = gen_random(init_file_size)
    checking = sys.getsizeof(",".join(str(d) for d in data))
    new_range = checking_size_two(checking, init_file_size) * targeted_file_size * multiplier
    data = gen_random(new_range)
    # print("Size of file:", sys.getsizeof(",".join(str(d) for d in data), "bytes")

    f = open("omnilytics.txt", "w", encoding='utf-8')
    f.write(",".join(str(d) for d in data))
    f.close()
    print("Time taken to execute Challenge A:", time.time() - start, "s")


if __name__ == '__main__':
    to_generate()
