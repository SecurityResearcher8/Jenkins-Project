import sys
import os
import requests
from mobsfscan.mobsfscan import MobSFScan

path = os.environ['JENKINS_HOME']+'/workspace/'+os.environ['JOB_NAME']
print(path)
src = 'path'
scanner = MobSFScan([src], json=True)
scanner.scan()

#pip install mobsfscan
#mobsfscan app

#opt2 = sys.argv[1]
#appID = sys.argv[2]
#opt3 = sys.argv[3]
#token = sys.argv[4]

#url = 'https://appsecure.accenture.com/api/executive_report/'

#url = 'http://api/v1/download_pdf/'

#print apk_file

#path = os.environ['JENKINS_HOME']+'/jobs/'+os.environ['JOB_NAME']+'/ws/'+name

#print(path)

#files = {'file': open(path,'rb')}

#values = {
#		  'Uid' : appID,
#           }
		
#authtoken = "JWT "+str(token)

#headers = { "Authorization" : authtoken }

#response = requests.post(url,data=values,headers=headers)

#open("Report-file", "wb").write(response.content)
    
#python download.py -hash 96fcb6161620da89c82d3211df514848 -scan_type apk -Authorization 7e4fa6e935d190361b3a8b193c4051e1cb6f897c0a334121e0dfa1f1c3559251
