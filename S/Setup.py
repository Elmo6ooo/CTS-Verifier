import os
import time
from uiautomator import Device

def click(d,switch,input,sleep):
    if switch == 't':
        d(text=input).click()
        time.sleep(sleep)
    elif switch == "r":
        d(resourceId=input).click()
        time.sleep(sleep)
    elif switch == "c":
        d(className=input).click()
        time.sleep(sleep)

def runCmd(device,input,sleep):
    cmd = input % device
    os.system(cmd)
    time.sleep(sleep)

def nPress(d,n,input,sleep):
    for i in range(n):
        d.press(input)
    time.sleep(sleep)

def Setup(device):
    d = Device(device)
    d.press("volume_mute")
    time.sleep(1)
    runCmd(device,"adb -s %s shell am start -a android.settings.SETTINGS" ,1)
    d(resourceId="com.android.settings:id/main_content_scrollable_container").scroll.to(text="Display")
    click(d,'t',"Display",1)
    click(d,'t',"Screen timeout",1)
    click(d,'t',"30 minutes",1)
    nPress(d,2,"back",1)
    d(resourceId="com.android.settings:id/main_content_scrollable_container").scroll.to(text="Security")
    click(d,'t',"Security",1)
    click(d,'t',"Screen lock",1)
    click(d,'t',"None",1)    
    runCmd(device,"adb -s %s shell settings put global hidden_api_policy 1",1)
    runCmd(device,"adb -s %s install -r -g CtsVerifier.apk",1)
    runCmd(device,"adb -s %s shell svc wifi enable",1)
    runCmd(device,"adb -s %s root",1)
    runCmd(device,"adb -s %s shell cmd wifi connect-network GoogleGuest open",1)
    d.press("home")
