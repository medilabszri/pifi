# pifi
python wifi helper in raspberry pi

# how to use
STEP 1    
```
cd /etc/wpa_supplicant/; cp wpa_supplicant.conf wpa_supplicant.conf.bak  
```
STEP 2  
```
from pifi import WifiHelper
WifiHelper.check_wlan0()
WifiHelper.clean_ssid()
WifiHelper.add_ssid(ssid, password)
```
