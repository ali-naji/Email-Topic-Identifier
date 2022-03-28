import pandas as pd
import numpy as np
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
nltk.download('wordnet')
nltk.download('omw-1.4')


def preprocess(text):
    text_p = re.sub(r'\S+[@./]\S+', '', text)  # get rid of emails / links
    text_p = re.sub(r'\s\S\s', ' ', text_p)
    text_p = word_tokenize(text_p)
    text_p = [t for t in text_p if re.match('[^\d\W]', t)]
    text_p = [t for t in text_p if t.lower() not in ['subject', 'e-mail',
                                                     'address', 'organization', 'lines']]
    text_p = [w.lower() for w in text_p if not w.lower() in stop_words]

    text_p = [lemmatizer.lemmatize(w) for w in text_p]

#     tagged = {w:t for w, t in nltk.pos_tag(text_p)}
#     text_p = [w for w in text_p if tagged[w][0]=='N']

#     text_p = [ps.stem(w) for w in text_p]
    return ' '.join(text_p)
