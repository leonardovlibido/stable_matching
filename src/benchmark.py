from stable_marriage_matcher import StableMarriageMatcher
from random import shuffle
import matplotlib.pyplot as plt
import time


def generate_execution_time_plot(sizes=None):
    if sizes is None:
        sizes = [3, 10, 30, 100, 300, 600, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
    data_gen_times = []
    alg_times = []
    bubble_sort_times = []

    for n in sizes:
        data_generation_time, algorithm_time = calculate_time_gale_shapley(n)
        data_gen_times.append(data_generation_time)
        alg_times.append(algorithm_time)
        bubble_sort_times.append(5*calculate_time_bubble_sort(n))

    plt.plot(sizes, data_gen_times, 'b', label='data_generation')
    plt.plot(sizes, alg_times, 'g', label='gale_shapley')
    plt.plot(sizes, bubble_sort_times, 'y', label='bubble_sort * 5')

    plt.xlabel("number of men/women")
    plt.ylabel("time of execution")
    plt.legend()
    plt.show()


def generate_men_and_woman_ranks(n):
    men_list = ["m"+str(i) for i in range(n)]
    women_list = ["w"+str(i) for i in range(n)]
    women_ranks = {}
    men_ranks = {}

    for m in men_list:
        shuffle(women_list)
        men_ranks[m] = women_list[:]

    for w in women_list:
        shuffle(men_list)
        women_ranks[w] = men_list[:]

    return men_ranks, women_ranks


def calculate_time_gale_shapley(n):
    print("Started data generation")
    start_time = time.time()
    men_ranks, women_ranks = generate_men_and_woman_ranks(n)
    matcher = StableMarriageMatcher(men_ranks, women_ranks)
    data_generation_time = time.time() - start_time
    print("--- %s seconds ---" % data_generation_time)

    print("Started algorithm")
    start_time = time.time()
    matcher.find_matching()
    assert(matcher.matching.is_stable() is True)
    algorithm_time = time.time() - start_time
    print("--- %s seconds ---" % algorithm_time)

    print("Done!")
    return data_generation_time, algorithm_time


def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]


def calculate_time_bubble_sort(n):
    nums = list(range(n))
    shuffle(nums)

    start_time = time.time()
    bubble_sort(nums)
    alg_time = time.time() - start_time

    return alg_time
