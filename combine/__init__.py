import logging
import requests
import azure.functions as func
from azure.cosmos import CosmosClient, PartitionKey

endpoint = "https://cpgoodley.documents.azure.com:443/"
key = "RFeeFcuGD1LyCZFTGPTHrWDSGizsQEpxR48E18Zuv8nJQzML5gtzVK77RfndzyTrJTDfCwjW99kAUfAn29mt9g=="

client = CosmosClient(endpoint, key)

database_name = 'AzureRandomStringDatabase'
database = client.create_database_if_not_exists(id=database_name)

container_name = 'StringContainer'
container = database.create_container_if_not_exists(
    id=container_name,
    partition_key=PartitionKey(path="/id"),
    offer_throughput=400
)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    numbers = requests.get('http://cpgoodleyapp.azurewebsites.net/api/randNum?code=Gn0SvYj1DpuDZ44XKygDOFUewnBbo8qtvUR7a4gtx4mlCaX7RmFayw==')
    letters = requests.get('http://cpgoodleyapp.azurewebsites.net/api/randletters?code=2GaJ3fsreVjYsUi48Vc7Kqc/Ipr78KNYCVmTjknJE8SpQ2VdegeNhA==')
    combine = ''
    
    for i in range(5):
        combine += numbers.text[i]
        combine += letters.text[i]
    randomStringDict = {'id': combine}
    container.create_item(body=randomStringDict)

    return combine
