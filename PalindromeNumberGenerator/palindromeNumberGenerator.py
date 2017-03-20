"""
User inputs a number. Program counts number of times:

num + reverse_num = num_1
num_1 + reverse_num_1 = num_2
...

must be performed before num_n is a palindrome.

Ex:
23 + 32 = 55
result: 1 repetition
"""


def pal_num_gen(num, count):
    """
    Check  how many steps of num + rev_num must be taken
    to produce a palindrome
    """
    # Turn the number into a string
    num_str = str(num)
    print(num)

    # if rev_and_sum is palindrome
    if check_pal(num_str, 0, len(num_str) - 1):
        return count

    # if not palindrome
    if not check_pal(num_str, 0, len(num_str) - 1):
        # [::-1] => python trick to reverse a string
        rev_and_sum = int(num_str) + int(num_str[::-1])
        return pal_num_gen(rev_and_sum, count + 1)

def check_pal(str_num, idx1, idx2):

    """
    Check if given str(some_num) is a palindrome
    str_num must be passed in as a string.
    idx1 should first be passed as 0
    idx2 should first be passed as len(str_num) - 1
    """
    # If you've checked everything
    if idx1 >= idx2:
        return 1
    # If it's not a palindrome
    if str_num[idx1] != str_num[idx2]:
        return 0
    # Haven't checked the whole string yet
    return check_pal(str_num, idx1 + 1, idx2 - 1)


def main():
    num = int(input("Enter: "))
    res = pal_num_gen(num, 0)
    print(res)


if __name__ == '__main__':
    main()
