# -*- coding: utf-8 -*-
from language_detector.languages import LANGUAGES
"""This is the entry point of the program."""

def detect_language(text, languages=LANGUAGES):
    language_word_count = {}
    """Returns the detected language of given text."""
    text_list = text.split()
    for word in text_list:
        for language in languages:
            if word in language['common_words']:
                language_word_count[language['name']] = language_word_count.get(language['name'], 1) + 1
    most_words = None
    word_count = None
    for language, count in language_word_count.items():
        if most_words == None:
            most_words = language
            word_count = count
        elif count > word_count:
            most_words = language
            word_count = count
    return most_words