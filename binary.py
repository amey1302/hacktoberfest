def binary_search(l1, n):  
    low = 0  
    high = len(l1) - 1  
    mid = 0  
  
    while low <= high:  
        # for get integer result   
        mid = (high + low) // 2  
  
        # Check if n is present at mid   
        if l1[mid] < n:  
            low = mid + 1  
  
        # If n is greater, compare to the right of mid   
        elif l1[mid] > n:  
            high = mid - 1  
  
        # If n is smaller, compared to the left of mid  
        else:  
            return mid  
  
            # element was not present in the list, return -1  
    return -1  
  
  
# Initial l1  
l1 = [23,44,56,78,29,10,45,76]  
n = 45  
  
res = binary_search(l1, n)  
  
if res != -1:  
    print("Element is present at index", str(res))  
else:  
    print("Element is not present in l1")  
