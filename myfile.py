def sum_list(numbers):
    sum_ans = sum(numbers)
    return sum_ans

def count(numbers):
    cnt = len(numbers)
    return cnt


print("Welcome to our demonstration")

numbers = [i for i in range (1,10)] # List Comprehension

print ("Our array is: ", numbers)

sum_ans = sum_list(numbers)
print("The sum of the array elements are: ", sum_ans)

cnt = count(numbers)
print("The number of elements: ", cnt)

mean = sum_ans/cnt

print("Mean of the elements in the array is: ", mean)

