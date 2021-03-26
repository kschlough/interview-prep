def checkMagazine(magazine, note):
    # below is the speedier version learned from discussions - using Counter
    # from collections import Counter
    # if (Counter(note) - Counter(magazine)) == {}:
    #     print("Yes")
    # else:
    #     print("No")
        
    note_dict = {}
    for word in note:
        if word in note_dict:
            note_dict[word] += 1
        else:
            note_dict[word] = 1
            
    magazine_dict = {}
    for word in magazine:
        if word in magazine_dict:
            magazine_dict[word] += 1
        else:
            magazine_dict[word] = 1
            
    result = {}
    for key, value in note_dict.items():
        if key not in magazine_dict:
            result[key] = value
        elif note_dict[key] > magazine_dict[key]:
            result[key] = (note_dict[key] - magazine_dict[key])
            
    if result == {}:
        print("Yes")
    else:
        print("No")


# pseudocode
# map every word in note to a dictionary with val false
# iterate through words in magazine and if word in note, change val for the word key to true
# if any false in dictionary, return false otherwise return true