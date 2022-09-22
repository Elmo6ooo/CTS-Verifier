import resource
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

def Device_Owner_Tests(device):
    d = Device(device)

    if d(text="Device Owner Tests").exists:
        click(d,'t',"Device Owner Tests",1)
        runCmd(device,"adb -s %s install -r -t CtsEmptyDeviceOwner.apk",1)
        runCmd(device,"adb -s %s shell dpm set-device-owner --user 0 com.android.cts.emptydeviceowner/.EmptyDeviceAdmin",1)
        click(d,'t',"OK",1)

        #Check device owner
        if d(text="Check device owner").exists:
            click(d,'t',"Check device owner",1)

        #Device administrator settings
        if d(text="Device administrator settings").exists:
            click(d,'t',"Device administrator settings",1)
            click(d,'t',"GO",1)
            click(d,'t',"Device admin apps",1)
            Fail = False
            if not d(resourceId="android:id/switch_widget")[0].info['checked']:
                Fail = True
            nPress(d,2,"back",1)
            if not Fail:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        #WiFi configuration lockdown
        if d(text="WiFi configuration lockdown").exists:
            click(d,'t',"WiFi configuration lockdown",1)
            click(d,'t',"OK",1)
            d(resourceId="com.android.cts.verifier:id/device_owner_wifi_ssid").set_text("GoogleGuest")
            d.press("back")
            click(d,'t',"None",1)
            click(d,'t',"CREATE WIFI CONFIGURATION",1)
            click(d,'t',"Unlocked config is modifiable in Settings",1)
            click(d,'t',"WIFI CONFIG LOCKDOWN OFF",1)
            click(d,'t',"GO TO WIFI SETTINGS",1)
            click(d,'t',"GoogleGuest",1)
            d(resourceId="com.android.settings:id/collapsing_toolbar").child(className="android.widget.TextView").click()
            time.sleep(1)
            Fail = False
            if d(text="Blocked by your IT admin").exists:
                Fail = True
            nPress(d,3,"back",1)
            if not Fail:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
            click(d,'t',"Locked config is not modifiable in Settings",1)
            click(d,'t',"WIFI CONFIG LOCKDOWN ON",1)
            click(d,'t',"GO TO WIFI SETTINGS",1)
            click(d,'t',"GoogleGuest",1)
            d(resourceId="com.android.settings:id/collapsing_toolbar").child(className="android.widget.TextView").click()
            time.sleep(1)
            Fail2 = False
            if not d(text="Blocked by your IT admin").exists:
                Fail2 = True
            nPress(d,3,"back",1)
            if not Fail2:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
            click(d,'t',"Locked config can be connected to",1)
            click(d,'t',"WIFI CONFIG LOCKDOWN ON",1)
            click(d,'t',"GO TO WIFI SETTINGS",1)
            click(d,'t',"GoogleGuest",1)
            Fail3 = False
            try:
                click(d,'t',"DISCONNECT",1)
                click(d,'t',"CONNECT",1)
            except:
                Fail3 = True
            nPress(d,2,"back",1)
            if not Fail3:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
            click(d,'t',"Unlocked config can be forgotten in Settings",1)
            click(d,'t',"WIFI CONFIG LOCKDOWN OFF",1)
            click(d,'t',"GO TO WIFI SETTINGS",1)
            click(d,'t',"GoogleGuest",1)
            Fail4 = True
            if d(text="FORGET").exists:
                click(d,'t',"FORGET",1)
                Fail4 = False
            d.press("back")
            if not Fail4:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
            if not Fail and not Fail2 and not Fail3 and not Fail4:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
        
        #Disallow configuring WiFi
        if d(text="Disallow configuring WiFi").exists:
            click(d,'t',"Disallow configuring WiFi",1)
            click(d,'t',"SET RESTRICTION",1)
            click(d,'t',"GO",1)
            Fail = False
            if not d(text="Blocked by your IT admin").exists:
                Fail = True
            d.press("back")
            click(d,'t',"CLEAR RESTRICTION (BEFORE LEAVING TEST)",1)
            if not Fail:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        #Disallow configuring VPN
        if d(text="Disallow configuring VPN").exists:
            click(d,'t',"Disallow configuring VPN",1)
            click(d,'t',"SET VPN RESTRICTION",1)
            click(d,'t',"GO",1)
            Fail = False
            if not d(text="Blocked by your IT admin").exists:
                Fail = True
            d.press("back")
            click(d,'t',"CHECK VPN",1)
            if d(text="Cannot establish a VPN connection.\n This was expected.\n Mark this test as passed.\n").exists:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
            click(d,'t',"CLEAR RESTRICTION (BEFORE LEAVING TEST)",1)
            if not Fail:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        #Disallow data roaming
        if d(text="Disallow data roaming").exists:
            click(d,'t',"Disallow data roaming",1)
            click(d,'t',"SET RESTRICTION",1)
            click(d,'t',"GO",1)
            Fail = False
            d(resourceId="com.android.settings:id/recycler_view").scroll.to(text="Roaming")
            click(d,'t',"Roaming",1)
            if not d(text="Blocked by your IT admin").exists:
                Fail = True
            nPress(d,2,'back',1)
            click(d,'t',"CLEAR RESTRICTION (BEFORE LEAVING TEST)",1)
            if not Fail:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        #Disallow factory reset
        if d(text="Disallow factory reset").exists:
            click(d,'t',"Disallow factory reset",1)
            click(d,'t',"SET RESTRICTION",1)
            runCmd(device,"adb -s %s shell am start -a android.settings.SETTINGS" ,1)
            d(resourceId="com.android.settings:id/main_content_scrollable_container").scroll.to(text="System")
            click(d,'t',"System",1)
            click(d,'t',"Reset options",1)
            click(d,'t',"Erase all data (factory reset)",1)
            Fail = False
            if not d(text="Blocked by your IT admin").exists:
                Fail = True
            nPress(d,2,'recent',1)
            click(d,'t',"CLEAR RESTRICTION (BEFORE LEAVING TEST)",1)
            if not Fail:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        d.swipe(540,2000,540,1600,steps=10)
        time.sleep(1)

        #Disallow configuring Bluetooth
        if d(text="Disallow configuring Bluetooth").exists:
            click(d,'t',"Disallow configuring Bluetooth",1)
            click(d,'t',"SET RESTRICTION",1)
            click(d,'t',"GO",1)
            click(d,'t',"Pair new device",1)
            Fail = False
            if not d(text="Blocked by your IT admin").exists:
                Fail = True
            nPress(d,2,"back",1)
            click(d,'t',"CLEAR RESTRICTION (BEFORE LEAVING TEST)",1)
            if not Fail:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        #Disable status bar
        if d(text="Disable status bar").exists:
            click(d,'t',"Disable status bar",1)
            click(d,'t',"DISABLE STATUS BAR",1)
            runCmd(device,"adb -s %s shell cmd statusbar expand-notifications",1)
            Fail = False
            if "Android System notification: USB debugging connected" in d.dump() \
            or d(text="Clear all").exists:
                Fail = True
            click(d,'t',"REENABLE STATUS BAR",1)
            if not Fail:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        #Disable keyguard
        if d(text="Disable keyguard").exists:
            click(d,'t',"Disable keyguard",1)
            click(d,'t',"DISABLE KEYGUARD",1)
            Fail = False
            d.screen.off()
            time.sleep(1)
            d.screen.on()
            time.sleep(1)
            if not d(text="Disable keyguard").exists:
                Fail = True
            click(d,'t',"REENABLE KEYGUARD",1)
            d.screen.off()
            time.sleep(1)
            d.screen.on()
            time.sleep(1)
            if d(text="Disable keyguard").exists:
                Fail = True
            d.swipe(540,2337,540,900,steps=10)
            if not Fail:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        d(resourceId="android:id/list").scroll.to(text="Policy transparency test")
        time.sleep(1)

        #LockTask UI
        '''if d(text="LockTask UI").exists:
            click(d,'t',"LockTask UI",1)
            click(d,'t',"START LOCKTASK MODE",1)
            #Default LockTask UI
            click(d,'t',"Default LockTask UI",1)
            click(d,'t',"DEFAULT LOCKTASK UI",1)
            Fail = False
            if d(resourceId="com.android.systemui:id/clock").exists \
            or d(resourceId="com.android.systemui:id/battery").exists \
            or "Android System notification: USB debugging connected" in d.dump():
                Fail = True
            runCmd(device,"adb -s %s shell cmd statusbar expand-notifications",1)
            if d(text="Clear all").exists:
                Fail = True
                runCmd(device,"adb -s %s shell cmd statusbar collapse",1)
            if d(resourceId="com.android.systemui:id/home").exists \
            or d(resourceId="com.android.systemui:id/recent_apps").exists:
                Fail = True
            runCmd(device,"adb -s %s shell input keyevent --longpress KEYCODE_POWER",1)
            if d(text="Power off").exists:
                Fail = True
            d.screen.off()
            time.sleep(1)
            d.screen.on()
            time.sleep(1)
            if not d(text="Default LockTask UI").exists:
                Fail = True
            runCmd(device,"adb -s %s shell input keyevent 26 keyevent 26",1)
            if not d(text="Default LockTask UI").exists:
                Fail = True
            if not Fail:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
            #Enable system info
            click(d,'t',"Enable system info",1)
            click(d,'t',"ENABLE SYSTEM INFO",1)
            Fail2 = False
            if not d(resourceId="com.android.systemui:id/clock").exists \
            or not d(resourceId="com.android.systemui:id/battery").exists \
            or "Android System notification: USB debugging connected" in d.dump():
                Fail2 = True
            runCmd(device,"adb -s %s shell cmd statusbar expand-notifications",1)
            if d(text="Clear all").exists:
                Fail2 = True
                runCmd(device,"adb -s %s shell cmd statusbar collapse",1)
            if d(resourceId="com.android.systemui:id/home").exists \
            or d(resourceId="com.android.systemui:id/recent_apps").exists:
                Fail2 = True
            runCmd(device,"adb -s %s shell input keyevent --longpress KEYCODE_POWER",1)
            if d(text="Power off").exists:
                Fail2 = True
            d.screen.off()
            time.sleep(1)
            d.screen.on()
            time.sleep(1)
            if not d(text="Enable system info").exists:
                Fail2 = True
            runCmd(device,"adb -s %s shell input keyevent 26 keyevent 26",1)
            if not d(text="Enable system info").exists:
                Fail2 = True
            if not Fail2:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
            #Enable notifications
            click(d,'t',"Enable notifications",1)
            click(d,'t',"ENABLE NOTIFICATIONS",1)
            Fail3 = False
            if d(resourceId="com.android.systemui:id/clock").exists \
            or d(resourceId="com.android.systemui:id/battery").exists \
            or not "Android System notification: USB debugging connected" in d.dump():
                Fail3 = True
            runCmd(device,"adb -s %s shell cmd statusbar expand-notifications",1)
            if not d(text="Clear all").exists:
                Fail3 = True
            runCmd(device,"adb -s %s shell cmd statusbar collapse",1)
            if not d(resourceId="com.android.systemui:id/home").exists \
            or d(resourceId="com.android.systemui:id/recent_apps").exists:
                Fail3 = True
            x = (d(resourceId="com.android.systemui:id/home").bounds["left"] + d(resourceId="com.android.systemui:id/home").bounds["right"]) / 2
            y = (d(resourceId="com.android.systemui:id/home").bounds["top"] + d(resourceId="com.android.systemui:id/home").bounds["bottom"]) / 2
            d.swipe(x,y,x+200,y)
            if not d(text="Enable notifications").exists:
                Fail3 = True
            runCmd(device,"adb -s %s shell input keyevent --longpress KEYCODE_POWER",1)
            if d(text="Power off").exists:
                Fail3 = True
            d.screen.off()
            time.sleep(1)
            d.screen.on()
            time.sleep(1)
            if not d(text="Enable notifications").exists:
                Fail3 = True
            runCmd(device,"adb -s %s shell input keyevent 26 keyevent 26",1)
            if not d(text="Enable notifications").exists:
                Fail3 = True
            if not Fail3:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
            #Enable Home button
            click(d,'t',"Enable Home button",1)
            click(d,'t',"ENABLE HOME BUTTON",1)
            Fail4 = False
            if d(resourceId="com.android.systemui:id/clock").exists \
            or d(resourceId="com.android.systemui:id/battery").exists \
            or "Android System notification: USB debugging connected" in d.dump():
                Fail4 = True
            runCmd(device,"adb -s %s shell cmd statusbar expand-notifications",1)
            if d(text="Clear all").exists:
                Fail4 = True
                runCmd(device,"adb -s %s shell cmd statusbar collapse",1)
            if not d(resourceId="com.android.systemui:id/home").exists \
            or d(resourceId="com.android.systemui:id/recent_apps").exists:
                Fail4 = True
            d.swipe(x,y,x+200,y)
            if not d(text="Enable Home button").exists:
                Fail4 = True
            runCmd(device,"adb -s %s shell input keyevent --longpress KEYCODE_POWER",1)
            if d(text="Power off").exists:
                Fail4 = True
            d.screen.off()
            time.sleep(1)
            d.screen.on()
            time.sleep(1)
            if not d(text="Enable Home button").exists:
                Fail4 = True
            runCmd(device,"adb -s %s shell input keyevent 26 keyevent 26",1)
            if not d(text="Enable Home button").exists:
                Fail4 = True
            if not Fail4:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
            #Enable Overview button
            click(d,'t',"Enable Overview button",1)
            click(d,'t',"ENABLE OVERVIEW BUTTON",1)
            Fail5 = False
            if d(resourceId="com.android.systemui:id/clock").exists \
            or d(resourceId="com.android.systemui:id/battery").exists \
            or "Android System notification: USB debugging connected" in d.dump():
                Fail5 = True
            runCmd(device,"adb -s %s shell cmd statusbar expand-notifications",1)
            if d(text="Clear all").exists:
                Fail5 = True
                runCmd(device,"adb -s %s shell cmd statusbar collapse",1)
            if not d(resourceId="com.android.systemui:id/home").exists \
            or not d(resourceId="com.android.systemui:id/recent_apps").exists:
                Fail5 = True
            nPress(d,2,"recent",1)
            if d(text="Enable Overview button").exists:
                Fail5 = True
            runCmd(device,"adb -s %s shell am start -n com.android.cts.verifier/.CtsVerifierActivity",0)
            runCmd(device,"adb -s %s shell input keyevent --longpress KEYCODE_POWER",1)
            if d(text="Power off").exists:
                Fail5 = True
            d.screen.off()
            time.sleep(1)
            d.screen.on()
            time.sleep(1)
            if not d(text="Enable Overview button").exists:
                Fail5 = True
            runCmd(device,"adb -s %s shell input keyevent 26 keyevent 26",1)
            if not d(text="Enable Overview button").exists:
                Fail5 = True
            if not Fail5:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
            #Enable global actions
            click(d,'t',"Enable global actions",1)
            click(d,'t',"ENABLE GLOBAL ACTIONS",1)
            Fail6 = False
            runCmd(device,"adb -s %s shell input keyevent --longpress KEYCODE_POWER",1)
            if not d(text="Power off").exists:
                Fail6 = True
            if d(resourceId="com.android.systemui:id/clock").exists \
            or d(resourceId="com.android.systemui:id/battery").exists \
            or "Android System notification: USB debugging connected" in d.dump():
                Fail6 = True
            runCmd(device,"adb -s %s shell cmd statusbar expand-notifications",1)
            if d(text="Clear all").exists:
                Fail6 = True
                runCmd(device,"adb -s %s shell cmd statusbar collapse",1)
            if d(resourceId="com.android.systemui:id/home").exists \
            or d(resourceId="com.android.systemui:id/recent_apps").exists:
                Fail6 = True
            d.screen.off()
            time.sleep(1)
            d.screen.on()
            time.sleep(1)
            if not d(text="Enable global actions").exists:
                Fail6 = True
            runCmd(device,"adb -s %s shell input keyevent 26 keyevent 26",1)
            if not d(text="Enable global actions").exists:
                Fail6 = True
            if not Fail6:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
            #Enable keyguard
            click(d,'t',"Enable keyguard",1)
            click(d,'t',"ENABLE KEYGUARD",1)
            Fail7 = True
            if d(resourceId="com.android.systemui:id/lock_icon_view").exists:
                Fail7 = False
                d.swipe(540,2337,540,1000,steps=10)
            if d(resourceId="com.android.systemui:id/clock").exists \
            or d(resourceId="com.android.systemui:id/battery").exists \
            or "Android System notification: USB debugging connected" in d.dump():
                Fail7 = True
            runCmd(device,"adb -s %s shell cmd statusbar expand-notifications",1)
            if d(text="Clear all").exists:
                Fail7 = True
                runCmd(device,"adb -s %s shell cmd statusbar collapse",1)
            if d(resourceId="com.android.systemui:id/home").exists \
            or d(resourceId="com.android.systemui:id/recent_apps").exists:
                Fail7 = True
            runCmd(device,"adb -s %s shell input keyevent --longpress KEYCODE_POWER",1)
            if d(text="Power off").exists:
                Fail7 = True
            runCmd(device,"adb -s %s shell input keyevent 26 keyevent 26",1)
            if not d(text="Enable keyguard").exists:
                Fail7 = True
            if not Fail7:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
            d.swipe(540,2000,540,1000,steps=10)
            #Stop LockTask mode
            click(d,'t',"Stop LockTask mode",1)
            click(d,'t',"STOP LOCKTASK MODE",1)
            Fail8 = False
            if not d(resourceId="com.android.systemui:id/home").exists \
            or not d(resourceId="com.android.systemui:id/recent_apps").exists:
                Fail8 = True
            if not d(resourceId="com.android.systemui:id/clock").exists \
            or not d(resourceId="com.android.systemui:id/battery").exists \
            or not "Android System notification: USB debugging connected" in d.dump():
                Fail8 = True
            if not Fail8:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
            if not Fail and not Fail2 and not Fail3 and not Fail4 and not Fail5 and not Fail6 and not Fail7 and not Fail8:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)'''
            
        #Setting the user icon
        if d(text="Setting the user icon").exists:
            click(d,'t',"Setting the user icon",1)
            click(d,'t',"GO",1)
            click(d,'t',"System",1)
            click(d,'t',"Multiple users",1)
            click(d,'t',"Use multiple users",1)
            nPress(d,2,"recent",1)
            click(d,'t',"SET USER ICON 1",1)
            nPress(d,2,"recent",1)
            runCmd(device,"adb -s %s shell screencap -p /sdcard/userIcon1.png",1)
            nPress(d,2,"recent",1)
            click(d,'t',"DISALLOW SET USER ICON",1)
            click(d,'t',"SET USER ICON 2",1)
            nPress(d,2,"recent",1)
            runCmd(device,"adb -s %s shell screencap -p /sdcard/userIcon2.png",1)
            click(d,'t',"You (Owner)",1)
            click(d,'r',"com.android.settings:id/user_photo",1)
            Fail = False
            if d(text="Take a photo").enabled:
                Fail = True
            nPress(d,2,"recent",1)
            click(d,'t',"CLEAR RESTRICTION (BEFORE LEAVING TEST)",1)
            if not Fail:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        #Permissions lockdown
        if d(text="Permissions lockdown").exists:
            click(d,'t',"Permissions lockdown",1)
            runCmd(device, "adb -s %s install CtsPermissionApp.apk",2)
            click(d,'t',"OK",1)
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
            nPress(d,3,"back",1)
            if not Fail and not Fail2 and not Fail3:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
        
        d.swipe(540,2000,540,1800,steps=10)
        time.sleep(1)

        #Policy transparency test
        if d(text="Policy transparency test").exists:
            click(d,'t',"Policy transparency test",1)
            click(d,'t',"SET SHORT SUPPORT MESSAGE",1)
            click(d,'t',"SET DEFAULT MESSAGE",1)
            click(d,'t',"SET MESSAGE",1)
            d.press("back")
            click(d,'t',"SET LONG SUPPORT MESSAGE",1)
            click(d,'t',"SET DEFAULT MESSAGE",1)
            click(d,'t',"SET MESSAGE",1)
            d.press("back")

            #Disallow add user
            if d(text="Disallow add user").exists:
                click(d,'t',"Disallow add user",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                click(d,'t',"System",1)
                click(d,'t',"Multiple users",1)
                click(d,'t',"Add user",1)
                Fail = False
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail = True
                else:
                    Fail = True
                nPress(d,4,"back",1)
                click(d,'c',"android.widget.Switch",1)
                if not Fail:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Disallow adjust volume
            if d(text="Disallow adjust volume").exists:
                click(d,'t',"Disallow adjust volume",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                Fail2 = False
                if d(text="Media volume").enabled or d(text="Call volume").enabled \
                or d(text="Ring & notification volume").enabled or d(text="Alarm volume").enabled:
                    Fail2 = True
                click(d,'t',"Media volume",1)
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail2 = True
                else:
                    Fail2 = True
                nPress(d,2,"back",1)
                click(d,'c',"android.widget.Switch",1)
                if not Fail2:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Disallow controlling apps
            if d(text="Disallow controlling apps").exists:
                click(d,'t',"Disallow controlling apps",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                click(d,'t',"Contacts",1)
                click(d,'t',"DISABLE",1)
                Fail3 = False
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail3 = True
                else:
                    Fail3 = True
                d.press("back")
                click(d,'t',"FORCE STOP",1)
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail3 = True
                else:
                    Fail3 = True
                nPress(d,2,"back",1)
                click(d,'t',"Cross Profile Test App",1)
                click(d,'t',"UNINSTALL",1)
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail3 = True
                else:
                    Fail3 = True
                nPress(d,3,"back",1)
                click(d,'c',"android.widget.Switch",1)
                if not Fail3:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Disallow config cell broadcasts
            if d(text="Disallow config cell broadcasts").exists:
                click(d,'t',"Disallow config cell broadcasts",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                click(d,'t',"Notifications",1)
                d(scrollable=True).scroll.to(text="Wireless emergency alerts")
                click(d,'t',"Wireless emergency alerts",1)
                Fail4 = False
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail4 = True
                else:
                    Fail4 = True
                nPress(d,3,"back",1)
                click(d,'c',"android.widget.Switch",1)
                if not Fail4:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Disallow config credentials
            if d(text="Disallow config credentials").exists:
                click(d,'t',"Disallow config credentials",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                click(d,'t',"Encryption & credentials",1)
                Fail5 = False
                click(d,'t',"User credentials",1)            
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail5 = True
                else:
                    Fail5 = True
                d.press("back")
                click(d,'t',"Install a certificate",1)            
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail5 = True
                else:
                    Fail5 = True
                d.press("back")
                click(d,'t',"Clear credentials",1)            
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail5 = True
                else:
                    Fail5 = True
                nPress(d,3,"back",1)
                click(d,'c',"android.widget.Switch",1)
                if not Fail5:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Disallow config mobile networks
            if d(text="Disallow config mobile networks").exists:
                click(d,'t',"Disallow config mobile networks",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                click(d,'t',"Internet",1)
                click(d,'r',"com.android.settings:id/settings_button",1)
                Fail6 = False       
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail6 = True
                else:
                    Fail6 = True
                nPress(d,3,"back",1)
                click(d,'c',"android.widget.Switch",1)
                if not Fail6:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Disallow config tethering
            if d(text="Disallow config tethering").exists:
                click(d,'t',"Disallow config tethering",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                click(d,'t',"Hotspot & tethering",1)
                Fail7 = False       
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail7 = True
                else:
                    Fail7 = True
                nPress(d,2,"back",1)
                click(d,'c',"android.widget.Switch",1)
                if not Fail7:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Disallow config Wi-Fi
            if d(text="Disallow config Wi-Fi").exists:
                click(d,'t',"Disallow config Wi-Fi",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                Fail8 = False       
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail8 = True
                else:
                    Fail8 = True
                d.press("back")
                click(d,'c',"android.widget.Switch",1)
                if not Fail8:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Disallow factory reset
            if d(text="Disallow factory reset").exists:
                click(d,'t',"Disallow factory reset",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                d(scrollable=True).scroll.to(text="System")
                click(d,'t',"System",1)
                click(d,'t',"Reset options",1)
                click(d,'t',"Erase all data (factory reset)",1)
                Fail9 = False       
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail9 = True
                else:
                    Fail9 = True
                nPress(d,4,"back",1)
                click(d,'c',"android.widget.Switch",1)
                if not Fail9:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Disallow fun
            if d(text="Disallow fun").exists:
                click(d,'t',"Disallow fun",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                d(scrollable=True).scroll.to(text="Android version")
                click(d,'t',"Android version",1)
                cmd = "adb -s %s shell input tap 540 800" % device
                for i in range(3):
                    os.system(cmd)            
                Fail10 = False       
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail10 = True
                else:
                    Fail10 = True
                nPress(d,3,"back",1)
                click(d,'c',"android.widget.Switch",1)
                if not Fail10:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Disallow install unknown sources
            if d(text="Disallow install unknown sources").exists:
                click(d,'t',"Disallow install unknown sources",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)       
                click(d,'t',"CTS Verifier",1)
                click(d,'t',"Allow from this source",1)
                Fail10 = False       
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail10 = True
                else:
                    Fail10 = True
                nPress(d,3,"back",1)
                click(d,'c',"android.widget.Switch",1)
                if not Fail10:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)
                
            d.swipe(540,1800,540,1200,steps=10)
            time.sleep(1)

            #Disallow modify accounts
            if d(text="Disallow modify accounts").exists:
                click(d,'t',"Disallow modify accounts",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                click(d,'t',"Add account",1)
                Fail11 = False
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail11 = True
                else:
                    Fail11 = True
                nPress(d,2,"back",1)
                click(d,'c',"android.widget.Switch",1)
                if not Fail11:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Disallow network reset
            if d(text="Disallow network reset").exists:
                click(d,'t',"Disallow network reset",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                d(scrollable=True).scroll.to(text="System")
                click(d,'t',"System",1)
                click(d,'t',"Reset options",1)
                click(d,'t',"Reset Wi-Fi, mobile & Bluetooth",1)
                Fail12 = False
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail12 = True
                else:
                    Fail12 = True
                nPress(d,4,"back",1)
                click(d,'c',"android.widget.Switch",1)
                if not Fail12:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Disallow share location
            if d(text="Disallow share location").exists:      
                click(d,'t',"Disallow share location",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                click(d,'t',"Use location",1)
                Fail13 = False
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail13 = True
                else:
                    Fail13 = True
                nPress(d,2,"back",1)
                click(d,'c',"android.widget.Switch",1)
                if not Fail13:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Disallow uninstall apps
            if d(text="Disallow uninstall apps").exists:   
                click(d,'t',"Disallow uninstall apps",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                click(d,'t',"Cross Profile Test App",1)
                click(d,'t',"UNINSTALL",1)
                Fail14 = False
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail14 = True
                else:
                    Fail14 = True
                nPress(d,3,"back",1)
                click(d,'c',"android.widget.Switch",1)
                if not Fail14:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Disallow config date time
            if d(text="Disallow config date time").exists:
                click(d,'t',"Disallow config date time",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                Fail15 = False
                if d(text="Set time automatically").enabled or d(text="Date").enabled or d(text="Time").enabled \
                or d(text="Set time zone automatically").enabled or d(text="Time zone")[1].enabled:
                    Fail15 = True
                click(d,'t',"Date",1)
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail15 = True
                else:
                    Fail15 = True
                nPress(d,2,"back",1)
                click(d,'c',"android.widget.Switch",1)
                if not Fail15:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Disallow config location
            if d(text="Disallow config location").exists:
                click(d,'t',"Disallow config location",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                click(d,'t',"Use location",1)
                Fail16 = False
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail16 = True
                else:
                    Fail16 = True
                nPress(d,2,"back",1)
                click(d,'c',"android.widget.Switch",1)
                if not Fail16:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Disallow airplane mode
            if d(text="Disallow airplane mode").exists:
                click(d,'t',"Disallow airplane mode",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                click(d,'t',"Airplane mode",1)
                Fail17 = False
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail17 = True
                else:
                    Fail17 = True
                nPress(d,2,"back",1)
                click(d,'c',"android.widget.Switch",1)
                if not Fail17:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Disallow config screen timeout
            if d(text="Disallow config screen timeout").exists:
                click(d,'t',"Disallow config screen timeout",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                click(d,'t',"Screen timeout",1)
                Fail18 = False
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail18 = True
                else:
                    Fail18 = True
                nPress(d,2,"back",1)
                click(d,'c',"android.widget.Switch",1)
                if not Fail18:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            d.swipe(540,1800,540,1200,steps=10)
            time.sleep(1)

            #Disallow config brightness
            if d(text="Disallow config brightness").exists:
                click(d,'t',"Disallow config brightness",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                click(d,'t',"Brightness level",1)
                Fail19 = False
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail19 = True
                else:
                    Fail19 = True
                nPress(d,2,"back",1)
                click(d,'c',"android.widget.Switch",1)
                if not Fail19:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Set auto (network) time required
            if d(text="Set auto (network) time required").exists:
                click(d,'t',"Set auto (network) time required",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                Fail20 = False
                if d(text="Set time automatically").enabled or d(text="Date").enabled or d(text="Time").enabled \
                or d(text="Set time zone automatically").enabled or d(text="Time zone")[1].enabled:
                    Fail20 = True
                click(d,'t',"Date",1)
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail20 = True
                else:
                    Fail20 = True
                nPress(d,2,"back",1)
                click(d,'c',"android.widget.Switch",1)
                if not Fail20:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Disallow lockscreen unredacted notification
            if d(text="Disallow lockscreen unredacted notification").exists:
                click(d,'t',"Disallow lockscreen unredacted notification",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                d(scrollable=True).scroll.to(text="Security")
                click(d,'t',"Security",1)
                click(d,'t',"Screen lock",1)
                click(d,'t',"PIN",1)
                d(resourceId="com.android.settings:id/password_entry").set_text("0000")
                click(d,'t',"NEXT",1)
                d(resourceId="com.android.settings:id/password_entry").set_text("0000")
                click(d,'t',"CONFIRM",1)
                click(d,'t',"Show all notification content",1)
                Fail21 = False
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail21 = True
                else:
                    Fail21 = True
                d.press("back")
                click(d,'t',"DONE",1)
                click(d,'t',"Screen lock",1)
                d(resourceId="com.android.settings:id/password_entry").set_text("0000")
                d.press("enter")
                click(d,'t',"None",1)
                click(d,'t',"DELETE",1)
                nPress(d,2,"back",1)
                click(d,'c',"android.widget.Switch",1)
                if not Fail21:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Set lock screen info
            if d(text="Set lock screen info").exists:
                click(d,'t',"Set lock screen info",1)
                d(resourceId="com.android.cts.verifier:id/edit_text_widget").set_text("TEST")
                click(d,'t',"UPDATE",1)
                click(d,'t',"OPEN SETTINGS",1)
                click(d,'t',"Lock screen",1)
                Fail22 = False
                if d(text="Add text on lock screen").down().info["text"] != "TEST":
                    Fail22 = True
                click(d,'t',"Add text on lock screen",1)
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail22 = True
                else:
                    Fail22 = True
                nPress(d,3,"back",1)
                if not Fail22:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Set maximum time to lock
            if d(text="Set maximum time to lock").exists:
                click(d,'t',"Set maximum time to lock",1)
                d(resourceId="com.android.cts.verifier:id/edit_text_widget").set_text("1000")
                click(d,'t',"UPDATE",1)
                click(d,'t',"OPEN SETTINGS",1)
                click(d,'t',"Screen timeout",1)
                Fail23 = False
                if not d(text="10 minutes").exists:
                    Fail23 = True
                nPress(d,2,"back",1)
                if not Fail23:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Set permitted accessibility services
            if d(text="Set permitted accessibility services").exists:
                click(d,'t',"Set permitted accessibility services",1)
                click(d,'c',"android.widget.Switch",1)
                click(d,'t',"OPEN SETTINGS",1)
                click(d,'t',"Test accessibility service",1)
                Fail23 = False
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail23 = True
                else:
                    Fail23 = True
                nPress(d,2,"back",1)
                click(d,'c',"android.widget.Switch",1)
                if not Fail23:
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
                click(d,'t',"On-screen keyboard",1)
                click(d,'t',"Manage on-screen keyboards",1)
                Fail24 = True
                click(d,'t',"Test input method",1)
                if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                    Fail24 = False
                    click(d,'t',"LEARN MORE",1)
                    if not d(text="Your admin can monitor and manage apps and data associated with this device, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                        Fail24 = True
                nPress(d,6,"back",1)
                click(d,'c',"android.widget.Switch",1)
                if not Fail24:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)
                d.press("back")
            
            d(scrollable=True).scroll.to(text="Policy transparency test")
            time.sleep(1)
            
        #Managed device info tests
        if d(text="Managed device info tests").exists:
            click(d,'t',"Managed device info tests",1)

            #Managed device info page
            if d(text="Managed device info page").exists:
                click(d,'t',"Managed device info page",1)
                click(d,'t',"GO",1)
                d(scrollable=True).scroll.to(text="Security")
                click(d,'t',"Security",1)
                Fail = False
                if d(text="Managed device info").exists:
                    click(d,'t',"Managed device info",1)
                else:
                    Fail = True
                nPress(d,2,"recent",1)
                if not Fail:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)
            
            #Retrieve traffic logs
            if d(text="Retrieve traffic logs").exists:
                click(d,'t',"Retrieve traffic logs",1)
                click(d,'t',"RETRIEVE TRAFFIC LOGS",1)
                click(d,'t',"OPEN SETTINGS",1)
                Fail2 = False
                if not d(text="Most recent network traffic log").exists:
                    Fail2 = True
                d.press("back")
                if not Fail2:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Request bug report
            if d(text="Request bug report").exists:
                click(d,'t',"Request bug report",1)
                click(d,'t',"REQUEST BUG REPORT",1)
                click(d,'t',"OPEN SETTINGS",1)
                runCmd(device,"adb -s %s shell cmd statusbar expand-notifications",1)
                click(d,'t',"Taking bug report…",1)
                click(d,'t',"DECLINE",1)
                runCmd(device,"adb -s %s shell cmd statusbar expand-notifications",1)
                click(d,'t',"Clear all",1)
                Fail3 = False
                if d(text="Most recent bug report").down().info["text"] == "None":
                    Fail3 = True
                d.press("back")
                if not Fail3:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)
            
            #Retrieve security logs
            if d(text="Retrieve security logs").exists:
                click(d,'t',"Retrieve security logs",1)
                click(d,'t',"RETRIEVE SECURITY LOGS",1)
                click(d,'t',"OPEN SETTINGS",1)
                Fail4 = False
                if not d(text="Most recent security log").exists:
                    Fail4 = True
                d.press("back")
                if not Fail4:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Enterprise-installed apps
            if d(text="Enterprise-installed apps").exists:
                click(d,'t',"Enterprise-installed apps",1)
                runCmd(device,"adb -s %s shell appops set com.android.cts.verifier MANAGE_EXTERNAL_STORAGE 0",1)
                runCmd(device,"adb -s %s push NotificationBot.apk /sdcard",1)
                click(d,'t',"UNINSTALL",1)
                click(d,'t',"OPEN SETTINGS",1)
                Fail5 = False
                d(scrollable=True).scroll.toEnd()
                if d(text="Apps installed").exists:
                    Fail5 = True
                d.press("back")
                click(d,'t',"INSTALL",1)
                click(d,'t',"OPEN SETTINGS",1)
                d(scrollable=True).scroll.toEnd()
                if not d(text="Apps installed").exists:
                    Fail5 = True
                d.press("back")
                click(d,'t',"UNINSTALL",1)
                runCmd(device,"adb -s %s shell rm /sdcard/NotificationBot.apk",1)
                if not Fail5:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Location access permission
            if d(text="Location access permission").exists:
                click(d,'t',"Location access permission",1)
                click(d,'t',"RESET",1)
                click(d,'t',"GRANT",1)
                runCmd(device,"adb -s %s shell cmd statusbar expand-notifications",1)
                Fail6 = False
                if not d(text="Location can be accessed").exists:
                    Fail6 = True
                click(d,'t',"Clear all",1)
                if not Fail6:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Microphone access permission
            if d(text="Microphone access permission").exists:
                click(d,'t',"Microphone access permission",1)
                click(d,'t',"RESET",1)
                click(d,'t',"OPEN SETTINGS",1)
                Fail7 = False
                d(scrollable=True).scroll.toEnd()
                if d(text="Microphone permissions").exists:
                    Fail7 = True
                d.press("back")
                click(d,'t',"GRANT",1)
                click(d,'t',"OPEN SETTINGS",1)
                d(scrollable=True).scroll.toEnd()
                if not d(text="Microphone permissions").exists:
                    Fail7 = True
                d.press("back")
                click(d,'t',"RESET",1)
                if not Fail7:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)
            
            #Camera access permission
            if d(text="Camera access permission").exists:
                click(d,'t',"Camera access permission",1)
                click(d,'t',"RESET",1)
                click(d,'t',"OPEN SETTINGS",1)
                Fail8 = False
                d(scrollable=True).scroll.toEnd()
                if d(text="Camera permissions").exists:
                    Fail8 = True
                d.press("back")
                click(d,'t',"GRANT",1)
                click(d,'t',"OPEN SETTINGS",1)
                d(scrollable=True).scroll.toEnd()
                if not d(text="Camera permissions").exists:
                    Fail8 = True
                d.press("back")
                click(d,'t',"RESET",1)
                if not Fail8:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)
            
            #Default apps
            if d(text="Default apps").exists:
                click(d,'t',"Default apps",1)
                click(d,'t',"RESET",1)
                click(d,'t',"OPEN SETTINGS",1)
                Fail9 = False
                d(scrollable=True).scroll.toEnd()
                if d(text="Default apps").exists:
                    Fail9 = True
                d.press("back")
                click(d,'t',"SET DEFAULT APPS",1)
                click(d,'t',"OPEN SETTINGS",1)
                d(scrollable=True).scroll.toEnd()
                if d(text="Default apps").down().info["text"] != "6 apps":
                    Fail9 = True
                d.press("back")
                click(d,'t',"RESET",1)
                if not Fail9:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Default keyboard
            if d(text="Default keyboard").exists:
                click(d,'t',"Default keyboard",1)
                click(d,'t',"OPEN SETTINGS",1)
                Fail10 = False
                d(scrollable=True).scroll.toEnd()
                if d(text="Default keyboard").exists:
                    Fail10 = True
                d.press("back")
                click(d,'t',"SET KEYBOARD",1)
                click(d,'t',"OPEN SETTINGS",1)
                d(scrollable=True).scroll.toEnd()
                if d(text="Default keyboard").down().info["text"] != "Set to CTS Verifier":
                    Fail10 = True
                d.press("back")
                click(d,'t',"FINISH",1)
                if not Fail10:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Always-on VPN
            if d(text="Always-on VPN").exists:
                click(d,'t',"Always-on VPN",1)
                click(d,'t',"OPEN SETTINGS",1)
                Fail11 = False
                d(scrollable=True).scroll.toEnd()
                if d(text="Always-on VPN turned on").exists:
                    Fail11 = True
                d.press("back")
                click(d,'t',"SET VPN",1)
                click(d,'t',"OPEN SETTINGS",1)
                d(scrollable=True).scroll.toEnd()
                if not d(text="Always-on VPN turned on").exists:
                    Fail11 = True
                d.press("back")
                click(d,'t',"FINISH",1)
                if not Fail11:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)          

            #Global HTTP Proxy
            if d(text="Global HTTP Proxy").exists:
                click(d,'t',"Global HTTP Proxy",1)
                click(d,'t',"OPEN SETTINGS",1)
                Fail12 = False
                d(scrollable=True).scroll.toEnd()
                if d(text="Global HTTP proxy set").exists:
                    Fail12 = True
                d.press("back")
                click(d,'t',"SET PROXY",1)
                click(d,'t',"OPEN SETTINGS",1)
                d(scrollable=True).scroll.toEnd()
                if not d(text="Global HTTP proxy set").exists:
                    Fail12 = True
                d.press("back")
                click(d,'t',"CLEAR PROXY",1)
                if not Fail12:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Trusted CA certs
            if d(text="Trusted CA certs").exists:
                click(d,'t',"Trusted CA certs",1)
                click(d,'t',"OPEN SETTINGS",1)
                Fail13 = False
                d(scrollable=True).scroll.toEnd()
                if d(text="Trusted credentials").exists:
                    Fail13 = True
                d.press("back")
                click(d,'t',"INSTALL CERT",1)
                click(d,'t',"OPEN SETTINGS",1)
                d(scrollable=True).scroll.toEnd()
                if not d(text="Trusted credentials").exists:
                    Fail13 = True
                d.press("back")
                click(d,'t',"FINISH",1)
                if not Fail13:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            d(scrollable=True).scroll.toEnd()
            time.sleep(1)

            #Wipe on authentication failure
            if d(text="Wipe on authentication failure").exists:
                click(d,'t',"Wipe on authentication failure",1)
                click(d,'t',"OPEN SETTINGS",1)
                Fail14 = False
                d(scrollable=True).scroll.toEnd()
                if d(text="Failed password attempts before deleting all device data").exists:
                    Fail14 = True
                d.press("back")
                click(d,'t',"SET LIMIT",1)
                click(d,'t',"OPEN SETTINGS",1)
                d(scrollable=True).scroll.toEnd()
                if not d(text="Failed password attempts before deleting all device data").exists:
                    Fail14 = True
                d.press("back")
                click(d,'t',"FINISH",1)
                if not Fail14:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Quick settings disclosure
            if d(text="Quick settings disclosure").exists:
                click(d,'t',"Quick settings disclosure",1)
                click(d,'t',"CLEAR ORG",1)
                runCmd(device,"adb -s %s shell cmd statusbar expand-settings",1)
                Fail15 = False
                if not d(text="This device belongs to your organization").exists:
                    Fail15 = True
                runCmd(device,"adb -s %s shell cmd statusbar collapse",1)
                click(d,'t',"SET ORG",1)
                runCmd(device,"adb -s %s shell cmd statusbar expand-settings",1)
                if not d(text="This device belongs to Foo, Inc.").exists:
                    Fail15 = True
                else:
                    click(d,'t',"This device belongs to Foo, Inc.",1)
                    click(d,'t',"VIEW POLICIES",1)
                    if not d(text="Types of information your organization can see").exists:
                        Fail15 = True
                d.press("back")
                click(d,'t',"CLEAR ORG",1)
                if not Fail15:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Keyguard disclosure
            if d(text="Keyguard disclosure").exists:
                click(d,'t',"Keyguard disclosure",1)
                #SWIPE
                click(d,'t',"CLEAR ORG",1)
                d.screen.off()
                time.sleep(1)
                d.screen.on()
                time.sleep(1)
                Fail16 = False
                while not d(text="This device belongs to your organization"):
                    i = 0
                    time.sleep(1)
                    i = i + 1
                    if i == 10:
                        Fail16 = True
                        break
                d.swipe(540,2337,540,900,steps=10)
                click(d,'t',"SET ORG",1)
                d.screen.off()
                time.sleep(1)
                d.screen.on()
                time.sleep(1)
                while not d(text="This device belongs to Foo, Inc."):
                    i = 0
                    time.sleep(1)
                    i = i + 1
                    if i == 10:
                        Fail16 = True
                        break
                d.swipe(540,2337,540,900,steps=10)

                #PATTERN
                click(d,'t',"OPEN SETTINGS",1)
                d(scrollable=True).scroll.to(text="Security")
                click(d,'t',"Security",1)
                click(d,'t',"Screen lock",1)
                click(d,'t',"Pattern",1)
                d.swipePoints([(237,1168),(237,1768),(837,1768)],steps=20)
                click(d,'t',"NEXT",1)
                d.swipePoints([(237,1168),(237,1700),(837,1700)],steps=20)
                click(d,'t',"CONFIRM",1)
                click(d,'t',"DONE",1)
                nPress(d,2,"back",1)
                click(d,'t',"CLEAR ORG",1)
                d.screen.off()
                time.sleep(1)
                d.screen.on()
                time.sleep(1)
                while not d(text="This device belongs to your organization"):
                    i = 0
                    time.sleep(1)
                    i = i + 1
                    if i == 10:
                        Fail16 = True
                        break
                d.swipe(540,2337,540,900,steps=10)
                time.sleep(1)
                d.swipePoints([(237,1300),(237,1875),(837,1875)],steps=20)
                click(d,'t',"SET ORG",1)
                d.screen.off()
                time.sleep(1)
                d.screen.on()
                time.sleep(1)
                while not d(text="This device belongs to Foo, Inc."):
                    i = 0
                    time.sleep(1)
                    i = i + 1
                    if i == 10:
                        Fail16 = True
                        break
                d.swipe(540,2337,540,900,steps=10)
                time.sleep(1)
                d.swipePoints([(237,1300),(237,1875),(837,1875)],steps=20)
                
                #PIN
                click(d,'t',"OPEN SETTINGS",1)
                d(scrollable=True).scroll.to(text="Security")
                click(d,'t',"Security",1)
                click(d,'t',"Screen lock",1)
                d.swipePoints([(237,1150),(237,1700),(837,1700)],steps=20) 
                click(d,'t',"PIN",1)
                d(resourceId="com.android.settings:id/password_entry").set_text("0000")
                click(d,'t',"NEXT",1)
                d(resourceId="com.android.settings:id/password_entry").set_text("0000")
                click(d,'t',"CONFIRM",1)
                nPress(d,2,"back",1)
                click(d,'t',"CLEAR ORG",1)
                d.screen.off()
                time.sleep(1)
                d.screen.on()
                time.sleep(1)
                while not d(text="This device belongs to your organization"):
                    i = 0
                    time.sleep(1)
                    i = i + 1
                    if i == 10:
                        Fail16 = True
                        break
                d.swipe(540,2337,540,900,steps=10)
                for i in range(4):  click(d,'r',"com.android.systemui:id/key0",0)
                d.press("enter")
                click(d,'t',"SET ORG",1)
                d.screen.off()
                time.sleep(1)
                d.screen.on()
                time.sleep(1)
                while not d(text="This device belongs to Foo, Inc."):
                    i = 0
                    time.sleep(1)
                    i = i + 1
                    if i == 10:
                        Fail16 = True
                        break
                d.swipe(540,2337,540,900,steps=10)
                for i in range(4):  click(d,'r',"com.android.systemui:id/key0",0)
                d.press("enter")
                
                #PASSWORD
                click(d,'t',"OPEN SETTINGS",1)
                d(scrollable=True).scroll.to(text="Security")
                click(d,'t',"Security",1)
                click(d,'t',"Screen lock",1)
                d(resourceId="com.android.settings:id/password_entry").set_text("0000")
                d.press("enter")
                time.sleep(1)
                click(d,'t',"Password",1)
                d(resourceId="com.android.settings:id/password_entry").set_text("test")
                click(d,'t',"NEXT",1)
                d(resourceId="com.android.settings:id/password_entry").set_text("test")
                click(d,'t',"CONFIRM",1)
                nPress(d,2,"back",1)
                click(d,'t',"CLEAR ORG",1)
                d.screen.off()
                time.sleep(1)
                d.screen.on()
                time.sleep(1)
                while not d(text="This device belongs to your organization"):
                    i = 0
                    time.sleep(1)
                    i = i + 1
                    if i == 10:
                        Fail16 = True
                        break
                d.swipe(540,2337,540,900,steps=10)
                d(resourceId="com.android.systemui:id/passwordEntry").set_text("test")
                d.press("enter")
                click(d,'t',"SET ORG",1)
                d.screen.off()
                time.sleep(1)
                d.screen.on()
                time.sleep(1)
                while not d(text="This device belongs to Foo, Inc."):
                    i = 0
                    time.sleep(1)
                    i = i + 1
                    if i == 10:
                        Fail16 = True
                        break
                d.swipe(540,2337,540,900,steps=10)
                d(resourceId="com.android.systemui:id/passwordEntry").set_text("test")
                d.press("enter")
                click(d,'t',"OPEN SETTINGS",1)
                d(scrollable=True).scroll.to(text="Security")
                click(d,'t',"Security",1)
                click(d,'t',"Screen lock",1)
                d(resourceId="com.android.settings:id/password_entry").set_text("test")
                d.press("enter")
                time.sleep(1)
                click(d,'t',"None",1)
                click(d,'t',"DELETE",1)
                nPress(d,2,"back",1)
                click(d,'t',"CLEAR ORG",1)
                if not Fail16:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Add account disclosure(blocked)
            if d(text="Add account disclosure").exists:
                click(d,'t',"Add account disclosure",1)
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)   

            click(d,'r',"com.android.cts.verifier:id/fail_button",1)   

            d(scrollable=True).scroll.to(text="Managed device info tests")

        #Managed User
        if d(text="Managed User").exists:
            result = False
            click(d,'t',"Managed User",1)
            click(d,'t',"GO",7)
            d.swipe(540,2337,540,900,steps=10)
            click(d,'t',"OK",1)
            runCmd(device,"adb -s %s install -r -t --user 12 CrossProfileTestApp.apk",1)

            #Check affiliated profile owner
            if d(text="Check affiliated profile owner").exists:
                click(d,'t',"Check affiliated profile owner",1)

            #Device administrator settings
            if d(text="Device administrator settings").exists:
                click(d,'t',"Device administrator settings",1)
                click(d,'t',"GO",1)
                click(d,'t',"Device admin apps",1)
                Fail = False
                if not d(resourceId="android:id/switch_widget")[0].info['checked']:
                    Fail = True
                nPress(d,2,"back",1)
                if not Fail:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            #Disable status bar
            if d(text="Disable status bar").exists:
                click(d,'t',"Disable status bar",1)
                click(d,'t',"DISABLE STATUS BAR",1)
                runCmd(device,"adb -s %s shell cmd statusbar expand-notifications",1)
                Fail2 = False
                if "Android System notification: USB debugging connected" in d.dump() \
                or d(text="Clear all").exists:
                    Fail2 = True
                click(d,'t',"REENABLE STATUS BAR",1)
                if not Fail2:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)
            

            #Disable keyguard
            if d(text="Disable keyguard").exists:
                click(d,'t',"Disable keyguard",1)
                click(d,'t',"DISABLE KEYGUARD",1)
                Fail3 = False
                d.screen.off()
                time.sleep(1)
                d.screen.on()
                time.sleep(1)
                if not d(text="Disable keyguard").exists:
                    Fail3 = True
                click(d,'t',"REENABLE KEYGUARD",1)
                d.screen.off()
                time.sleep(1)
                d.screen.on()
                time.sleep(1)
                if d(text="Disable keyguard").exists:
                    Fail3 = True
                d.swipe(540,2337,540,900,steps=10)
                if not Fail3:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)
            
            #Disallow remove user
            if d(text="Disallow remove user").exists:
                click(d,'t',"Disallow remove user",1)
                click(d,'t',"SET RESTRICTION",1)
                click(d,'t',"GO",1)
                d(className="android.widget.ImageButton")[1].click()
                time.sleep(1)
                click(d,'t',"Delete managed user from this device ",1)
                Fail4 = False
                if not  d(text="Blocked by your IT admin").exists:
                    Fail4 = True
                nPress(d,2,"back",1)
                if not Fail4:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)
            
            #Policy transparency test
            if d(text="Policy transparency test").exists:
                click(d,'t',"Policy transparency test",1)
                click(d,'t',"OK",1)
                click(d,'t',"SET SHORT SUPPORT MESSAGE",1)
                click(d,'t',"SET DEFAULT MESSAGE",1)
                click(d,'t',"SET MESSAGE",1)
                d.press("back")
                click(d,'t',"SET LONG SUPPORT MESSAGE",1)
                click(d,'t',"SET DEFAULT MESSAGE",1)
                click(d,'t',"SET MESSAGE",1)
                d.press("back")

                #Disallow adjust volume
                if d(text="Disallow adjust volume").exists:
                    click(d,'t',"Disallow adjust volume",1)
                    click(d,'c',"android.widget.Switch",1)
                    click(d,'t',"OPEN SETTINGS",1)
                    Fail = False
                    if d(text="Media volume").enabled or d(text="Call volume").enabled \
                    or d(text="Ring & notification volume").enabled or d(text="Alarm volume").enabled:
                        Fail = True
                    click(d,'t',"Media volume",1)
                    if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                        click(d,'t',"LEARN MORE",1)
                        if not d(text="Your admin can monitor and manage apps and data associated with this user, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                            Fail = True
                    else:
                        Fail = True
                    nPress(d,2,"back",1)
                    click(d,'c',"android.widget.Switch",1)
                    if not Fail:
                        click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                    else:
                        click(d,'r',"com.android.cts.verifier:id/fail_button",1)

                #Disallow controlling apps
                if d(text="Disallow controlling apps").exists:
                    click(d,'t',"Disallow controlling apps",1)
                    click(d,'c',"android.widget.Switch",1)
                    click(d,'t',"OPEN SETTINGS",1)
                    click(d,'t',"Contacts",1)
                    click(d,'t',"DISABLE",1)
                    Fail2 = False
                    if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                        click(d,'t',"LEARN MORE",1)
                        if not d(text="Your admin can monitor and manage apps and data associated with this user, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                            Fail2 = True
                    else:
                        Fail2 = True
                    d.press("back")
                    click(d,'t',"FORCE STOP",1)
                    if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                        click(d,'t',"LEARN MORE",1)
                        if not d(text="Your admin can monitor and manage apps and data associated with this user, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                            Fail2 = True
                    else:
                        Fail2 = True
                    nPress(d,2,"back",1)
                    click(d,'t',"Cross Profile Test App",1)
                    click(d,'t',"UNINSTALL",1)
                    if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                        click(d,'t',"LEARN MORE",1)
                        if not d(text="Your admin can monitor and manage apps and data associated with this user, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                            Fail2 = True
                    else:
                        Fail2 = True
                    nPress(d,3,"back",1)
                    click(d,'c',"android.widget.Switch",1)
                    if not Fail2:
                        click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                    else:
                        click(d,'r',"com.android.cts.verifier:id/fail_button",1)

                #Disallow config Wi-Fi
                if d(text="Disallow config Wi-Fi").exists:
                    click(d,'t',"Disallow config Wi-Fi",1)
                    click(d,'c',"android.widget.Switch",1)
                    click(d,'t',"OPEN SETTINGS",1)
                    Fail3 = False       
                    if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                        click(d,'t',"LEARN MORE",1)
                        if not d(text="Your admin can monitor and manage apps and data associated with this user, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                            Fail3 = True
                    else:
                        Fail3 = True
                    d.press("back")
                    click(d,'c',"android.widget.Switch",1)
                    if not Fail3:
                        click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                    else:
                        click(d,'r',"com.android.cts.verifier:id/fail_button",1)

                #Disallow install unknown sources
                if d(text="Disallow install unknown sources").exists:
                    click(d,'t',"Disallow install unknown sources",1)
                    click(d,'c',"android.widget.Switch",1)
                    click(d,'t',"OPEN SETTINGS",1)       
                    click(d,'t',"CTS Verifier",1)
                    click(d,'t',"Allow from this source",1)
                    Fail4 = False       
                    if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                        click(d,'t',"LEARN MORE",1)
                        if not d(text="Your admin can monitor and manage apps and data associated with this user, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                            Fail4 = True
                    else:
                        Fail4 = True
                    nPress(d,3,"back",1)
                    click(d,'c',"android.widget.Switch",1)
                    if not Fail4:
                        click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                    else:
                        click(d,'r',"com.android.cts.verifier:id/fail_button",1)

                #Disallow modify accounts
                if d(text="Disallow modify accounts").exists:
                    click(d,'t',"Disallow modify accounts",1)
                    click(d,'c',"android.widget.Switch",1)
                    click(d,'t',"OPEN SETTINGS",1)
                    click(d,'t',"Add account",1)
                    Fail5 = False
                    if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                        click(d,'t',"LEARN MORE",1)
                        if not d(text="Your admin can monitor and manage apps and data associated with this user, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                            Fail5 = True
                    else:
                        Fail5 = True
                    nPress(d,2,"back",1)
                    click(d,'c',"android.widget.Switch",1)
                    if not Fail5:
                        click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                    else:
                        click(d,'r',"com.android.cts.verifier:id/fail_button",1)

                #Disallow share location
                if d(text="Disallow share location").exists:      
                    click(d,'t',"Disallow share location",1)
                    click(d,'c',"android.widget.Switch",1)
                    click(d,'t',"OPEN SETTINGS",1)
                    click(d,'t',"Use location",1)
                    Fail6 = False
                    if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                        click(d,'t',"LEARN MORE",1)
                        if not d(text="Your admin can monitor and manage apps and data associated with this user, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                            Fail6 = True
                    else:
                        Fail6 = True
                    nPress(d,2,"back",1)
                    click(d,'c',"android.widget.Switch",1)
                    if not Fail6:
                        click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                    else:
                        click(d,'r',"com.android.cts.verifier:id/fail_button",1)

                #Disallow uninstall apps
                if d(text="Disallow uninstall apps").exists:   
                    click(d,'t',"Disallow uninstall apps",1)
                    click(d,'c',"android.widget.Switch",1)
                    click(d,'t',"OPEN SETTINGS",1)
                    click(d,'t',"Cross Profile Test App",1)
                    click(d,'t',"UNINSTALL",1)
                    Fail7 = False
                    if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                        click(d,'t',"LEARN MORE",1)
                        if not d(text="Your admin can monitor and manage apps and data associated with this user, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                            Fail7 = True
                    else:
                        Fail7 = True
                    nPress(d,3,"back",1)
                    click(d,'c',"android.widget.Switch",1)
                    if not Fail7:
                        click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                    else:
                        click(d,'r',"com.android.cts.verifier:id/fail_button",1)

                #Disallow config date time
                if d(text="Disallow config date time").exists:
                    click(d,'t',"Disallow config date time",1)
                    click(d,'c',"android.widget.Switch",1)
                    click(d,'t',"OPEN SETTINGS",1)
                    Fail8 = False
                    if d(text="Set time automatically").enabled or d(text="Date").enabled or d(text="Time").enabled \
                    or d(text="Set time zone automatically").enabled or d(text="Time zone")[1].enabled:
                        Fail8 = True
                    click(d,'t',"Date",1)
                    if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                        click(d,'t',"LEARN MORE",1)
                        if not d(text="Your admin can monitor and manage apps and data associated with this user, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                            Fail8 = True
                    else:
                        Fail8 = True
                    nPress(d,2,"back",1)
                    click(d,'c',"android.widget.Switch",1)
                    if not Fail8:
                        click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                    else:
                        click(d,'r',"com.android.cts.verifier:id/fail_button",1)

                #Disallow config location
                if d(text="Disallow config location").exists:
                    click(d,'t',"Disallow config location",1)
                    click(d,'c',"android.widget.Switch",1)
                    click(d,'t',"OPEN SETTINGS",1)
                    click(d,'t',"Use location",1)
                    Fail9 = False
                    if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                        click(d,'t',"LEARN MORE",1)
                        if not d(text="Your admin can monitor and manage apps and data associated with this user, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                            Fail9 = True
                    else:
                        Fail9 = True
                    nPress(d,2,"back",1)
                    click(d,'c',"android.widget.Switch",1)
                    if not Fail9:
                        click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                    else:
                        click(d,'r',"com.android.cts.verifier:id/fail_button",1)

                #Disallow config screen timeout
                if d(text="Disallow config screen timeout").exists:
                    click(d,'t',"Disallow config screen timeout",1)
                    click(d,'c',"android.widget.Switch",1)
                    click(d,'t',"OPEN SETTINGS",1)
                    click(d,'t',"Screen timeout",1)
                    Fail10 = False
                    if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                        click(d,'t',"LEARN MORE",1)
                        if not d(text="Your admin can monitor and manage apps and data associated with this user, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                            Fail10 = True
                    else:
                        Fail10 = True
                    nPress(d,2,"back",1)
                    click(d,'c',"android.widget.Switch",1)
                    if not Fail10:
                        click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                    else:
                        click(d,'r',"com.android.cts.verifier:id/fail_button",1)

                #Disallow config brightness
                if d(text="Disallow config brightness").exists:
                    click(d,'t',"Disallow config brightness",1)
                    click(d,'c',"android.widget.Switch",1)
                    click(d,'t',"OPEN SETTINGS",1)
                    click(d,'t',"Brightness level",1)
                    Fail11 = False
                    if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                        click(d,'t',"LEARN MORE",1)
                        if not d(text="Your admin can monitor and manage apps and data associated with this user, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                            Fail11 = True
                    else:
                        Fail11 = True
                    nPress(d,2,"back",1)
                    click(d,'c',"android.widget.Switch",1)
                    if not Fail11:
                        click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                    else:
                        click(d,'r',"com.android.cts.verifier:id/fail_button",1)

                #Set permitted accessibility services
                if d(text="Set permitted accessibility services").exists:
                    click(d,'t',"Set permitted accessibility services",1)
                    click(d,'c',"android.widget.Switch",1)
                    click(d,'t',"OPEN SETTINGS",1)
                    click(d,'t',"Test accessibility service",1)
                    Fail12 = False
                    if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                        click(d,'t',"LEARN MORE",1)
                        if not d(text="Your admin can monitor and manage apps and data associated with this user, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                            Fail12 = True
                    else:
                        Fail12 = True
                    nPress(d,2,"back",1)
                    click(d,'c',"android.widget.Switch",1)
                    if not Fail12:
                        click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                    else:
                        click(d,'r',"com.android.cts.verifier:id/fail_button",1)

                if d(scrollable=True):
                    d(scrollable=True).scroll.toEnd()
                    time.sleep(1)

                #Set permitted input methods
                if d(text="Set permitted input methods").exists:
                    click(d,'t',"Set permitted input methods",1)
                    click(d,'c',"android.widget.Switch",1)
                    click(d,'t',"OPEN SETTINGS",1)
                    d(className="android.widget.ScrollView").scroll.to(text="System")
                    click(d,'t',"System",1)
                    click(d,'t',"Languages & input",1)
                    click(d,'t',"On-screen keyboard",1)
                    click(d,'t',"Manage on-screen keyboards",1)
                    Fail13 = True
                    click(d,'t',"Test input method",1)
                    if d(text="This action is disabled by your administrator. Contact someone@example.com for support.").exists:
                        Fail13 = False
                        click(d,'t',"LEARN MORE",1)
                        if not d(text="Your admin can monitor and manage apps and data associated with this user, including settings, permissions, corporate access, network activity, and the device's location information.").exists:
                            Fail13 = True
                    nPress(d,6,"back",1)
                    click(d,'c',"android.widget.Switch",1)
                    if not Fail13:
                        click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                    else:
                        click(d,'r',"com.android.cts.verifier:id/fail_button",1)

                if d(resourceId="com.android.cts.verifier:id/pass_button").enabled:
                    click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                else:
                    click(d,'r',"com.android.cts.verifier:id/fail_button",1)

            if d(resourceId="com.android.cts.verifier:id/pass_button").enabled:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
                result = True
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
            
            time.sleep(1)
            d.swipe(540,2337,540,900,steps=10)
            time.sleep(1)
            nPress(d,2,"recent",1)
            if result:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
    
        d(scrollable=True).scroll.toEnd()
        time.sleep(1)

        #Disallow user switch
        if d(text="Disallow user switch").exists:
            click(d,'t',"Disallow user switch",1)
            click(d,'t',"CREATE UNINITIALIZED USER",1)
            click(d,'t',"SET RESTRICTION",1)
            click(d,'t',"GO",1)
            Fail = False
            if d(text="Use multiple users").enabled:
                Fail = True
            d.press("back")
            click(d,'t',"CLEAR RESTRICTION (BEFORE LEAVING TEST)",1)
            if not Fail:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        #Disallow remove user
        if d(text="Disallow remove user").exists:
            click(d,'t',"Disallow remove user",1)
            click(d,'t',"SET RESTRICTION",1)
            click(d,'t',"GO",1)
            click(d,'t',"managed user",1)
            click(d,'t',"Delete user",1)            
            Fail = False
            if not d(text="Blocked by your IT admin"):
                Fail = True
            nPress(d,3,"back",1)
            click(d,'t',"CLEAR RESTRICTION (BEFORE LEAVING TEST)",1)
            click(d,'t',"REMOVE UNINITIALIZED USER",1)
            if not Fail:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        #Network Logging UI
        if d(text="Network Logging UI").exists:
            click(d,'t',"Network Logging UI",1)
            Fail = False
            runCmd(device,"adb -s %s shell cmd statusbar expand-settings",1)
            if not d(text="This device belongs to your organization"):
                Fail = True
            runCmd(device,"adb -s %s shell cmd statusbar collapse",1)
            click(d,'t',"ENABLE NETWORK LOGGING",1)
            runCmd(device,"adb -s %s shell cmd statusbar expand-settings",1)
            click(d,'t',"Your organization owns this device and may monitor network traffic",1)
            if not d(text="Device management").exists:
                Fail = True
            click(d,'t',"OK",1)
            runCmd(device,"adb -s %s shell cmd statusbar collapse",1)
            click(d,'t',"DISABLE NETWORK LOGGING",1)
            runCmd(device,"adb -s %s shell cmd statusbar expand-notifications",1)
            if d(text="Device is managed").exists:
                Fail = True
            runCmd(device,"adb -s %s shell cmd statusbar collapse",1)
            if not Fail:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        #Customize Lock Screen Message
        if d(text="Customize Lock Screen Message").exists:
            click(d,'t',"Customize Lock Screen Message",1)
            d(resourceId="com.android.cts.verifier:id/lockscreen_message_edit_text").set_text("TEST")
            d.press("back") 
            click(d,'t',"SET LOCK SCREEN MESSAGE",1)
            d.screen.off()
            time.sleep(1)
            d.screen.on()
            time.sleep(1)
            Fail = False
            while not d(text="TEST"):
                    i = 0
                    time.sleep(1)
                    i = i + 1
                    if i == 10:
                        Fail = True
                        break
            d.swipe(540,2337,540,900,steps=10)
            click(d,'t',"GO",1)
            d(scrollable=True).scroll.to(text="Display")
            click(d,'t',"Display",1)
            click(d,'t',"Lock screen",1)
            click(d,'t',"Add text on lock screen",1)
            if not d(text="Blocked by your IT admin"):
                Fail = True
            nPress(d,4,"back",1)
            if not Fail:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        #Set required password complexity
        if d(text="Set required password complexity").exists:
            click(d,'t',"Set required password complexity",1)
            click(d,'t',"SET LOW REQUIRED PASSWORD COMPLEXITY",1)
            click(d,'t',"GO",1)
            click(d,'t',"Screen lock",1)
            Fail = False
            if d(text="None").enabled or d(text="Swipe").enabled:
                Fail = True
            nPress(d,2,"back",1)
            click(d,'t',"SET MEDIUM REQUIRED PASSWORD COMPLEXITY",1)
            click(d,'t',"GO",1)
            click(d,'t',"Screen lock",1)
            if d(text="None").enabled or d(text="Swipe").enabled or d(text="Pattern").enabled:
                Fail = True
            click(d,'t',"PIN",1)
            d(resourceId="com.android.settings:id/password_entry").set_text("4444")
            time.sleep(1)
            if not d(text="Ascending, descending, or repeated sequence of digits isn't allowed"):
                Fail = True
            d(resourceId="com.android.settings:id/password_entry").set_text("1234")
            time.sleep(1)
            if not d(text="Ascending, descending, or repeated sequence of digits isn't allowed"):
                Fail = True
            d(resourceId="com.android.settings:id/password_entry").set_text("4321")
            time.sleep(1)
            if not d(text="Ascending, descending, or repeated sequence of digits isn't allowed"):
                Fail = True
            d(resourceId="com.android.settings:id/password_entry").set_text("2468")
            time.sleep(1)
            if not d(text="Ascending, descending, or repeated sequence of digits isn't allowed"):
                Fail = True
            nPress(d,4,"back",1)
            click(d,'t',"SET HIGH REQUIRED PASSWORD COMPLEXITY",1)
            click(d,'t',"GO",1)
            click(d,'t',"Screen lock",1)
            if d(text="None").enabled or d(text="Swipe").enabled or d(text="Pattern").enabled:
                Fail = True
            click(d,'t',"PIN",1)
            d(resourceId="com.android.settings:id/password_entry").set_text("4444")
            time.sleep(1)
            if not d(text="Ascending, descending, or repeated sequence of digits isn't allowed") \
                and not d(text="PIN must be at least 8 digits"):
                Fail = True
            d(resourceId="com.android.settings:id/password_entry").set_text("12345678")
            time.sleep(1)
            if not d(text="Ascending, descending, or repeated sequence of digits isn't allowed"):
                Fail = True
            d(resourceId="com.android.settings:id/password_entry").set_text("4321")
            time.sleep(1)
            if not d(text="Ascending, descending, or repeated sequence of digits isn't allowed") \
                and not d(text="PIN must be at least 8 digits"):
                Fail = True
            d(resourceId="com.android.settings:id/password_entry").set_text("02468101")
            time.sleep(1)
            if not d(text="Ascending, descending, or repeated sequence of digits isn't allowed"):
                Fail = True
            d(resourceId="com.android.settings:id/password_entry").set_text("90891044")
            time.sleep(1)
            if d(text="Ascending, descending, or repeated sequence of digits isn't allowed"):
                Fail = True
            nPress(d,4,"back",1)    
            click(d,'t',"REMOVE REQUIRED PASSWORD COMPLEXITY",1)
            if not Fail:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        #Remove device owner
        if d(text="Remove device owner").exists:
            click(d,'t',"Remove device owner",1)
            click(d,'t',"REMOVE DEVICE OWNER",1)
            runCmd(device,"adb -s %s shell am start -a android.settings.SETTINGS" ,1)
            d(scrollable=True).scroll.to(text="Security")
            click(d,'t',"Security",1)
            click(d,'t',"Device admin apps",1)
            Fail = False
            if d(resourceId="android:id/switch_widget")[0].info['checked']:
                Fail = True
            nPress(d,2,"recent",1)
            if not Fail:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
        d.press("back")