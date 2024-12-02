from datetime import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as f:
        line = f.readline()
        all_data.append(line.strip())

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]


    start_time = datetime.now()
    for filename in filenames:
        read_info(filename)
    linear_time = datetime.now() - start_time
    print(f"{linear_time} (линейный)")

    """start_time = datetime.now()

    with Pool() as pool:
        pool.map(read_info, filenames)

    multiprocessing_time = datetime.now() - start_time
    print(f"{multiprocessing_time} (многопроцессный)")"""
