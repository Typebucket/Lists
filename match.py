def match(words):
    count = 0
    list = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            count += 1
            list.append(word)
    print("The words having the first and last characters the same are: ", list)
    print("The number of the words that are matched are: ", count)

random_list = ["Dvd", "VdV" , "abc" , "Kwesi", "CDC"]
match(random_list)