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
            FAIL = False
            if not d(resourceId="android:id/switch_widget")[0].info['checked']:
                FAIL = True
            nPress(d,2,"back",1)
            if not FAIL:
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
            FAIL2 = False
            if not Fail and not Fail2 and not Fail3 and not Fail4:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
                FAIL2 = True
        
        #Disallow configuring WiFi
        if d(text="Disallow configuring WiFi").exists:
            click(d,'t',"Disallow configuring WiFi",1)
            click(d,'t',"SET RESTRICTION",1)
            click(d,'t',"GO",1)
            FAIL3 = False
            if not d(text="Blocked by your IT admin").exists:
                FAIL3 = True
            d.press("back")
            click(d,'t',"CLEAR RESTRICTION (BEFORE LEAVING TEST)",1)
            if not FAIL3:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        #Disallow configuring VPN
        if d(text="Disallow configuring VPN").exists:
            click(d,'t',"Disallow configuring VPN",1)
            click(d,'t',"SET VPN RESTRICTION",1)
            click(d,'t',"GO",1)
            FAIL4 = False
            if not d(text="Blocked by your IT admin").exists:
                FAIL4 = True
            d.press("back")
            click(d,'t',"CHECK VPN",1)
            if d(text="Cannot establish a VPN connection.\n This was expected.\n Mark this test as passed.\n").exists:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)
            click(d,'t',"CLEAR RESTRICTION (BEFORE LEAVING TEST)",1)
            if not FAIL4:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        #Disallow data roaming
        if d(text="Disallow data roaming").exists:
            click(d,'t',"Disallow data roaming",1)
            click(d,'t',"SET RESTRICTION",1)
            click(d,'t',"GO",1)
            FAIL5 = False
            d(resourceId="com.android.settings:id/recycler_view").scroll.to(text="Roaming")
            click(d,'t',"Roaming",1)
            if not d(text="Blocked by your IT admin").exists:
                FAIL5 = True
            nPress(d,2,'back',1)
            click(d,'t',"CLEAR RESTRICTION (BEFORE LEAVING TEST)",1)
            if not FAIL5:
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
            FAIL6 = False
            if not d(text="Blocked by your IT admin").exists:
                FAIL6 = True
            nPress(d,2,'recent',1)
            click(d,'t',"CLEAR RESTRICTION (BEFORE LEAVING TEST)",1)
            if not FAIL6:
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
            FAIL7 = False
            if not d(text="Blocked by your IT admin").exists:
                FAIL7 = True
            nPress(d,2,"back",1)
            click(d,'t',"CLEAR RESTRICTION (BEFORE LEAVING TEST)",1)
            if not FAIL7:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        #Disable status bar
        if d(text="Disable status bar").exists:
            click(d,'t',"Disable status bar",1)
            click(d,'t',"DISABLE STATUS BAR",1)
            runCmd(device,"adb -s %s shell cmd statusbar expand-notifications",1)
            FAIL8 = False
            if "Android System notification: USB debugging connected" in d.dump() \
            or d(text="Clear all").exists:
                FAIL8 = True
            click(d,'t',"REENABLE STATUS BAR",1)
            if not FAIL8:
                click(d,'r',"com.android.cts.verifier:id/pass_button",1)
            else:
                click(d,'r',"com.android.cts.verifier:id/fail_button",1)

        #Disable keyguard
        if d(text="Disable keyguard").exists:
            click(d,'t',"Disable keyguard",1)
            click(d,'t',"DISABLE KEYGUARD",1)
            FAIL9 = False
            d.screen.off()
            time.sleep(1)
            d.screen.on()
            time.sleep(1)
            if not d(text="Disable keyguard").exists:
                FAIL9 = True
            click(d,'t',"REENABLE KEYGUARD",1)
            d.screen.off()
            time.sleep(1)
            d.screen.on()
            time.sleep(1)
            if d(text="Disable keyguard").exists:
                FAIL9 = True
            d.swipe(540,2337,540,900,steps=10)
            if not FAIL9:
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
            


