import nltk, pickle

from ..get_data import get_tags


def get_tnt_tagger():
    saved_data = 'nepali_pos_tagger_tnt.pickle'
    try:
        tnt_tagger = nltk.data.load(saved_data)
    except Exception:
        tnt_tagger = nltk.tag.tnt.TnT()
        training_data = get_tags()
        tnt_tagger.train(training_data)
        f = open(saved_data, 'wb')
        pickle.dump(tnt_tagger, f)
        f.close()

    return tnt_tagger
