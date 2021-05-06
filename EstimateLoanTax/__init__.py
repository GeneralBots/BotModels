import logging

import azure.functions as func
#set STORAGE_BLOB_URL='https://pythonazurestorage12345.blob.core.windows.net'

def main(req: func.HttpRequest) -> func.HttpResponse:
    # https://docs.microsoft.com/pt-br/azure/developer/python/azure-sdk-example-storage-use?tabs=cmd
    logging.info('Python HTTP trigger function processed a request.')

    age = req.params.get('age')
    income = req.params.get('income')
    employeeTime = req.params.get('employeeTime')
    
    # Code here.

    returnedTax = 1;

    if name:
        return func.HttpResponse(returnedTax)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
