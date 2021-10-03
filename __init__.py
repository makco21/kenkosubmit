import json

import requests
import locale


if __name__ == '__main__':


    url = 'https://free-api.heweather.net/s6/weather/forecast?location=广州&key=b906d88cc8cb42ed88080fd41e730ec6'
    requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
    s = requests.session()
    s.keep_alive = False # 关闭多余连接
    res = requests.get(url)
    res = json.loads(res.text)
    result = res['HeWeather6'][0]['daily_forecast']
    names = ['城市','时间','天气状况','最高温','最低温','日出','日落']
    for data in result:
        date = data['date']
        cond = data['cond_txt_d']
        max = data['tmp_max']
        min = data['tmp_min']
        sr = data['sr']
        ss = data['ss']
        print(date,cond,max,min,sr,ss)

    
