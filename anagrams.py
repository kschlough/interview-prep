
def anagrams(word_list):
    anagrams = {}
    for word in word_list:
        anagram_word = ''.join(sorted(word))
        if anagram_word not in anagrams:
            anagrams[anagram_word] = [word]
        else:
            anagrams[anagram_word].append(word)
    
    list_length = 0
    for key in anagrams:
        anagrams[key] = sorted(anagrams[key])
        if len(anagrams[key]) > list_length:
            list_length = len(anagrams[key])
            longest_list = anagrams[key]
   
    print(longest_list[0])


anagrams(["tac", "cat", "pal", "lap", "act"])