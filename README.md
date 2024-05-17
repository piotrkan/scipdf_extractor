# scipdf_extractor
This is a code repo for the Scientific PDF entity extractor PoC as a part of the coding challenge. I developed this repo using Windows Machine on VSCode. 

You are more than welcome to check the [hugging face spaces](https://huggingface.co/spaces/piotrkan/scipdf_extract_app) however the development work is captured in this github repo (on development branch to be precise, but I merged it with main via PR). 

## Live App
You can find the deployed version of this app on https://huggingface.co/spaces/piotrkan/scipdf_extract_app. The deployed application is using the same codebase as present in this repo, with some hacks to facilitate deployment & acquisition of pretrained models from online urls. While the application is live and running and I have manually tested it without breaking, it is possible that the app will break if Hugging face server is down - therefore, if the application is down, you can let me know via github.

If you would like to use the API endpoint from the hosted app, run:
~~~
#enfothelial_dysfunction is an example pdf paper from data/ dir
api_call.py --name enfothelial_dysfunction --live
~~~

The application can be also reproduced locally by following this github, see below. Please note that the app is a **prototype** as it is far from perfect in terms of both performance and deployment.

## Setup
To reproduce the repo locally, run the following
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

To start the gradio app locally, run:
~~~
python app.py
~~~

Once that is achieved, you should be able to access your application using the following link on your machine:  http://127.0.0.1:7861

If you wish to use the app's local API,  you can run: 

~~~
#enfothelial_dysfunction is an example pdf paper from data/ dir
api_call.py --name enfothelial_dysfunction 
~~~

This will then create the results directory where json files are being saved.

To examine the exploratory work which I used for decision making, see explore.ipynb

## Final Comment
Initially I was planning to only focus on the ML part of the project and not work on API, as I am not a software developer. However I realized that there is no clear model, output or data specifications/requirements, and that there is no labelled data (pdfs were provided but not associated entities; of course in real-world scenario we often don't have labels but then we should have domain experts / more information about what is actually needed) - therefore I decided to attempt completing the whole challenge. 

My solution is far from perfect or production-ready software and I am aware of it - but as I needed to complete the entire challenge in a relatively short timeframe, I decided to do more of a 'prototype' app rather than a final product. Some areas for improvement: both preprocessing of the data and post-processing of the output still need to be done; API and the APP should be more standalone, secure and optimized; NER system would also require fine-tuning, however as the time

## Repo structure
~~~
ml_challenge/
├── data/          # Data directory; normally would be empty or not present in git 
│                  # as its bad practice to put data in git; for the purpose of this task, will be present
├── results/       # Results directory; created upon running api_call 
├── flagged/       # errors log, errors flagged by app users; created upon running the gradio app 
├── src/           # Source code
│   ├── models.py  # nlp related utilities
│   └── data.py    # data-related utilities
│
├── notebooks/
│   └── data.py    # exploratory notebook with benchmarking and pdf parsing solutions  
├── ANSWERS.md     # answers to the questions
└── README.md      # Project README
~~~
