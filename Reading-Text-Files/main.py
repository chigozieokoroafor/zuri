# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    text = open(filename, "r")
    
    return text


def count_words(filename):
    text = read_file_content(filename)
    ls = []
    for i in text:
        ls.append(i)
    
    word_joined = []
    for sentence in ls:
        sentence = sentence.split()
        word_joined = word_joined + sentence

    result = {}
    for word in word_joined:
        count = word_joined.count(word)
        if word not in result:
            result[word] = count

    return result