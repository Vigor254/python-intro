from function import my_function

numbers=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
# initialise sum variables
sum_even=0
# iterate over each number in a list
for number in numbers:
    if number % 2 == 0:
        sum_even+=number
print(f"the sum of all even numbers is: {sum_even}")
my_function()