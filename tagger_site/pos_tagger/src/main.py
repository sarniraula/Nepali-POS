from tnt import TntTagger
import re
import time


def get_user_input():
    raw_text = input("\033[95mEnter your sentence: \033[0m")
    tokenized_text = tokenize_text(raw_text)
    stemmed_text = stem_text(tokenized_text)
    return tokenized_text

def tokenize_text(sentence):
    tokenized_text = re.sub(r"([\।,?])", r" \1 ", sentence).split()
    return tokenized_text


def stem_word(word):
    suffix_list = {'मा', 'सँग', 'ेको', 'ेका', 'िलो', 'हरु', 'ले', 'बाट', 'माथि', 'तल', 'लाई'}
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
        return False


def stem_text(text):
    for i, word in enumerate(text):
        core, suffix = stem_word(word)
        if core != False:
            text.insert(i, core)
            text.insert(i + 1, suffix)

    return text

def tag_text(sentence):
    tokenized_text = tokenize_text(sentence)
    stemmed_text = stem_text(tokenized_text)
    tagger = TntTagger()

    tags = tagger.tag(stemmed_text)

    return tags


def test():
    start_time = time.time()

    nepali_hmm = TntTagger()

    end_time = time.time()
    print('(Time to initialize Nepali Corpus: %s)' % (end_time - start_time))

    while 1:
        # user_input = get_user_input()
        sentence = input("enter sentence: ")
        start_time = time.time()

        # y = nepali_hmm.get_tag_sequence(user_input)
        y = tag_text(sentence)
        end_time = time.time()

        if y == '':
            print("Please input text and retry")
        else:
            print("\nThe best tag sequence is:", y)
            print('(Time to tag this sentence: %s)' % (end_time - start_time))


test()