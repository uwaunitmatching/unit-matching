#import re
##
##unitregex = re.compile("[a-z]{3,5}[0-9]{3,5}", re.IGNORECASE)
##        
##if unitregex.search("FFFS3334"):
##    codeloc = unitregex.search("adsfadsfadfad FFFS3334")
##    print("Unit Found!! building unit data " + codeloc.group(0))
##    
##http://catalog.colostate.edu/general-catalog/courses-az/
##http://handbooks.uwa.edu.au/units/unitdetails?code=cits3200
##http://www.mdh.se/utbildning/kurser/sok-kurs-1.34444?l=en_UK&kod=MFY010&anmalningskod=11083&termin=vt16
##-r http://www.mdh.se/utbildning/kurser/sok-kurs-1.34444?l=en_UK&kod=MFY010&anmalningskod=11083&termin=vt16
##
## http://www.mdh.se/utbildning/kurser/kursplaner-1.35552?l=en_UK&kursplan=25743
##
##
##WORKING
##http://handbooks.uwa.edu.au/units/unitdetails?code=cits3200
##http://www.mdh.se/utbildning/kurser?l=en_UK
##http://www.mdh.se/utbildning/kurser/sok-kurs-1.34444?l=en_UK&kod=MFY010&anmalningskod=11083&termin=vt16

import unittest

import blob
import DBconfig
import downTools
import Unit
import sys
import handleHTML


class Tester(unittest.TestCase):

    

    #TESTS FOR DBconfig.py
    
    def testDB_constructor(self):
        DBtest = DBconfig.DBconfig()
        self.assertIsNotNone(DBtest)

    def testDB_setIP_getIP(self):
        db = DBconfig.DBconfig()
        db.setIP("Test Sting")
        self.assertEqual("Test Sting",db.getIP())

    def testDB_setUser_getUser(self):
        db = DBconfig.DBconfig()
        db.setUser("Test Sting")
        self.assertEqual("Test Sting",db.getUser())

    def testDB_setPW_getPW(self):
        db = DBconfig.DBconfig()
        db.setPW("Test Sting")
        self.assertEqual("Test Sting",db.getPW())

    def testDB_setDBname_getDBname(self):
        db = DBconfig.DBconfig()
        db.setDBname("Test Sting")
        self.assertEqual("Test Sting",db.getDBname())

   #TESTS FOR Unit.py

    def testUnit_constructor(self):
       Unit_Test = Unit.Unit("http://test", DBconfig.DBconfig())
       self.assertIsNotNone(Unit_Test)

    def testUnit_set_url(self):
        Unit_Test = Unit.Unit("http://test", DBconfig.DBconfig())
        Unit_Test.set_url("http://test2")
        self.assertEqual("http://test2", Unit_Test.unit_page)

    def testUnit_add_unitcode(self):
        Unit_Test = Unit.Unit("http://test", DBconfig.DBconfig())
        Unit_Test.add_unitcode("CITS3200")
        self.assertEqual("CITS3200", Unit_Test.unitcode)

    def testUnit_add_title(self):
        Unit_Test = Unit.Unit("http://test", DBconfig.DBconfig())
        Unit_Test.add_title("CITS3200")
        self.assertEqual("CITS3200", Unit_Test.title)

    def testUnit_add_description(self):
        Unit_Test = Unit.Unit("http://test", DBconfig.DBconfig())
        Unit_Test.add_description("test")
        Unit_Test.add_description("test")
        self.assertEqual("test test ", Unit_Test.description)

    def testUnit_checkinfo(self):
        Unit_Test = Unit.Unit("http://test", DBconfig.DBconfig())
        Unit_Test.checkInfo()
        self.assertEqual("NULL", Unit_Test.description)

    def testUnit_insertUnit(self):
        Unit_Test = Unit.Unit("http://test", DBconfig.DBconfig())
        Unit_Test.insertUnit()
        self.assertIsNotNone(Unit_Test.sql)

    #tests for downTools.py
  
    def test_downTools_recursiveLoad(self):
        #should only connect to 1 site then stop as dom is set to a invalid domain
        downTools.recursiveload("http://handbooks.uwa.edu.au/units/unitdetails?code=cits3200", "nonstartme", DBconfig.DBconfig())
        pass #if it got here it ran

    def test_downTools_loadUrl_build_unit(self):
        downTools.loadUrl("http://handbooks.uwa.edu.au/units/unitdetails?code=cits3200", 0, DBconfig.DBconfig())
        pass #if it got here it ran

    #tests for handleHTML html parser

    def test_handleHTML_regex_test_http(self):
        parser = handleHTML.parse()
        result = parser.http_regex.match("http://handbooks.uwa.edu.au/units/unitdetails?code=cits3200")
        if (result):
            pass
        else:
            self.fail()

    def test_handleHTML_regex_test_slash(self):
        parser = handleHTML.parse()
        result = parser.slash_regex.match("/handbooks.uwa.edu.au/units/unitdetails?code=cits3200")
        if (result):
            pass
        else:
            self.fail()

    def test_handleHTML_regex_test_double_slash(self):
        parser = handleHTML.parse()
        result = parser.double_slash_regex.match("//handbooks.uwa.edu.au/units/unitdetails?code=cits3200")
        if (result):
            pass
        else:
            self.fail()
            
    def test_handleHTML_regex_heading_tag(self):
        parser = handleHTML.parse()
        result = parser.heading_tag_regex.match("h5")
        if (result):
            pass
        else:
            self.fail()

    def test_handleHTML_regex_unit_code_test1(self):
        parser = handleHTML.parse()
        result = parser.unit_regex.match("CITS3200")
        if (result):
            pass
        else:
            self.fail()

    def test_handleHTML_regex_unit_code_test2(self):
        parser = handleHTML.parse()
        result = parser.unit_regex.match("pys101")
        if (result):
            pass
        else:
            self.fail()

    def test_handleHTML_regex_unit_code_test3(self):
        parser = handleHTML.parse()
        result = parser.unit_regex.match("year 2015")
        if (not result):
            pass
        else:
            self.fail()
    def test_handleHTML_handle_start_tag(self):
        parser = handleHTML.parse()
        parser.feed("<body>")
        self.assertTrue(parser.body_tag_open)

    def test_handleHTML_handle_end_tag(self):
        parser = handleHTML.parse()
        parser.feed("<body></body>")
        self.assertTrue(not parser.body_tag_open)

    def test_handleHTML_get_domain(self):
        parser = handleHTML.parse()
        parser.url = "http://handbooks.uwa.edu.au/units/unitdetails?code=cits3200"
        dom = parser.get_domain()
        self.assertEqual(dom, "handbooks.uwa.edu.au")

    def test_keyword_extractor(self):
        result = blob.acceptBlobText("Level 3 core unit in the Computer Science; Data Science major sequences Category B broadening unit for Bachelor of Arts, Bachelor of Commerce and  Bachelor of Design students This unit teaches communication skills, an appreciation of the ethical and social implications of computing projects, and skills in project management and quality assurance. A number of lectures are given to introduce the principles of project management and the fundamental ethical and social principles involved in large-scale computing projects. The bulk of the unit is then taken up with a large group project, involving about six students per group. The project gives the students opportunities to practise va")
        self.assertTrue("computer science" in result)
        
if __name__ == '__main__':
    unittest.main()
