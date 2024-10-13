def all_variants(text):

    for i in range(len(text) + 1):
        for j in range(i, len(text) + 1):
            if i != j:
                yield text[i:j]



a = all_variants("abc")
for i in a:
    print(i)