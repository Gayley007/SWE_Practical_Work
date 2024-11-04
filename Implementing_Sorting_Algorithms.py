# Implement Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(test_arr.copy())
print("Bubble Sort Result:", sorted_arr)

# Implement Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(test_arr)
print("Merge Sort Result:", sorted_arr)

#Implement Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(test_arr)
print("Quick Sort Result:", sorted_arr)

#Compare Performance
import time
import random
def compare_sorting_algorithms(arr):
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort)
    ]
    for name, func in algorithms:
        arr_copy = arr.copy()
        start_time = time.time()
        func(arr_copy)
        end_time = time.time()
        print(f"{name} took {end_time - start_time:.6f} seconds")
# Generate a large random array
large_arr = [random.randint(1, 1000) for _ in range(1000)]
# Compare the algorithms
compare_sorting_algorithms(large_arr)


# Implement Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Implement Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Update the compare_sorting_algorithms function to include the new algorithms
def compare_sorting_algorithms(arr, trials=5):
    import time
    import random
    from statistics import mean

    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Insertion Sort", insertion_sort),
        ("Selection Sort", selection_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort)
    ]

    performance = {name: [] for name, _ in algorithms}

    for trial in range(trials):
        print(f"Trial {trial + 1}/{trials}")
        for name, func in algorithms:
            arr_copy = arr.copy()
            start_time = time.time()
            func(arr_copy)
            end_time = time.time()
            elapsed_time = end_time - start_time
            performance[name].append(elapsed_time)
            print(f"  {name} took {elapsed_time:.6f} seconds")
    
    # Calculate average times
    average_performance = {name: mean(times) for name, times in performance.items()}
    print("\nAverage Performance over", trials, "trials:")
    for name, avg_time in average_performance.items():
        print(f"{name}: {avg_time:.6f} seconds")
    
    return average_performance

# Visualize the performance using matplotlib
def visualize_performance(performance):
    import matplotlib.pyplot as plt

    algorithms = list(performance.keys())
    times = list(performance.values())

    plt.figure(figsize=(10, 6))
    bars = plt.bar(algorithms, times, color=['blue', 'orange', 'green', 'red', 'purple'])
    plt.xlabel('Sorting Algorithms')
    plt.ylabel('Average Time (seconds)')
    plt.title('Performance Comparison of Sorting Algorithms')
    plt.ylim(0, max(times) * 1.1)

    # Add the exact time on top of each bar
    for bar, time_val in zip(bars, times):
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + max(times)*0.01, f'{time_val:.6f}', 
                 ha='center', va='bottom')
    plt.show()

large_arr = [random.randint(1, 1000) for _ in range(1000)]
average_performance = compare_sorting_algorithms(large_arr, trials=5)
visualize_performance(average_performance)