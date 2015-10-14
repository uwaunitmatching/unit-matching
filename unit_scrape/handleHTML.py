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
    title_tag_open = False
    script_tag_open = False
    
    temp_title = None
        
    http_regex = re.compile("^http://", re.IGNORECASE)
    slash_regex = re.compile("^/", re.IGNORECASE)
    double_slash_regex = re.compile("^//", re.IGNORECASE)
    heading_tag_regex = re.compile("^h\d$", re.IGNORECASE)    
    unit_regex = re.compile("[a-z]{2,5}[0-9]{3,5}", re.IGNORECASE)
    
    def re_init(self, stack, visited, in_stack, db):
        self.stack = stack
        self.visited = visited
        self.in_stack = in_stack
        self.unit = Unit(self.url, db)

    
    def set_url(self, url):
        self.url = url
        self.unit.set_url(url)
           
    def setUnitTrue(self):
        self.isUnit = True
    
    def setUnitFalse(self):
        self.isUnit = False
    
    def count_words(self, data):
        words = data.split()
        return len(words)
    
    def get_domain(self):
        return self.url.split('/')[2]
    
    def handle_starttag(self, tag, attrs):
        if (tag == "a"):
            for name, value in attrs:
                if name == "href":
                    if self.http_regex.match(value):
                        if value not in self.visited and value not in self.in_stack:
                            self.stack.push(value)
                            self.in_stack.add(value)
#                            print("pushing " + value)
                    elif self.double_slash_regex.match(value):
                        if ("http:" + value) not in self.visited and ("http:" + value) not in self.in_stack:
                            self.stack.push("http:" + value)
                            self.in_stack.add("http:" + value)                        
                    elif self.slash_regex.match(value):
                        if ("http://" + self.get_domain() + value) not in self.visited and ("http://" + self.get_domain() + value) not in self.in_stack:
                            self.stack.push("http://" + self.get_domain() + value)
                            self.in_stack.add("http://" + self.get_domain() + value)
#                        else:
#                            self.stack.push("http:" + value)
#                            print("pushing " + "http:" + value)
        else:
#            print("tag is " + tag)
            if self.heading_tag_regex.match(tag):
                self.heading_tag_open = True
            elif tag == "body" or tag == "p":
                self.body_tag_open = True
            elif tag == "title":
                self.title_tag_open = True
            elif tag == "script":
                self.script_tag_open = True
            
    def handle_endtag(self, tag):
        if self.heading_tag_regex.match(tag):
                self.heading_tag_open = False 
        elif tag == "body":
            self.body_tag_open = False
        elif tag == "title":
            self.title_tag_open = False
        elif tag == "script":
            self.script_tag_open = False    
      
    def handle_data(self, data):
        if not self.isUnit: 
            if self.heading_tag_open:
                result = self.unit_regex.search(data)
                if result:
                    self.isUnit = True
                    self.unit.add_unitcode(result.group(0))
                    self.unit.add_title(data)
            if self.body_tag_open and self.count_words(data) == 1 and self.unit_regex.search(data):
                self.isUnit = True
                if self.temp_title:
                    self.unit.add_title(self.temp_title)
                self.unit.add_unitcode(self.unit_regex.search(data).group(0))    
        if self.body_tag_open and not self.script_tag_open:
            if self.count_words(data) > 10:
                self.unit.add_description(data)
        if self.title_tag_open:
            if self.isUnit:
                self.unit.add_title(data)
            else: 
                self.temp_title = data
        if self.script_tag_open:
            res = re.finditer("href=.*$", data, re.MULTILINE)
            if res:
                for line in res:
                    new_address = line.group()
                    new_address = new_address.replace("&amp;","&")
                    new_address = re.search("\'.*\'", new_address, re.IGNORECASE).group(0)
                    new_address = new_address[1:len(new_address)-1]
#                   print(new_address)
                    if self.http_regex.match(new_address):
                        if new_address not in self.visited and new_address not in self.in_stack:
                            self.stack.push(new_address)
                            self.in_stack.add(new_address)
    #                            print("pushing " + value)
                    elif self.double_slash_regex.match(new_address):
                        if "http:" + new_address not in self.visited and "http:" + new_address not in self.in_stack:
                            self.stack.push("http:" + new_address)
                            self.in_stack.add("http:" + new_address)                        
                    elif self.slash_regex.match(new_address):
                        if "http://" + self.get_domain() + new_address not in self.visited and "http://" + self.get_domain() + new_address not in self.in_stack:
                            self.stack.push("http://" + self.get_domain() + new_address)
                            self.in_stack.add("http://" + self.get_domain() + new_address)

                    
            
                
                 
            
    
        
