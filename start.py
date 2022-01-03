import requests
import json
import time
import platform    # For getting the operating system name
import subprocess  # For executing a shell command

#Monolithic prehistorical shitty script. Please blame the Lord of Time. That shit runs fast and is priceless
def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

def checkUpdatesFromEnvironment():
  ping()
  #lookUpForDevicesOnVPN()
  #lookUpForDevicesOnLocal()

def readJsonFile(path):
  structure = {}
  with open(path) as json_file:
    structure = json.load(json_file)
  return structure

def getDataFromDB():
  response = {}
  response["activity"] = requests.get(baseInfo["router"]["address"] + "activity.json").json()
  response["address"] = requests.get(baseInfo["router"]["address"] + "address.json").json()
  response["addressLocal"] = requests.get(baseInfo["router"]["address"] + "addressLocal.json").json()
  response["heartbeat"] = requests.get(baseInfo["router"]["address"] + "heartbeat.json").json()
  return response


  

#def getJsonFromUrl(url):
#  pass

#def 

 
baseInfo : dict = readJsonFile('structure.json')
print(baseInfo)



print(getDataFromDB())

while(True):
  checkUpdatesFromEnvironment()
  getDataFromDB()
  #getDataComparison()
  #pushNewChanges()
  #waitPeriodTime()