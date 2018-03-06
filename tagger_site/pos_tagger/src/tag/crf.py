import nltk, pickle

from ..get_data import get_tags


def get_crf_tagger():
    saved_data = 'nepali_pos_tagger_crf.pickle'
    try:
        crf_tagger = nltk.data.load(saved_data)
    except Exception:
        crf_tagger = nltk.tag.crf.CRFTagger()
        training_data = get_tags()
        print(training_data[0])
        crf_tagger.train(training_data)
        f = open(saved_data, 'wb')
        pickle.dump(crf_tagger, f)
        f.close()

    return crf_tagger
