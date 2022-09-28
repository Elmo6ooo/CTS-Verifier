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

def No_Device_Owner_Tests(device):
    d = Device(device)

    if d(text="No Device Owner Tests").exists:
        click(d,'t',"No Device Owner Tests",1)

        #Device owner provisioning
        if d(text="Device owner provisioning").exists:
            click(d,'t',"Device owner provisioning",1)
            click(d,'t',"START PROVISIONING",1)
            Fail = False    
            if not d(text="Device is already set up").exists:
                Fail = True
            else:
                click(d,'t',"OK",1)
            if not Fail:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        #Quick settings disclosure
        if d(text="Quick settings disclosure").exists:
            click(d,'t',"Quick settings disclosure",1)
            runCmd(device,"adb -s %s shell cmd statusbar expand-settings",1)
            Fail = False
            if d(text="This device belongs to your organization").exists:
                Fail = True
            runCmd(device,"adb -s %s shell cmd statusbar collapse",1)
            if not Fail:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        #Keyguard disclosure
        if d(text="Keyguard disclosure").exists:
            click(d,'t',"Keyguard disclosure",1)

            #SWIPE
            d.screen.off()
            time.sleep(1)
            d.screen.on()
            time.sleep(1)
            Fail = True
            i = 0
            while not d(text="This device belongs to your organization"):
                time.sleep(1)
                i = i + 1
                if i == 10:
                    Fail = False
                    break
            d.swipe(540,2337,540,900,steps=10)
            
            #PATTERN
            click(d,'t',"GO",1)
            d(scrollable=True).scroll.to(text="Security")
            click(d,'t',"Security",1)
            click(d,'t',"Screen lock",1)
            click(d,'t',"Pattern",1)
            d.swipePoints([(237,1168),(237,1768),(837,1768)],steps=20)
            click(d,'t',"NEXT",1)
            d.swipePoints([(237,1168),(237,1700),(837,1700)],steps=20)
            click(d,'t',"CONFIRM",1)
            click(d,'t',"DONE",1)
            d.screen.off()
            time.sleep(1)
            d.screen.on()
            time.sleep(1)
            Fail2 = True
            i = 0
            while not d(text="This device belongs to your organization"):
                time.sleep(1)
                i = i + 1
                if i == 10:
                    Fail2 = False
                    break
            d.swipe(540,2337,540,900,steps=10)
            time.sleep(1)
            d.swipePoints([(237,1300),(237,1875),(837,1875)],steps=20)
            
            #PIN
            click(d,'t',"Screen lock",1)
            d.swipePoints([(237,1150),(237,1700),(837,1700)],steps=20) 
            click(d,'t',"PIN",1)
            d(resourceId="com.android.settings:id/password_entry").set_text("0000")
            click(d,'t',"NEXT",1)
            d(resourceId="com.android.settings:id/password_entry").set_text("0000")
            click(d,'t',"CONFIRM",1)
            d.screen.off()
            time.sleep(1)
            d.screen.on()
            time.sleep(1)
            Fail3 = True
            i = 0
            while not d(text="This device belongs to your organization"):
                time.sleep(1)
                i = i + 1
                if i == 10:
                    Fail3 = False
                    break
            d.swipe(540,2337,540,900,steps=10)
            for i in range(4):  click(d,'r',"com.android.systemui:id/key0",0)
            d.press("enter")
            
            #PASSWORD
            click(d,'t',"Screen lock",1)
            d(resourceId="com.android.settings:id/password_entry").set_text("0000")
            d.press("enter")
            time.sleep(1)
            click(d,'t',"Password",1)
            d(resourceId="com.android.settings:id/password_entry").set_text("test")
            click(d,'t',"NEXT",1)
            d(resourceId="com.android.settings:id/password_entry").set_text("test")
            click(d,'t',"CONFIRM",1)
            d.screen.off()
            time.sleep(1)
            d.screen.on()
            time.sleep(1)
            Fail4 = True
            i = 0
            while not d(text="This device belongs to your organization"):
                time.sleep(1)
                i = i + 1
                if i == 10:
                    Fail4 = False
                    break
            d.swipe(540,2337,540,900,steps=10)
            d(resourceId="com.android.systemui:id/passwordEntry").set_text("test")
            d.press("enter")
            click(d,'t',"Screen lock",1)
            d(resourceId="com.android.settings:id/password_entry").set_text("test")
            d.press("enter")
            time.sleep(1)
            click(d,'t',"None",1)
            click(d,'t',"DELETE",1)
            nPress(d,2,"back",1)
            if not Fail and not Fail2 and not Fail3 and not Fail4:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        #Add account disclosure(blocked)
        if d(text="Add account disclosure").exists:
            click(d,'t',"Add account disclosure",1)
            click(d,'r',"com.android.cts.verifier:id/fail_button",1)
        
        click(d,'r',"com.android.cts.verifier:id/fail_button",1)
