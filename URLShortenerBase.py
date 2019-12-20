import hashlib
import sys

baseSite = "https://www.asko.tt"

# def getURLInput():
#     URLInput = input("Please enter the URL you want to shorten ")
#     URLInput = str(URLInput)
#     return URLInput

def sysArgURLInput():
    URLInput = sys.argv[1]
    return URLInput

def printURLInput(URLInput):
    URLInput = str(URLInput)
    print("\nThis is the URL you input: %s" % (URLInput))

def convertURL(URLInput):
    URLInput = str(URLInput)
    ConvertedURLInput = hashlib.md5(URLInput.encode())
    ConvertedURLInput = ConvertedURLInput.hexdigest()
    return ConvertedURLInput

def shortenURL(baseSite, ConvertedURLInput):
    baseSite = str(baseSite)
    shortenedURL = "{0}/{1}".format(baseSite, ConvertedURLInput)
    return shortenedURL

#Function Calls
URLInput = sysArgURLInput()
printURLInput(URLInput)
ConvertedURLInput = convertURL(URLInput)
shortenedURL = shortenURL(baseSite, ConvertedURLInput)

print(shortenedURL)
