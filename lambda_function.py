import json, boto3, os, base64
import constants as cnst
from boto3.dynamodb.conditions import Key, Attr
import operator
from functools import reduce

def lambda_handler(event, context):
    
    print(event)
    resource = boto3.resource(cnst.DYNAMODB)
    table = resource.Table(cnst.TABLE_NAME_QA)
    
    if cnst.REQUEST_ATTRIBUTE_LIST.sort() != list(event.keys()).sort():
        return "Bad Request"

    response = table.put_item(
        Item= {
            cnst.EMAIL: event[cnst.EMAIL],
            cnst.TIME_STAMP: event[cnst.TIME_STAMP],
            cnst.FIRST_NAME: event[cnst.FIRST_NAME],
            cnst.LAST_NAME:  event[cnst.LAST_NAME],
            cnst.INTEREST: event[cnst.INTEREST],
            cnst.MESSAGE: event[cnst.MESSAGE]
        }
    )
    
    return response["ResponseMetadata"]["HTTPStatusCode"]
    
