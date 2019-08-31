import urllib.request
import urllib.parse

# Python urllib module allows us to access URL data 
# programmatically.

try:
    test = urllib.request.urlopen(r'https://www.google.com')

    testfile = open('testfile.txt', 'w')
    testfile.write(str(test.read()))
    testfile.close()

except Exception as e:
    print(str(e))

#_______________________________________________________________________
# This server doesn’t allow programmatic access to the 
# website data because it’s meant for browsers that can 
# parse HTML data. Usually we can overcome this error by 
# sending User-Agent header in request

# We are creating request headers using dictionary 
# and then sending it in the request.
try:
    url = 'https://www.google.com/search?q=ada'

    headers = {}
    headers['User-Agent'] = r"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41"
    req = urllib.request.Request(url, headers = headers)
    resp =  urllib.request.urlopen(req) 
    respData = resp.read()

    
    with open('withHeaders.html', 'w') as saveFile:
        saveFile.write(str(respData))

    # We can get response headers by calling info() 
    # function on response object. 
    # This returns a dictionary. 
    # We can also extract specific header data from 
    # response. Ex : "content-type"
    print(resp.info()["content-type"])

except Exception as e :
    print(str(e))



# List of 'User-Agent' headers

# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent

# Chrome UA string
# Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36

# Opera UA string
# Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41

# Internet Explorer UA string
# Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)