import urllib2
import urllib
import json

from BeautifulSoup import BeautifulSoup

# Returns translated text scraped

def fromHtml(self, text, languageFrom, languageTo):

    # List of keys and value to represent language codes

    langCode = { "arabic":"ar", "bulgarian":"bg", "chinese":"zh-CN",
                 "croatian":"hr", "czech":"cs", "danish":"da", "dutch":"nl",
                 "english":"en", "finnish":"fi", "french":"fr", "german":"de",
                 "greek":"el", "hindi":"hi", "italian":"it", "japanese":"ja",
                 "korean":"ko", "norwegian":"no", "polish":"pl", "portugese":"pt",
                 "romanian":"ro", "russian":"ru", "spanish":"es", "swedish":"sv" }

    # setting user agent

    urllib.FancyURLopener.version = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"
    
    #Encode the parameters we're going to send to the Google servers.

    try:
        
        postParameters = urllib.urlencode({"langpair":"%s|%s" %(langCode[languageFrom.lower()],langCode[languageTo.lower()]), "text":text,"ie":"UTF8", "oe":"UTF8"})

    except KeyError, error:

        print "Currently we do not support %s" %(error.args[0])
        return

    #Send the request with 'postParameters and save to the 'page' variable written below.

    page = urllib.urlopen("http://translate.google.com/translate_t", postParameters)

    #content now contains the HTML source code of the website.

    content = page.read()

    # close connection

    page.close()

    #content now contains the HTML source code of the website.

    content = page.read()

    htmlSource = BeautifulSoup(content)

    #Google creates a span with title the same as the text you wanted to translate.
    #So let's find a 'span' that has as a Title the 'text' we passed to this method.

    translation = htmlSource.find('span', title=text )

    #the renderContents() method returns the body that is inside of the span we found.

    return translation.renderContents()


