from subjects.prime_num_generator import prime_num_generator
from subjects.validator_ip import validate_ip
from subjects.print_os import get_os
from subjects.palindrom import palindrom
from faker import Faker


def test_prime_num_generator():
    subject_one = prime_num_generator()
    true_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for i in true_prime:
        assert next(subject_one) == i

    index = 101
    subject_two = prime_num_generator()
    for i, v in enumerate(subject_two):
        # index-1 because it counts from zero in enumerate
        if i is index - 1:
            assert v == 547
            break


def test_validator_ip():
    faker = Faker()
    ip_addr = faker.ipv4()
    for i in range(50):
        assert validate_ip(ip_addr) == True
