"""
LAB RESTRICTIONS, PLEASE READ:
Do not add any imports, the ones that you need will be given to you.
Do not use try-except statements, you should be able to anticipate
or prevent any errors from happening at all!
"""

from typing import Callable

from lab10 import find_email


def test_template(f: Callable) -> None:
    """
    This is a template for the tests you will write for this lab.

    Implement your tests as top level functions that begin with the
    word 'test' and take in a callable function <f>.

    You are free to do some amount of work to construct your tests cases
    within the function but your function must end with an assert statement
    of the form <assert f('string') == 'some string'>.

    An assert statement means that you expect the boolean expression following
    to evaluate to True. With regards to this lab, it means that you expect the
    function call on the left to return the string on the right. If this does
    not happen, then the assert statement will raise an AssertionError, which
    we will catch and take it to mean that this particular test failed.

    IMPORTANT:
    The goal of this part of the lab is to write a set of tests such that that
    ALL of them pass for any correct implementation, but AT LEAST ONE of them
    fail for any incorrect implementation (of "find_email").
    """
    assert f('test@0.com') == 'test@0.com'


def test_1(f: Callable) -> None:
    """
    """
    assert f('test') == ''


def test_1(f: Callable) -> None:
    """
    """
    assert f('') == ''


def test_2(f: Callable) -> None:
    """
    """
    assert f('_@5.com') == ''


def test_3(f: Callable) -> None:
    """
    """
    assert f('@5.com') == ''


def test_4(f: Callable) -> None:
    """
    """
    assert f('jim_@125.com') == ''


def test_5(f: Callable) -> None:
    """
    """
    assert f('jim@3.com') == ''


def test_6(f: Callable) -> None:
    """
    """
    assert f('jim@5.COM') == ''


def test_7(f: Callable) -> None:
    """
    """
    assert f('jim@5.com') == 'jim@5.com'


def test_8(f: Callable) -> None:
    """
    """
    assert f('jim@5.ca') == 'jim@5.ca'


def test_9(f: Callable) -> None:
    """
    """
    assert f('a_b@5.ca') == 'a_b@5.ca'


def test_10(f: Callable) -> None:
    """
    """
    assert f('a_b@a0.ca') == ''


def test_11(f: Callable) -> None:
    """
    """
    assert f('a_b@333333330.ca') == 'a_b@333333330.ca'


def test_12(f: Callable) -> None:
    """
    """
    assert f('a_b333333330.ca') == ''


def test_13(f: Callable) -> None:
    """
    """
    assert f('A__B..C--D@115.ca') == 'A__B..C--D@115.ca'


def test_14(f: Callable) -> None:
    """
    """
    assert f('1nt3r3st.1ng@115.ca') == '1nt3r3st.1ng@115.ca'


def test_15(f: Callable) -> None:
    """
    """
    assert f('aaaaaaaaaaaaa@115.ca') == 'aaaaaaaaaaaa@115.ca'


def test_16(f: Callable) -> None:
    """
    """
    assert f('aaaaaaaaaaaaa_a@115.ca') == 'aaaaaaaaaa_a@115.ca'


def test_17(f: Callable) -> None:
    """
    """
    assert f('aaaaaaaaa_aaaa_a@115.ca') == 'aaaaa_aaaa_a@115.ca'


def test_18(f: Callable) -> None:
    """
    """
    assert f('a@5.ca') == 'a@5.ca'


def test_19(f: Callable) -> None:
    """
    """
    assert f('11@5=ca') == ''


def test_20(f: Callable) -> None:
    """
    """
    assert f('11@@5.ca') == ''


def test_21(f: Callable) -> None:
    """
    """
    assert f('a..........a@0.ca') == 'a..........a@0.ca'

    
def run_tests() -> tuple:
    """
    Runs all tests in this file if run as main.

    Do not modify this function. You can leave it in for the final submission.
    """
    passed, failed = [], []
    for name, func in globals().items():
        if name.startswith('test') and callable(func):
            try:
                func(find_email)
            except AssertionError:
                failed.append(func.__name__)
                continue
            passed.append(func.__name__)
    return passed, failed


if __name__ == '__main__':
    np, nf = run_tests()
    print(f'Total {len(np) + len(nf)} tests detected. '
          f'{len(np)} passed and {len(nf)} failed.')
    print('Tests passed:')
    x = [print(p) for p in np]
    del x
    print('\nTests failed:')
    x = [print(f) for f in nf]
    del x
