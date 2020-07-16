import logging
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    numbers = requests.get('https://cpgoodleyapp.azurewebsites.net/api/randnum?code=Gn0SvYj1DpuDZ44XKygDOFUewnBbo8qtvUR7a4gtx4mlCaX7RmFayw==')
    letters = requests.get('https://cpgoodleyapp.azurewebsites.net/api/randletters?code=2GaJ3fsreVjYsUi48Vc7Kqc/Ipr78KNYCVmTjknJE8SpQ2VdegeNhA==')
    combine = ''

    for i in range(len(numbers)):
        combine += numbers[i]
        combine += letters[i]

    return combine
