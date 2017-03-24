def overlap():
    with open('One.txt', 'r') as file:
        numbers = file.read()
        list_numbers = list(map(int, numbers.split()))

    with open('the other.txt', 'r') as file_two:
        numbers_two = file_two.read()
        list_prime_numbers = list(map(int, numbers_two.split()))

    overlap_number = [i for i in list_numbers if i in list_prime_numbers]

    [print(i) for i in overlap_number]

if __name__ == '__main__':
    overlap()