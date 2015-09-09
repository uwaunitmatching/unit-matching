import re

unitregex = re.compile("[a-z]{3,5}[0-9]{3,5}", re.IGNORECASE)
        
if unitregex.search("FFFS3334"):
    codeloc = unitregex.search("adsfadsfadfad FFFS3334")
    print("Unit Found!! building unit data " + codeloc.group(0))