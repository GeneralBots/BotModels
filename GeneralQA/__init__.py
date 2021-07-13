import logging
import azure.functions as func
import os
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
from allennlp.predictors.predictor import Predictor
import json

# https://ai.google.com/research/NaturalQuestions

predictor = None

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('General Bots QA.')

    content = req.form.get('content')
    question = req.params.get('question')
                                     
    global predictor
    if predictor is None:
        predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/transformer-qa-2020-10-03.tar.gz")
    
    answer = predictor.predict(
        passage=content,
        question=question
    )['best_span_str']
       

    if answer:
        return func.HttpResponse(answer)
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
    )
