import sys
import os
import requests

Authorization = sys.argv[8]
hash = sys.argv[2]
scan_type = sys.argv[4]
file_name = sys.argv[6]


url = 'http://127.0.0.1:8004/api/v1/scan'

#print apk_file

#path = os.environ['JENKINS_HOME']+'/jobs/'+os.environ['JOB_NAME']+'/ws/'+name

#print(path)

#files = {'file': open(path,'rb')}

data = {
	'hash' : hash,
	'scan_type' : scan_type,
	'file_name' : file_name,
           }
		
headers = { "Authorization" : Authorization }

response = requests.post(url,data=data,headers=headers)

#print(response.json())


#curl -X POST --url http://localhost:8000/api/v1/scan --data "scan_type=apk&file_name=diva-beta.apk&hash=82ab8b2193b3cfb1c737e3a786be363a" -H "Authorization:563d64fc5054d3b239ac0419f1d6b2378465f5c80e1778c283eb1e3265bdd7ae"
#python Scan.py -hash 96fcb6161620da89c82d3211df514848 -scan_type apk -file_name TargetApp.apk -Authorization 7e4fa6e935d190361b3a8b193c4051e1cb6f897c0a334121e0dfa1f1c3559251
