# Step 1
# Implement SelectionSort & MergeSort

# random
import numpy as np
from numpy import random
import time
import matplotlib.pyplot as plt

# empty array
marray = []

# measure running times for inputs n = [100, 500, 1000, 5000]
def generate_list(sz):
    return np.random.randint(low=1, high=sz, size=sz).tolist()


# timer - check how long certain inputs take
def time_algorithm(algo, arr):
    start = time.perf_counter()
    algo(arr.copy())
    end = time.perf_counter()
    return end - start

# Selection Sort
# 1 - find the smallest element and swap with the 0 element
# 2 - find smallest among remaining and swap with 1 element
# 3 - continue until the end of the array

def selection_sort(arr):
    n = len(arr) #get amount in array
    for i in range(n):
        min_idx = i #set min index to current index
        for j in range(i+1, n): #loop through remaining elements - stop at n
            if arr[j] < arr[min_idx]: # check if current smaller
                min_idx = j # update min if true
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # switch
    return arr

# Merge Sort
# divide recursively into halves
# sort subarray
# merge
def merge_sort(arr): #divide part
    n = len(arr)
    if n > 1:
        sub_arr1 = arr[0:n//2] #get first and second halves
        sub_arr2 = arr[n//2:n] # if n is odd, this will have one more element
        
        # divide until n == 1
        merge_sort(sub_arr1)
        merge_sort(sub_arr2)

        i = j = k = 0 # i = arr1, j = arr2, k = arr

        # Find smallest 
        while i < len(sub_arr1) and j < len(sub_arr2):
            if sub_arr1[i] < sub_arr2[j]:
                arr[k] = sub_arr1[i] #copy smallest over
                i += 1 # for array1
            else:
                arr[k] = sub_arr2[j]
                j += 1 #array2
            k += 1 #ensure k index changes

        # copy remaining elements from sub_arr1
        # this is essential because we pick from the smallest side
        # depleting one side means there will be lots remaining on the other side
        while i < len(sub_arr1):
            arr[k] = sub_arr1[i]
            i += 1 #track index
            k += 1 

        # incase leftovers
        while j < len(sub_arr2):
            arr[k] = sub_arr2[j]
            j += 1
            k += 1

    return arr

# def plot_results(sizes):
#     # have x be time
#     ypts = sizes



if __name__ == "__main__":
    sizes = [100, 500, 1000, 5000]
    trials = 30

    # make empty array to track data
    s_meds_times = []
    m_meds_times = []

    for sz in sizes:
        s_time_list = []
        m_time_list = []

        for _ in range(trials):
            arr = generate_list(sz)
            # track times
            s_time_list.append(time_algorithm(selection_sort, arr))
            m_time_list.append(time_algorithm(merge_sort, arr))

        # record mediam times 
        s_median = np.median(s_time_list)
        m_median = np.median(m_time_list)

        # put into array
        s_meds_times.append(s_median)
        m_meds_times.append(m_median)

    # Plot 1: Linear Scale
    plt.figure(figsize=(10, 6))
    # x = n, y = selection median times 
    plt.plot(sizes, s_meds_times, marker='o', label='Selection Sort')
    plt.plot(sizes, m_meds_times, marker='o', label='Merge Sort')
    # label x and y axis + title
    plt.xlabel("Input size (n)")
    plt.ylabel("Median time (seconds)")
    plt.title("Linear Scale: Sorting Time vs Input Size")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Plot 2: Log–Log Scale
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, s_meds_times, marker='o', label='Selection Sort')
    plt.plot(sizes, m_meds_times, marker='o', label='Merge Sort')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel("Input size (log scale)")
    plt.ylabel("Median time (log scale)")
    plt.title("Log–Log Scale: Sorting Time vs Input Size")
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.tight_layout()
    plt.show()

