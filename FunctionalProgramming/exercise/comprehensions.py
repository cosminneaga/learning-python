ls = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list(set([letter for letter in ls if ls.count(letter) > 1]))
print(duplicates)
