import telepot
import requests
import time

bot = telepot.Bot('802292118:AAFkh5j5k4y47rQbRfk-jkhas4uij84')	#Your bot token which is given by botfather.
sendString = ""
i=0
eventIdSaved = 0

try:
    fobject = open("bot.txt", "r")
    eventIdSaved = fobject.read()
    fobject.close()
except Exception as e:
    print(e)
    
while True:
    print("Checking for new events..")
    jsonData = requests.get("https://api.github.com/orgs/Prabal-Bhavishya/events?page=1").json()	#Github org's url
    
    #Checking for different type of events
    if (jsonData[i]['type'] == "PushEvent"):
        eventId = jsonData[i]['id']
        sendString = jsonData[i]['type'] + " by " + jsonData[i]['actor']['login']
        sendString = sendString + ("\nRepo Name: " + jsonData[i]['repo']['name'])
        sendString = sendString + ("\nRepo Url: " + jsonData[i]['repo']['url'])
        sendString = sendString + ("\nCommit name: " + jsonData[i]['payload']['commits'][0]['author']['name'])
        sendString = sendString + ("\nCommit message: " + jsonData[i]['payload']['commits'][0]['message'])
    elif (jsonData[i]['type'] == "WatchEvent"):
        eventId = jsonData[i]['id']
        sendString = (jsonData[i]['type'] + " by " + jsonData[i]['actor']['login'])
        sendString = sendString + ("\nRepo Name: " + jsonData[i]['repo']['name'])
        sendString = sendString + ("\nRepo Url: " + jsonData[i]['repo']['url'])
        sendString = sendString + ("\nAction: " + jsonData[i]['payload']['action'])
    elif (jsonData[i]['type'] == "CreateEvent"):
        eventId = jsonData[i]['id']
        sendString = (jsonData[i]['type'] + " by " + jsonData[i]['actor']['login'])
        sendString = sendString + ("\nRepo Name: " + jsonData[i]['repo']['name'])
        sendString = sendString + ("\nRepo Url: " + jsonData[i]['repo']['url'])
        sendString = sendString + ("\nRef: " + str(jsonData[i]['payload']['ref']))
        sendString = sendString + ("\nRef_Type: " + jsonData[i]['payload']['ref_type'])
        sendString = sendString + ("\nPusher_Type: " + jsonData[i]['payload']['pusher_type'])
    elif (jsonData[i]['type'] == "IssueCommentEvent"):
        eventId = jsonData[i]['id']
        sendString = (jsonData[i]['type'] + " by " + jsonData[i]['actor']['login'])
        sendString = sendString + ("\nRepo Name: " + jsonData[i]['repo']['name'])
        sendString = sendString + ("\nRepo Url: " + jsonData[i]['repo']['url'])
        sendString = sendString + ("\nAction: " + jsonData[i]['payload']['action'])
        sendString = sendString + ("\nRef_Type: " + jsonData[i]['payload']['ref_type'])
        sendString = sendString + ("\nComments_url: " + jsonData[i]['payload']['issue']['comments_url'])
        sendString = sendString + ("\nIssue Title: " + jsonData[i]['payload']['issue']['title'])
        sendString = sendString + ("\nComment: " + jsonData[i]['payload']['issue']['body'])
        sendString = sendString + ("\nState: " + jsonData[i]['payload']['issue']['state'])
        sendString = sendString + ("\nAssignee: " + jsonData[i]['payload']['issue']['assignee'])
    elif (jsonData[i]['type'] == "IssuesEvent"):
        eventId = jsonData[i]['id']
        sendString = (jsonData[i]['type'] + " by " + jsonData[i]['actor']['login'])
        sendString = sendString + ("\nRepo Name: " + jsonData[i]['repo']['name'])
        sendString = sendString + ("\nRepo Url: " + jsonData[i]['repo']['url'])
        sendString = sendString + ("\nAction: " + jsonData[i]['payload']['action'])
        sendString = sendString + ("\nTitle: " + jsonData[i]['payload']['issue']['title'])
        sendString = sendString + ("\nComments_url: " + jsonData[i]['payload']['issue']['comments_url'])
        sendString = sendString + ("\nIssue Title: " + jsonData[i]['payload']['issue']['title'])
        sendString = sendString + ("\nIssue Body: " + jsonData[i]['payload']['issue']['body'])
        sendString = sendString + ("\nIssue Title: " + jsonData[i]['payload']['issue']['title'])
        sendString = sendString + ("\nState: " + jsonData[i]['payload']['issue']['state'])
        sendString = sendString + ("\nAssignee: " + str(jsonData[i]['payload']['issue']['assignee']))

    if (eventIdSaved != eventId):	#If latest event is not same as saved event then update
        fobject = open("bot.txt", "w")
        fobject.write(eventId)
        fobject.close()
        eventIdSaved = eventId
        bot.sendMessage(-12345678910112, sendString)		#sendString to group whose id is -12345678910112, use your group id here.
        
    time.sleep(120)		#Check for new events every 2 minutes
