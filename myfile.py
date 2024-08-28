def sum_list(numbers):
    sum_ans = sum(numbers)
    return sum_ans

def count(numbers):
    cnt = len(numbers)
    return cnt


print("Welcome to our demonstration for HW 1")
print("-------------------------------------")
print("Homework 1 for SE CSC 510")
numbers = [i for i in range (1,10)]

print ("Our array: ", numbers)

sum_ans = sum_list(numbers)
print("The sum of the array elements: ", sum_ans)

cnt = count(numbers)
print("The number of elements: ", cnt)

mean = sum_ans/cnt

print("Mean of the elements in the array: ", mean)

