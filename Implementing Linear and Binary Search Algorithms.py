# Implement Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1 
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search(test_list, 6)
print(f"Linear Search: Index of 6 is {result}")

# Implement Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1 
test_list_sorted = sorted(test_list)
result = binary_search(test_list_sorted, 6)
print(f"Binary Search: Index of 6 in sorted list is {result}")

#Compare Performance
import time

def compare_search_algorithms(arr, target):
    start_time = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start_time

    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result = binary_search(arr_sorted, target)
    binary_time = time.time() - start_time
    
    print(f"Linear Search: Found at index {linear_result}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Time: {binary_time:.6f} seconds")
large_list = list(range(10000))
compare_search_algorithms(large_list, 8888)

# Implement Recursive Binary Search
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
result = binary_search_recursive(test_list_sorted, 6, 0, len(test_list_sorted) - 1)
print(f"Recursive Binary Search: Index of 6 in sorted list is {result}")

#Create a Main Function
def main():
    import random
    test_list = [random.randint(1, 100) for _ in range(20)]
    
    print("Original list:", test_list)
    print("Sorted list:", sorted(test_list))
    
    target = random.choice(test_list) 
    print(f"\nSearching for: {target}")
    
    result = linear_search(test_list, target)
    print(f"Linear Search: Found at index {result}")
    
    sorted_list = sorted(test_list)
    result = binary_search(sorted_list, target)
    print(f"Binary Search (iterative): Found at index {result}")
    
    result = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
    print(f"Binary Search (recursive): Found at index {result}")

    print("\nPerformance Comparison:")
    compare_search_algorithms(list(range(100000)), 99999)
if __name__ == "__main__":
    main()


#linear search function with its comparison
def linear_search_all(arr, target):
  indices = []
  compare_count = 0
  for i in range(len(arr)):
    compare_count += 1
    if arr[i] == target:
      indices.append(i)
  return indices, compare_count

#Use binary search with its comparison
def binary_search_insertion_point(arr, target):
  left = 0
  right = len(arr) - 1
  compare_count = 0
  while left <= right:
    mid = (left + right) // 2
    compare_count += 1
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return left, compare_count

#jump search algorithm with its comparison
def jump_search(arr, target):
  l = len(arr)
  jump = int(l**0.5)
  prev = 0
  compare_count = 0

  if arr[0] > target:
    return -1, compare_count

  while prev < l and arr[min(jump, l) - 1] < target:
    compare_count += 1
    prev = jump
    jump += int(l**0.5)
    if prev >= l:
      return -1, compare_count

  while prev < l and arr[prev] < target:
    compare_count += 1
    prev += 1
    if prev == min(jump, l):
      return -1, compare_count

  compare_count += 1
  if prev < l and arr[prev] == target:
      return prev, compare_count
  return -1, compare_count

#Print
if __name__ == "__main__":
  arr = [1, 3, 7, 8, 7, 5, 6, 7, 4]
  target = 7

  result, comparisons = linear_search_all(arr, target)
  print(f"Indices of {target}: {result}")
  print(f"Number of comparisons: {comparisons}")

  sorted_arr=sorted(arr)
  insertion_point= binary_search_insertion_point(sorted_arr, target)
  def binary_search_insertion_point(sorted_arr, target):
    return insertion_point, comparisons
  
  insertion_point, comparisons = binary_search_insertion_point(sorted_arr, target)
  print(f"Insertion Point: {insertion_point}, Comparisons: {comparisons}")

  index, comparisons = jump_search(sorted_arr, target)
  print(f"Index of {target} using jump search: {index}")
  print(f"Number of comparisons: {comparisons}")