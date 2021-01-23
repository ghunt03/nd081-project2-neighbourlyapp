import logging

import azure.functions as func
import pymongo
import json
from  bson.json_util import dumps
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        post_id = req.params.get("id")
        if not post_id:
            try:
                req_body = req.get_json()
            except ValueError:
                pass
            else:
                post_id = req_body.get("id")

        if post_id:
            url = os.environ['MyDBConnection']
            client = pymongo.MongoClient(url)
            database = client['ghneighborlydb']
            collection = database['posts']
            result = collection.find({"_id": post_id})
            result = dumps(result)
            return func.HttpResponse(result, mimetype="application/json", charset="utf-8")
        else:
            return func.HttpResponse("Missing post id, please provide ID", status_code=400)

    except ConnectionError:
        return func.HttpResponse("Unable to connect to mongodb", status_code=400)

    
