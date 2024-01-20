import random
import math
import time
import multiprocessing

def wait():
    n = 0
    
    while n <= 10000000:
        n += 1

x = []
s = []
Y = True
N = False
y = True
n = False

print("-" * 10 + " MEMORY AND CPU DESTROYER PROGRAM " + "-" * 10 + "\n")
print("THIS PROGRAM IS HARMFUL AND IT WILL DAMAGE YOUR COMPUTER")
print("I HIGHLY NOT RECOMMEND USING THIS")
print("PLEASE BE CAREFUL!!!\n")
wait()
wait()

print("LOADING THE WEAPON...\n")
wait()
print("READY...\n")
wait()
destroy_memory = input("DO YOU WANT TO DESTROY YOUR MEMORY ? (Y/N): ")
destroy_cpu = input("DO YOU WANT TO DESTROY YOUR CPU ? (Y/N): ")
num = 1
n = 0
destroy_rate = 1000

def destroy():
    for q in range(num):
        for j in range(20):
            ns = []
            print("\nTHREAT NUMBER " + str(j + 1))
            print("DOING DESTRCUTIVE CPU_MATH WORK...")
            for k in range(destroy_rate):
                n = 0
                for a in range(destroy_rate * (j + 1) if destroy_cpu else 1):
                    n += math.log(math.pow(random.uniform(math.ceil(math.log(random.uniform(0, 1))), math.ceil(math.log(random.uniform(0, 1)))), 2) + 1, 10)
                for i in range(random.randint(0, 10)):
                    n = math.log(n + 1, 2) * (10 * random.randint(1, 10))
                ns.append(n)
            print("DOING DESTRCUTIVE MEM_WRITE WORK...")
            for z in range(int(math.pow(destroy_rate, 2)) + len(s) if destroy_memory else 1):
                s.append(ns)
               

processes = []

for i in range(12):
    p = multiprocessing.Process(target=destroy)
    p.start()
    processes.append(p)

for p in processes:
    p.join()

print("\nYOUR COMPUTER SURVIVED FROM THREATS...")


    
