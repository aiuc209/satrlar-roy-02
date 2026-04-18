import pytest

def repeat_words(lines):
    result = []
    for line in lines:
        words = line.split()
        new_line = ' '.join([word * 2 for word in words])
        result.append(new_line)
    return result

def test_repeat_words():
    lines = ["Hello world", "This is a test"]
    expected = ["HelloHello worldworld", "ThisThis isis aatest"]
    assert repeat_words(lines) == expected

def test_repeat_words_empty():
    lines = []
    expected = []
    assert repeat_words(lines) == expected

def test_repeat_words_single_line():
    lines = ["Hello world"]
    expected = ["HelloHello worldworld"]
    assert repeat_words(lines) == expected

def test_repeat_words_single_word():
    lines = ["Hello"]
    expected = ["HelloHello"]
    assert repeat_words(lines) == expected
