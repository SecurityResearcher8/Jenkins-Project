

import sys
import os
import requests

opt1 = sys.argv[1]
file = sys.argv[2]
opt2 = sys.argv[3]
Authorization = sys.argv[4]

url = 'http://127.0.0.1:8004/api/v1/upload'

# url = 'http://0.0.0.0:8000/api/v1/upload'

path = os.environ['JENKINS_HOME']+'/workspace/'+os.environ['JOB_NAME']+'/'+file

print(path)

# /Users/NowSecure/.jenkins/workspace/Test

# FileNotFoundError: [Errno 2] No such file or directory: '/Users/NowSecure/.jenkins/jobs/Build/lastStable/workspace/app/diva-beta.apk'

# /var/lib/jenkins/jobs/Build/lastStable/archive/app$ 
# /var/lib/jenkins/workspace/Dynamic Analysis

#path = os.environ['JENKINS_HOME']+'/jobs/'+os.environ['JOB_NAME']/'+'/workspace/'+file

#/var/lib/jenkins/workspace/Dynamic Analysis

#path = os.environ['JENKINS_HOME']+'/workspace/'+os.environ['JOB_NAME']/+file

print(file)

#files = {'file': (file,open(path,'rb'), "multipart/form-data")}

files = {'file': (file,open(path,'rb'), "multipart/form-data")}

headers = { "Authorization" : Authorization }

response = requests.post(url, files=files, headers=headers)

print(file)

print(response.json())

#curl -F 'file=@/home/asha/Desktop/diva-beta.apk' http://localhost:8002/api/v1/upload -H "Authorization:89080b7094fad62ea187f3fc09883183cccbeb87100ce24f5eb5797492b95c08"

#python wrapper.py -file App_Name.apk -Authorization <API_KEY>
