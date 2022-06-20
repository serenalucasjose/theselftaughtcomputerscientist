import time

start = time.time()
count = 0
for i in range(1, 6):
    print(i)
    count += i
end = time.time()
print(end - start)

"""
Numero de pasos necesarios para evaluar

fn(n) = 1 + 2n
"""

