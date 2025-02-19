import random
import secrets
from collections import Counter
random_numbersR = [random.randint(1, 16) for _ in range(100)] #makes a list of random numbers 1-16

random_numbersS = [secrets.randbelow(16) + 1 for _ in range(100)] # makes a list of random numbers 1-16 using secrets instead of random

count_random = Counter(random_numbersR) # counts random numbers apperance

print(count_random)

print("\n")

count_secrets = Counter(random_numbersS)

print(count_secrets)

print("\n")

print ("It seems both repeat a lot of times, but Random repeats more than Secrets")

print("\n")

random_numbers_Random_Big = [random.randint(1, 65535) for _ in range(100)] #makes a list of random numbers 1-65535

random_numbers_Secrets_Big = [secrets.randbelow(65535) + 1 for _ in range(100)] # makes a list of random numbers 1-16 using secrets instead of random

count_Random = Counter(random_numbers_Random_Big) # counts random numbers apperance

print(count_Random)

print("\n")

count_Secrets = Counter(random_numbers_Secrets_Big)

print(count_Secrets)

print("\n")

print("It seems both can handle not repeating another number from the output")

print("\n")

random_list = [random.randint(1, 16) for _ in range(100)]

def bubble_sort(arr):
    # Get the length
    L = len(arr)
    
    # Moves through the elements
    for i in range(L):
        # sorted
        for k in range(0, L-i-1):
            #moves if bigger
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
    return arr

Sorted_list = bubble_sort(random_list)

print (Sorted_list)

print("\n")

random_list2 = [random.randint(1, 65535) for _ in range(100)]

Sorted_list2 = bubble_sort(random_list2)

print (Sorted_list2)

print("\n")

random_list3 = [random.randint(1, 65535) for _ in range(500)]

Sorted_list3 = bubble_sort(random_list3)

print (Sorted_list3)

print("\n")

print("The sorting method, bubble sort takes more time with bigger elements list, but I found the time difference in this test to be small")