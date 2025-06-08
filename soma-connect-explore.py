from api.soma_api import SomaApi
from pprint import pprint


def main():
    s= SomaApi( "192.168.87.145", 3000)
    devs = s.list_devices()
    pprint( devs )
    mac = devs['shades'][0]['mac']

    light = s.get_light_level( mac )
    pprint( light )

    state = s.get_shade_state( mac )
    pprint( state )

    bat = s.get_battery_level( mac )
    pprint( bat )


    name = devs['shades'][0]['name']
    pos = state['position']
    bat_mv = bat['battery_level']
    bat_pct = bat['battery_percentage']
    print()
    print( f"state of { name } [{mac}]:")
    print( f"\tShade is {pos}% closed")
    print( f"\tBattery at {bat_pct}% [{bat_mv/100}V]" )





if __name__ == '__main__':
    main()
