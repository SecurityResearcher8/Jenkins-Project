import sys
import os
import requests

opt1 = sys.argv[1]
appName = sys.argv[2]
opt2 = sys.argv[3]
appId = sys.argv[4]
opt3 = sys.argv[5]
token = sys.argv[6]

url = 'http://10.171.25.115:9090/api/scan_binary/'

#path = os.environ['JENKINS_HOME']+'/jobs/'+os.environ['JOB_NAME']+'/'+appName

# path = os.environ['JENKINS_HOME']+'/jobs/'+'/Build/'+'/lastStable/'+'archive/'+'app/'+appName

path = os.environ['JENKINS_HOME']+'/workspace/'+os.environ['JOB_NAME']+'/'+appName

files = {'binaryFile': open(path,'rb')}

values = {
		  'Uid' : appId,
           }

authtoken = "JWT "+str(token)

headers = { "Authorization" : authtoken }

response = requests.post(url, data=values,files=files,headers=headers)

print (response.json())
