import logging
import random
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    all_numbers = '0987654321'
    random_numbers = ''
    
    while len(random_numbers) < 5:
        random_numbers += random.choice(all_numbers)

    return random_numbers
    
