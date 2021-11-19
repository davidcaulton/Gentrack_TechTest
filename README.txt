ReadMe

1> What was done > 
	Using the ElementTree module to parse the XML file given I retrieved the text content of
	the CSVIntervalData element. 
	
	The CSVIntervalData is then used as a parameter in the checkCSVData function which 
	splits the CSVIntervalData into individual lines and runs a for loop to check each line.
	
	Each iteration of the loop checks the beginning value of each line.
	
	The whitespace and additional empty values are removed for each line. 
	
	When 100 is found it is put in a header variable .
	
	When 200 is found a new instance of a list object is put in a list of lists called li,
	the second value of the 200 line is added to a list called fn to use as the CSV Files name,
   	the header and the current line are appended to that list object.
	
	For each 300 value they are also added to the current list object until the next 200 value.
	
	When the next 200 value is found the step is repeated with a new list object until the end of the file.
	
	When the 900 value is found it is added to the footer variable.
	
	For each list object in my list of lists the footer variable is added and newCSVFile is called, 
	this takes the current list object and the fn at the same index value.
	
	In the newCSVFile function, the fn taken from checkCSVData is made into a string adding .csv to the end
	the string is used to name a new file that is opened as write and a writer is created.
	
	For each value in the list it is written to the new file. This function is repeatedly called in checkCSVData
	until each list object has been used.
	
	There are five exceptions in the checkCSVData that can be raised if the right circumstances are not met
	-If a current line does not start with 100,200,300,900
	-If 100 shows up more than once
	-If 900 shows up more than once
	-If 300 does not show up directly after 200 
	-If any of the values doesnt show up at least once

	For each exception I wrote a unit test that checks that if all the values are correct it passes 
	and whether the exception is raised in the specific instance the exception should be raised.

2> What wasn't done >
    To the best of my knowledge I feel like I was able to accomplish what was asked of me

3> What would be done with more time >
	With more time I would have liked to ensure that, if the XML file contained multiple Transaction
	that each instance of CSVIntervalData for each Transaction could be processed through, A single instance
	can but I would have liked to have seen whether my code could handle more.

	The use case tests could have been tested against a larger amount of variables, the way I did the tests
	I test one instance of a raised exception and that is it, more instances should be tested.  
