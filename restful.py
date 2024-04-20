import email
import requests
import json

#from fake_useragent import UserAgent

#*******************************************
#app deploy state
#*******************************************
# url_userDeployState = 'http://192.168.5.15:8015/api/task/getUserDelpoyState/11'
#request_ = requests.get(url_userDeployState)

# result = json.loads(request_.content)
# responses_ = result['data']['UserDeployRespose']
# for response_ in responses_:
#     resp_ = json.loads(response_['response'])
#     state = resp_['state']
#     print(state)

#     mail = response_['userMail']
#     print(mail)


#*******************************************
#user login ip
#*******************************************
# url_userLoginIP = 'http://192.168.5.15:8015/api/task/getUserLoginState/test'
# request_ = requests.get(url_userLoginIP)
# #request_ = requests.get('http://192.168.5.3:8099/GXZC_JCDDDL/cas/auth/queryTokenListByUserMail?userMail=RWGL')

# result = json.loads(request_.content)
# responses_ = result['data']['UserLoginRespose']
# for response_ in responses_:
#     resp_ = json.loads(response_['response'])
#     loginIp = resp_['date'][0]["loginIp"]
#     print(loginIp)

#*******************************************
#upm token apply , user login
#*******************************************
#url_getToken    = "http://192.168.5.3:8099/GXZC_JCPZZX/api/kj/token/apply?serviceCode=api_test&secret=436425648B7E6470C0BC04EED257F6C8"
url_getToken    = "http://192.168.0.120:8200/GXZC_JCPZZX/api/token/apply" #?client_id=api_test&client_secret=436425648B7E6470C0BC04EED257F6C8"
#url_getToken    = "http://192.168.240.128:8015/api/task/postTaskSave"
url_login       = "http://192.168.0.120:8300/GXZC_JCDDDL/cas/auth/login"
url_resAuth     = "http://192.168.0.120:8300/GXZC_JCQXYY/api/qxyy/findUserResourcesBySystemComponent"
url_Roles     = "http://192.168.0.120:8300/GXZC_JCQXYY/api/qxyy/getInRolesByUser"

client_id = "CJ_TEST"
client_secret = "A2D2B408AA1960DC8D736F49B810891B"
emailId = "test1"
password = "123456"
userMail = ""
sysComp = "CJFWKZ"

# get token
#post_data = json.dumps({'client_id':'api_test','client_secret':'436425648B7E6470C0BC04EED257F6C8'})
print("***********Query visit_token******************")
post_data = "client_id="+ client_id +"&client_secret=" + client_secret
#post_data = json.dumps({'schemeid':'112','name':'test111'})
print(post_data)

header = {
        "Content-Type": "application/json",
    }

request_ = requests.post(url_getToken, headers=header,  params=post_data)
#print (request_.text)
result = json.loads(request_.text)
visit_token = result['data']['visit_token']
print("visit_token = " + visit_token)

#*******************************************
#test login
#*******************************************
print("\r\n*********** user Login******************")
header = {
        "visit_token": visit_token,
        "Content-Type": "application/json",
    }
post_data = "emailId=" + emailId +"&password=" + password #json.dumps({'emailId':'test','password':'1'})
print(post_data)

request_ = requests.post(url_login,  headers=header, params=post_data)
#print (request_.text)

result = json.loads(request_.text)
token = result['props']['refeshToken']
print("token = " + token)


# *****************************************************query user info
print("\r\n***********Query user info by name******************")
url_userInfo = "http://192.168.0.120:8300/GXZC_JCJGFW/api/user/name"
header = {
        "visit_token": visit_token,
        "Content-Type": "application/json",
    }
post_data = "name=" + emailId #json.dumps({'emailId':'test','password':'1'})
print(post_data)
request_ = requests.get(url_userInfo,  headers=header, params=post_data)
#print (request_.text)
result = json.loads(request_.text)
userMail = result['data'][0]['mail']
print("mail = " + userMail)

#*******************************************
#test resource Authority
#*******************************************
print("\r\n***********Query user resource Authority******************")
header = {
        "visit_token": visit_token,
        "Content-Type": "application/json",
    }
post_data = "userMail=" + userMail + "&systemComponent=" + sysComp #json.dumps({'emailId':'test','password':'1'})
print(post_data)

request_ = requests.get(url_resAuth,  headers=header, params=post_data)
#print (request_.text)

result = json.loads(request_.text)
userResourses = result['data']['menuResources'][0]['resourceName']
print("user [" + emailId + "], resources [" + userResourses +"]")


#*******************************************
#test user Roles
#*******************************************
print("\r\n***********Query user roles******************")
header = {
        "visit_token": visit_token,
        "Content-Type": "application/json",
    }
post_data = "userMail=" + userMail +"&systemComponent=" + sysComp #json.dumps({'emailId':'test','password':'1'})
print(post_data)

request_ = requests.get(url_Roles,  headers=header, params=post_data)
#print (request_.text)
result = json.loads(request_.text)
userRoles = result['data'][0]['roleName']
print("user [" + emailId + "], Role [" + userRoles +"]")





#***************************************************** query user info by token
print("\r\n***********Query user info by token******************")
url_userInfo = "http://192.168.0.120:8300/GXZC_JCDDDL/api/oauth/token/validate"
header = {
        "visit_token": visit_token,
        "Content-Type": "application/json",
    }

post_data = "token=" + token #json.dumps({'emailId':'test','password':'1'})
print(post_data)

request_ = requests.post(url_userInfo,  headers=header, params=post_data)
print (request_.text)

result = json.loads(request_.text)
userName = result['data']['user']['person']['personLoginName']
print("userName = " + userName)


# url_rti = "http://192.168.5.3:10000/pilot/uddi/$sxgl/RTI_SER"
# request_ = requests.get(url_rti)
# print (request_.text)



