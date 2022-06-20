def removeDuplicates(phrase):
    a_dict = {}
    clean_phrase = []
    for word in phrase.split():
        if word in a_dict:
            continue
        else:
            a_dict[word] = 1
            clean_phrase.append(word)

    return " ".join(clean_phrase)

# Client
phrase = 'I am a self-taught programmer looking for a job as a programmer'
print(removeDuplicates(phrase))