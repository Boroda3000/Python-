def single_root_words (root_word, *other_words):
    same_words = []
    for i in other_words:
        if (i.upper()).count(root_word.upper()) == 1:
            same_words.append(i)
    for j in other_words:
        if (root_word.upper()).count(j.upper()) == 1:
            same_words.append(j)
    return same_words



result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)