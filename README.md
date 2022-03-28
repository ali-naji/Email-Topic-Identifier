## Email Topic Modeling

This project aims to develop an unsupervised email topic identifier model. This model utilizes a doc2vec model to embed textual features of the email's sender, organization of sender, subject and content into a dense representation that then a K-Means clustering model uses to identify it to its closest topic (or cluster of interest)

As part of this repository, we developed an app that receives request in a webpage and returns the topic predictions.

### Installation Instructions

- Clone git repository to your favorite directory

`git clone https://github.com/ali-naji/Email-Topic-Identifier.git`

- Move into project folder

`cd Email-Topic-Identifier`

- create and activate a virtual environment

`python -m venv .`

Windows: `Scripts\activate.bat`

Linux/MAC: `source bin/activate`

- Install project dependencies\*

`pip install -r requirements.txt`

- Run Flask App

`flask run`

- Open a browser window with the link shown in terminal

- Deactivate and delete virtual environment / project

`deactivate`
`cd ..`
`rm -r ../Email-Topic-Identifier`

\* Note: requirements are for the webapp only, research notebook requires other dependencies which are not included for fast installation.
