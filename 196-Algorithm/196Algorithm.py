"""
Process: Game called "reverse and add". Are there any Lychrel Numbers?
User inputs a number. Program counts number of times:

num + reverse_num = num_1
num_1 + reverse_num_1 = num_2
...

must be performed before num_n is a palindrome.

Ex:
23 + 32 = 55
result: 1 repetition

Interesting cases 89, 196
"""


NONE = 0



def one_ninety_six(num, count):
    """
    Check  how many steps of num + rev_num must be taken
    to produce a palindrome
    """
    # Turn the number into a string
    num_str = str(num)
    print(num)

    # Check the number
    pal = check_pal(num_str, 0, len(num_str) - 1)

    # if current number is palindrome
    if pal:
        return count

    # if not palindrome
    if not pal:
        # [::-1] => python trick to reverse a string
        rev_and_sum = int(num_str) + int(num_str[::-1])
        print(num_str, '+', num_str[::-1])
        return one_ninety_six(rev_and_sum, count + 1)


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
    res = one_ninety_six(num, NONE)
    print(res, "repetition(s)", sep=' ')


if __name__ == '__main__':
    main()
