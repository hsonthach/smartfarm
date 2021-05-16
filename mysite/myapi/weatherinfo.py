from .models import Device


weatherinfo = None


def get_weatherinfo():
    print('Geting weather info ...')
    if not (weatherinfo):
        update_weatherinfo()
    return weatherinfo


def set_weatherinfo(new_weatherinfo):
    global weatherinfo
    weatherinfo = new_weatherinfo


def update_weatherinfo():
    device_query_all = Device.objects.all()
    overall_weatherinfo = {
        'light': {
            'sum': 0,
            'count': 0,
        },
        'soil': {
            'sum': 0,
            'count': 0,
        },
        'temp': {
            'sum': 0,
            'count': 0,
        },
        'humid': {
            'sum': 0,
            'count': 0,
        }
    }
    number_of_device = len(device_query_all)
    number_of_light = 0
    for i, device_query in enumerate(device_query_all):
        device_query_dict = device_query.__dict__
        if (device_query_dict['name'] == 'LIGHT'):
            overall_weatherinfo['light']['sum'] += float(
                device_query_dict['data'])
            overall_weatherinfo['light']['count'] += 1
        elif (device_query_dict['name'] == 'SOIL'):
            overall_weatherinfo['soil']['sum'] += float(
                device_query_dict['data'])
            overall_weatherinfo['soil']['count'] += 1
        elif (device_query_dict['name'] == 'TEMP-HUMID'):
            [temp, humid] = device_query_dict['data'] .split('-')
            overall_weatherinfo['temp']['sum'] += float(temp)
            overall_weatherinfo['temp']['count'] += 1
            overall_weatherinfo['humid']['sum'] += float(humid)
            overall_weatherinfo['humid']['count'] += 1

    set_weatherinfo({
        'light': overall_weatherinfo['light']['sum']/overall_weatherinfo['light']['count'],
        'temp': overall_weatherinfo['temp']['sum']/overall_weatherinfo['temp']['count'],
        'humid': overall_weatherinfo['humid']['sum']/overall_weatherinfo['humid']['count'],
        'soil': overall_weatherinfo['soil']['sum']/overall_weatherinfo['soil']['count'],
    })
