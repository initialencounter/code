def reverse(s: str) -> str:
    word2 = ""
    n1 = 0
    s = s + "A"
    print(s)
    if s[0].islower():
        for i in range(len(s)):
            if i + 1 in range(len(s)):
                if s[i].islower() and s[i + 1].isupper():
                    new = s[0:i + 1]
                    word2 += new
                    s2 = s[i+1:]
                    break
        for i in range(len(s2)):
            if s2[i].isupper():
                new = s2[n1:i]
                n1 = i
                new = new[::-1]
                word2 += new
    else:
        for i in range(len(s)):
            if s[i].isupper():
                new = s[n1:i]
                n1 = i
                new = new[::-1]
                word2 += new
    return word2

def reverse_sentence_boolean(s):
    n1 = 0  # 单词的头部序号
    new2 = ''
    boln = True
    s = s+'A'
    for i in range(len(s)):
        if s[i].isupper()==False and s[i+1].isupper():
            for j in range(i):
                if s[j].isupper():
                    boln=False
            if boln==True:
                new = s[0:i+1]
                n1 = i+1
                new2 = new2 + new
        else:
            if s[i].isupper():
                new = s[n1:i]
                n1 = i
                new=new[::-1]
                new2 = new2 + new
    return new2


def reverse_sentence(s):
    n1 = 0
    new2 = ""
    s = s + "L"
    for i in range(len(s)):
        if s[0].islower() and s[i-1].islower() and s[i].isupper():
            new = s[0:i]
            n1 = i
            new2 += new
            s = s[0].upper()+s[1:]
        else:
            if s[i].isupper():
                new = s[n1:i]
                n1 = i
                new = new[::-1]
                new2 += new

    return new2

s='AbcAdc'
print(reverse_sentence(s))