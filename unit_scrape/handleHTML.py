#
#extends HTML parser to extract data from html
#author : Adrian Sasse
#

from html.parser import HTMLParser
import re

class parse(HTMLParser):
    
    isUnit = False
    record_titles = False
    record_desc = False
    
    def re_init(self, stack, visited):
        self.stack = stack
        self.visited = visited
    
    def set_unit(self, unit):
        self.unit = unit
           
    def setUnitTrue(self):
        self.isUnit = True
    
    def setUnitFalse(self):
        self.isUnit = False
    
    def count_words(self, data):
        words = data.split()
        return len(words)
    
    def handle_starttag(self, tag, attrs):
        a = re.compile("^http:", re.IGNORECASE)
        b = re.compile("^h\d$", re.IGNORECASE)
        if (tag == "a"):
            for name, value in attrs:
                if name == "href":
                    if value not in self.visited:
                        if a.match(value):
                            self.stack.push(value)
                        else: 
                            self.stack.push("http:" + value)
        if (b.match(tag) and self.isUnit):
            #print("found " + tag + " tag" )
            self.record_titles = True
        if (tag == "body"):
            self.record_desc = True
            
    def handle_endtag(self, tag):
        b = re.compile("^h\d$", re.IGNORECASE)
        if (b.match(tag) and self.isUnit):
            self.record_titles = False
        if (tag == "body"):
            self.record_desc = False
        
      
    def handle_data(self, data):
        c = re.compile(self.unit.unitcode, re.IGNORECASE)
        if (self.record_titles):
            if (c.search(data)):
                self.unit.addTitle(data)
        if (self.record_desc and self.count_words(data) > 10):
            self.unit.addDescription(data) 
            
    
        