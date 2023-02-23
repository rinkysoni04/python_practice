import threading
from multiprocessing import Process
import time

#Threading examples - 

def square(num, result):
    time.sleep(1)
    result[num] = num**2

#Example-1:

results = {}
t1 = threading.Thread(target = square, args=(2, results))
t2 = threading.Thread(target = square, args=(4, results))

t1.start()
t2.start()

t1.join()
t2.join()

print(results)

print()

# #Example-2:

results2 = {}

thread = [threading.Thread(target = square, args=(n, results2)) for n in range(1, 10)]

[t.start() for t in thread]
[t.join() for t in thread]

print(results2)
print()


#Processes examples - 

def squareProcess(num, result):
    print(num**2)   #Process dont share memory; they work in their own space and we do not have access to it. Thus instead of returning; we can print the result.
    print("--Finished computing {} --".format(num))
    print()

#Example-1:

results3 = {}
p1 = Process(target = squareProcess, args=(2, results3))
p2 = Process(target = squareProcess, args=(4, results3))

p1.start()
p2.start()

p1.join()
p2.join()

print()

#Example-2:

results4 = {}

process = [Process(target = squareProcess, args=(n, results4)) for n in range(1, 11)]

[p.start() for p in process]
[p.join() for p in process]

print()



