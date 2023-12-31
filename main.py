a = 'ABCAAC1C'


def strcounter(a):  # O(N**2)
    for char in a:
        counter = 0
        for sub_char in a:
            if char == sub_char:
                counter += 1
            print(char, counter)


def strcounter1(a): # O(N*M)
    for char in set(a):
        counter = 0
        for sub_char in a:
            if char == sub_char:
                counter += 1
        print(char, counter)


def strcounter2(a):  # O(N)
    syms_counter = {}
    for char in a:
        syms_counter[char] = syms_counter.get(char, 0) + 1
    print(syms_counter)


strcounter2(a)

# asdfkaj;sdfj;asdjkfa;fja a;sldkfja;sdkfj;adfj jk;afksjd;faksd jfa;dfjka;
