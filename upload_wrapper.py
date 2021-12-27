

import sys
import os
import requests

file = sys.argv[2]
Authorization = sys.argv[4]

url = 'http://127.0.0.1:8001/api/v1/upload'

# url = 'http://0.0.0.0:8000/api/v1/upload'

path = os.environ['JENKINS_HOME']+'/workspace/'+os.environ['JOB_NAME']+'/'+file

# /Users/NowSecure/.jenkins/workspace/Test

# FileNotFoundError: [Errno 2] No such file or directory: '/Users/NowSecure/.jenkins/jobs/Build/lastStable/workspace/app/diva-beta.apk'

# /var/lib/jenkins/jobs/Build/lastStable/archive/app$ 
# /var/lib/jenkins/workspace/Dynamic Analysis

#path = os.environ['JENKINS_HOME']+'/jobs/'+os.environ['JOB_NAME']/'+'/workspace/'+file

#/var/lib/jenkins/workspace/Dynamic Analysis

#path = os.environ['JENKINS_HOME']+'/workspace/'+os.environ['JOB_NAME']/+file

print(file)

files = {'file': (file,open(path,'rb'), "multipart/form-data")}

headers = { "Authorization" : Authorization }

response = requests.post(url,files=files,headers=headers)

# print(response.json())

#python wrapper.py -n App_Name.apk -Authorization <API_KEY>
