import os
import logging
import azure.functions as func
from azure.storage.blob import BlobClient
from tempfile import NamedTemporaryFile
#from azure.storage.blob import BlockBlobService

#set STORAGE_BLOB_URL='https://pythonazurestorage12345.blob.core.windows.net'


# def get_file(filename):
#     local_file = NamedTemporaryFile()
#     container_name="datalake"
#     BlockBlobService.get_blob_to_stream(container_name, filename, stream=local_file, 
#     max_connections=2)

#     local_file.seek(0)
#     return local_file

# http://localhost:7071/api/EstimateLoanTax?age=23&income=20000&employeeTime=2
def main(req: func.HttpRequest) -> func.HttpResponse:

    #key  = '';

    # Create the client object for the resource identified by the connection string,
    # indicating also the blob container and the name of the specific blob we want.
    #blob_client = BlobClient.from_connection_string(key,  blob_name="sample.csv")

    # Open a local file and upload its contents to Blob Storage
    #with open("./sample.csv", "rb") as data:
    #    blob_client.upload_blob(data)


    # https://docs.microsoft.com/pt-br/azure/developer/python/azure-sdk-example-storage-use?tabs=cmd
    logging.info('Python HTTP trigger function processed a request.')

    age = req.params.get('age')
    income = req.params.get('income')
    employeeTime = req.params.get('employeeTime')
    
    # Code here.

    returnedTax = 1;

    if returnedTax:
        return func.HttpResponse('1')
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
