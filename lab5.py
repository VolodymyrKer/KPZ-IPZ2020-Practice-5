import pytest

from subjects.prime_num_generator import prime_num_generator
from subjects.validator_ip import validate_ip
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
    assert isinstance(next(subject_one), int) == True


def test_validator_ip():
    faker = Faker()
    ip_addr = faker.ipv4()


    for i in range(50):
        assert validate_ip(ip_addr) == True

    with pytest.raises(Exception):
        assert False == validate_ip("1.0.0.")

    with pytest.raises(Exception):
        assert False == validate_ip(123)

    assert isinstance(validate_ip(faker.ipv4()), bool) == True


def test_palindrom():
    subject = "Hello, kayak, phrase!address. mom ,!,wow ,deed ,,mom " \
              "repaper level,уму,йой,зараз,файно,радар,!дід,пів,кугут,що "
    palindrom_arr = ["kayak", "mom", "wow", "deed", "mom", "repaper", "level", "уму", "йой", "зараз", "радар", "дід"]

    assert palindrom_arr == palindrom(subject)

    with pytest.raises(Exception):
        assert [] == palindrom("11")

    with pytest.raises(Exception):
        assert [] == palindrom(123)

    assert isinstance(palindrom(subject), list)
