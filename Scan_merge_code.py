
# Importing libraries

import urllib.request
import os
from  bs4 import BeautifulSoup


#list to fetch all the scan ids

Scanid_final = []

# open a connection to a URL using urllib. This URL provided will be used to fetch a fresh guid.

webUrl  = urllib.request.urlopen('https://www.uuidgenerator.net/guid')

#get the result code and print it

print ("result code: " + str(webUrl.getcode()))

# read the data from the URL and print it

data = webUrl.read()
soup = BeautifulSoup(data)
print(soup)
guid = soup.select_one("span[id=generated-uuid]").text

#Create_Merged_Scan , Merging_SCan & Export_Scan are three variables storing 3 different commands to be executed.

Create_Merged_Scan = r"C:\FortifyWebInspect\wi.exe" + " " + "-ic" + " " + str(guid) + " " + "mergedscan"
Merging_Scan = r"C:\FortifyWebInspect\wi.exe" + " " + "-im" + " " + str(guid)
Export_Scan = r"C:\FortifyWebInspect\wi -ix" + " " + str(guid) + " " + "-ep" + " " + r"C:\FortifyWebInspect\Scanresults\targetscan.fpr"

#Execute Create_Merged_Scan for creating a merge scan

os.system(Create_Merged_Scan)

# Input on the number of scans user wants to merge

number_of_scan = int(input("Enter the number of scan you want to merge"))

#For loop for appending all the scan ids in Merging_Scan variable

for i in range(number_of_scan):
    Scanid= input("Enter the Scan Id of" + str(i+1) + "scan")
    Scanid_final.append(Scanid)
    Merging_Scan = str(Merging_Scan + " " + Scanid_final[i])

#Executing Merging_Scan to merge two or more scans together

os.system(Merging_Scan)

#This is a final step to export the scan results in the form of fpr

os.system(Export_Scan)

#end
