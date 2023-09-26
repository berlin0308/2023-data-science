"""C-3
Two words are a “reverse pair” if each is the reverse of the other. Write a function that finds all 
the reverse pairs in the word list using the following template

def find_reverse_pair(word_list): 
  reverse_pair_list = [] 
  #TODO 
  return reverse_pair_list
"""

def find_reverse_pair(word_list): 
    reverse_pair_list = [] 
    for word1 in word_list:
        reversed_word1 = word1[::-1]

        for word2 in word_list:
            if word1 != word2 and word2 == reversed_word1:
                reverse_pair_list.append((word1, word2))

    return reverse_pair_list

if __name__ == '__main__':
    word_list = ["hello", "olleh", "world", "dlrow", "python", "nohtyp"]
    reverse_pairs = find_reverse_pair(word_list)
    print(reverse_pairs)