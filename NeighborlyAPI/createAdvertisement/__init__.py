import logging

import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import os


def main(req: func.HttpRequest) -> func.HttpResponse:
    request = req.get_json()
    if request:
        try:
            # add your connection string here
            url = os.environ["MyDBConnection"]
            client = pymongo.MongoClient(url)
            database = client["ghneighborlydb"]
            collection = database["advertisements"]

            # replace the insert_one variable with what you think should be in the bracket
            rec_id1 = collection.insert_one(eval(request))

            # we are returnign the request body so you can take a look at the results
            return func.HttpResponse(req.get_body())

        except ValueError:
            return func.HttpResponse('Database connection error.', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass the correct JSON format in the body of the request object",
            status_code=400
        )