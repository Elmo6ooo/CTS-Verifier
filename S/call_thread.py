from Setup import Setup
from BYOD_Managed_Provisioning import BYOD_Managed_Provisioning
from BYOD_Provisioning_tests import BYOD_Provisioning_tests
from Device_Owner_Requesting_Bugreport_Tests import Device_Owner_Requesting_Bugreport_Tests
from Device_Owner_Tests import Device_Owner_Tests
from No_Device_Owner_Tests import No_Device_Owner_Tests
import threading
import time

Devices = ['09221FQCB00033','0A261FDD4000JM']

#SETUP DEVICE
threads = []
for device in Devices:
	t = threading.Thread(target =Setup , args = (device,))
	threads.append(t)
#excute thread
for i in range(len(Devices)):
	threads[i].start()
#wait for end of t
for i in range(len(Devices)):
	threads[i].join()

time.sleep(1)

#BYOD_Managed_Provisioning
threads2 = []
for device in Devices:
	t = threading.Thread(target =BYOD_Managed_Provisioning , args = (device,))
	threads2.append(t)
for i in range(len(Devices)):
	threads2[i].start()
for i in range(len(Devices)):
	threads2[i].join()

time.sleep(10)

#BYOD_Provisioning_tests
threads2 = []
for device in Devices:
	t = threading.Thread(target =BYOD_Provisioning_tests , args = (device,))
	threads2.append(t)
for i in range(len(Devices)):
	threads2[i].start()
for i in range(len(Devices)):
	threads2[i].join()

time.sleep(1)

#Device_Owner_Requesting_Bugreport_Tests
threads3 = []
for device in Devices:
	t = threading.Thread(target =Device_Owner_Requesting_Bugreport_Tests , args = (device,))
	threads3.append(t)
for i in range(len(Devices)):
	threads3[i].start()
for i in range(len(Devices)):
	threads3[i].join()

time.sleep(1)

#Device_Owner_Tests
threads4 = []
for device in Devices:
	t = threading.Thread(target =Device_Owner_Tests , args = (device,))
	threads4.append(t)
for i in range(len(Devices)):
	threads4[i].start()
for i in range(len(Devices)):
	threads4[i].join()

#No_Device_Owner_Tests
threads4 = []
for device in Devices:
	t = threading.Thread(target =No_Device_Owner_Tests , args = (device,))
	threads4.append(t)
for i in range(len(Devices)):
	threads4[i].start()
for i in range(len(Devices)):
	threads4[i].join()

print("complete")



#update cts apk
#require insert sim card
#Q,R should skip Device owner tests - data roaming(no sim card)

#===BYOD_Managed_Provisioning===
#Skip Keyguard disabled features
#Skip Authentication-bound keys
#Recents redaction test use screenshot remember to check photo
#Camera need to check screenshot and screenrecords
#Skip test about location
#===Device_Owner_Tests===
#Skip Disallow USB file transfer
#if can't open power menu skip LockTask UI
#Setting user icon use screenshot remember to check photo
#Skip Disallow debugging features, this will close debugging
#Skip User switcher message
#Skip Logout long press power not working
#Skip Disable USB data signaling, this will close debugging