from solver import a_star_search
from timechecker import Profiler

if __name__ == '__main__':
    # start = (2, 8, 3, 1, 6, 4, 7, 0, 5)
    # goal = (1, 2, 3, 8, 0, 4, 7, 6, 5)
    start = (1, 2, 0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 3, 15)
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)
    with Profiler() as profiler:
        statistics = a_star_search(start, goal)
        print(statistics)
