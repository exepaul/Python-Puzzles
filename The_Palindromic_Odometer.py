odometer_seq = []


def odometer_speed(x):
    x = 100000

    while x < 999996:
        x += 1

        odometer_seq.append(str(x))


odometer_speed(1000)

four_digit_palindromic = []
five_digit_palindromic = []
middle_four_palindromic = []
six_digit_palindromic = []


def four_digit(zz):
    for i in zz:

        if i[2:] == i[2:][::-1] and len(i[2:]) == 4:
            four_digit_palindromic.append(int(i))


four_digit(odometer_seq)


def five_digit(z1):
    for j in z1:
        if j[1:] == j[1:][::-1] and len(j[1:]) == 5:
            five_digit_palindromic.append(int(j))


five_digit(odometer_seq)


def middle_four(z2):
    for k in z2:
        if k[1:][:-1] == k[1:][:-1][::-1] and len(k[1:][:-1]) == 4:
            middle_four_palindromic.append(int(k))


middle_four(odometer_seq)


def six_digit(z3):
    for h in z3:
        if h[:] == h[::-1] and len(h[:]) == 6:
            six_digit_palindromic.append(int(h))


six_digit(odometer_seq)



def checker(list_a,list_b,list_c,list_d):
    for i in list_a:

        i+=1
        if i in list_b:
            i+=1
            if i in list_c:
                i+=1
                if i in list_d:
                    print(i)
    

Final_result=checker(four_digit_palindromic,five_digit_palindromic,middle_four_palindromic,six_digit_palindromic)


print(Final_result)
