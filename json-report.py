import sys
import os
import requests

Authorization = sys.argv[1]
hash = sys.argv[2]
url = 'http://127.0.0.1:8004/api/v1/report_json'

#print apk_file

#path = os.environ['JENKINS_HOME']+'/jobs/'+os.environ['JOB_NAME']+'/ws/'+name

#print(path)

#files = {'file': open(path,'rb')}

data = {"hash" : hash }
		
headers = { "Authorization" : Authorization }

response = requests.post(url,data=data,headers=headers)

print(response.json())

open("/home/asha/Desktop/DevSecOps-Reports/Json-Report-file", "wb").write(response.content)

# curl -X POST --url http://localhost:8000/api/v1/report_json --data "hash=82ab8b2193b3cfb1c737e3a786be363a" -H "Authorization:89080b7094fad62ea187f3fc09883183cccbeb87100ce24f5eb5797492b95c08"

#python json-report.py -hash 96fcb6161620da89c82d3211df514848 -scan_type apk -Authorization 7e4fa6e935d190361b3a8b193c4051e1cb6f897c0a334121e0dfa1f1c3559251
