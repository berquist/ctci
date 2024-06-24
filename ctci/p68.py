# n = 1000
n = 35

def s1(n):
    lst = []
    for a in range(1, 1 + n):
        for b in range(1, 1 + n):
            for c in range(1, 1 + n):
                for d in range(1, 1 + n):
                    if ((a ** 3) + (b ** 3)) == ((c ** 3) + (d ** 3)):
                        t = (a, b, c, d)
                        # print(t)
                        lst.append(t)
    return lst

def s2(n):
    lst = []
    for a in range(1, 1 + n):
        for b in range(1, 1 + n):
            for c in range(1, 1 + n):
                for d in range(1, 1 + n):
                    if ((a ** 3) + (b ** 3)) == ((c ** 3) + (d ** 3)):
                        t = (a, b, c, d)
                        # print(t)
                        lst.append(t)
                        break
    return lst

# def s3(n):
#     l = []
#     for a in range(1, 1 + n):
#         for b in range(1, 1 + n):
#             for c in range(1, 1 + n):
#                 d = int((((a ** 3) + (b ** 3) - (c ** 3)) ** (1 / 3)).real)
#                 if ((a ** 3) + (b ** 3)) == ((c ** 3) + (d ** 3)):
#                     t = (a, b, c, d)
#                     # print(t)
#                     l.append(t)
#     return l

def s4(n):
    # l = []
    count = 0
    rd = dict()
    for c in range(1, 1 + n):
        for d in range(1, 1 + n):
            result = (c ** 3) + (d ** 3)
            if result not in rd:
                rd[result] = []
            rd[result].append((c, d))
    for a in range(1, 1 + n):
        for b in range(1, 1 + n):
            result = (a ** 3) + (b ** 3)
            rl = rd[result]
            for pair in rl:
                count += 1
    # return l
    return count

def s5(n):
    count = 0
    rd = dict()
    for c in range(1, 1 + n):
        for d in range(1, 1 + n):
            result = (c ** 3) + (d ** 3)
            if result not in rd:
                rd[result] = []
            rd[result].append((c, d))
    for (result, rl) in rd.items():
        # for pair1 in rl:
        #     for pair2 in rl:
        #         count += 1
        # for _ in rl:
        #     count += len(rl)
        count += len(rl) ** 2
    return count


if __name__ == '__main__':
    print('1')
    l1 = s1(n)
    print(len(l1))

    print('2')
    l2 = s2(n)
    print(len(l2))

    # print('3')
    # l3 = s3(n)
    # print(len(l3))

    print('4')
    c4 = s4(n)
    print(c4)

    print('5')
    c5 = s5(n)
    print(c5)
