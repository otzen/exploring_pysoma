from api.soma_api import SomaApi
from pprint import pprint
from requests import RequestException


class SomaConnectExplore(SomaApi):
    def __init__(self, ip:str):
        super().__init__(ip, 3000)
        print("initialized")

    def show_device_info(self, dev: dict, show_json:bool=False ):
        mac = dev['mac']
        name = dev['name']

        state = self.get_shade_state(mac)
        if show_json: pprint(state)
        pos = state['position'] if state['result'] == 'success' else state['msg']

        bat = self.get_battery_level(mac)
        if show_json: pprint(bat)
        bat_mv = bat['battery_level'] if bat['result'] == 'success' else bat['msg']
        bat_pct = bat['battery_percentage'] if bat['result'] == 'success' else bat['msg']

        light = self.get_light_level(mac)
        if show_json: pprint(light)
        light_lvl = light['light_level'] if light['result'] == 'success' else light['msg']

        print()
        print(f"{name} [{mac}]:")
        print(f"\tShade is {pos}% closed")
        print(f"\tBattery at {bat_pct}% [{bat_mv / 100}V]")
        print(f"\tLigt at {light_lvl}")

    def get_battery_level(self, mac:str):
        try:
            response = super().get_battery_level(mac)
        except RequestException as e:
            response = { "result": "error",
                         'msg': str(e)
                         }
        return response

    def get_shade_state(self, mac:str):
        try:
            response = super().get_shade_state(mac)
        except RequestException as e:
            response = { "result": "error",
                         'msg': str(e)
                         }
        return response

    def get_light_level(self, mac):
        try:
            response = super().get_light_level(mac)
        except RequestException as e:
            response = { "result": "error",
                         'msg': str(e)
                         }
        return response


    def show_verbose_devlist(self, show_json:bool=False):
        devs:dict = self.list_devices()
        if show_json: pprint( devs )

        if devs['result'] == 'success':
            dev_count = len(devs['shades'])
        else:
            print( devs['msg'])
            return
        print(f"Found {dev_count} device(s)")

        for dev in devs['shades']:
            self.show_device_info(dev, show_json)

    def make_bat_table(self):
        devs: dict = self.list_devices()

        for dev in devs['shades']:
            mac = dev['mac']
            bat = self.get_battery_level(mac)
            if bat['result'] == 'success':
                bat_mv = bat['battery_level']
                bat_pct = bat['battery_percentage']
                print( f"{bat_mv/100}; {bat_pct}")


if __name__ == '__main__':
    s = SomaConnectExplore("192.168.87.145" )
    s.show_verbose_devlist(False)
    #s.make_bat_table()
