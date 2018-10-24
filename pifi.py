# coding=utf-8
import subprocess
import threading, time

abs_file=__file__
print("abs path is %s" %(__file__))
abs_dir=abs_file[:abs_file.rfind("/")]     # windows下用\\分隔路径，linux下用/分隔路径
print abs_dir

class WifiHelper(object):

    @staticmethod
    def get_wlan_macaddress():
        hostName= subprocess.check_output("hostname", shell=True)
        s = ''
        if hostName == "ShubindeMacBook-Air.local\n":
            s = subprocess.check_output("/sbin/ifconfig en0 | grep ether", shell=True)
            s1 = s[s.find('ether'):]
        else:
            s = subprocess.check_output("/sbin/ifconfig wlan0 | grep HW", shell=True)
            s1 = s[s.find('HW'):]
        result= s1.split(' ')[1].replace(':', '')
        print result
        return result

    @staticmethod
    def check_wlan0():
        return 'Bcast' in subprocess.check_output(['/sbin/ifconfig', 'wlan0'])

    @staticmethod
    def isAp():
        return '10.0.0.1' in subprocess.check_output(['/sbin/ifconfig', 'wlan0'])

    @staticmethod
    def add_ssid(ssid, password):
        WifiHelper.clean_ssid()
        for s in ["network={",
                  r'ssid="%s"' % (ssid),
                  r'psk="%s"' % (password),
                  "}"]:
            subprocess.call("echo '%s' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf" % (s), shell=True)
        subprocess.call("sudo /sbin/wpa_cli -i wlan0 reconfigure", shell=True)

    @staticmethod
    def clean_ssid():
        subprocess.call("sudo cp /etc/wpa_supplicant/wpa_supplicant.conf.bak /etc/wpa_supplicant/wpa_supplicant.conf",
                        shell=True)
        subprocess.call("sudo /sbin/wpa_cli -i wlan0 reconfigure", shell=True)

    @staticmethod
    def start_ap():
        print("starting ap...")
        for cmd in ["sudo bash %s/start_ap.sh"%(abs_dir),
                    "sudo shutdown -r 0"]:
            subprocess.call(cmd, shell=True)

    @staticmethod
    def stop_ap():
        print("stoping ap...")
        for cmd in ["sudo bash %s/stop_ap.sh"%(abs_dir),
                    "sudo shutdown -r 0"]:
            subprocess.call(cmd, shell=True)

    def __init__(self):
        self.is_add_ssid=False
        self.isconnect = False
        self.time_interval = 5

    def set_time_interval(self, time_interval):
        self.time_interval= time_interval

    def work(self):
        """
        周期性检查网络连接状态
        """
        self.working = True
        while self.working:
            oh= self.on_working_callback
            if oh:
                oh()
            self.isconnect = self.check_wlan0()
            if self.isconnect:
                oh = self.on_wifi_available_callback
                if oh:
                    oh()
            else:
                oh = self.on_wifi_disconnect_callback
                if oh:
                    oh()
            time.sleep(self.time_interval)

        oh= self.on_stop_callback
        if oh:
            print("wifiHelper on stopping:")
            oh()

    def spin(self):
        self.t = threading.Thread(target=self.work)
        self.t.start()

    def join(self):
        self.t.join()

    def set_callback(self, on_wifi_disconnect_callback=None, on_wifi_available_callback=None, on_working_callback=None, on_stop_callback=None):
        """
        :param on_wifi_disconnect_callback: 如其名
        :param on_wifi_available_callback: 如其名
        """
        self.on_stop_callback=on_stop_callback
        self.on_wifi_disconnect_callback = on_wifi_disconnect_callback
        self.on_wifi_available_callback = on_wifi_available_callback
        self.on_working_callback= on_working_callback

    def stop(self):
        self.working = False

