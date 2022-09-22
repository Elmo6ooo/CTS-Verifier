from ast import Expression
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

def BYOD_Managed_Provisioning(device):
    d = Device(device)


    #open CTS-V 
    runCmd(device,"adb -s %s shell am start -n com.android.cts.verifier/.CtsVerifierActivity",0)

    #scroll to BYOD Managed Provisioning
    d(resourceId="android:id/list").scroll.to(text="BYOD Managed Provisioning")
    if d(text="BYOD Managed Provisioning").exists:
        click(d,'t',"BYOD Managed Provisioning",1)
        click(d,'t',"OK",1)

        #START BYOD PROVISIONING FLOW
        click(d,'r',"com.android.cts.verifier:id/prepare_test_button",1)
        click(d,'t',"Accept & continue",20)
        click(d,'t',"Next",5)

        #Full disk encryption enabled
        if d(text="Full disk encryption enabled").exists:
            click(d,'t',"Full disk encryption enabled",1)

        #Badged work apps visible in Launcher
        if d(text="Badged work apps visible in Launcher").exists:
            click(d,'t',"Badged work apps visible in Launcher",1)
            d.press("home")
            d.swipe(540,2337,540,900,steps=10)
            time.sleep(1)
            click(d,'t',"WORK",1)
            tmp = d.dump()
            nPress(d,2,"recent",1)
            if "content-desc=\"Work CTS Verifier\"" in tmp:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)

        #Work notification is badged
        if d(text="Work notification is badged").exists:
            click(d,'t',"Work notification is badged",1)
            click(d,'t',"GO",1)
            runCmd(device,"adb -s %s shell cmd statusbar expand-notifications",1)
            tmp = d.dump()
            runCmd(device,"adb -s %s shell cmd statusbar collapse",1)
            if "resource-id=\"android:id/profile_badge\"" in tmp:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)

        #Work status icon is displayed
        if d(text="Work status icon is displayed").exists:
            click(d,'t',"Work status icon is displayed",1)
            click(d,'t',"GO",1)
            tmp = d.dump()
            click(d,'t',"FINISH",1)
            if "content-desc=\"Work profile\"" in tmp:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)  

        #Profile-aware accounts settings
        if d(text="Profile-aware accounts settings").exists:
            click(d,'t',"Profile-aware accounts settings",1)
            click(d,'t',"GO",1)
            d(className="android.widget.ScrollView").scroll.to(text="Passwords & accounts")
            click(d,'t',"Passwords & accounts",1)
            click(d,'t',"Work",1)
            tmp = d.dump()
            nPress(d,2,"recent",1)
            if "text=\"Personal\"" in tmp and "text=\"Work\"" in tmp and "text=\"Remove work profile\"" in tmp:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)  

        #Profile-aware device administrator settings
        if d(text="Profile-aware device administrator settings").exists:
            click(d,'t',"Profile-aware device administrator settings",1)
            click(d,'t',"GO",1)
            click(d,'t',"Device admin apps",1)
            d.click(540,1002)
            time.sleep(1)
            tmp = d.dump()
            nPress(d,3,"back",1)
            if "text=\"Remove work profile\"" in tmp:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1) 

        #Profile-aware trusted credential settings
        if d(text="Profile-aware trusted credential settings").exists:
            click(d,'t',"Profile-aware trusted credential settings",1)
            click(d,'t',"GO",1)
            click(d,'t',"Encryption & credentials",1)
            click(d,'t',"Trusted credentials",1)
            tmp = d.dump()
            nPress(d,3,"back",1)
            if "text=\"Personal\"" in tmp and "text=\"Work\"" in tmp:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1) 

        #Profile-aware user settings
        if d(text="Profile-aware user settings").exists:
            click(d,'t',"Profile-aware user settings",1)
            click(d,'t',"GO",1)
            d(className="android.widget.ScrollView").scroll.to(text="Passwords & accounts")
            click(d,'t',"Passwords & accounts",1)
            click(d,'t',"Auto-sync personal data",1)
            personal = False
            tmp = d.dump()
            if "text=\"This will conserve data and battery usage, but you’ll need to sync each account manually to collect recent information. And you won’t receive notifications when updates occur.\"" in tmp:
                personal = True
            click(d,'t',"CANCEL",1)
            click(d,'t',"Work",1)
            click(d,'t',"Auto-sync work data",1)
            work = False
            tmp = d.dump()
            if "text=\"This will conserve data and battery usage, but you’ll need to sync each account manually to collect recent information. And you won’t receive notifications when updates occur.\"" in tmp:
                work = True
            nPress(d,3,"back",1)
            if personal and work:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1) 

        #Profile-aware app settings
        if d(text="Profile-aware app settings").exists:
            click(d,'t',"Profile-aware app settings",1)
            click(d,'t',"GO",1)
            tmp = d.dump()
            d.press("back")
            if "text=\"Personal\"" in tmp and "text=\"Work\"" in tmp:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1) 

        #Profile-aware location settings
        if d(text="Profile-aware location settings").exists:
            click(d,'t',"Profile-aware location settings",1)
            click(d,'t',"GO",1)
            click(d,'t',"Use location",1)
            if d(text="Location for work profile").sibling(text="Location is off").exists:
                off = True
            click(d,'t',"Use location",1)
            if d(text="Location for work profile").sibling(text="On").exists:
                on = True
            d.press("back")
            if on and off:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1) 

        #Profile-aware printing settings
        if d(text="Profile-aware printing settings").exists:
            click(d,'t',"Profile-aware printing settings",1)
            click(d,'t',"GO",1)
            click(d,'t',"Personal",1)
            click(d,'t',"Work",1)
            tmp = d.dump()
            d.press("back")
            if "text=\"Default Print Service\"" in tmp:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1) 

        #Personal ringtones
        if d(text="Personal ringtones").exists:
            click(d,'t',"Personal ringtones",1)
            click(d,'t',"GO",1)
            d(className="androidx.recyclerview.widget.RecyclerView").scroll.to(text="Work profile sounds")
            click(d,'t',"Work profile sounds",1)
            if d(text="Same as personal profile").exists:
                click(d,'t',"Use personal profile sounds",1)
            click(d,'t',"Work phone ringtone",1)
            click(d,'t',"Free Flight",1)
            click(d,'t',"OK",1)
            click(d,'t',"Default work notification sound",1)
            click(d,'t',"Pizzicato",1)
            click(d,'t',"OK",1)
            click(d,'t',"Default work alarm sound",1)
            click(d,'t',"Helium",1)
            click(d,'t',"OK",1)
            d.press("back")
            d(className="androidx.recyclerview.widget.RecyclerView").scroll.to(text="Phone ringtone")
            ringtone = False
            if not d(text="Phone ringtone").sibling(text="Free Flight").exists:
                ringtone = True
            d(className="androidx.recyclerview.widget.RecyclerView").scroll.to(text="Default notification sound")
            notification = False
            if not d(text="Default notification sound").sibling(text="Pizzicato").exists:
                notification = True
            d(className="androidx.recyclerview.widget.RecyclerView").scroll.to(text="Default alarm sound")
            alarm = False
            if not d(text="Default alarm sound").sibling(text="Helium").exists:
                alarm = True
            d.press("back")
            if ringtone and notification and alarm:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1) 

        #Open app cross profiles from the personal side
        if d(text="Open app cross profiles from the personal side").exists:
            click(d,'t',"Open app cross profiles from the personal side",1)
            click(d,'t',"GO",1)
            click(d,'t',"CTS Verifier",1)
            Fail = False
            if d(text="You selected the ctsverifier option").exists:
                click(d,'t',"FINISH",1)
            else:
                Fail = True
            click(d,'t',"GO",1)
            click(d,'t',"Work",2)
            click(d,'t',"CTS Verifier",1)
            Fail2 = False
            if d(text="You selected the Work option.").exists:
                click(d,'t',"FINISH",1)
            else:
                Fail2 = True
            if not Fail and not Fail2:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1) 
        
        #Open app cross profiles from the work side
        if d(text="Open app cross profiles from the work side").exists:
            click(d,'t',"Open app cross profiles from the work side",1)
            click(d,'t',"GO",1)
            click(d,'t',"CTS Verifier",1)
            Fail = False
            if d(text="You selected the ctsverifier option").exists:
                click(d,'t',"FINISH",1)
            else:
                Fail = True
            click(d,'t',"GO",1)
            click(d,'t',"Personal",2)
            click(d,'t',"CTS Verifier",1)
            Fail2 = False
            if d(text="You selected the personal option.").exists:
                click(d,'t',"FINISH",1)
            else:
                Fail2 = True
            if not Fail and not Fail2:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)
        
        #Cross profile intent filters are set
        if d(text="Cross profile intent filters are set").exists:
            click(d,'t',"Cross profile intent filters are set",1) 
        
        #Cross profile permission control
        if d(text="Cross profile permission control").exists:
            click(d,'t',"Cross profile permission control",1) 
            runCmd(device,"adb -s %s install -r -t CrossProfileTestApp.apk",2)
            runCmd(device,"adb -s %s install -r -t --user 10 CrossProfileTestApp.apk",2)
            click(d,'t',"OK",1)
            click(d,'t',"PREPARE TEST",1)
            click(d,'t',"Cross profile permission disabled by default",1)
            click(d,'t',"GO",1)
            Fail = False
            if not d(text="Cross Profile Test App").sibling(text="Not connected").exists:
                Fail = True
            d.press("back")
            if not Fail:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)
            click(d,'t',"Cross profile permission enabled",1)
            click(d,'t',"GO",1)
            click(d,'t',"OPEN SETTINGS",1)
            click(d,'t',"Connect these apps",1)
            click(d,'t',"ALLOW",1)
            Fail2 = False
            if not d(text="INTERACTING ACROSS PROFILES ALLOWED").exists:
                Fail2 = True
            d.press("back")
            if not Fail2:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)
            click(d,'t',"Cross profile permission disabled",1)
            click(d,'t',"GO",1)
            click(d,'t',"OPEN SETTINGS",1)
            click(d,'t',"Connected",1)
            d.press("back")
            Fail3 = False
            if not d(text="INTERACTING ACROSS PROFILES NOT ALLOWED").exists:
                Fail3 = True
            d.press("back")
            if not Fail3:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)
            if not Fail and not Fail2 and not Fail3:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        d.swipe(540,2000,540,1800,steps=10)
        time.sleep(1)

        #"Non-market app installation restrictions"
        if d(text="Non-market app installation restrictions").exists:
            click(d,'t',"Non-market app installation restrictions",1)
            click(d,'t',"OK",1)
            click(d,'t',"Disable non-market apps",1)
            click(d,'t',"GO",1)
            Fail = False
            if not d(text="Blocked by your IT admin").exists:
                Fail = True
            else:
                click(d,'t',"OK",1)
            if not Fail:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)
            click(d,'t',"Enable non-market apps",1)
            click(d,'t',"GO",1)
            click(d,'t',"SETTINGS",1)
            click(d,'t',"Allow from this source",1)
            nPress(d,2,"back",1)
            Fail2 = False
            if d(text="Blocked by your IT admin").exists:
                Fail2 = True
            else:
                click(d,'t',"UPDATE",1)
            if not Fail2:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)
            click(d,'t',"Disable non-market apps (global restriction)",1)
            click(d,'t',"GO",1)
            Fail3 = False
            if not d(text="Blocked by your IT admin").exists:
                Fail3 = True
            else:
                click(d,'t',"OK",1)
            if not Fail3:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)
            click(d,'t',"Enable non-market apps (global restriction)",1)
            click(d,'t',"GO",1)
            Fail4 = False
            if d(text="Blocked by your IT admin").exists:
                Fail4 = True
            else:
                click(d,'t',"UPDATE",1)
            if not Fail4:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)
            click(d,'t',"Disable primary user non-market apps (global restriction)",1)
            runCmd(device,"adb -s %s push NotificationBot.apk /data/local/tmp/",2)
            click(d,'t',"GO",1)
            Fail5 = False
            if not d(text="Blocked by your IT admin").exists:
                Fail5 = True
            else:
                click(d,'t',"OK",1)
            if not Fail5:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)
            click(d,'t',"Enable primary user non-market apps (global restriction)",1)
            click(d,'t',"GO",1)
            click(d,'t',"SETTINGS",1)
            click(d,'t',"Allow from this source",1)
            nPress(d,2,"back",1)
            Fail6 = False
            if d(text="Blocked by your IT admin").exists:
                Fail6 = True
            else:
                click(d,'t',"GO",1)
                click(d,'t',"INSTALL",1)
            if not Fail6:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)
            if not Fail and not Fail2 and not Fail3 and not Fail4 and not Fail5 and not Fail6: 
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        #Permissions lockdown
        if d(text="Permissions lockdown").exists:
            click(d,'t',"Permissions lockdown",1)
            runCmd(device, "adb -s %s install CtsPermissionApp.apk",2)
            click(d,'t',"GO",1)
            click(d,'t',"OPEN APPLICATION SETTINGS",1)
            click(d,'t',"Permissions",1)
            click(d,'t',"Contacts",1)
            Fail = False
            if not d(text="Allow").enabled or not d(text="Don’t allow").enabled:
                Fail = True
            nPress(d,3,"back",1)
            click(d,'t',"Grant",1)
            click(d,'t',"OPEN APPLICATION SETTINGS",1)
            click(d,'t',"Permissions",1)
            click(d,'t',"Contacts",1)
            Fail2 = False
            if d(text="Allow").enabled  or d(text="Don’t allow").enabled or d(text="Don’t allow").checked:
                Fail2 = True
            nPress(d,3,"back",1)
            click(d,'t',"Deny",1)
            click(d,'t',"OPEN APPLICATION SETTINGS",1)
            click(d,'t',"Permissions",1)
            click(d,'t',"Contacts",1)
            Fail3 = False
            if d(text="Allow").enabled  or d(text="Don’t allow").enabled or d(text="Allow").checked:
                Fail3 = True
            nPress(d,4,"back",1)
            if not Fail and not Fail2 and not Fail3:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)

        d.swipe(540,2000,540,1700,steps=10)
        time.sleep(1)

        #VPN test
        if d(text="VPN test").exists:
            click(d,'t',"VPN test",1)
            if d(text="Cannot establish a VPN connection.\n This was expected.\n Mark this test as passed.\n").exists:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
        
        #Always-on VPN Settings
        if d(text="Always-on VPN Settings").exists:
            click(d,'t',"Always-on VPN Settings",1)
            click(d,'t',"OK",1)
            runCmd(device,"adb -s %s uninstall com.android.cts.vpnfirewall",1)
            runCmd(device,"adb -s %s install -r CtsVpnFirewallAppApi23.apk",2)
            click(d,'t',"PREPARE VPN",1)
            click(d,'t',"OK",1)
            click(d,'t',"VPN app targeting SDK 23",1)
            click(d,'t',"GO",1)
            click(d,'r',"com.android.settings:id/settings_button",1)
            Fail = False
            if d(text="Always-on VPN").enabled \
                or d(text="Always-on VPN").right().child(resourceId="android:id/switch_widget").checked \
                or d(text="Block connections without VPN").enabled \
                or d(text="Block connections without VPN").right().child(resourceId="android:id/switch_widget").checked:
                Fail = True
            nPress(d,2,"back",1)
            if not Fail:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)
            runCmd(device,"adb -s %s install -r CtsVpnFirewallAppApi24.apk",2)
            click(d,'t',"VPN app targeting SDK 24",1)
            click(d,'t',"GO",1)
            click(d,'r',"com.android.settings:id/settings_button",1)
            Fail2 = False
            if not d(text="Stay connected to VPN at all times").right().child(resourceId="android:id/switch_widget").enabled \
                or d(text="Stay connected to VPN at all times").right().child(resourceId="android:id/switch_widget").checked \
                or d(text="Block connections without VPN").right().child(resourceId="android:id/switch_widget").enabled\
                or d(text="Block connections without VPN").right().child(resourceId="android:id/switch_widget").checked:
                Fail2 = True
            click(d,'t',"Always-on VPN",1)
            if d(text="Stay connected to VPN at all times").right().child(resourceId="android:id/switch_widget").checked \
                and not d(text="Block connections without VPN").right().child(resourceId="android:id/switch_widget").enabled:
                Fail2 = True    
            nPress(d,2,"back",1)
            if not Fail2:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)
            runCmd(device,"adb -s %s install -r CtsVpnFirewallAppNotAlwaysOn.apk",2)
            click(d,'t',"VPN app with opt-out",1)
            click(d,'t',"GO",1)
            click(d,'r',"com.android.settings:id/settings_button",1)
            Fail3 = False
            if d(text="Always-on VPN").enabled \
                or d(text="Always-on VPN").right().child(resourceId="android:id/switch_widget").checked \
                or d(text="Block connections without VPN").enabled \
                or d(text="Block connections without VPN").right().child(resourceId="android:id/switch_widget").checked:
                Fail3 = True
            nPress(d,2,"back",1)
            if not Fail3:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)
            if not Fail and not Fail2 and not Fail3:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
            runCmd(device,"adb -s %s uninstall com.android.cts.vpnfirewall",1)

        d.swipe(540,2000,540,1800,steps=10)
        time.sleep(1)

        #Turn off work profile
        if d(text="Turn off work profile").exists:
            click(d,'t',"Turn off work profile",1)
            click(d,'t',"OK",1)
            click(d,'t',"Prepare a work notification",1)
            click(d,'t',"GO",1)
            runCmd(device,"adb -s %s shell cmd statusbar expand-notifications",1)
            tmp = d.dump()
            runCmd(device,"adb -s %s shell cmd statusbar collapse",1)
            Fail = False
            if not "This is a notification" in tmp:
                Fail = True
                click(d,'t',"FAIL",1)
            else:
                click(d,'t',"PASS",1)
            click(d,'t',"OPEN SETTINGS TO TOGGLE WORK PROFILE",1)
            click(d,'t',"Work",1)
            click(d,'t',"Work profile settings",1)
            click(d,'t',"Work profile",1)
            nPress(d,2,"back",1)
            time.sleep(5)
            click(d,'t',"Notifications when work profile is off",1)
            runCmd(device,"adb -s %s shell cmd statusbar expand-notifications",1)
            tmp = d.dump()
            runCmd(device,"adb -s %s shell cmd statusbar collapse",1)
            Fail2 = False
            if "This is a notification" in tmp:
                Fail2 = True
                click(d,'t',"FAIL",1)
            else:
                click(d,'t',"PASS",1)
            d.press("home")
            d.swipe(540,2337,540,900,steps=10)
            time.sleep(1)
            click(d,'t',"TURN ON WORK APPS",1)
            x = (d(text="Files").bounds["left"] + d(text="Files").bounds["right"]) / 2
            y = (d(text="Files").bounds["top"] + d(text="Files").bounds["bottom"]) / 2
            d.drag(x,y,x+100,y+100,steps=10)
            time.sleep(1)
            d.swipe(540,2337,540,900,steps=10)
            time.sleep(1)
            click(d,'t',"Turn off work apps",1)
            d.press("home")
            click(d,'t',"Files",1)
            Fail2 = False
            if not d(text="Turn on work apps?"):
                Fail2 = True
            click(d,'t',"CANCEL",1)
            nPress(d,2,"recent",1)
            click(d,'t',"Starting work apps when work profile is off",1)
            if not Fail2:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)
            click(d,'t',"OPEN SETTINGS TO TOGGLE WORK PROFILE",1)
            click(d,'t',"Work",1)
            click(d,'t',"Work profile settings",1)
            click(d,'t',"Work profile",1)
            nPress(d,2,"back",1)
            time.sleep(2)
            click(d,'t',"Status bar icon when work profile is on",1)
            click(d,'t',"GO",1)
            Fail3 = False
            if d(text="Work profile is off").exists:
                Fail3 = True
            d.press("back")
            if not Fail3:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)
            click(d,'t',"Starting work apps when work profile is on",1)
            click(d,'t',"GO",1)
            click(d,'t',"Files",1)
            Fail4 = False
            if d(text="Turn on work apps?"):
                Fail4 = True
            nPress(d,2,"recent",1)
            if not Fail4:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)
            if not Fail and not Fail2 and not Fail3 and not Fail4:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
        
        #Select work lock test
        if d(text="Select work lock test").exists:
            click(d,'t',"Select work lock test",1)
            click(d,'t',"GO",1)
            Fail = False
            try:
                click(d,'t',"Continue without fingerprint",1)
                click(d,'t',"PIN",1)
                d(resourceId="com.android.settings:id/password_entry").set_text("0000")
                click(d,'t',"NEXT",1)
                d(resourceId="com.android.settings:id/password_entry").set_text("0000")
                click(d,'t',"CONFIRM",1)
                click(d,'t',"DONE",1)
            except:
                Fail = True
            if not Fail:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)    

        #Confirm work lock test
        if d(text="Confirm work lock test").exists:
            click(d,'t',"Confirm work lock test",1)
            click(d,'t',"GO",1)
            d.screen.off()
            time.sleep(1)
            d.screen.on()
            time.sleep(1)
            click(d,'t',"Files",1)
            Fail = False    
            try:
                if "android.widget.ImageView" in d(text="CtsVerifier").up().child().info['className']:
                    d(resourceId="com.android.settings:id/password_entry").set_text("0000")
                    d.press("enter")
                    time.sleep(1)
                if d(text="Turn on work apps?"):
                    Fail = True
            except:
                Fail = True
            nPress(d,2,"recent",1)
            if not Fail:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)

        # Confirm pattern lock test
        if d(text="Confirm pattern lock test").exists:
            click(d,'t',"Confirm pattern lock test",1)
            click(d,'t',"GO",1)
            d(resourceId="com.android.settings:id/password_entry").set_text("0000")
            d.press("enter")
            time.sleep(1)
            click(d,'t',"Continue without fingerprint",1)
            click(d,'t',"Pattern",1)
            d.swipePoints([(237,1168),(237,1768),(837,1768)],steps=20)
            click(d,'t',"NEXT",1)
            d.swipePoints([(237,1168),(237,1700),(837,1700)],steps=20)
            click(d,'t',"CONFIRM",1)
            d.screen.off()
            time.sleep(1)
            d.screen.on()
            time.sleep(1)
            d.press("home")
            time.sleep(1)
            click(d,'t',"Files",1)
            Fail = False
            try:
                if "android.widget.ImageView" in d(text="CtsVerifier").up().info["className"]:
                    d.swipePoints([(237,1168),(237,1700),(837,1700)],steps=20) 
                    time.sleep(1)
                if d(text="Turn on work apps?"):
                    Fail = True
            except:
                Fail = True
            nPress(d,2,"recent",1)
            if not Fail:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)

         #Recents redaction test
        if d(text="Recents redaction test").exists:
            click(d,'t',"Recents redaction test",1)
            click(d,'t',"OK",1)
            click(d,'t',"Verify recents are redacted when locked.",1)
            d.screen.off()
            time.sleep(1)
            d.screen.on()
            time.sleep(1)
            d.press("home")
            d.press("recent")
            time.sleep(1)
            runCmd(device,"adb -s %s shell screencap -p /sdcard/Hidden.png",1)
            d.press("recent")
            time.sleep(1)
            d.swipePoints([(237,1168),(237,1700),(837,1700)],steps=20)
            time.sleep(1)
            click(d,'t',"PASS",1)
            click(d,'t',"Verify recents are not redacted when unlocked.",1)
            click(d,'t',"GO",1)
            d(scrollable=True).scroll.to(text="Use one lock")
            click(d,'t',"Use one lock",1)
            d.swipePoints([(237,1168),(237,1700),(837,1700)],steps=20)
            d.press("back")
            d.press("recent")
            time.sleep(1)
            runCmd(device,"adb -s %s shell screencap -p /sdcard/unHidden.png",1)
            d.click(540,1000)
            time.sleep(1)
            click(d,'t',"GO",1)
            d(scrollable=True).scroll.to(text="Use one lock")
            click(d,'t',"Use one lock",1)
            click(d,'t',"Pattern",1)
            d.swipePoints([(237,1168),(237,1768),(837,1768)],steps=20)
            click(d,'t',"NEXT",1)
            d.swipePoints([(237,1168),(237,1700),(837,1700)],steps=20)
            click(d,'t',"CONFIRM",1)
            click(d,'t',"DONE",1)
            d.press("back")
            click(d,'t',"PASS",1)
            click(d,'r',"com.android.cts.verifier:id/pass_button",1)

        d.swipe(540,2000,540,1800,steps=10)
        time.sleep(1)
        
        #Organization Info
        if d(text="Organization Info").exists:
            click(d,'t',"Organization Info",1)
            d(resourceId="com.android.cts.verifier:id/organization_name_edit_text").set_text("TEST")
            click(d,'r',"com.android.systemui:id/back",1)
            time.sleep(1)
            click(d,'t',"SET",1)
            click(d,'t',"GO",1)
            Fail = False
            if not d(text="TEST").exists:
                Fail = True
            d.swipePoints([(237,1168),(237,1700),(837,1700)],steps=20) 
            time.sleep(1)
            if not Fail:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        #Personal password test
        if d(text="Personal password test").exists:
            click(d,'t',"Personal password test",1)
            click(d,'t',"GO",1)
            Fail = False
            try:
                click(d,'t',"Continue without fingerprint",1)
                click(d,'t',"PIN",1)
                d(resourceId="com.android.settings:id/password_entry").set_text("0000")
                click(d,'t',"NEXT",1)
                d(resourceId="com.android.settings:id/password_entry").set_text("0000")
                click(d,'t',"CONFIRM",1)
                click(d,'t',"DONE",1)
                d.screen.off()
                time.sleep(1)
                d.screen.on()
                time.sleep(1)
                d.swipe(540,2337,540,900,steps=10)
                for i in range(4):  click(d,'r',"com.android.systemui:id/key0",0)
                d.press("enter")
            except:
                Fail = True
            if not Fail:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)

        #Policy transparency test
        if d(text="Policy transparency test").exists:
            click(d,'t',"Policy transparency test",1)
            click(d,'t',"OK",1)
            click(d,'t',"SET SHORT SUPPORT MESSAGE",1)
            d.swipePoints([(237,1168),(237,1700),(837,1700)],steps=20) 
            time.sleep(1)
            nPress(d,2,'recent',1)
            click(d,'t',"SET SHORT SUPPORT MESSAGE",1)
            click(d,'t',"SET DEFAULT MESSAGE",1)
            click(d,'t',"SET MESSAGE",1)
            d.press("back")
            click(d,'t',"SET LONG SUPPORT MESSAGE",1)
            click(d,'t',"SET DEFAULT MESSAGE",1)
            click(d,'t',"SET MESSAGE",1)
            d.press("back")

            #Disallow controlling apps
            if d(text="Disallow controlling apps").exists:
                click(d,'t',"Disallow controlling apps",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                click(d,'t',"Work",1)
                Fail = True
                click(d,'t',"Contacts",1)
                click(d,'t',"DISABLE",1)
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    Fail = False
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with your work profile, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail = True                
                nPress(d,2,"back",1)
                Fail2 = True
                Fail3 = True
                click(d,'t',"Cross Profile Test App",1)
                click(d,'t',"UNINSTALL",1)
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    Fail2 = False
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with your work profile, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail2 = True  
                d.press("back")
                click(d,'t',"FORCE STOP",1)
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    Fail3 = False
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with your work profile, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail3 = True  
                nPress(d,3,"back",1)
                if not Fail and not Fail2 and not Fail3:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Disallow uninstall apps
            if d(text="Disallow uninstall apps").exists:
                click(d,'t',"Disallow uninstall apps",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                click(d,'t',"Work",1)
                Fail4 = True
                click(d,'t',"Cross Profile Test App",1)
                click(d,'t',"UNINSTALL",1)
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    Fail4 = False
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with your work profile, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail4 = True  
                nPress(d,3,"back",1)
                if not Fail4:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Disallow modify accounts
            if d(text="Disallow modify accounts").exists:
                click(d,'t',"Disallow modify accounts",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                click(d,'t',"Work",1)
                Fail5 = True
                click(d,'t',"Add account",1)
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    Fail5 = False
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with your work profile, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail5 = True  
                nPress(d,2,"back",1)
                if not Fail5:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Disallow share location
            if d(text="Disallow share location").exists:
                click(d,'t',"Disallow share location",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                Fail6 = True
                click(d,'t',"Location for work profile",1)
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    Fail6 = False
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with your work profile, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail6 = True  
                nPress(d,2,"back",1)
                if not Fail6:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Disallow unified challenge
            if d(text="Disallow unified challenge").exists:
                click(d,'t',"Disallow unified challenge",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                d(className="androidx.recyclerview.widget.RecyclerView").scroll.to(text="Use one lock")
                Fail7 = True
                click(d,'t',"Use one lock",1)
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    Fail7 = False
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with your work profile, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail7 = True  
                nPress(d,2,"back",1)
                if not Fail7:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Disallow config location
            if d(text="Disallow config location").exists:
                click(d,'t',"Disallow config location",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                Fail8 = True
                click(d,'t',"Location for work profile",1)
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    Fail8 = False
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with your work profile, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail8 = True  
                nPress(d,2,"back",1)
                if not Fail8:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Set permitted accessibility services
            if d(text="Set permitted accessibility services").exists:
                click(d,'t',"Set permitted accessibility services",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                Fail9 = True
                click(d,'t',"Test accessibility service",1)
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    Fail9 = False
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with your work profile, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail9 = True  
                nPress(d,2,"back",1)
                if not Fail9:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Set permitted input methods
            if d(text="Set permitted input methods").exists:
                click(d,'t',"Set permitted input methods",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                d(className="android.widget.ScrollView").scroll.to(text="System")
                click(d,'t',"System",1)
                click(d,'t',"Languages & input",1)
                d(className="androidx.recyclerview.widget.RecyclerView").scroll.to(text="On-screen keyboard for work")
                click(d,'t',"On-screen keyboard for work",1)
                click(d,'t',"Manage on-screen keyboards",1)
                Fail0 = True
                click(d,'t',"Test input method",1)
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    Fail0 = False
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with your work profile, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail0 = True  
                nPress(d,6,"back",1)
                if not Fail0:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)
                if not Fail and not Fail2 and not Fail3 and not Fail4 and not Fail5 and not Fail6 and not Fail7 and not Fail8 and not Fail9 and not Fail0:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)


        d.swipe(540,2000,540,1600,steps=10)
        time.sleep(1)

        #Profile-aware data usage settings (Wi-Fi)
        if d(text="Profile-aware data usage settings (Wi-Fi)").exists:
            click(d,'t',"Profile-aware data usage settings (Wi-Fi)",1)
            click(d,'t',"GO",1)
            click(d,'t',"Network & internet",1)
            click(d,'t',"Internet",1)
            d(scrollable=True).scroll.toEnd()
            Fail = False
            if not d(text="Non-carrier data usage").enabled:
                Fail = True
            #runCmd(device,"adb -s %s shell screencap -p /sdcard/wifiDataUsage.png",1)
            runCmd(device,"adb -s %s shell cmd wifi forget-network 0",1)
            runCmd(device,"adb -s %s shell svc wifi disable",1)
            nPress(d,3,"back",1)
            if not Fail:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)

        #Profile-aware data usage settings (Mobile)
        if d(text="Profile-aware data usage settings (Mobile)").exists:
            click(d,'t',"Profile-aware data usage settings (Mobile)",1)
            click(d,'t',"GO",1)
            click(d,'t',"Network & internet",1)
            click(d,'t',"Internet",1)
            click(d,'r',"com.android.settings:id/settings_button",1)
            Fail = False
            if not int(d(resourceId="com.android.settings:id/data_usage_view").info["text"][0]) > 0:
                Fail = True
            #runCmd(device,"adb -s %s shell screencap -p /sdcard/mobileDataUsage.png",1)
            nPress(d,4,"back",1)
            if not Fail:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)

        #Disallow apps control
        if d(text="Disallow apps control").exists:
            click(d,'t',"Disallow apps control",1)
            click(d,'t',"OK",1)
            click(d,'t',"PREPARE TEST",1)
            click(d,'t',"Disabled uninstall button",1)
            click(d,'t',"GO",1)
            click(d,'t',"Work",1)
            Fail = True
            click(d,'t',"Contacts",1)
            click(d,'t',"DISABLE",1)
            if d(text="Blocked by your IT admin").exists:
                Fail = False
            nPress(d,2,"back",1)
            Fail2 = True
            click(d,'t',"Cross Profile Test App",1)
            click(d,'t',"UNINSTALL",1)
            if d(text="Blocked by your IT admin").exists:
                Fail2 = False
            d.press("back")
            Fail3 = True
            click(d,'t',"FORCE STOP",1)
            if d(text="Blocked by your IT admin").exists:
                Fail3 = False
            d.press("back")
            Fail4 = True
            click(d,'t',"Storage & cache",1)
            click(d,'t',"CLEAR CACHE",1)
            if d(text="Blocked by your IT admin").exists:
                Fail4 = False
            nPress(d,4,"back",1)
            if not Fail and not Fail2:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)
            click(d,'t',"Disabled force stop button",1)
            if not Fail3:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)
            click(d,'t',"Disabled app storage buttons",1)
            if not Fail4:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)
            if not Fail and not Fail2 and not Fail3 and not Fail4:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
        
        #Camera support cross profile image capture
        if d(text="Camera support cross profile image capture").exists:
            click(d,'t',"Camera support cross profile image capture",1)
            click(d,'t',"GO",1)
            click(d,'t',"WHILE USING THE APP",1)
            click(d,'r',"com.android.camera2:id/shutter_button",3)
            click(d,'r',"com.android.camera2:id/done_button",3)
            runCmd(device,"adb -s %s shell screencap -p /sdcard/imageCapture.png",1)
            click(d,'t',"CLOSE",1)
            click(d,'t',"PASS",1)

        #Camera support cross profile video capture (with extra output path)
        if d(text="Camera support cross profile video capture (with extra output path)").exists:
            click(d,'t',"Camera support cross profile video capture (with extra output path)",1)
            click(d,'t',"GO",1)
            click(d,'r',"com.android.camera2:id/shutter_button",10)
            click(d,'r',"com.android.camera2:id/shutter_button",3)
            click(d,'r',"com.android.camera2:id/done_button",1)
            d(text="PLAY").click()
            runCmd(device,"adb -s %s shell screenrecord --time-limit 15 /sdcard/videoWith.mp4",1)
            click(d,'t',"CLOSE",1)
            click(d,'t',"PASS",1)

        #Camera support cross profile video capture (without extra output path)
        if d(text="Camera support cross profile video capture (without extra output path)").exists:
            click(d,'t',"Camera support cross profile video capture (without extra output path)",1)
            click(d,'t',"GO",1)
            click(d,'r',"com.android.camera2:id/shutter_button",10)
            click(d,'r',"com.android.camera2:id/shutter_button",3)
            click(d,'r',"com.android.camera2:id/done_button",1)
            d(text="PLAY").click()
            runCmd(device,"adb -s %s shell screenrecord --time-limit 15 /sdcard/videoWithout.mp4",1)
            click(d,'t',"CLOSE",1)
            click(d,'t',"FAIL",1)

        d.swipe(540,2000,540,1600,steps=10)
        time.sleep(1)

        #KeyChain test
        if d(text="KeyChain test").exists:
            click(d,'t',"KeyChain test",1)
            click(d,'t',"PREPARE TEST",3)
            click(d,'t',"GO",1)
            click(d,'t',"SELECT",1)
            click(d,'t',"RUN 2ND TEST",1)
            if d(resourceId="com.android.cts.verifier:id/pass_button").enabled:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
            
        d.swipe(540,2000,540,1600,steps=10)
        time.sleep(1)


        x = d.info["displayWidth"] / 2
        y = d.info["displayHeight"] / 2
        #Work profile widget
        if d(text="Work profile widget").exists:
            click(d,'t',"Work profile widget",1)
            click(d,'t',"OK",1)
            nPress(d,2,"home",1)
            d.long_click(x,y)
            click(d,'t',"Widgets",1)
            click(d,'t',"GOT IT",1)
            click(d,'t',"WORK",1)
            click(d,'t',"CTS Verifier",1)
            d.long_click(x,y)
            time.sleep(1)
            d.click(x,y)
            time.sleep(1)
            Fail = False
            if not d(text="This is a test of the widget framework"):
                Fail = True
            nPress(d,2,"recent",1)
            if not Fail:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        #Uninstall work app from launcher
        if d(text="Uninstall work app from launcher").exists:
            click(d,'t',"Uninstall work app from launcher",1)
            runCmd(device,"adb -s %s push NotificationBot.apk /data/local/tmp/",1)
            click(d,'t',"GO",1)
            click(d,'t',"INSTALL",1)
            d.press("home")
            time.sleep(1)
            d.swipe(x,y,x-450,y,10)
            time.sleep(1)
            x = (d(text="CTS Robot").bounds["left"] + d(text="CTS Robot").bounds["right"]) / 2
            y = (d(text="CTS Robot").bounds["top"] + d(text="CTS Robot").bounds["bottom"]) / 2
            d.drag(x,y,x+700,y-50,steps=10)
            time.sleep(1)
            click(d,'t',"OK",1)
            Fail = False
            if d(text="Blocked by your IT admin").exists:
                Fail = True
            nPress(d,2,"recent",1)
            if not Fail:
                click(d,'t',"PASS",1)
            else:
                click(d,'t',"FAIL",1)
            runCmd(device,"adb -s %s shell am start -a android.settings.SETTINGS" ,1)
            d(resourceId="com.android.settings:id/main_content_scrollable_container").scroll.to(text="Security")
            click(d,'t',"Security",1)
            click(d,'t',"Screen lock",1)
            d(resourceId="com.android.settings:id/password_entry").set_text("0000")
            d.press("enter")
            click(d,'t',"None",1)
            click(d,'t',"DELETE",1)
            nPress(d,2,"recent",1)
            d.press("back") 