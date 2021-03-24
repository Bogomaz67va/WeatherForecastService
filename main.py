import requests


class ForecastService():
    def __init__(self, *parametr):
        self.param_list = []
        self.min_temp = []
        self.param_list.append(parametr)
        self.url = 'http://api.openweathermap.org/data/2.5/forecast?'
        self.params = {
            'cnt': 35,
            'appid': '36bb80e983a3fc54e52347d2c5cff68c',
            'lang': 'ru',
            'units': 'metric',
        }
        if len(self.param_list[0]) == 2:
            self.params['lon'] = self.param_list[0][0]
            self.params['lat'] = self.param_list[0][1]
        elif len(self.param_list[0]) == 1:
            self.params['id'] = self.param_list[0][0]
        else:
            print('error paramlist')

    def max_pressure_five(self):
        """Подсчет максимального давления за предстоящие 5 дней"""
        r = requests.get(self.url, params=self.params)
        if r.status_code == 200:
            five_temperature = r.json()['list']
            city_temp = r.json()['city']['name']
            pressure = []
            dt_txt = []
            for item in five_temperature:
                pressure.append(int(item['main']['pressure']))

            for item in five_temperature:
                if int(item['main']['pressure']) == max(pressure):
                    dt_txt.append(item['dt_txt'])
            print(f"{city_temp} максимальное давление за предстоящие 5 дней = {max(pressure)} гПа,"
                  f" День и время: {dt_txt}")
        else:
            print('error')

    def min_temperatura(self):
        """День с минимальной разницей между ночью и утром"""
        r = requests.get(self.url, params=self.params)
        if r.status_code == 200:
            five_temperature = r.json()['list']
            pressure = []
            dt_txt = []
            for item in five_temperature:
                pressure.append(float(item['main']['feels_like']))

            for item in five_temperature:
                if float(item['main']['feels_like']) == min(pressure):
                    dt_txt.append(item['dt_txt'])
            print(f"Минимальная температура (ночь) и (день) = {min(pressure)} ℃, День и время: {dt_txt}")
        else:
            print('error')


i = ForecastService(39.730278, 43.599998)
i.max_pressure_five()
i.min_temperatura()

# "id": 491422,
# "name": "Sochi",
# "country": "RU",
# "coord": {
#     "lon": 39.730278,
#     "lat": 43.599998
# }
