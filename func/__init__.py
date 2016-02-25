import os

if os.getcwd().endswith('fibonacci-packet'):
    file_name = 'data/numbers.txt'
else:
    file_name = 'packets/fibonacci-packet/data/numbers.txt'


def get_by_num(n):
    """
    Get fibonacci number by it's number in Fibonacci sequence

    :param n: int from 1, number in list
    :return: int, number in Fibonacci sequence
    """
    sequence = open(file_name).readlines()
    try:
        return int(sequence[n + 1].strip())
    except IndexError:
        return None


def get_sequence(n):
    """
    Get first n items in Fibonacci sequence

    :param n: number of items
    :return: list of int, Fibonacci sequence
    """
    sequence = open(file_name).readlines()
    return list(map(int, sequence))[:n]
