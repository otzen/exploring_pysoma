from api.soma_api import SomaApi
from pprint import pprint
from datetime import datetime
from time import sleep


class SomaConnectExplore(SomaApi):
    def __init__(self, ip:str):
        super().__init__(ip, 3000)


    def pull_current(self, show_json:bool=False ):
        mac = 'de:01:d6:c8:cd:41'

        print("cl")
        self.close_shade( mac )
        print("_cl")

        bat = self.get_battery_level(mac)
        if show_json: pprint(bat)
        bat_mv = bat['battery_level'] if bat['result'] == 'success' else bat['msg']
        bat_pct = bat['battery_percentage'] if bat['result'] == 'success' else bat['msg']
        print( f"{datetime.now().isoformat(timespec="seconds")};{bat_mv/100};{bat_pct}", flush=True)

        sleep(30)

        bat = self.get_battery_level(mac)
        if show_json: pprint(bat)
        bat_mv = bat['battery_level'] if bat['result'] == 'success' else bat['msg']
        bat_pct = bat['battery_percentage'] if bat['result'] == 'success' else bat['msg']
        print( f"{datetime.now().isoformat(timespec="seconds")};{bat_mv/100};{bat_pct}", flush=True)

        print("opn")
        self.open_shade( mac )
        print("_opn")

        bat = self.get_battery_level(mac)
        if show_json: pprint(bat)
        bat_mv = bat['battery_level'] if bat['result'] == 'success' else bat['msg']
        bat_pct = bat['battery_percentage'] if bat['result'] == 'success' else bat['msg']
        print( f"{datetime.now().isoformat(timespec="seconds")};{bat_mv/100};{bat_pct}", flush=True)

        sleep(30)

        bat = self.get_battery_level(mac)
        if show_json: pprint(bat)
        bat_mv = bat['battery_level'] if bat['result'] == 'success' else bat['msg']
        bat_pct = bat['battery_percentage'] if bat['result'] == 'success' else bat['msg']
        print( f"{datetime.now().isoformat(timespec="seconds")};{bat_mv/100};{bat_pct}", flush=True)

if __name__ == '__main__':
    s = SomaConnectExplore("192.168.87.145" )
    while True:
        s.pull_current()
