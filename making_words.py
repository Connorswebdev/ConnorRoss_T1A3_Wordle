import string
from nltk.corpus import words

UPPERCASE = list(string.ascii_uppercase)

word_list = words.words()
op = set()

# Writing every 5 letter word listed in the nltk module
with open("word_list.txt", "w") as word_file:
    count = 0
    for word in word_list:
        if len(word) == 5 and word[0] not in UPPERCASE:
            if word not in op:
                op.add(word)
                count += 1
                word_file.write(word + ", ")
                if count % 10 == 0:
                    word_file.write("\n")