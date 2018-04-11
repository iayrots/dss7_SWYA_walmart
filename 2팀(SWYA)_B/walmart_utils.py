from collections import Counter
import numpy as np
import pandas as pd

def category_counts(data):
    """
    Count total number of unique DepartmentDescription made on each trip.
    """
    counts = []
    for array in np.asarray(data.loc[:, "1-HR PHOTO":"WIRELESS"]):
        count = 0
        for item in array:
            if item > 0:
                count += 1
        counts.append(count)
    cat_counts = pd.DataFrame(counts)
    cat_counts = cat_counts.rename(columns={0: "CategoryCount"})
    cat_counts = cat_counts.set_index(data.index)

    data.insert(6, "CategoryCounts", cat_counts)

    return data


def company(x):
    """
    Return company code from given Upc code.
    :param x: "Upc" column of DataFrame
    :return: company code
    """
    try:
        p = x[:6]
        if p == "000000":
            return x[-5]
        return p
    except:
        return -9999


def float_to_str(obj):
    """
    Convert Upc code from float to string
    Use this function by applying lambda
    :param obj: "Upc" column of DataFrame
    :return: string converted Upc removing dot.
    """
    while obj != "nan":
        obj = str(obj).split(".")[0]
        return obj


def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    ls = [x_i for x_i, count in counts.items() if count == max_count]
    return ls[0]


def check_digit(x):
    try:
        odd = map(int, ','.join(x[-1::-2]).split(','))
        even = map(int, ','.join(x[-2::-2]).split(','))
        sum_odd3 = sum(odd) * 3
        total = sum_odd3 + sum(even)
        rem = total % 10
        if rem == 0:
            return rem
        return 10 - rem
    except:
        return -9999
