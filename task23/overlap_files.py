'''
Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a list of all
prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes, happy numbers are a real
thing in mathematics - you can look it up on Wikipedia. The explanation is easier with an example, which I will describe below.)
'''

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
