#Script to condense fitment information for multiple rows in single rows
#with specific fitment data comma separated in a single field.

import sys, csv

#initialize sentinels
li = []
recordCount = 0
uniqueCount = 0

#open csv file sent through command line
with open(sys.argv[1], 'rb') as csvfile:
    #create csv reader instance
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    
    #initialize header sentinel
    parsedHeader = False
    print "Condensing CSV..."
    
    #iterate row by row from csv reader instance.  Operate on rows of unique SKU.
    #When a new unique SKU occurs, write the condensed row and move forward.
    for row in csvreader:
        
        #Check if we have written the header
        if not(parsedHeader):
            
            #create write instance of csv using command line file name
            newCsv = open(sys.argv[2], 'wb')
            wr = csv.writer(newCsv, quoting = csv.QUOTE_ALL)
            
            #commit header to file
            wr.writerow(row)
            #clear list
            li = []
            #set sentinel to indicate header was written
            parsedHeader = True
            continue
            
        #check if current SKU is not unique, indicating we have a NEW SKU
        if not(row[3] in li):
            
            #progress indicator
            sys.stdout.write(".")
            sys.stdout.flush()
            
            #ensure this is an actual row, not the header row.
            if (uniqueCount > 0):
                wr.writerow(li)
            uniqueCount += 1
            li = []
            
            #This is a new row, so populate list with this row's data.
            for field in row:
                li.append(field)
        else:
            
            #non-unique SKU.  update current SKU list, appending fitment data to fields
            #malformed CSV has less than standard fields in various rows.  Annoying.
            if (len(row) > 170):
                #check length of new field value, to avoid appending whitespace
                if (len(str(row[169]).strip()) > 0):
                    #check if we already have this value in the field
                    if ((str(li[169]).find(str(row[169]).strip())) < 0):
                        #append new data to field
                        li[169] = str(li[169]).strip() + ", " + str(row[169]).strip()
                        
                #check length of new field value, to avoid appending whitespace
                if (len(str(row[170]).strip()) > 0):
                    #check if we already have this value in the field
                    if ((str(li[170]).find(str(row[170]).strip())) < 0):
                        #append new data to field
                        li[170] = str(li[170]).strip() + ", " + str(row[170]).strip()
                        
                #check length of new field value, to avoid appending whitespace
                if (len(str(row[171]).strip()) > 0):
                    #check if we already have this value in the field
                    if ((str(li[171]).find(str(row[171]).strip())) < 0):
                        #append new data to field
                        li[171] = str(li[171]).strip() + ", " + str(row[171]).strip()
                        
                #check length of new field value, to avoid appending whitespace
                if (len(str(row[172]).strip()) > 0):
                    #check if we already have this value in the field
                    if ((str(li[172]).find(str(row[172]).strip())) < 0):
                        #append new data to field
                        li[172] = str(li[172]).strip() + ", " + str(row[172]).strip()
        recordCount += 1
    print "\nUnique SKUs: ", uniqueCount
    print "Total Rows: ", recordCount
    
    
    
    
    