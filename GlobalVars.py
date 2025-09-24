RANDOM_KEY_ARR = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                  "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

CHART_API_ID_DICT = {
    'ActiveElectricQuantity': 'YGDL',
    'FrozenElectricQuantity': 'DJDL',
    'AntiFrozenElectricQuantity': 'FDJDL',
    'ReactiveElectricQuantity': 'WGDL',
    'ActiveReactiveElectricQuantity': 'TotalEnergy',
    'ActivePower': 'YGGL',
    'ReactivePower': 'WGGL',
    'ActiveReactivePower': 'LoadPower',
    'ApparentPower': 'SZGL',
    'PowerFactor': 'GLYS',
    'MaximumDemand': 'ZDXL',
    'Voltage': 'DY',
    'Current': 'DL',
    'VoltageCurrentHz': 'VAHz',
    'ElectricityBill': 'DF_FFL'
}

SUMMARY_API_ID_DICT = {
    'SummaryActiveElectricQuantity': 'YGDL',
    'SummaryFrozenElectricQuantity': 'DJDL',
    'SummaryAntiFrozenElectricQuantity': 'FDJDL',
    'SummaryReactiveElectricQuantity': 'WGDL',
    'SummaryActiveReactiveElectricQuantity': 'TotalEnergy',
    'SummaryActiveReactivePower': 'LoadPower',
    'SummaryVoltageCurrentHz': 'VAHz',
    'SummaryElectricityBill': 'DF_FFL'
}


GET_PASS_KEY_HEADERS = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://nh2.yunjichaobiao.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://nh2.yunjichaobiao.com/',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Microsoft Edge";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0',
}

GET_PASS_KEY_JSON_DATA = {
        'keyStr': ''  # 在GetPaKey.py中生成
    }

LOGIN_HEADERS = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://nh2.yunjichaobiao.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://nh2.yunjichaobiao.com/',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Microsoft Edge";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0',
}

LOGIN_JSON_DATA = {
    'UserID': '',  # 在Login.py中由用户填写
    'Password': '',  # 在Login.py中由用户填写
    'client': '0',
    'KeyStr': '',  # 在GetPaKey.py中生成
    'Code': '',  # 在Login.py中由用户填写
    'Language': 'cn',
}

SPIDER_HEADERS = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'authorization': 'Bearer ',  # 从Token.txt中获取，不要删除空格
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://nh2.yunjichaobiao.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://nh2.yunjichaobiao.com/',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Microsoft Edge";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0',
}

