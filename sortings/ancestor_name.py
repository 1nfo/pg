rome2num = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
}
def parse(name):
    full_name, rome = name.split(" ", 2)
    number = 0
    for i, c in enumerate(rome):
        if i + 1 < len(rome) and rome2num[c] < rome2num[rome[i+1]]:
            number -= rome2num[c]
        else:
            number += rome2num[c]

    return full_name, number, name

def sort_names(names):

    names = [parse(name) for name in names]
    names.sort()

    for name in names:
        print(name[-1])

if __name__ == "__main__":
    sort_names(["Steven XL", "Steven XVI", "David IX", "Mary XV", "Mary XIII", "Mary XX"])