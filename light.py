from api.soma_api import SomaApi
from pprint import pprint
from datetime import datetime, time
from time import sleep

class SomaConnectExplore(SomaApi):
    def __init__(self, ip:str):
        super().__init__(ip, 3000)


    def pull_light(self, show_json:bool=False ):
        mac = 'd6:e8:c7:6b:55:2b'
        light = self.get_light_level(mac)
        if show_json: pprint(light)
        light_lvl = light['light_level'] if light['result'] == 'success' else light['msg']

        bat = self.get_battery_level(mac)
        if show_json: pprint(bat)
        bat_mv = bat['battery_level'] if bat['result'] == 'success' else bat['msg']
        bat_pct = bat['battery_percentage'] if bat['result'] == 'success' else bat['msg']

        n=datetime.now()

        print( f"{datetime.now().isoformat( timespec='seconds')};{bat_mv/100};{bat_pct};{light_lvl}".replace('.',','), flush=True)


if __name__ == '__main__':
    s = SomaConnectExplore("192.168.87.145" )
    while True:
        s.pull_light()
        sleep(600)
