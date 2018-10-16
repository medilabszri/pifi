sudo rm /etc/network/interfaces
sudo ln -f /etc/pi-ap/standard-config /etc/network/interfaces
sudo sed -i -- 's/denyinterfaces wlan0//g' /etc/dhcpcd.conf
sudo systemctl disable hostapd
sudo systemctl disable dnsmasq
sudo service hostapd stop
sudo service dnsmasq stop
