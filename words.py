'''For a list of words, print out each word on a separate line, change word to uppercase.'''


def print_upper_words(words):
    '''Print each word on a sep line, uppercased. '''
    for word in words:
        print(word.upper())

def print_upper_words2(words):
    '''Print each word on sep line, uppercased , if it starts with E or e.'''
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def print_upper_words3(words, must_start_with):
    '''Print each word on a sep line, uppercased, if starts with one of given letters.'''
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break