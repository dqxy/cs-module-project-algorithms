'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # Declaring empty list and zero count
    nums = []
    zero_count = 0

    for num in arr:
        # If number is non-zero, add number to the list
        if num != 0:
            nums.append(num)
        # If number is zero, zero counter is incremented
        else:
            zero_count += 1

    # Add zeroes to the end of the list
    nums.extend([0] * zero_count)
    return nums

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")