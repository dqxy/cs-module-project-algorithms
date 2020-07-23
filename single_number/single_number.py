'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

# First run: nested for loops
# Inner loop needs to be over whole range to catch matches before current number.
def single_number(arr):
    # Your code here
    # Sort array
    arr.sort()

    # Define single number and iteration variable
    single = 0
    i = 0

    # Loop sorted array
    while i < len(arr):
        # If last element reached in the array, single number target is found
        if i == len(arr) - 1:
            single = arr[i]
            return single
        # If the number is equal to it's neighbor on the right then skip neighbor
        elif arr[i] == arr[i + 1]:
            i += 2
        # Return the single number
        else:
            single = arr[i]
            return single

    return single

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")