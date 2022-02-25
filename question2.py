import time
from random import randint
import matplotlib.pyplot as plt
import numpy as np

#https://introcs.cs.princeton.edu/python/42sort/insertion.py.html
def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        j = i
        while j > 0 and a[j] < a[j-1]:
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
        
        
def insertion_sort_tim(a, lo, hi):
    for i in range(lo+1, hi):
        j = i
        while j > lo and a[j] < a[j-1]:
            a[j-1], a[j] = a[j], a[j-1]
            j -= 1
        
        
def tim_sort(a, lo, hi, aux, k):
    n = hi - lo
    if n <= 1:
        return
    if n <= k:
        insertion_sort_tim(a, lo, hi)
    else:
        mid = (lo + hi) // 2
        tim_sort(a, lo, mid, aux, k)
        tim_sort(a, mid, hi, aux, k)
        merge(a, lo, mid, hi, aux)


def test_all():
    insertion_times = []
    merge_times = []
    tim_times = []
    trials = 5
    n = 300
    k = 16
    for i in range(1, n+1):
        insertion_temp = 0
        merge_temp = 0
        tim_temp = 0
        for j in range(trials):
            list1 = [randint(1, 101) for x in range(i)]
            list2 = list1[:]
            list3 = list1[:]
            
            i_start = time.time()
            insertion_sort(list1)
            i_end = time.time()
        
            m_start = time.time()
            merge_sort(list2, 0, len(list2), [0]*len(list2))
            m_end = time.time()
            
            t_start = time.time()
            tim_sort(list3, 0, len(list3), [0]*len(list3), k)
            t_end = time.time()
            
            insertion_temp += i_end - i_start
            merge_temp += m_end - m_start
            tim_temp += t_end - t_start
        insertion_times.append(insertion_temp/trials)
        merge_times.append(merge_temp/trials)
        tim_times.append(tim_temp/trials)
        
    x = np.linspace(0, n, n)
    
    plt.plot(x, insertion_times, label='Insertion')
    plt.plot(x, merge_times, label='Merge')
    plt.plot(x, tim_times, label=f'Tim k = {k}')
    
    plt.title('Insertion Sort vs Merge Sort vs Tim Sort')
    plt.xlabel('list size')
    plt.ylabel('average time taken to sort over 5 trials')
    plt.legend()
    

def test_tim_k():
    tim_times = []
    k_times = []
    trials = 5
    n = 300
    for k in range(1, 51):
        for i in range(1, n+1):
            tim_temp = 0
            for j in range(trials):
                list1 = [randint(1, 101) for x in range(i)]
        
                t_start = time.time()
                tim_sort(list1, 0, len(list1), [0]*len(list1), k)
                t_end = time.time()
                
                tim_temp += t_end - t_start
            tim_times.append(tim_temp/trials)
        k_times.append(sum(tim_times)/len(tim_times))
        
    x = np.linspace(0, 50, 50)
    plt.plot(x, k_times)
    plt.title('Best k for Tim Sort')
    plt.xlabel('k')
    plt.ylabel(f'average time taken to sort lists of size n=1 to n={n}')
    
    print(np.argmin(k_times))
    
    
test_all()
