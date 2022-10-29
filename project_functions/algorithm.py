import random

# The dictt is in the form of keys as unique words from text file, and value as a list of all words the comes after the
# unique key in the file. The algorithm chooses a word in random as the first word of the sentence and then continues to
# choose a random word from list of the words that follow the unique word(key, value). The function stops and returns a
# complete sentence if the sentence is 10 words or there is a word that ends with a dot.
# The function returns a complete sentence and the length of the sentence(for statistics)


def build_sentence(dictt):
    current_word = random.choice(list(dictt.keys()))
    while dictt[current_word] is None:
        current_word = random.choice(list(dictt.keys()))
    sentence_parts = [current_word]
    while len(sentence_parts) < 10:
        try:
            new_word = random.choice(dictt[current_word])
        except IndexError:
            new_word = random.choice(list(dictt.keys()))
        sentence_parts.append(new_word)
        if new_word.endswith("."):
            break
        current_word = new_word
    sentence_complete = " ".join(sentence_parts)
    return sentence_complete, len(sentence_parts)
