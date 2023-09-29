"""
LAB RESTRICTIONS, PLEASE READ:
Do not add any imports, the ones that you need will be given to you.
Do not use try-except statements, you should be able to anticipate
or prevent any errors from happening at all!
"""

import re
"""
    Given a string <s>, return the email that exists in the string.

    Preconditions:
        <s> contains at most 1 email, or none at all.

    If <s> does not contain an email, return the empty string.

    Email definition:
        An email address is defined as 'name@domain.com' or 'name@domain.ca'
        with the following specifications:

            name: the name is an alphanumeric string that is less than or
                  equal to 12 characters. Additional characters allowed are
                  dash (-), period (.) and underscore (_). But the email
                  cannot start or end with these additional characters.
                  The name must also be at least 1 character long.
                  Example names:
                                a
                                ab
                                a_b
                                A__B..C--D
                                1nt3r3st.1ng

            domain: the domain is strictly numerical, and the number must be
                    divisible by 5. the length of the domain is unrestricted.
                    Example domains:
                                984125
                                0

            ending: the email must end with a (.com) or (.ca) (case sensitive)

    Note: you must not use any loops (for, while) here.
          We want you to just use the re library for this function.

    >>> find_email('12345a_test_email@165265365.com!')
    'a_test_email@165265365.com'
    """

def find_email(s: str) -> str:
    string = ''
    # name [a-zA-Z][0-9a-zA-Z_]*[^_] [a-zA-Z]以英文字母开头，[0-9a-zA-Z_]匹配0或多个数字或英文以及下划线，[^_]结尾不能是下划线_
    # domain @[0-9]+ 匹配以@开头的0或多个数字
    # end \.com|\.ca 匹配以.com或.ca
    # c = re.findall("(\w[\w_.-]{0,10}[^-_.@]@\d+\.(com|ca))", s)

    c = re.findall("\w[\w_.-]{0,10}[^-_.@]@\d+\.com|\w[\w_.-]{0,10}[^-_.@]@\d+\.ca", s)


    #test2、test4与test18发生冲突，即name长度为1时，无法匹配，加一个判断匹配name为1的email
    b = re.findall("[^-_.@]@\d+\.com|\w@\d+\.ca",s)
    if len(c)==0 and len(b)!=0:
        c=b
    # print(c)
    #c为list，若c为空list，后面return c[0]会报错，这里提前返回退出函数

    if len(c)==0:
        return string
    # 匹配domain的数字，若domain不能被5整除，则返回''
    num = re.findall("@[0-9]+",s)
    # print(c,num)
    if len(num)==0:
        return string
    if int(num[0][1:])%5!=0 or len(c)==0:
        return string
    return c[0]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
