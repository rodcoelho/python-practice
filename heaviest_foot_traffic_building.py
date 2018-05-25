#!/usr/bin/env python3

# you have a log of data that shows people entering and leaving a building
# find at what time the population was the largest

log = [  [1487799425, 14, 1],
         [1487799425, 4,  0],
         [1487799425, 2,  0],
         [1487800378, 10, 1],
         [1487801478, 18, 0],
         [1487801478, 18, 1],
         [1487901013, 1,  0],
         [1487901211, 7,  1],
         [1487901211, 7,  0]  ]


def find_busiest_period(data):
    current_time = data[0][0]
    current_population = data[0][1] if data[0][2] == 1 else -data[0][1]
    max_population = current_population
    max_population_time = current_time
    total_population = 0

    for i in range(1, len(data)):
        if data[i][0] == current_time:
            if data[i][2] == 1:
                current_population += data[i][1]
            else:
                current_population -= data[i][1]
        else:
            total_population += current_population
            current_population = data[i][1] if data[i][2] else -data[i][1]
            if total_population > max_population:
                max_population_time = current_time
                max_population = total_population
            current_time = data[i][0]
    total_population += current_population
    if total_population > max_population:
        max_population_time = data[-1][0]
    return max_population_time


if __name__ == '__main__':
    assert find_busiest_period(log) == 1487800378, 'error1'

