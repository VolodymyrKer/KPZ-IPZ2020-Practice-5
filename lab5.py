from subjects.prime_num_generator import prime_num_generator
from subjects.validatorIP import validate_ip
from subjects.printOS import get_os
from subjects.palindrom import palindrom


def test_prime_num_generator():
    subject_one = prime_num_generator()
    true_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for i in true_prime:
        assert next(subject_one) == i

    # 100 because it counts from zero in the enumerate
    index = 100
    subject_two = prime_num_generator()
    for i,v in enumerate(subject_two):
        if i is index:
            assert v == 547
            break
