import sys
import os
import requests


opt1 = sys.argv[1]
appId = sys.argv[2]
opt2 = sys.argv[3]
token = sys.argv[4]

url = 'https://appsecure.accenture.com/api/executive_report/'

values = {
		  'appId' : appId,
           }

authtoken = "JWT "+str(token)

headers = { "Authorization" : authtoken }

response = requests.post(url,data=values,headers=headers)

print(response.json()) 



open("/home/asha/Desktop/DevSecOps-Reports/Executive-Report-file", "wb").write(response.content)




# 84d445e521016df17d6a05c0ac532270

#http://127.0.0.1:9090/api/executive_report/ "Authorization: JWT eyJh9.eyJ1c2VybmciIE1fQ.S_f02rEXo" appId="5687cbdeda9bff022f9a1e07725b57a4"
#python3 Executive-SAST-Report.py -token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFzaGE4MyIsIm9yaWdfaWF0IjoxNTI5OTI3NDkwLCJ1c2VyX2lkIjo0NiwiZW1haWwiOiJhc2hhLm11bml5YXBwYUBhY2NlbnR1cmUuY29tIiwiZXhwIjoxNTMwMDEzODkwfQ.wBl_Fr2bPUhk1Hr24hWz8yRHDwq7MYdxCXafJRMyDvA -appId d995d8f40dd658cba6a04127a463e6c9