SPIDER_JSON_DATA_DICT = {  # 由于请求数据都不一样，所以要确定每种类型对应的json数据
    'ActiveElectricQuantity': {
        'dateType': 'mi15',
         'areaID': 0,
         'ammeterID': '',
         'startTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
         'endTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
         'isCompare': False,
         'startTime2': '',
         'endTime2': '',
         'valueType': 'SJZ',
         'PrivAddr': ''
    },
    'FrozenElectricQuantity': {
        'dateType': 'D',
        'areaID': 0,
        'ammeterID': '',
        'startTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'endTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'valueType': 'SJZ',
        'isCompare': False,
        'startTime2': '',
        'endTime2': '',
        'singleRate': False,
        'PrivAddr': '%2FEnergy%2Fdjdl.html'
    },
    'AntiFrozenElectricQuantity': {
        'dateType': 'D',
        'areaID': 0,
        'ammeterID': '',
        'startTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'endTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'valueType': 'SJZ',
        'isCompare': False,
        'startTime2': '',
        'endTime2': '',
        'singleRate': False,
        'PrivAddr': '%2FEnergy%2Fdjdl.html'
    },
    'ReactiveElectricQuantity': {
        'dateType': 'mi15',
        'areaID': 0,
        'ammeterID': '',
        'startTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'endTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'valueType': 'SJZ',
        'isCompare': False,
        'startTime2': '',
        'endTime2': '',
        'PrivAddr': '%2FEnergy%2Fwgdl.html'
    },
    'ActiveReactiveElectricQuantity': {
        'dateType': 'mi15',
        'areaID': '82021',
        'ammeterID': '156275',
        'startTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'endTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'valueType': 'SJZ',
        'PrivAddr': '%2FEnergy%2Fygwgzdn.html',
    },
    'ActivePower': {
        'dateType': 'mi15',
        'areaID': '82021',
        'ammeterID': '156275',
        'startTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'endTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'valueType': 'SJZ',
        'isCompare': False,
        'startTime2': '',
        'endTime2': '',
        'PrivAddr': '%2FEnergy%2Fyggl.html'
    },
    'ReactivePower': {
        'dateType': 'mi15',
        'areaID': '82021',
        'ammeterID': '156275',
        'startTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'endTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'valueType': 'SJZ',
        'isCompare': False,
        'startTime2': '',
        'endTime2': '',
        'PrivAddr': '%2FEnergy%2Fwggl.html'
    },
    'ActiveReactivePower': {
        'dateType': 'mi15',
        'areaID': '82021',
        'ammeterID': '156275',
        'startTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'endTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'valueType': 'SJZ',
        'PrivAddr': '%2FEnergy%2Fygwggl.html',
    },
    'ApparentPower': {
        'dateType': 'mi15',
        'areaID': '82021',
        'ammeterID': '156275',
        'startTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'endTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'valueType': 'SJZ',
        'isCompare': False,
        'startTime2': '',
        'endTime2': '',
        'PrivAddr': '%2FEnergy%2Fszgl.html'
    },
    'PowerFactor': {
        'dateType': 'mi15',
        'areaID': '82021',
        'ammeterID': '156275',
        'startTime': '',
        'endTime': '',
        'isCompare': False,
        'startTime2': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'endTime2': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'valueType': 'SJZ',
        'PrivAddr': '%2FEnergy%2Fglys.html'
    },
    'MaximumDemand': {
        'dateType': 'D',
        'areaID': '82021',
        'ammeterID': '156275',
        'startTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'endTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'valueType': 'SJZ',
        'isCompare': False,
        'startTime2': '',
        'endTime2': '',
        'PrivAddr': '%2FEnergy%2Fzdxl.html'
    },
    'Voltage': {
        'dateType': 'mi15',
        'areaID': '82021',
        'ammeterID': '156275',
        'startTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'endTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'valueType': 'SJZ',
        'isCompare': False,
        'startTime2': '',
        'endTime2': '',
        'PrivAddr': '%2FEnergy%2Fdy.html'
    },
    'Current': {
        'dateType': 'mi15',
        'areaID': '82021',
        'ammeterID': '156275',
        'startTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'endTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'valueType': 'SJZ',
        'isCompare': False,
        'startTime2': '',
        'endTime2': '',
        'PrivAddr': '%2FEnergy%2Fdl.html'
    },
    'VoltageCurrentHz': {
        'dateType': 'mi15',
        'areaID': '82021',
        'ammeterID': '156275',
        'startTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'endTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'valueType': 'SJZ',
        'PrivAddr': '%2FEnergy%2Fdldypl.html',
    },
    'ElectricityBill': {
        'dateType': 'D',
        'areaID': 0,
        'ammeterID': '',
        'startTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'endTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'valueType': 'SJZ',
        'isCompare': False,
        'startTime2': '',
        'endTime2': '',
        'PrivAddr': '%2FEnergy%2Fdf.html'
    },
    'SummaryActiveElectricQuantity': {
        'dateType': 'mi15',
         'areaID': 0,
         'ammeterID': '',
         'startTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
         'endTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
         'isCompare': False,
         'startTime2': '',
         'endTime2': '',
         'valueType': 'SJZ',
         'PrivAddr': ''
    },
    'SummaryFrozenElectricQuantity': {
        'dateType': 'D',
        'areaID': 0,
        'ammeterID': '',
        'startTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'endTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'valueType': 'SJZ',
        'isCompare': False,
        'startTime2': '',
        'endTime2': '',
        'singleRate': False,
        'PrivAddr': '%2FEnergy%2Fdjdl.html'
    },
    'SummaryAntiFrozenElectricQuantity': {
        'dateType': 'D',
        'areaID': 0,
        'ammeterID': '',
        'startTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'endTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'singleRate': False,
        'valueType': 'SJZ',
        'PrivAddr': '%2FEnergy%2Fdjdl.html',
    },
    'SummaryReactiveElectricQuantity': {
        'dateType': 'mi15',
        'areaID': '82021',
        'ammeterID': '156275',
        'startTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'endTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'valueType': 'SJZ',
        'PrivAddr': '%2FEnergy%2Fwgdl.html',
    },
    'SummaryActiveReactiveElectricQuantity': {
        'dateType': 'mi15',
        'areaID': '82021',
        'ammeterID': '156275',
        'startTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'endTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'valueType': 'SJZ',
        'PrivAddr': '%2FEnergy%2Fygwgzdn.html',
    },
    'SummaryActiveReactivePower': {
        'dateType': 'mi15',
        'areaID': '82021',
        'ammeterID': '156275',
        'startTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'endTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'valueType': 'SJZ',
        'PrivAddr': '%2FEnergy%2Fygwggl.html',
    },
    'SummaryVoltageCurrentHz': {
        'dateType': 'mi15',
        'areaID': '82021',
        'ammeterID': '156275',
        'startTime': '', # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'endTime': '', # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'valueType': 'SJZ',
        'PrivAddr': '%2FEnergy%2Fdldypl.html',
    },
    'SummaryElectricityBill': {
        'dateType': 'D',
        'areaID': 0,
        'ammeterID': '',
        'startTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'endTime': '',  # 此处由参数控制，确定范围，格式：yyyy-MM-dd HH:mm，如果是天数，则是yyyy-MM-dd
        'valueType': 'SJZ',
        'PrivAddr': '%2FEnergy%2Fdf.html',
    }
}