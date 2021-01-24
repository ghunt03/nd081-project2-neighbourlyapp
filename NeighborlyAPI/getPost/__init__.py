import logging

import azure.functions as func
import pymongo
import json
from  bson.json_util import dumps
from bson.objectid import ObjectId
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        id = req.params.get("id")
        if not id:
            try:
                req_body = req.get_json()
            except ValueError:
                pass
            else:
                id = req_body.get("id")

        if id:
            url = os.environ['MyDBConnection']
            client = pymongo.MongoClient(url)
            database = client['ghneighborlydb']
            collection = database['posts']
            query = {'_id': ObjectId(id)}
            result = collection.find(query)
            result = dumps(result)
            return func.HttpResponse(result, mimetype="application/json", charset="utf-8")
        else:
            return func.HttpResponse("Missing post id, please provide ID", status_code=400)

    except ConnectionError:
        return func.HttpResponse("Unable to connect to mongodb", status_code=400)

    
