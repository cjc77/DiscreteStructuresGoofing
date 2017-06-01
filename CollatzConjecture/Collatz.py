def collatz(n):
    """
    Return number of iterations taken to get to 1.
    """
    iterCount = 0
    while(n != 1):
        if(n & 1):
            n = 3 * n + 1
        else:
            n //= 2
        iterCount += 1
    return iterCount



def main():
    num = int(input("Enter: "))
    ans = collatz(num)
    print("Operations to 1: ", ans)


if __name__ == '__main__':
    main()
