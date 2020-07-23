'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, arr=None):
    # Your code here
    if n == 0: # 0 Cookies
        return 1
    elif n < 0: # Negative cookies
        return 0
    # Return sum of outcomes for n >= 1 cookies
    # Eat either 1, 2, or 3 cookies at a time
    else:
        return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")