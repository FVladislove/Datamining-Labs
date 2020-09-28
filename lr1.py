import math


def calculate_median(data: list):
    return sum(data) / len(data)


def calculate_standard_deviation(data: list):
    median = calculate_median(data)
    return math.sqrt(
        sum(list(map(lambda value: (value - median) ** 2, data))) / (len(data) - 1))


def classify_into_2_classes(sample, median, standard_deviation):
    class1 = []
    class2 = []
    left_border = median - 3 * standard_deviation
    right_border = median + 3 * standard_deviation
    for elem in sample:
        if left_border < elem < right_border:
            class1.append(elem)
        else:
            class2.append(elem)
    return class1, class2


def main():
    train_sample = [2, 2, 4, 3, 3, 5, 8, 8, 8, 6, 6, 6, 7, 7, 5, 5, 4, 2, 4, 3, 4, 4, 5, 5, 7]
    target_sample = [2, 2, 4, 3, 3, 5, 8, 56, 92, 6, 6, 6, 72, 7, 5, 5, 4, 2, 4, 3, 4, 4, 5, 81, 7]
    class1, class2 = classify_into_2_classes(target_sample,
                                             calculate_median(train_sample),
                                             calculate_standard_deviation(train_sample))
    print(class1, class2)


main()
