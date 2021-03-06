import logging

import azure.functions as func
from .OsrmHelper import OsrmHelper

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    name = req.params.get('name') # get param received
    if not name:
        try:
            req_body = req.get_json() # post data received
        except ValueError:
            pass
        else:
            name = req_body.get('name') + ', New to your location are ' + OsrmHelper().getNearByPlaces({'lat_lng':'28,77'}) + ' with in ' + OsrmHelper().getDistances({'lat_lng':'28,77'})

    if name:
        return func.HttpResponse(f"Hello, {name}.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

    
