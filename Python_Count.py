def wordcount (string):
    frequency = dict()
    # Splits the entire sentence into chunks of words
    words = string.split()

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

sentence = input('Enter the sentence: ').lower()
print(wordcount(sentence))
