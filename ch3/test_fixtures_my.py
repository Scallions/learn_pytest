import pytest


@pytest.fixture()
def version():
    return '1.0'


@pytest.fixture()
def dic():
    return {
        'version': '1.0',
        'name': 'pytest'
    }

@pytest.fixture()
def list_():
    return list(range(10))

@pytest.fixture()
def tuple_():
    return (1,2)

@pytest.fixture(scope='module')
def list1():
    print('before')
    yield list(range(10))
    print('after')


def test_list(list1):
    assert list1[-1] == 9

def test_version(version):
    assert version == '1.0'

def test_dic(dic):
    assert dic['name'] == 'pytest'



def test_list2(list1):
    assert list1[0] == 0

def test_tuple(tuple_):
    assert tuple_[1] == 2