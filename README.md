# LeadList

This is a tool that automatically generates a list of potential leads for a salesforce based on their previous contacting behavior using Machine Learning.

## Setup

Start by running the following command:

    pip install -r requirements.txt

Download NLTK Stopwords from: [nltk](http://www.nltk.org/index.html) package. 

Run a Python interpreter and type the following:

    import nltk
    nltk.download('stopwords')


**PS:** We're also experimenting with a neural net (in TensorFlow) in the nn.py file.


# Using

Create a CSV file of company name and description. I have used FullContact API to retrieve company descriptions.

## train_algorithm

This script trains the algorithms on  input data. It expects two excel sheets named **qualified** and **disqualified** in the input. These sheets need to contain two columns:

- URL
- Description


Run the script using:

    python run.py

It'll dump three files into the qualify_leads
- algorithm
- vectorizer
- tfidf_vectorizer

You're now ready to start classifying your sales leads!

## Qualify_leads

This is the script that actually predicts the quality of the leads. Add an excel sheet named **data** in the input folder in qualify_leads. Use the same format as the example file that's already there.

Run the script:

    python run.py

It'll output an excel sheet with a column named **Prediction**, where 1 equals *qualified* and 0 equals *disqualified*:

##Todo:
1. Test more algorithms
2. Add functionality for other company data like team_size, location etc.
