def counting_sort(arr):
    a, b = min(arr), max(arr)
    counts = [0] * (b - a + 1)

    for i in arr:
        counts[i - a] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    arr2 = [0] * len(arr)

    for i in arr:
        counts[i - a] -= 1
        arr2[counts[i - a]] = i

    return arr2


def demo():
    from random import randint

    arr = [randint(0, 100) for i in range(20)]

    arr2 = counting_sort(arr)

    print(arr, arr2)


if __name__ == '__main__':
    demo()


import requests
requests.get()