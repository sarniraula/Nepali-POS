from django.shortcuts import render
from nltk import word_tokenize

from .src.tag.tnt import get_tnt_tagger
from .src.stemmer import stem

from .src.tnt import TntTagger
from .src import preprocessor

# import requests
# from django.shortcuts import HttpResponse


def index(request):
    return render(request, 'pos_tagger/index.html')


def output(request):
    input_text = request.POST['input_text']

    tag_name = {'N':'Noun', 'P':'Pronoun', 'V':'Verb', 'Y':'Punctuation', 'J':'Adjective',
                'D':'Determiner', 'R':'Adverb', 'C':'Conjunction', 'F':'Foreign word', 'T':'Particle',
                 'Q':'Question Marker', 'U':'Interjection', 'M':'Ordinal',}

    if input_text == '':
        error_message = "You didn't enter the text"
        return render(request, 'pos_tagger/index.html', {'error_message': error_message, })
    else:
        print(type(input_text))
        tagged_text = max_entropy(input_text)   # similar to above

        formatted_tag = list()
        for word, tag in tagged_text:
            simplified_tag = tag_name[tag[0]]
            formatted_tag.append((word, simplified_tag, tag))

        context = {
            'tagged_text': formatted_tag,
        }
        return render(request, 'pos_tagger/output.html', context)


# move this function to src.tnt
def tnt(input_text):
    tnt_tagger = get_tnt_tagger()
    tagged_text = tnt_tagger.tag(word_tokenize(input_text))
    for i, (word, tag) in enumerate(tagged_text):
        if tag == 'Unk':
            root_word = stem(word)
            new_tag = tnt_tagger.tag(root_word)
            tagged_text[i] = new_tag

    return tagged_text


# move this function to src.max_entropy
def max_entropy(input_text):
    tagger = TntTagger()
    tokenized_text = preprocessor.tokenize_text(input_text)
    stemmed_text = preprocessor.stem_text(tokenized_text)
    print(stemmed_text)
    tagged_text = tagger.tag(tokenized_text)

    return tagged_text
