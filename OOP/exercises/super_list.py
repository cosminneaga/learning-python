class SuperList:

    def __len__(self, ls):
        count = 0
        for _ in ls:
            count += 1
        print(count)
        return count

    def __append__(self, ls, el):
        l = self.__len__(ls)
        ls[l] = el
        print(ls)
        return ls


sl = SuperList()

# ls = [1, 2, 3, 4]
# sl.__len__(ls)
# sl.__append__(ls, 5)


class SuperList(list):

    def __len__(self):
        return 1000


sl = SuperList()

print(len(sl))
sl.append(5)
print(sl[0])
print(issubclass(SuperList, list))
print(issubclass(SuperList, object))
