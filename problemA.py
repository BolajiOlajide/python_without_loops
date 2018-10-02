import math
import check

print1 = "The total is: {0}"
print2 = "Bye!"


# recursive method to always request for user input
def add_sum(sum):
    # get the first user input
    user_input = input('Enter a positive integer: ')
    # flip the user input so it starts from behind to the front
    flip_input = user_input[::-1]
    # convert string to integer
    number_input = int(flip_input)
    # add the integer to the sum above
    sum += int(number_input)

    # stop the recursion when the user enters 0
    if number_input == 0:
        return sum
    # recursively call the add_sum method again
    return add_sum(sum)


def reverse_nat():
    # initialize the sum to zero since we start counting from zero
    sum = 0

    # get the o
    reverse_sum = add_sum(sum)

    # print the results
    print(print1.format(reverse_sum))
    print(print2)
    return
