# RULES:
#   - given same input returns same output always: [1,2,3] ? each * 2 == [2,4,6]
#   - should not produce any side effects: print(''), external variables ... (no interaction with outside world)


def mul(li):
    n_li = []
    for i in li:
        n_li.append(i * 2)

    return n_li


print(mul([1, 2, 3]))
