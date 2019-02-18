import requests
import json


BASE_URL = "http://35.202.191.171"
TABLE_NAME = "users"

def sending_request(url):

    print "Sending request to URL: {0}".format(url)

    return requests.get(url)


def getEqualTo(selectedID):

    url = "{0}/{1}/id/{2}".format(BASE_URL,TABLE_NAME,selectedID)

    res = sending_request(url)

    print res.text


def getContainParam(param_name):
    url = "{0}/{1}/name/Contains/{2}".format(BASE_URL,TABLE_NAME,param_name)

    res = sending_request(url)

    print "Result return from server"
    json_obj = json.loads(res.text)

    print "Got {0} results from server".format(len(json_obj))


def getLessThan(id):
    url = "{0}/{1}/id/LT/{2}".format(BASE_URL, TABLE_NAME, id)

    res = sending_request(url)

    print "Result return from server"
    json_obj = json.loads(res.text)

    print "Got {0} results from server".format(len(json_obj))


if __name__ == "__main__":
    getEqualTo(1234)
    print "------------------------"
    getContainParam("er13")
    print "------------------------"
    getLessThan(250)
