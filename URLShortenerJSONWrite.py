import json
from config import json_path as JSONPath

URLInput = "asdf.com"
URLShort = "https://www.asko.tt/asdfcom1"  

def URLPairingAndTurnToDictionary(OriginalURL, ShortenedURL):
    PairedURL = {"Original URL" : str(OriginalURL), "Shortened URL": str(ShortenedURL)}
    return PairedURL

def JSONTableLoad():
    with open(JSONPath) as f:
        URLJSON = json.load(f)
    return URLJSON

def TableAppendDict(URLJSON, PairedURL):
    AppendedDict = URLJSON
    AppendedDict["URLs"].append(PairedURL)
    return AppendedDict

def JSONTableAppend(AppendedDict):
    with open("URLTableJSON.json","w") as f:
        json.dump(AppendedDict, f)
    print("Writing \n{} \nto {}".format(str(PairedURL), JSONPath))

def ShortenedURLOverlapCheck(URLShort, URLJSON):
    URLMatches = 0
    for pairs in URLJSON["URLs"]:
        if URLShort == pairs["Shortened URL"]:
            URLMatches += 1
    if URLMatches > 0:
        print("The Shortened URL {} already exists. Please try again.".format(URLShort))
        exit()
    else:
        return None


PairedURL = URLPairingAndTurnToDictionary(URLInput, URLShort)
URLJSON = JSONTableLoad()
ShortenedURLOverlapCheck(URLShort,URLJSON)
AppendedDict = TableAppendDict(URLJSON,PairedURL)
JSONTableAppend(AppendedDict)

