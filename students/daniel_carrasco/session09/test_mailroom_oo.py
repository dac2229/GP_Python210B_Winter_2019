import pytest
from donor_models import *


def test_init():
    """
    This only tests that it can be initialized with and without
    some content -- but it's a start
    """
    c = Donor('Daniel')


def test_donations():
    """
    This test if you can make an initial donation and add donations
    """
    c = Donor('Daniel')
    c.donations = 1000
    print(c)
    assert c.donations == 1000
    c.donations = 1000
    assert c.donations == 2000


def test_counter():
    """
    This test if it counts the initial number of donations and if it keeps track of total number of
    donations correctly
    """
    c = Donor('Daniel')
    c.donations = 1000
    c.counter = 4
    assert c.counter != 1
    assert c.counter == 4
    c.donations = 1000
    assert c.counter == 5
    ddb.Donor_Data.data_dict.clear()


def test_showallnames():
    """
    This test is to see if all names are accounted for
    """
    names = ['Jim', 'Pam', 'Ally']
    for name in names:
        Donor(name)
    x = Donor.showallnames()
    assert x == names
    ddb.Donor_Data.data_dict.clear()


def test_showalldonations():
    """
    This will test if it correctly shows all donations
    """
    names = ['Mike', 'Carl', 'Al']
    donations = [1000 / 1, 1000 / 2, 1000 / 3]
    for i, name in enumerate(names):
        Donor(name).donations = 1000 / (i + 1)
    x = Donor.showalldonations()
    assert x == donations
    ddb.Donor_Data.data_dict.clear()


def test_showallcounts():
    """
    This will show if the number of times each person donated is correct
    """
    names = ['Lisa', 'Shara', 'Musan']
    count = [10, 4, 2]
    for i, name in enumerate(names):
        Donor(name).counter = count[i]
    x = Donor.showallcounts()
    assert x == count
    ddb.Donor_Data.data_dict.clear()


def test_showavg():
    """
    This will show if the average is calculated correctly
    """
    names = ['Lisa', 'Shara', 'Musan']
    count = [10, 4, 2]
    for i, name in enumerate(names):
        Donor(name).donations = 1000
        Donor(name).counter = count[i]
    average = [1000 / 10, 1000 / 4, 1000 / 2]
    x = Donor.showavg()
    assert x == average
    assert x != [1000 / 6, 1000 / 3, 1000 / 3]
    ddb.Donor_Data.data_dict.clear()
