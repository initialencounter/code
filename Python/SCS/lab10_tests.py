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
    assert f('test_@0.com') == ''
    assert f('test@1.com') == ''
    assert f('_test@0.com') == 'test@0.com'
    assert f('t____est@0.com') == 'test@0.com'


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
