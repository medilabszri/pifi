#coding=utf-8
import subprocess
class WifiHelper(object):

    @staticmethod
    def check_wlan0():
        return 'broadcast' in subprocess.check_output(['/sbin/ifconfig', 'wlan0'])

    @staticmethod
    def add_ssid(ssid, password):
        WifiHelper.clean_ssid()
        for s in ["network={", r'ssid="%s"'%(ssid), r'psk="%s"'%(password), "}"]:
            subprocess.call("echo '%s' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf"%(s), shell=True)
        subprocess.call("/sbin/wpa_cli -i wlan0 reconfigure", shell=True)

    @staticmethod
    def clean_ssid():
        subprocess.call("sudo cp /etc/wpa_supplicant/wpa_supplicant.conf.bak /etc/wpa_supplicant/wpa_supplicant.conf", shell=True)
        subprocess.call("/sbin/wpa_cli -i wlan0 reconfigure", shell=True)
