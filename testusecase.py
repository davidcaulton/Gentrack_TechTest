from GentrackTechnical import *
import unittest

 
class TestUseCases(unittest.TestCase):

    def testValidVal(self):
        validString = """100,
200,30,
300
900"""
        invalidString= """100,
twohundred,
300"""
        #Test a string filled with lines that start with valid values should return no errors
        checkCSVData(validString,1)
        self.assertTrue 
        #Test a string filled with invalid start values should throw specific exception
        self.assertRaisesRegex(Exception,'There is an invalid element',checkCSVData,invalidString,1)
    
    def testEachVal(self):
        validString = """100,
200,30,
300,
900"""
        invalidString= """100,
200,30,
300,
300"""
        #Test a string filled with lines that start with valid values should return no errors
        checkCSVData(validString,1)
        self.assertTrue 
        #Test a string that does not contain at least one of each value should throw specific exception
        self.assertRaisesRegex(Exception,' element must appear in at least one row',checkCSVData,invalidString,1)

    def testAppearsOnce(self):
        validString = """100,
200,30,
300,
900"""
        moreHundred= """100,
100,
200,30,
300,
300,
900"""
        moreNineHundred="""100,
200,30,
300,
900,
900"""
        #Test a string filled with lines that start with valid values should return no errors
        checkCSVData(validString,1)
        self.assertTrue 
        #Tests string that has more than one instance of the 100 value should throw specific exception
        self.assertRaisesRegex(Exception,'100 Appears more than once',checkCSVData,moreHundred,1)
        #Tests string that has more than one instance of the 900 value should throw specific exception
        self.assertRaisesRegex(Exception,'900 Appears more than once',checkCSVData,moreNineHundred,1)
    def testShowsAfter(self):
        validString = """100,
200,30,
300,
900"""
        invalidString= """100,
200,30,
900"""
        #Test a string filled with lines that start with valid values should return no errors
        checkCSVData(validString,1)
        self.assertTrue 
        #Tests when 200 value is read that 300 value is the next one read should throw specific exception
        self.assertRaisesRegex(Exception,'300 must follow 200',checkCSVData,invalidString,1)

if __name__ == '__main__':
    unittest.main()