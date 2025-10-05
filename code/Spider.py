import json
import requests

from datetime import datetime
from copy import deepcopy

from GlobalVars import CHART_API_ID_DICT, SPIDER_JSON_DATA_DICT, SUMMARY_API_ID_DICT, SPIDER_HEADERS


def get_chart_data(chart_name: str, time_range: list[str] | tuple[str]) -> dict:
    """
    获取电力数据（表格）
    :param chart_name: 所需的电力数据表格名称，从chart_api_dict的键获取
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: dict: {'status': 'success/error', 'message': message_str}
    """


    try:

        this_headers = deepcopy(SPIDER_HEADERS)

        with open('./Save/Token.txt', 'r', encoding='utf-8') as f:
            this_headers['authorization'] += f.read()

        this_json_data_dict = deepcopy(SPIDER_JSON_DATA_DICT[chart_name])

        if this_json_data_dict['dateType'] == 'mi15':

            try:
                datetime.strptime(time_range[0], "%Y-%m-%d %H:%M")
                datetime.strptime(time_range[1], "%Y-%m-%d %H:%M")
            except ValueError:
                return {'status': 'error', 'message': '输入时间格式错误，应为yyyy-MM-dd HH:mm', 'data': None}

            if datetime.strptime(
                    time_range[0], "%Y-%m-%d %H:%M") > datetime.strptime(time_range[1], "%Y-%m-%d %H:%M"):
                return {'status': 'error', 'message': '输入时间范围错误，开始时间不能大于结束时间', 'data': None}

        elif this_json_data_dict['dateType'] == 'D':

            try:
                datetime.strptime(time_range[0], "%Y-%m-%d")
                datetime.strptime(time_range[1], "%Y-%m-%d")
            except ValueError:
                return {'status': 'error', 'message': '输入时间格式错误，应为yyyy-MM-dd', 'data': None}

            if datetime.strptime(
                    time_range[0], "%Y-%m-%d") > datetime.strptime(time_range[1], "%Y-%m-%d"):
                return {'status': 'error', 'message': '输入时间范围错误，开始时间不能大于结束时间', 'data': None}

        this_json_data_dict['startTime'] = time_range[0]
        this_json_data_dict['endTime'] = time_range[1]

    except FileNotFoundError:
        return {'status': 'error', 'message': 'Token文件不存在，请运行Login.py获取Token', 'data': None}
    except KeyError:
        return {'status': 'error', 'message': '输入表格名称错误，或是网站更改了响应信息', 'data': None}
    except Exception as e:
        print(e)
        return {'status': 'error', 'message': str(e), 'data': None}

    try:
        chart_api_id = CHART_API_ID_DICT[chart_name]
        response = requests.post(
            f'https://nh2api.yunjichaobiao.com/api/Monitor/Chart{chart_api_id}',
            headers=this_headers,
            json=this_json_data_dict
        )
        try:  # 傻逼网站，Token正常的时候返回的是字符串，过期的时候返回的是json
            res_json = json.loads(response.json())
            if res_json['IsSuccess']:
                electricity_data = json.loads(json.loads(response.json())['Data'])
                print(f'{chart_name}数据获取成功！')
            else:
                return {'status': 'error', 'message': res_json['ErrorMsg'], 'data': None}
        except TypeError:

            try:
                res_json = response.json()
                return {
                    'status': 'error',
                    'message': res_json['ErrorMsg'] + '，如果Token过期，请运行Login.py刷新Token',
                    'data': None
                }
            except Exception as e:
                return {'status': 'error', 'message': str(e), 'data': None}

    except Exception as e:
        return {'status': 'error', 'message': str(e), 'data': None}
    if response.status_code != 200:
        return {'status': 'error', 'message': f'数据获取失败！状态码：{response.status_code}', 'data': None}
    return {'status': 'success', 'message': '数据获取成功！', 'data': electricity_data}

def get_summary_data(summary_name: str, time_range: list[str] | tuple[str]) -> dict:
    """
    获取电力数据（汇总）
    :param summary_name: 所需的电力数据表格名称，从chart_api_dict的键获取
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: dict: {'status': 'success/error', 'message': message_str}
    """

    try:
        this_headers = deepcopy(SPIDER_HEADERS)

        with open('./Save/Token.txt', 'r', encoding='utf-8') as f:
            this_headers['authorization'] += f.read()

        this_json_data_dict = deepcopy(SPIDER_JSON_DATA_DICT[summary_name])

        if this_json_data_dict['dateType'] == 'mi15':

            try:
                datetime.strptime(time_range[0], "%Y-%m-%d %H:%M")
                datetime.strptime(time_range[1], "%Y-%m-%d %H:%M")
            except ValueError:
                return {'status': 'error', 'message': '输入时间格式错误，应为yyyy-MM-dd HH:mm', 'data': None}

            if datetime.strptime(
                    time_range[0], "%Y-%m-%d %H:%M") > datetime.strptime(time_range[1], "%Y-%m-%d %H:%M"):
                return {'status': 'error', 'message': '输入时间范围错误，开始时间不能大于结束时间', 'data': None}

        elif this_json_data_dict['dateType'] == 'D':

            try:
                datetime.strptime(time_range[0], "%Y-%m-%d")
                datetime.strptime(time_range[1], "%Y-%m-%d")
            except ValueError:
                return {'status': 'error', 'message': '输入时间格式错误，应为yyyy-MM-dd', 'data': None}

            if datetime.strptime(
                    time_range[0], "%Y-%m-%d") > datetime.strptime(time_range[1], "%Y-%m-%d"):
                return {'status': 'error', 'message': '输入时间范围错误，开始时间不能大于结束时间', 'data': None}

        this_json_data_dict['startTime'] = time_range[0]
        this_json_data_dict['endTime'] = time_range[1]

    except KeyError:
        return {'status': 'error', 'message': '输入表格名称错误，或是网站更改了响应信息', 'data': None}
    except FileNotFoundError:
        return {'status': 'error', 'message': 'Token文件不存在，请运行Login.py获取Token', 'data': None}
    except Exception as e:
        return {'status': 'error', 'message': str(e), 'data': None}


    try:
        summary_api_id = SUMMARY_API_ID_DICT[summary_name]
        response = requests.post(
            f'https://nh2api.yunjichaobiao.com/api/Monitor/Summary{summary_api_id}',
            headers=this_headers,
            json=this_json_data_dict
        )

        try:
            res_json = json.loads(response.json())
            if res_json['IsSuccess']:
                electricity_data = json.loads(json.loads(response.json())['Data'])
                print(f'{summary_name}数据获取成功！')
            else:
                return {'status': 'error', 'message': res_json['ErrorMsg'], 'data': None}
        except TypeError:

            try:
                res_json = response.json()
                return {
                    'status': 'error',
                    'message': res_json['ErrorMsg'] + '，如果Token过期，请运行Login.py刷新Token',
                    'data': None
                }
            except Exception as e:
                print(e)
                return {'status': 'error', 'message': str(e), 'data': None}

    except Exception as e:
        print(e)
        return {'status': 'error', 'message': str(e), 'data': None}

    if response.status_code != 200:
        print(f'数据获取失败！状态码：{response.status_code}')
        return {'status': 'error', 'message': f'数据获取失败！状态码：{response.status_code}', 'data': None}
    return {'status': 'success', 'message': '数据获取成功！', 'data': electricity_data}