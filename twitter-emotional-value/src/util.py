import os, re

def getFiles(tweetFileName, outputFileName):
    rf = open(getAbsoluteFilePath(f'../out/{tweetFileName}'), 'r')

    # Empty output file
    of = open(getAbsoluteFilePath(f'../out/{outputFileName}'), 'w').close()
    of = open(getAbsoluteFilePath(f'../out/{outputFileName}'), 'a+')

    return (rf, of)

def getAbsoluteFilePath(path):
    return os.path.join(os.path.dirname(__file__), path)

def generalizeTerm(term):
    filtered = re.sub(r'[^a-zA-Z]', '', term.strip().lower())

    if len(filtered) < 2 or re.match(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', term):
        return ''
    else:
        return filtered
