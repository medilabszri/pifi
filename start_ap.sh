sudo rm /etc/network/interfaces
sudo ln -f /etc/pi-ap/ap-mode-config /etc/network/interfaces
sudo echo "denyinterfaces wlan0" >> /etc/dhcpcd.conf
sudo systemctl enable hostapd
sudo systemctl enable dnsmasq
sudo service hostapd start
sudo service dnsmasq start
