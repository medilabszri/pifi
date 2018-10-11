# pifi
python wifi helper in raspberry pi

# how to use

STEP 0, https://gist.github.com/Lewiscowles1986/fecd4de0b45b2029c390#gistcomment-1716402
```
sudo mkdir -p /etc/pi-ap
sudo cp /etc/network/interfaces /etc/pi-ap/standard-config
wget https://gist.github.com/Lewiscowles1986/fecd4de0b45b2029c390/raw/0c8b3af3530a35db9ab958defe9629cb5ea99972/rPi3-ap-setup.sh
chmod +x rPi3-ap-setup.sh
sudo apt-get update
sudo ./rPi3-ap-setup.sh password apname
sudo cp /etc/network/interfaces /etc/pi-ap/ap-mode-config
```

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
