# Check if the first and last number of a list is the same

num_list = [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 10]

def check_list(list):
    if list[0] == list[-1]:
        return True
    else:
        return False

print("Result is {}".format(check_list(num_list)))

