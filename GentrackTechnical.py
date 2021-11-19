import xml.etree.ElementTree as eTree
import csv

#parsing the XML file
tree = eTree.parse("testfile.xml")
root = tree.getroot()

for MeterDataNotification in root.iter('MeterDataNotification'):
    CSVIntervalData = MeterDataNotification.find('CSVIntervalData').text

def newCSVFile(n,fn):
   #Create CSV file
   fList = n
   fileName = fn + '.csv'
   with open(fileName,'w') as f:
      writer = csv.writer(f)
      for i in fList:
        #itterate through list adds to CSV File
        writer.writerow(i)

       
def checkCSVData(CSVIntervalData,t):
    header = ''
    trailer = ''
    currLine = ''
    prevLine = ''
    elem = ''
    fn = []
    li = []
    i = -1
    x = 0
    #For loop splits CSVIntervalData into each line and removes whitespace before and after elements
    for line in CSVIntervalData.strip().splitlines():
        #Splits each line by commas and removes any blank values
        currLine = line.split(',')
        currLine = list(filter(None, currLine))
        if not line.startswith('100') and not line.startswith('200') and not line.startswith('300') and not line.startswith('900'):
            #Raised if the current line does not start with a valid value
            raise Exception('There is an invalid element')
        if prevLine == '200' and not line.startswith('300'):
            #Raised if 200 value is not fllowed by 300
            raise Exception('300 must follow 200')
        if line.startswith('100'):
            #creates the header for the CSV files
            if not header:
                header = currLine
                prevLine = currLine[0]
                elem += '100'
                continue
            else:
                #Raised if another 100 value appears after the first instance
                raise Exception('100 Appears more than once')
        if line.startswith('200'):
            #creates a new list object in list of lists
            i += 1
            li.append([])
            #adds to list the second field of 200 value to name file later
            fn.append(currLine[1])
            #adds header and current line to list object
            li[i].append(header)
            li[i].append(currLine)
            prevLine = currLine[0]
            elem += '200'
            continue
        if line.startswith('300'):
            #adds current line to list object
            li[i].append(currLine)
            prevLine = currLine[0]
            elem += '300'
        if line.startswith('900'):
            #creates trailer for CSV files
            if not trailer:
                trailer = currLine
                elem += '900'
                prevLine = currLine[0]
                continue
            else:
                #Raised if another 900 value appears after the first instance
                raise Exception('900 Appears more than once')
    if t == 0:    
        while x <= i:
            #loop to add trailer to each list object and then starts newCSVFile for each list
            li[x].append(trailer)
            newCSVFile(li[x],fn[x])
            x += 1       
    for char in ['100','200','300','900']:
        #Raised if any of these values do not appear at least once
        if char not in elem:
            raise Exception(char + ' element must appear in at least one row')
           
if __name__ == '__main__':          
    checkCSVData(CSVIntervalData,0)