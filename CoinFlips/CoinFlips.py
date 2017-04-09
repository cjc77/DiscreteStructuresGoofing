"""
This program models the compound probability of a coin flips.
It also finds all permutations of flipping n number of coins. 
"""


import random


def flip_coins(flip_count, flip_options):
    """
    Flip coins (flip_count times) and return the resulting sequence.
    """
    # How many choices?
    choice_size = len(flip_options)
    flip_results = ''
    rand_idx = 0
    # Flip coins and populate flip_results sequence
    for i in range(flip_count):
        rand_idx = random.randrange(choice_size)
        flip_results += flip_options[rand_idx]
    return flip_results


def find_permutations(target_length, char_bank, permutations):
    """
    Find all possible permutations of from char_bank of
    target_length.
    ex: ['H', 'T'], target_length = 3, 2^2 = 4, HH HT TH TT
    """
    char_options = len(char_bank)
    possible_perms = char_options ** target_length
    temp_str = ''
    while len(permutations) < possible_perms:
        temp_str = ''
        for i in range(target_length):
            rand_idx = random.randrange(char_options)
            temp_str += char_bank[rand_idx]
        if temp_str not in permutations:
            permutations.append(temp_str)


def zero_permutations(permutations, perm_dict):
    """
    Set value of each key in perm_dict to 0
    """
    for i in range(len(permutations)):
        perm_dict[permutations[i]] = 0


def compare_likelihood(string_dict, flip_options, key_len, number_trials):
    """
    Set the weights for the keys (sequences) in string_dict.
    Ex: {'HH': 21, 'HT' : 23, ...}
    """
    flip_result = ''
    for i in range(number_trials):
        flip_result = flip_coins(key_len, flip_options)
        string_dict[flip_result] += 1


def get_input():
    """
    Retrieve input from the user.
    """
    print('\n\n\n')
    string_length = int(input("Length of Sequence?  "))
    trial_num = int(input("How Many Trials? "))
    return string_length, trial_num


def likelihoods(weights, trials):
    """Print the likelihoods of each event."""
    for key, val in weights.items():
        print("Likelihood of " + key + ": " + str(round((weights[key] / trials * 100), 5)) +
              "% ")


def main():
    char_bank = ['H', 'T']
    inp = get_input()
    string_length = inp[0]
    trials = inp[1]
    permutations = []
    permutation_weights = {}
    find_permutations(string_length, char_bank, permutations)
    zero_permutations(permutations, permutation_weights)
    compare_likelihood(permutation_weights, char_bank, string_length, trials)
    print("Possible Permutations: " + str(len(permutations)))
    print(permutations)
    likelihoods(permutation_weights, trials)
    return


if __name__ == '__main__':
    main()
