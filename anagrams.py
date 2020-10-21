
def anagrams(word_list):
    anagrams = {}
    for word in word_list:
        anagram_word = ''.join(sorted(word))
        if anagram_word not in anagrams:
            anagrams[anagram_word] = [word]
        else:
            anagrams[anagram_word].append(word)
    for key in anagrams:
        

    print(anagrams)


anagrams(["tac", "cat", "pal", "lap", "act"])