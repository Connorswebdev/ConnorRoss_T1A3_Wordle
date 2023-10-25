import string
from nltk.corpus import words

UPPERCASE = list(string.ascii_uppercase)

nltk_word_list = words.words()
filter_words= [word for word in nltk_word_list if len(word) in [5, 7]]

with open("word_list.txt", "w") as file:
    for word in filter_words:
        file.write(f" {word}\n")
# Writing every 5 letter word listed in the nltk module
# with open("word_list.txt", "w") as word_file:
#     count = 0
#     for word in word_list:
#         if len(word) == 5 and word[0] not in UPPERCASE:
#             if word not in op:
#                 op.add(word)
#                 count += 1
#                 word_file.write(word + ", ")
#                 if count % 10 == 0:
#                     word_file.write("\n")


#Creating a secondary script for the hard mode to generate every 5 and 7 letter words

# with open("word_list.txt", "w") as word_file:
#     count = 0
#     for word in word_list:
#         if len(word) == 5 and 7 and word[0] not in UPPERCASE:
#             if word not in op:
#                 op.add(word)
#                 count += 1
#                 word_file.write(word + ", ")
#                 if count % 10 == 0:
#                     word_file.write("\n")


