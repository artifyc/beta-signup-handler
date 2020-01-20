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
            cnst.EMAIL: {
                'S': event[cnst.EMAIL]
            },
            cnst.TIME_STAMP: {
                'S': event[cnst.TIME_STAMP]
            },
            cnst.FIRST_NAME: {
                'S': event[cnst.FIRST_NAME]
            },
            cnst.LAST_NAME: {
                'S': event[cnst.LAST_NAME]
            },
            cnst.INTEREST: {
                'S': event[cnst.INTEREST]
            },
            cnst.MESSAGE: {
                'S': event[cnst.MESSAGE]
            }
        }
    )
    
    return response
    
