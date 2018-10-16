wget https://gist.githubusercontent.com/Lewiscowles1986/fecd4de0b45b2029c390/raw/0c8b3af3530a35db9ab958defe9629cb5ea99972/rPi3-ap-setup.sh
sed -i -- 's/-yqq/-y/g' rPi3-ap-setup.sh
chmod +x rPi3-ap-setup.sh
sudo ./rPi3-ap-setup.sh password apname
sudo cp /etc/network/interfaces /etc/pi-ap/ap-mode-config
