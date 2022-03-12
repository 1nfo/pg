def pigeon_hole_sort(arr):
    a, b = min(arr), max(arr)
    holes = [0] * (b - a + 1)

    for i in arr:
        holes[i - a] += 1

    arr2 = []
    for i in range(len(holes)):
        for j in range(holes[i]):
            arr2.append(a + i)

    return arr2


def demo():
    from random import randint

    arr = [randint(0, 100) for i in range(20)]

    arr2 = pigeon_hole_sort(arr)

    print(arr, arr2, sep='\n')


if __name__ == '__main__':
    demo()
