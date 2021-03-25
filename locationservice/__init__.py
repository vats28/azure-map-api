import json
import logging

import azure.functions as func
from requests.models import Response
from .HeremapHelper import HeremapHelper

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    req_body = req.get_json()
    type = req_body["type"] # req.params.get('name') # get param received
    coordinates = req_body["coordinates"] # get param received
    response = {
        "success": "0",
        "msg":"some error occured"
    }

    if not type:
            return func.HttpResponse(f"No action mentioned!!!!")
    else:
        if(type == "geocode"):
             response = HeremapHelper().getNearByPlaces(coordinates)
        else:
             response = HeremapHelper().getDistances(coordinates)
    
    return func.HttpResponse(
                str(response),
                status_code=200,
                mimetype='application/json'
            )
