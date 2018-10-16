# pifi
wifi helper in raspberry pi

# how to use
##____________________________________________________________________________________________________
##下载jessie并刷到TF卡，使用最新的strech系统有兼容性问题
##在mac下使用ether进行烧录镜像到tf卡
http://downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2017-07-05/2017-07-05-raspbian-jessie-lite.zip

##____________________________________________________________________________________________________
##更换清华镜像源
##REF https://blog.csdn.net/la9998372/article/details/77886806
wget https://raw.githubusercontent.com/medilabszri/pifi/master/change_source.sh
sudo bash change_source.sh

##____________________________________________________________________________________________________
##下载pifi
sudo apt-get install git -y
git clone https://github.com/medilabszri/pifi.git

##____________________________________________________________________________________________________
##开ap前，备份系统的配置文件
bash backup_config.sh


##____________________________________________________________________________________________________
##下载并安装开ap的脚本
bash install_ap.sh

##____________________________________________________________________________________________________
##备份开ap后系统的配置文件
sudo cp /etc/network/interfaces /etc/pi-ap/ap-mode-config

##____________________________________________________________________________________________________
##关闭ap
bash stop_ap.sh
sudo shutdown -r 0

##____________________________________________________________________________________________________
重开ap
bash start_ap.sh
sudo shutdown -r 0
