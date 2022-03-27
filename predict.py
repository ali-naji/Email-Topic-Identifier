import pandas as pd
import numpy as np
from gensim.models.doc2vec import Doc2Vec
from preprocessor import preprocess

model = Doc2Vec.load('./model_resources/doc2vec_model')
topic_vectors = np.load('./model_resources/topic_vectors.npy')


def predict(email_data, topn=5):
    """
    Predict the topic of the email.
    :param email_data: The email data.
    :return: The predicted topic.
    """
    email_data = preprocess(email_data)
    # Get the vector of the email.
    email_vector = model.infer_vector(email_data.split())
    # Get the similarity of the email to all the topic vectors.
    most_similar_topic_vector = sorted(
        topic_vectors, key=lambda x: email_vector.dot(x))[0]
    most_similar_topic = model.wv.most_similar(
        positive=most_similar_topic_vector, topn=5)

    return f"Most similar topics were {', '.join([str(i[0]) for i in most_similar_topic]) }"
