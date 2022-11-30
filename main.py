import os
from multiprocessing import Process
import time
#EMİRCAN FURKAN BAYENDUR
class FindTriplets:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def find_pythogorean_triplets(self, lower_index,  upper_limit):
        while self.c < upper_limit:
            for i in range(0+lower_index,upper_limit+10, os.cpu_count()):
                for k in range(1, i):
                    self.c = i * i + k * k
                    self.a = i * i - k * k
                    self.b = 2 * i * k
                    if self.c > upper_limit:
                        break
                    print(self.a, self.b, self.c)
            if i == lower_index+os.cpu_count()-1:
                break


if __name__ == "__main__":
    t1 = time.time()
    upper_limit = 200
    for number_of_p in range(1, os.cpu_count()+1):
        find_triplets = []
        processes = []

    for i in range(number_of_p):
        find_triplets.append(FindTriplets())
        processes.append(Process(target=find_triplets[i].find_pythogorean_triplets, args=(i,upper_limit)))

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    t2 = time.time()
    print(f"{t2-t1} seconds")


