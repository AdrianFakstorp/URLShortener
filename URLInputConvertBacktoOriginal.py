import json
import sys
from config import json_path as JSONPath 

URLInput = "asko.tt/google"

# def sysArgURLInput():
#     URLInput = sys.argv[1]
#     return URLInput

def JSONTableLoad():
    with open(JSONPath) as f:
        URLJSON = json.load(f)
    return URLJSON

def ShortenedURLOverlapCheck(URLInput, URLJSON):
    URLMatches = 0
    for pairs in URLJSON["URLs"]:
        if URLInput == pairs["Shortened URL"]:
            URLMatches += 1
    if URLMatches > 1:
        print("The Shortened URL {} already exists. Please try again.".format(URLInput))
        exit()
    else:
        return None

def InputURLJSONMatch(URLInput, URLJSON):
    URLOutput = None
    for pairs in URLJSON["URLs"]:
        print(pairs)
        if URLInput == pairs["Shortened URL"]:
            URLOutput = pairs["Original URL"]
            print("Your returned URL is {}.".format(URLOutput))
        else:
            print("Your URL {} was not found. Please try again.".format(URLInput))
            exit()
    if URLOutput != None:
        return URLOutput
    else:
        print("There was an error.")
        exit()
    
URLJSON = JSONTableLoad()
ShortenedURLOverlapCheck (URLInput, URLJSON)
InputURLJSONMatch(URLInput, URLJSON)


