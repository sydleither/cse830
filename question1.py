import time
from random import randint
import matplotlib.pyplot as plt
import numpy as np

#https://introcs.cs.princeton.edu/python/42sort/insertion.py.html
def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        j = i
        while (j > 0) and (a[j] < a[j-1]):
            a[j-1], a[j] = a[j], a[j-1]
            j -= 1


#https://introcs.cs.princeton.edu/python/42sort/merge.py.html
def merge(a, lo, mid, hi, aux):
    n = hi - lo
    i = lo
    j = mid
    for k in range(n):
        if i == mid:
            aux[k] = a[j]
            j += 1
        elif j == hi:
            aux[k] = a[i]
            i += 1
        elif a[j] < a[i]:
            aux[k] = a[j]
            j += 1
        else:
            aux[k] = a[i]
            i += 1
    a[lo:hi] = aux[0:n]
    

def merge_sort(a, lo, hi, aux):
    n = hi - lo
    if n <= 1:
        return
    mid = (lo + hi) // 2
    merge_sort(a, lo, mid, aux)
    merge_sort(a, mid, hi, aux)
    merge(a, lo, mid, hi, aux)


insertion_times = []
merge_times = []
trials = 10
for i in range(1, 101):
    insertion_temp = 0
    merge_temp = 0
    for j in range(trials):
        list1 = [randint(1, 101) for x in range(i)]
        list2 = list1[:]
        
        i_start = time.time()
        insertion_sort(list1)
        i_end = time.time()
    
        m_start = time.time()
        merge_sort(list2, 0, len(list2), [0]*len(list2))
        m_end = time.time()
        
        insertion_temp += i_end - i_start
        merge_temp += m_end - m_start
    insertion_times.append(insertion_temp/trials)
    merge_times.append(merge_temp/trials)
    
x = np.linspace(0,100,100)

plt.plot(x, insertion_times, label='Insertion')
plt.plot(x, merge_times, label='Merge')

plt.title('Insertion Sort vs Merge Sort')
plt.xlabel('list size')
plt.ylabel('time taken to sort')
plt.legend()

#https://stackoverflow.com/questions/28766692/intersection-of-two-graphs-in-python-find-the-x-value
idx = np.argwhere(np.diff(np.sign(np.array(insertion_times) - np.array(merge_times)))).flatten()
print(x[idx])
