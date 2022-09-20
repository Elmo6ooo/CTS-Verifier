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

#this will continue BYOD_Mangaged_Provisioning
def BYOD_Provisioning_tests(device):
    d=Device(device)

    if d(text="BYOD Provisioning tests").exists:
        #Open BYOD_Provisioning_tests
        click(d,'t',"BYOD Provisioning tests",1)

        #Custom provisioning image
        if d(text="Custom provisioning image").exists:
            click(d,'t',"Custom provisioning image",1)
            click(d,'t',"GO",1)
            Fail = False
            d(text="Accept & continue").click()
            while not d(text="Next").exists:
                if d(className="android.widget.ImageView")[0].info['bounds'] == "504":
                    Fail = True
            click(d,'t',"Next",1)
            if not Fail:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        #Custom terms
        if d(text="Custom terms").exists:
            click(d,'t',"Custom terms",1)
            click(d,'t',"GO",1)
            click(d,'t',"View terms",1)
            click(d,'t',"Company ABC",1)
            Fail2 = False
            if not d(text="Company Terms Content. ").exists:
                Fail2 = True
            nPress(d,2,"back",1)
            click(d,'t',"YES",1)
            if not Fail2:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        if not Fail and not Fail2:
            click(d,'r',"com.android.cts.verifier:id/pass_button",1)
        else:
            click(d,'r',"com.android.cts.verifier:id/fail_button",1)
