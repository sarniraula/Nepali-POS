import re


def tokenize_text(sentence):
    tokenized_text = re.sub(r"([\।,?,!])", r" \1 ", sentence).split()
    return tokenized_text


def stem_word(word):
    suffix_list = {'मा', 'सँग', 'को', 'का', 'हरु', 'ले', 'बाट', 'माथि', 'तल','लाई'}
    sanitized_word = word
    word_suffix = ''
    stemmed = False
    for i in range(len(sanitized_word) - 1, -1, -1):
        word_suffix = sanitized_word[i] + word_suffix
        for suffix in suffix_list:
            if word_suffix == suffix:
                stemmed = True
                break
        if stemmed:
            break

    core_word = word[:(len(word) - len(word_suffix))]
    if stemmed:
        return core_word, word_suffix
    else:
        return 0, 0

def stem_text(text):
    for i, word in enumerate(text):
        core, suffix = stem_word(text[i])
        if core != 0:
            text[i] = core
            # print(suffix)
            # text[i+1] = suffix

    return text