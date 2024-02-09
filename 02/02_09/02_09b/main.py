def find_second_smallest(my_list):
    return None if len(my_list) <= 1 else sorted(my_list)[1]

print(find_second_smallest([5, 8, 3, 2, 6]))
print(find_second_smallest([5]))
print(find_second_smallest([]))
print(find_second_smallest([5, 8, 3, 2, 6, 33]))
print(find_second_smallest(['person', 'woman', 'man', 'camera', 'tv']))