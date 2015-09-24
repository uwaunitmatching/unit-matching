#
#extends HTML parser to extract data from html
#author : Adrian Sasse
#

from html.parser import HTMLParser
import re
from Unit import Unit

class parse(HTMLParser):
    
    url = ""
    unit = None
    isUnit = False
    heading_tag_open = False
    body_tag_open = False
    
    http_regex = re.compile("^http:", re.IGNORECASE)
    heading_tag_regex = re.compile("^h\d$", re.IGNORECASE)    
    unit_regex = re.compile("[a-z]{3,5}[0-9]{3,5}", re.IGNORECASE)
    
    def re_init(self, stack, visited):
        self.stack = stack
        self.visited = visited
    
    def set_url(self, url):
        self.url = url
           
    def setUnitTrue(self):
        self.isUnit = True
    
    def setUnitFalse(self):
        self.isUnit = False
    
    def count_words(self, data):
        words = data.split()
        return len(words)
    
    def handle_starttag(self, tag, attrs):
        if (tag == "a"):
            for name, value in attrs:
                if name == "href":
                    if value not in self.visited:
                        if self.http_regex.match(value):
                            self.stack.push(value)
                        else:
                            self.stack.push("http:" + value)
        else:
#            print("tag is " + tag)
            if self.heading_tag_regex.match(tag):
                self.heading_tag_open = True
            elif tag == "body":
                self.body_tag_open = True        
            
    def handle_endtag(self, tag):
        if self.heading_tag_regex.match(tag):
                self.heading_tag_open = False 
        elif tag == "body":
            self.body_tag_open = True    
      
    def handle_data(self, data):
        if self.heading_tag_open:
            result = self.unit_regex.search(data)
            if result:
                self.unit = Unit(self.url)
                self.isUnit = True
                self.unit.add_unitcode(result.group(0))
                self.unit.add_title(data)
        if self.body_tag_open and self.isUnit:
            if self.count_words(data) > 10:
                self.unit.add_description(data)
             
            
    
        