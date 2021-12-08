

import sys
import os
import requests

file = sys.argv[2]
Authorization = sys.argv[4]

url = 'http://127.0.0.1:8000/api/v1/upload'

# path = os.environ['JENKINS_HOME']+'/jobs/'+'Build'+'/lastStable/'+'archive/'+'app/'+file

# /var/lib/jenkins/jobs/Build/lastStable/archive/app$ 


path = os.environ['JENKINS_HOME']+'/jobs/'+os.environ['JOB_NAME']+'/workspace/'+file

#path = os.environ['JENKINS_HOME']+'/jobs/'+'/workspace/'+os.environ['JOB_NAME']/+file


print(file)

files = {'file': (file,open(path,'rb'), "multipart/form-data")}

headers = { "Authorization" : Authorization }

response = requests.post(url,files=files,headers=headers)

print(response.json())

#python wrapper.py -n App_Name.apk -Authorization <API_KEY>
