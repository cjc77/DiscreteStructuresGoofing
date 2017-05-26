"""
There are 8 Lisa's out of 172 active clients. What is the probability that 2
Lisa's will take the same fitness class on the same day? 57 fitness classes are
offered each week.

1 = Lisa
0 = Not Lisa

Assume attendance btwn 1 and 15 for all classes
57 Total classes
8 Lisa's (1s)

"""
import random

NUM_MEMS = 172
NUM_LISA = 8
NUM_CLASSES = 57

MAX_CLASSES = 3


def fill_in_members(member_ls):
    """
    Fill in members with first 8 being Lisa (1) and the other 164 not Lisa (0)
    Format is [0, 0]
    with 0th idx being name and 1st idx being number of visits this week
    """
    # First 8 items will be [[1, 0], [1, 0], ...]
    for i in range(NUM_LISA):
        member_ls[i][0] = 1
    # print(member_ls)


def initialize_classes(rosters, members):
    """
    Create 57 classes with rosters of random size 1-15
    Initialize class rosters with -1s
    """
    for i in range(NUM_CLASSES):
        # generate random roster size
        roster_size = random.randrange(1, 16)
        # create class
        rosters["c" + str(i + 1)] = [-1] * roster_size
    # for k, v in rosters.items():
    #     print(k, v, sep=" -- ")


def fill_class_rosters(rosters, members):
    # go through all classes
    for k in rosters:
        already_chosen = []
        # go through roster of current class
        for i in range(len(rosters[k])):

            # pick a member and check if they've already taken 3 classes
            # or if they're already signed up for this particular class
            r_member = random.randrange(NUM_MEMS)
            while r_member in already_chosen or members[r_member][1] == MAX_CLASSES:
                r_member = random.randrange(NUM_MEMS)

            # add to the roster
            rosters[k][i] = members[r_member][0]
            # update exclusion criteria
            members[r_member][1] += 1
            already_chosen.append(r_member)


def check_more_than_one_lisa(rosters):
    same_name_occurances = 0
    for k, v in rosters.items():
        lisa_count = 0
        for i in range(len(v)):
            if v[i] == 1:
                lisa_count += 1
            if lisa_count > 2:
                same_name_occurances += 1
                break
    return same_name_occurances



def main():
    studio_members = [[0] * 2 for i in range(NUM_MEMS)]
    class_rosters = {}
    for i in range(100):
        fill_in_members(studio_members)
        initialize_classes(class_rosters, studio_members)
        fill_class_rosters(class_rosters, studio_members)
        res = check_more_than_one_lisa(class_rosters)
        print(res)
        studio_members = [[0] * 2 for i in range(NUM_MEMS)]
        class_rosters = {}
    # for k, v in class_rosters.items():
    #     print(k, v, sep=" -- ")















if __name__ == '__main__':
    main()
