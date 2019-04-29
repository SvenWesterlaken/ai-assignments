import os, re

def getFiles(tweetFileName, outputFileName):
    rf = getFile(tweetFileName)
    of = getFile(outputFileName, 'w+')

    return (rf, of)

def getFile(fileName, mode = 'r'):
    return open(getAbsoluteFilePath(f'../out/{fileName}'), mode)

def getAbsoluteFilePath(path):
    return os.path.join(os.path.dirname(__file__), path)

def removeUrls(text, urls = []):
    if urls:
        return re.compile('|'.join(map(lambda u: re.escape(u['url']), urls))).sub('', text)
    else:
        return text

def generalizeTerm(term):
    filtered = re.sub(r'[^a-zA-Z]', '', term.strip().lower())
    filters = ['rt', 'https']

    if len(filtered) < 2 or re.match(r'.+t\.co\/([a-zA-Z]|[0-9]){0,10}$', term) or filtered in filters:
        return ''
    else:
        return filtered
