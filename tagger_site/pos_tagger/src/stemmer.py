def stem(word):
    suffix_list = {'मा', 'सँग', 'ेको', 'ेका', 'िलो', 'हरु', 'ले', 'बाट', 'माथि', 'तल'}
    sanitized_word = sanitize(word)
    word_suffix = ''
    stemmed = False
    for i in range(len(sanitized_word)-1, -1, -1):
        word_suffix = sanitized_word[i] + word_suffix
        for suffix in suffix_list:
            if word_suffix == suffix:
                stemmed = True
                break
        if stemmed:
            break

    core_word = word[:(len(word)-len(word_suffix))]
    return core_word, word_suffix


def sanitize(word):
    map_rule = {
        'ि' : 'इ',
        'ी' : 'ई',
        # 'े' : '   ए',
    }

    sanitized_word = list(word)
    for i in range(0, len(word)):
        for key, value in map_rule.items():
            if sanitized_word[i] == key:
                sanitized_word[i] = value

    return sanitized_word

# word = input()
# print(stem(word))

# i = 0
# while 1:
#     i += 1
#     print('pass', i)
#     (core, suffix) = stem(word)
#     if suffix == '':
#         break
#     print(core, ' ', suffix)
#     word = core
