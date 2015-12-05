#!/usr/bin/env python3

'''CPSC 254 - Git exercise'''


def test(got, expected):
    '''Simple test to print what a function returns vs. what it's supposed to
    return.
    '''
    prefix = ' OK ' if got == expected else '  X '
    print('%s got: %s - expected: %s' % (prefix, repr(got), repr(expected)))


def build_dict(filepath):
    '''Given a path to a text file `filepath`, return a dictionary of the word
    (key) and its count/frequency (value), or how often it apears. You need
    store all the words in lowercase, (e.g., 'The' and 'the' are counted as
    the same word).

    Note: For this exercise, you don't need to worry about punctuation.

    Hint: Use str.split() (no argument) to split on all whitespace.
    '''
    # +++your code here+++
    word_freq_dict = {}
    text_file = open(filepath)
    for line in text_file:
        words = line.lower().split()
        for word in words:
            word_freq_dict[word] = word_freq_dict.get(word, 0) + 1
    text_file.close()
    return word_freq_dict


def test_build_dict():
    '''Provide test cases for build_dict function'''
    test(build_dict('small-test-file.txt'), None)



if __name__ == '__main__':
    test_build_dict()
