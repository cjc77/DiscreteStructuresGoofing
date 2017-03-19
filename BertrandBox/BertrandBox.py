import random


def run_experiment(exp_number):
    """
    Return probability of finding 'GG' given that first was 'G'
    Space = { (G,G), (G,S), (S,S) }
    """
    # Initial Setup
    all_chests = [['G', 'G'], ['G', 'S'], ['S', 'S']]

    # Important data
    gold_first_count = silver_second_count = gold_second_count = 0

    # Run n experiments
    for trial in range(exp_number):
        chest_chosen = all_chests[random.randrange(3)]
        drawer_1 = random.randrange(2)
        drawer_2 = 0

        # choose your first coin
        coin1 = chest_chosen[drawer_1]
        # Need we continue?
        if coin1 == 'G':
            gold_first_count += 1
            # Choose the second coin
            drawer_2 = 1 - drawer_1
            coin2 = chest_chosen[drawer_2]
            if coin2 == 'G':
                gold_second_count += 1
            elif coin2 == 'S':
                silver_second_count += 1

    gold_given_gold = gold_second_count / gold_first_count
    return gold_given_gold


def main():
    result = run_experiment(10000)
    expected = 2 / 3
    error = abs((result - expected) / expected)
    print("\nOdds of choosing G if first choice was G... \n")
    print("Result: ", result)
    print("Accuracy: ", 1 - error)


if __name__ == '__main__':
    main()
