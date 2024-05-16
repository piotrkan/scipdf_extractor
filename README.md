# scipdf_extractor
This is a code repo for the Scientific PDF entity extractor PoC as a part of the coding challenge. I developed this repo using Windows Machine on VSCode. 



## Live App
You can find the deployed version of this app on https://huggingface.co/spaces/piotrkan/scipdf_extract_app. The deployed application is using the same codebase as present in this repo, with some hacks to facilitate deployment & acquisition of pretrained models from online urls. While the application is live and running and I have manually tested it without breaking, it is possible that the app will break if Hugging face server is down - therefore, if the application is down, you can let me know via github.

If you would like to use the API endpoint from the hosted app, run:
~~~
api_call.py --name enfothelial_dysfunction #example pdf paper from data/
~~~

The application can be also reproduced locally by following this github.

## Setup
To reproduce the repo, run the following
~~~
#clone
git clone https://github.com/piotrkan/scipdf_extractor.git

#create venv, can also create conda but venv is more universal
python -m venv .venv_name

#windows activation
.\.venv_name\Scripts\activate

#linux or mac activation
source ./.venv_name/bin/activate

#once activated, install dependencies
pip install -r requirements.txt

# if you wish to reproduce the notebook
python -m ipykernel install --user --name=venv_name

~~~

## Workflow

To start the gradio app, run:
~~~
python app.py
~~~

Once that is achieved, you should be able to access your application using the following link:  http://127.0.0.1:7861

If you wish to use the app's API,  you can run: 

~~~
api_call.py --name enfothelial_dysfunction #example pdf paper from data/
~~~

This will then create the results 

To examine the exploratory work which I used for decision making, see explore.ipynb

## Repo structure
~~~
ml_challenge/
├── data/          # Data directory; normally would be empty or not present in git 
│                   # as its bad practice to put data in git; for the purpose of this task, will be present
├── results/       # Results directory; created upon running api 
├── flagged/       # errors log, errors flagged by app users; created upon running api 
├── src/           # Source code
│   ├── models.py # nlp related utilities
│   └── data.py   # data-related utilities
│
├── notebooks/
│   └── data.py   # exploratory notebook with benchmarking and pdf parsing solutions  
├── ANSWERS.md     # answers to the questions
└── README.md      # Project README
~~~