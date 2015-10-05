import re

unitregex = re.compile("[a-z]{3,5}[0-9]{3,5}", re.IGNORECASE)
        
if unitregex.search("FFFS3334"):
    codeloc = unitregex.search("adsfadsfadfad FFFS3334")
    print("Unit Found!! building unit data " + codeloc.group(0))
    
http://catalog.colostate.edu/general-catalog/courses-az/
http://handbooks.uwa.edu.au/units/unitdetails?code=cits3200
http://www.mdh.se/utbildning/kurser/sok-kurs-1.34444?l=en_UK&kod=MFY010&anmalningskod=11083&termin=vt16
-r http://www.mdh.se/utbildning/kurser/sok-kurs-1.34444?l=en_UK&kod=MFY010&anmalningskod=11083&termin=vt16

 http://www.mdh.se/utbildning/kurser/kursplaner-1.35552?l=en_UK&kursplan=25743


WORKING
http://handbooks.uwa.edu.au/units/unitdetails?code=cits3200
http://www.mdh.se/utbildning/kurser?l=en_UK
http://www.mdh.se/utbildning/kurser/sok-kurs-1.34444?l=en_UK&kod=MFY010&anmalningskod=11083&termin=vt16
