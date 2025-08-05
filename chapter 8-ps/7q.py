def rem(l, word):
    for item in l:
        l.remove(word)
        return l
l = ["Har", "FAB", "gou"]

print(rem(l, "gou"))