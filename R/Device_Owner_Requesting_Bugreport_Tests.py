from pickle import FALSE
from uiautomator import Device
import os
import time

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

#this will continue BYOD_Provisioning_tests
def Device_Owner_Requesting_Bugreport_Tests(device):
    d=Device(device)
    
    if d(text="Device Owner Requesting Bugreport Tests").exists:
        click(d,'t',"Device Owner Requesting Bugreport Tests",1)
        runCmd(device,"adb -s %s install -r -t CtsEmptyDeviceOwner.apk",1)
        runCmd(device,"adb -s %s shell dpm set-device-owner --user 0 com.android.cts.emptydeviceowner/.EmptyDeviceAdmin",1)
        click(d,'t',"OK",1)

        #Check device owner
        if d(text="Check device owner").exists:
            click(d,'t',"Check device owner",1)

        #Sharing of requested bugreport declined while being taken
        if d(text="Sharing of requested bugreport declined while being taken").exists:
            click(d,'t',"Sharing of requested bugreport declined while being taken",1)
            click(d,'t',"REQUEST BUGREPORT",1)
            runCmd(device,"adb -s %s shell cmd statusbar expand-notifications",1)
            Fail = False
            if not d(text="Taking bug report…").exists:
                Fail = True
            runCmd(device,"adb -s %s shell cmd statusbar collapse",1)
            click(d,'t',"REQUEST BUGREPORT",1)
            runCmd(device,"adb -s %s shell cmd statusbar expand-notifications",1)
            Fail2 = False
            if not d(text="Device Owner Requesting Bugreport Tests").exists \
            or not d(text="Bugreport is already being collected on this device").exists:
                Fail2 = True
            click(d,'t',"Taking bug report…",1)
            Fail3 = False
            if not d(text="Share bug report?").exists or not d(text="DECLINE").exists or not d(text="SHARE").exists:
                Fail3 = True
            click(d,'t',"DECLINE",1)
            runCmd(device,"adb -s %s shell cmd statusbar expand-notifications",1)
            Fail4 = False
            if d(text="Taking bug report…").exists or not d(text="Device Owner Requesting Bugreport Tests").exists \
            or not d(text="Bugreport sharing declined"):
                Fail4 = True
            click(d,'t',"Clear all",1)
            FAIL = False
            if not Fail and not Fail2 and not Fail3 and not Fail4:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
                FAIL = True

        #Sharing of requested bugreport accepted while being taken
        if d(text="Sharing of requested bugreport accepted while being taken").exists:
            click(d,'t',"Sharing of requested bugreport accepted while being taken",1)
            click(d,'t',"REQUEST BUGREPORT",1)
            runCmd(device,"adb -s %s shell cmd statusbar expand-notifications",1)
            Fail = False
            if not d(text="Taking bug report…").exists:
                Fail = True
            click(d,'t',"Taking bug report…",1)
            Fail2 = False
            if not d(text="Share bug report?").exists or not d(text="Your IT admin requested a bug report to "
            +"help troubleshoot this device. Apps and data may be shared, and your device may temporarily slow down.") \
            or not d(text="DECLINE").exists or not d(text="SHARE").exists:
                Fail2 = True
            click(d,'t',"SHARE",1)
            runCmd(device,"adb -s %s shell cmd statusbar expand-notifications",1)
            Fail3 = False
            while not d(text="Device Owner Requesting Bugreport Tests").exists \
            and not d(text="Bugreport shared successfully").exists:
                if d(text="Taking bug report…").exists:
                    Fail3 = True
            if d(text="Sharing bug report…").exists:
                Fail3 = True
            click(d,'t',"Clear all",1)
            FAIL2 = False
            if not Fail and not Fail2 and not Fail3:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
                FAIL2 = True

        #Sharing of requested bugreport declined after having been taken
        if d(text="Sharing of requested bugreport declined after having been taken").exists:
            click(d,'t',"Sharing of requested bugreport declined after having been taken",1)
            click(d,'t',"REQUEST BUGREPORT",1)
            runCmd(device,"adb -s %s shell cmd statusbar expand-notifications",1)
            Fail = False
            if not d(text="Taking bug report…").exists:
                Fail = True
            while d(text="Taking bug report…").exists and not d(text="Share bug report?").exists:
                pass
            Fail2 = False
            if not d(text="Share bug report?").exists or not d(text="Your admin requested a bug "
            +"report to help troubleshoot this device. Apps and data may be shared.") \
            or not d(text="DECLINE").exists or not d(text="SHARE").exists:
                Fail2 = True
            click(d,'t',"DECLINE",1)
            Fail3 = False
            if not d(text="Device Owner Requesting Bugreport Tests").exists \
            or not d(text="Bugreport sharing declined").exists \
            or d(text="Taking bug report…").exists:
                    Fail3 = True
            click(d,'t',"Clear all",1)
            FAIL3 = False
            if not Fail and not Fail2 and not Fail3:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
                FAIL3 = True

        #Sharing of requested bugreport accepted after having been taken
        if d(text="Sharing of requested bugreport accepted after having been taken").exists:
            click(d,'t',"Sharing of requested bugreport accepted after having been taken",1)
            click(d,'t',"REQUEST BUGREPORT",1)
            runCmd(device,"adb -s %s shell cmd statusbar expand-notifications",1)
            Fail = False
            if not d(text="Taking bug report…").exists:
                Fail = True
            while d(text="Taking bug report…").exists and not d(text="Share bug report?").exists:
                pass
            Fail2 = False
            if not d(text="Share bug report?").exists or not d(text="Your admin requested a bug "
            +"report to help troubleshoot this device. Apps and data may be shared.") \
            or not d(text="DECLINE").exists or not d(text="SHARE").exists:
                Fail2 = True
            click(d,'t',"SHARE",1)
            runCmd(device,"adb -s %s shell cmd statusbar expand-notifications",1)
            Fail3 = False
            if not d(text="Device Owner Requesting Bugreport Tests").exists \
            or not d(text="Bugreport shared successfully").exists \
            or d(text="Taking bug report…").exists:
                    Fail3 = True
            click(d,'t',"Clear all",1)
            FAIL4 = False
            if not Fail and not Fail2 and not Fail3:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
                FAIL4 = True

        #Remove device owner
        if d(text="Remove device owner").exists:
            click(d,'t',"Remove device owner",1)
            click(d,'t',"REMOVE DEVICE OWNER",1)
            runCmd(device,"adb -s %s shell am start -a android.settings.SETTINGS" ,1)
            d(resourceId="com.android.settings:id/main_content_scrollable_container").scroll.to(text="Security")
            click(d,'t',"Security",1)
            click(d,'t',"Device admin apps",1)
            nPress(d,2,"recent",1)
            FAIL5 = False
            if "checked=\"true\"" not in d.dump():
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
                FAIL5 = True
        
        if not FAIL and not FAIL2 and not FAIL3 and not FAIL4 and not FAIL5:
            click(d,'r',"com.android.cts.verifier:id/pass_button",1)
        else:
            click(d,'r',"com.android.cts.verifier:id/fail_button",1)
            
    d.swipe(540,2000,540,1800,steps=10)
    time.sleep(1)