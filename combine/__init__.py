import logging
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    numbers = requests.get('http://cpgoodleyapp.azurewebsites.net/api/randNum?code=Gn0SvYj1DpuDZ44XKygDOFUewnBbo8qtvUR7a4gtx4mlCaX7RmFayw==')
    letters = requests.get('http://cpgoodleyapp.azurewebsites.net/api/randletters?code=2GaJ3fsreVjYsUi48Vc7Kqc/Ipr78KNYCVmTjknJE8SpQ2VdegeNhA==')
    combine = ''
    
    for i in range(5):
        combine += numbers.text[i]
        combine += letters.text[i]

    return combine
