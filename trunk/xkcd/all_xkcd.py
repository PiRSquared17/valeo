#Downloads all XKCD comics

#import Web, Reg. Exp, and Operating System libraries
import urllib, re, os
from sys import argv

#RegExp for the EndNum variable
CurrentRegExp = re.compile('<h3>Permanent link.*</h3>')

#Check the main XKCD page
site = urllib.urlopen("http://www.xkcd.com/")
contentLine = None

#For each line in the homepage's source...
for line in site.readlines():
    #Break when you find the variable information
    if CurrentRegExp.search(line):
       contentLine = line
       break

#First and Last comics user wishes to download
StartNum = 1
EndNum = 455

#IF the information was found successfuly automatically change EndNum
#ELSE set it to the latest comic as of this writing
if contentLine:
    contentLine = contentLine.split('/')
    EndNum = int(contentLine[3])

#Get StartNum from the command line argument
if len(argv) > 1:
    try:
        if int(argv[1])>EndNum:
            raise Exception
        StartNum = int(argv[1])
    except:
        print("The start number you entered is not a valid comic number.")

#Make sure destination folder exists
destinationFolder = "F:\\xkcd"
#if not os.path.exists(os.path.expanduser("~/") + destinationFolder):
#    os.mkdir(os.path.expanduser("~/") + destinationFolder)

#Full path of "Alt Text" file doesn't need to pre-exist.
#Info will be appended to the end of the file
textFile = open(os.path.join(destinationFolder,"AltText.txt"),'a')

#Regular Exp. used to find the comics in the webpage source
RegExp = re.compile('<img src="(http://imgs.xkcd.com/comics/[^"]+)" title="([^"]*)" alt="([^"]*)" />')

#XRange creates an iterator to go over the comics
for i in xrange(StartNum, EndNum+1):

    #Gets the Site of the i-th comic
    site = urllib.urlopen("http://www.xkcd.com/"+str(i)+"/")

    #For each line in the webpage's source...
    for line in site.readlines():
        #Break when you find the image information
        match = RegExp.search(line)
        if match:
            source = match.group(1)
            title = match.group(2)
            alt = match.group(3)
            srcType = source.split(".")[-1] #everything after the last dot

            #Printing User-Friendly Messages
            print "Comic %d Found. Downloading..." % i

            #Save image from XKCD to Destination Folder
            comicFilename = os.path.join(destinationFolder,str(i)+"."+srcType)
            urllib.urlretrieve(source, comicFilename)
           
            # Writes the title and alt to a text file
            textFile.write("Comic "+str(i) + ': Alt: "' + alt + '" Title: "' + title + '"\n')
            break

#Download the translated version of comic 191
comicFilename = os.path.join(destinationFolder,"191 Translated.png")
if not os.path.exists(comicFilename):     
    urllib.urlretrieve("http://imgs.xkcd.com/comics/lojban_translated.png", comicFilename)

#Graceful program termination
print str(EndNum-StartNum) + " Comics Downloaded"
textFile.close()
