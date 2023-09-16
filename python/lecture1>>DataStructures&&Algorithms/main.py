# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def find_nod(a, b):
    while a != b:
        if a > b:
            a -= 1
        else:
            b -= 1

    return a


def main():
    a = int(input('Enter value of a: '))
    b = int(input('Enter value of b: '))
    find_nod(a, b)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
