## Email Topic Modeling

This project aims to develop an unsupervised email topic identifier model. This model utilizes a doc2vec model to embed textual features of the email's sender, organization of sender, subject and content into a dense representation that then a K-Means clustering model uses to identify it to its closest topic (or cluster of interest)

As part of this repository, we developed an app that receives request in a webpage and returns the topic predictions.

### Installation Instructions

Clone git repository to your favorite directory

`git clone https://github.com/ali-naji/Email-Topic-Identifier.git`

Move into project folder
`cd Email-Topic-Identifier`

Install project dependencies
`pip install .`

Run Flask App
`flask run`

Open a browser window with the link shown in terminal
