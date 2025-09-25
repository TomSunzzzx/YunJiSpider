import pandas as pd
import ast

from tabulate import tabulate

from Spider import get_chart_data, get_summary_data

def active_electric_quantity_data2csv(time_range: list[str] | tuple[str]) -> None:
    """
    获取有功电量并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: None
    """

    spider_data = get_chart_data('ActiveElectricQuantity', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return

    electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_data1__total_positive_active_electric_quantity = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__total_negative_active_electric_quantity = ast.literal_eval(electricity_data['y_Data2'])

    y_data1__total_positive_active_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data1__total_positive_active_electric_quantity))
    )
    y_data2__total_negative_active_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data2__total_negative_active_electric_quantity))
    )

    df = pd.DataFrame(
        {
            '时间': x_axis__time,
            '正向有功总电量': y_data1__total_positive_active_electric_quantity,
            '反向有功总电量': y_data2__total_negative_active_electric_quantity
        }
    )

    df.to_csv('./Save/ActiveElectricQuantity.csv', index=False)

def get_active_electric_quantity_data(time_range: list[str] | tuple[str], terminal_output: bool = True) -> dict:
    """
    获取有功电量
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :param terminal_output: 控制终端是否输出
    :return: dict(time:{items: values}) / dict(None)
    """

    spider_data = get_chart_data('ActiveElectricQuantity', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return {}

    electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_data1__total_positive_active_electric_quantity = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__total_negative_active_electric_quantity = ast.literal_eval(electricity_data['y_Data2'])

    y_data1__total_positive_active_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data1__total_positive_active_electric_quantity))
    )
    y_data2__total_negative_active_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data2__total_negative_active_electric_quantity))
    )

    return_data = {}

    for i in range(len(x_axis__time)):
        return_data[x_axis__time[i]] = {
            'total_positive_active_electric_quantity': y_data1__total_positive_active_electric_quantity[i],
            'total_negative_active_electric_quantity': y_data2__total_negative_active_electric_quantity[i]
        }

    show_data = {
        'time': x_axis__time,
        'total_positive_active_electric_quantity': y_data1__total_positive_active_electric_quantity,
        'total_negative_active_electric_quantity': y_data2__total_negative_active_electric_quantity
    }

    if terminal_output:
        print(tabulate(show_data, headers='keys', tablefmt='simple', showindex=False))

    return return_data

def frozen_electric_quantity2csv(time_range: list[str] | tuple[str]) -> None:
    """
    获取冻结电量并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: None
    """

    spider_data = get_chart_data('FrozenElectricQuantity', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return

    electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_data1__sharp_frozen_electric_quantity = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__peak_frozen_electric_quantity = ast.literal_eval(electricity_data['y_Data2'])
    y_data3__flat_frozen_electric_quantity = ast.literal_eval(electricity_data['y_Data3'])
    y_data4__valley_frozen_electric_quantity = ast.literal_eval(electricity_data['y_Data4'])
    y_data_total__total_real_frozen_electric_quantity = ast.literal_eval(electricity_data['y_DataTotal'])

    y_data1__sharp_frozen_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data1__sharp_frozen_electric_quantity))
    )
    y_data2__peak_frozen_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data2__peak_frozen_electric_quantity))
    )
    y_data3__flat_frozen_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data3__flat_frozen_electric_quantity))
    )
    y_data4__valley_frozen_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data4__valley_frozen_electric_quantity))
    )
    y_data_total__total_real_frozen_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data_total__total_real_frozen_electric_quantity))
    )

    df = pd.DataFrame(
        {
            '时间': x_axis__time,
            '尖电量': y_data1__sharp_frozen_electric_quantity,
            '峰电量': y_data2__peak_frozen_electric_quantity,
            '平电量': y_data3__flat_frozen_electric_quantity,
            '谷电量': y_data4__valley_frozen_electric_quantity,
            '实际总电量': y_data_total__total_real_frozen_electric_quantity
        }
    )

    df.to_csv('./Save/FrozenElectricQuantity.csv', index=False)


def get_frozen_electric_quantity_data(time_range: list[str] | tuple[str], terminal_output: bool = True) -> dict:
    """
    获取冻结电量并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :param terminal_output: 控制终端是否输出
    :return: dict(time:{items: values}) / dict(None)
    """

    spider_data = get_chart_data('FrozenElectricQuantity', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return {}

    electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_data1__sharp_frozen_electric_quantity = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__peak_frozen_electric_quantity = ast.literal_eval(electricity_data['y_Data2'])
    y_data3__flat_frozen_electric_quantity = ast.literal_eval(electricity_data['y_Data3'])
    y_data4__valley_frozen_electric_quantity = ast.literal_eval(electricity_data['y_Data4'])
    y_data_total__total_real_frozen_electric_quantity = ast.literal_eval(electricity_data['y_DataTotal'])

    y_data1__sharp_frozen_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data1__sharp_frozen_electric_quantity))
    )
    y_data2__peak_frozen_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data2__peak_frozen_electric_quantity))
    )
    y_data3__flat_frozen_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data3__flat_frozen_electric_quantity))
    )
    y_data4__valley_frozen_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data4__valley_frozen_electric_quantity))
    )
    y_data_total__total_real_frozen_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data_total__total_real_frozen_electric_quantity))
    )

    return_data = {}

    for i in range(len(x_axis__time)):
        return_data[x_axis__time[i]] = {
            'sharp_frozen_electric_quantity': y_data1__sharp_frozen_electric_quantity[i],
            'peak_frozen_electric_quantity': y_data2__peak_frozen_electric_quantity[i],
            'flat_frozen_electric_quantity': y_data3__flat_frozen_electric_quantity[i],
            'valley_frozen_electric_quantity': y_data4__valley_frozen_electric_quantity[i],
            'total_real_frozen__electric_quantity': y_data_total__total_real_frozen_electric_quantity[i]
        }

    show_data = {
        'time': x_axis__time,
        'sharp_frozen_electric_quantity': y_data1__sharp_frozen_electric_quantity,
        'peak_frozen_electric_quantity': y_data2__peak_frozen_electric_quantity,
        'flat_frozen_electric_quantity': y_data3__flat_frozen_electric_quantity,
        'valley_frozen_electric_quantity': y_data4__valley_frozen_electric_quantity,
        'total_real_frozen_electric_quantity': y_data_total__total_real_frozen_electric_quantity
    }

    if terminal_output:
        print(tabulate(show_data, headers='keys', tablefmt='simple', showindex=False))

    return return_data

def anti_frozen_electric_quantity2csv(time_range: list[str] | tuple[str]) -> None:
    """
    获取反向冻结电量并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: None
    """

    spider_data = get_chart_data('AntiFrozenElectricQuantity', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return

    electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_data1__sharp_anti_frozen_electric_quantity = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__peak_anti_frozen_electric_quantity = ast.literal_eval(electricity_data['y_Data2'])
    y_data3__flat_anti_frozen_electric_quantity = ast.literal_eval(electricity_data['y_Data3'])
    y_data4__valley_anti_frozen_electric_quantity = ast.literal_eval(electricity_data['y_Data4'])
    y_data_total__total_real_anti_frozen_electric_quantity = ast.literal_eval(electricity_data['y_DataTotal'])

    y_data1__sharp_anti_frozen_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data1__sharp_anti_frozen_electric_quantity))
    )
    y_data2__peak_anti_frozen_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data2__peak_anti_frozen_electric_quantity))
    )
    y_data3__flat_anti_frozen_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data3__flat_anti_frozen_electric_quantity))
    )
    y_data4__valley_anti_frozen_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data4__valley_anti_frozen_electric_quantity))
    )
    y_data_total__total_real_anti_frozen_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data_total__total_real_anti_frozen_electric_quantity))
    )

    df = pd.DataFrame(
        {
            '时间': x_axis__time,
            '尖电量': y_data1__sharp_anti_frozen_electric_quantity,
            '峰电量': y_data2__peak_anti_frozen_electric_quantity,
            '平电量': y_data3__flat_anti_frozen_electric_quantity,
            '谷电量': y_data4__valley_anti_frozen_electric_quantity,
            '实际总电量': y_data_total__total_real_anti_frozen_electric_quantity
        }
    )

    df.to_csv('./Save/AntiFrozenElectricQuantity.csv', index=False)


def get_anti_frozen_electric_quantity_data(time_range: list[str] | tuple[str], terminal_output: bool = True) -> dict:
    """
    获取反向冻结电量并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :param terminal_output: 控制终端是否输出
    :return: dict(time:{items: values}) / dict(None)
    """

    spider_data = get_chart_data('AntiFrozenElectricQuantity', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return {}

    electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_data1__sharp_anti_frozen_electric_quantity = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__peak_anti_frozen_electric_quantity = ast.literal_eval(electricity_data['y_Data2'])
    y_data3__flat_anti_frozen_electric_quantity = ast.literal_eval(electricity_data['y_Data3'])
    y_data4__valley_anti_frozen_electric_quantity = ast.literal_eval(electricity_data['y_Data4'])
    y_data_total__total_real_anti_frozen_electric_quantity = ast.literal_eval(electricity_data['y_DataTotal'])

    y_data1__sharp_anti_frozen_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data1__sharp_anti_frozen_electric_quantity))
    )
    y_data2__peak_anti_frozen_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data2__peak_anti_frozen_electric_quantity))
    )
    y_data3__flat_anti_frozen_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data3__flat_anti_frozen_electric_quantity))
    )
    y_data4__valley_anti_frozen_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data4__valley_anti_frozen_electric_quantity))
    )
    y_data_total__total_real_anti_frozen_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data_total__total_real_anti_frozen_electric_quantity))
    )

    return_data = {}

    for i in range(len(x_axis__time)):
        return_data[x_axis__time[i]] = {
            'sharp_anti_frozen_electric_quantity': y_data1__sharp_anti_frozen_electric_quantity[i],
            'peak_anti_frozen_electric_quantity': y_data2__peak_anti_frozen_electric_quantity[i],
            'flat_anti_frozen_electric_quantity': y_data3__flat_anti_frozen_electric_quantity[i],
            'valley_anti_frozen_electric_quantity': y_data4__valley_anti_frozen_electric_quantity[i],
            'total_real_anti_frozen_electric_quantity': y_data_total__total_real_anti_frozen_electric_quantity[i]
        }
    show_data = {
        'time': x_axis__time,
        'sharp_anti_frozen_electric_quantity': y_data1__sharp_anti_frozen_electric_quantity,
        'peak_anti_frozen_electric_quantity': y_data2__peak_anti_frozen_electric_quantity,
        'flat_anti_frozen_electric_quantity': y_data3__flat_anti_frozen_electric_quantity,
        'valley_anti_frozen_electric_quantity': y_data4__valley_anti_frozen_electric_quantity,
        'total_anti_frozen_real_electric_quantity': y_data_total__total_real_anti_frozen_electric_quantity
    }

    if terminal_output:
        print(tabulate(show_data, headers='keys', tablefmt='simple', showindex=False))

    return return_data



def reactive_electric_quantity2csv(time_range: list[str] | tuple[str]) -> None:
    """
    获取无功电量并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: None
    """

    spider_data = get_chart_data('ReactiveElectricQuantity', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return

    electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_data1__total_positive_reactive_electric_quantity = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__total_negative_reactive_electric_quantity = ast.literal_eval(electricity_data['y_Data2'])

    y_data1__total_positive_reactive_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data1__total_positive_reactive_electric_quantity))
    )
    y_data2__total_negative_reactive_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data2__total_negative_reactive_electric_quantity))
    )

    df = pd.DataFrame(
        {
            '时间': x_axis__time,
            '正向无功总电量': y_data1__total_positive_reactive_electric_quantity,
            '反向无功总电量': y_data2__total_negative_reactive_electric_quantity
        }
    )

    df.to_csv('./Save/ReactiveElectricQuantity.csv', index=False)

def get_reactive_electric_quantity_data(time_range: list[str] | tuple[str], terminal_output: bool = True) -> dict:
    """
    获取无功电量
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :param terminal_output: 控制终端是否输出
    :return: dict(time:{items: values}) / dict(None)
    """
    spider_data = get_chart_data('ReactiveElectricQuantity', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return {}

    electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_data1__total_positive_reactive_electric_quantity = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__total_negative_reactive_electric_quantity = ast.literal_eval(electricity_data['y_Data2'])

    y_data1__total_positive_reactive_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data1__total_positive_reactive_electric_quantity))
    )
    y_data2__total_negative_reactive_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data2__total_negative_reactive_electric_quantity))
    )

    return_data = {}

    for i in range(len(x_axis__time)):
        return_data[x_axis__time[i]] = {
            'total_positive_reactive_electric_quantity': y_data1__total_positive_reactive_electric_quantity[i],
            'total_negative_reactive_electric_quantity': y_data2__total_negative_reactive_electric_quantity[i]
        }

    show_data = {
        'time': x_axis__time,
        'total_positive_reactive_electric_quantity': y_data1__total_positive_reactive_electric_quantity,
        'total_negative_reactive_electric_quantity': y_data2__total_negative_reactive_electric_quantity
    }

    if terminal_output:
        print(tabulate(show_data, headers='keys', tablefmt='simple', showindex=False))

    return return_data

def active_reactive_electric_quantity2csv(time_range: list[str] | tuple[str]) -> None:
    """
    获取有功无功电量并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: None
    """

    spider_data = get_chart_data('ActiveReactiveElectricQuantity', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return

    electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_data1__total_positive_active_electric_quantity = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__total_positive_reactive_electric_quantity = ast.literal_eval(electricity_data['y_Data2'])
    y_data3__total_negative_active_electric_quantity = ast.literal_eval(electricity_data['y_Data3'])
    y_data4__total_negative_reactive_electric_quantity = ast.literal_eval(electricity_data['y_Data4'])

    y_data1__total_positive_active_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data1__total_positive_active_electric_quantity))
    )
    y_data2__total_positive_reactive_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data2__total_positive_reactive_electric_quantity))
    )
    y_data3__total_negative_active_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data3__total_negative_active_electric_quantity))
    )
    y_data4__total_negative_reactive_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data4__total_negative_reactive_electric_quantity))
    )

    df = pd.DataFrame(
        {
            '时间': x_axis__time,
            '正向有功总电量': y_data1__total_positive_active_electric_quantity,
            '正向无功总电量': y_data2__total_positive_reactive_electric_quantity,
            '反向有功总电量': y_data3__total_negative_active_electric_quantity,
            '反向无功总电量': y_data4__total_negative_reactive_electric_quantity
        }
    )

    df.to_csv('./Save/ActiveReactiveElectricQuantity.csv', index=False)

def get_active_reactive_electric_quantity_data(
        time_range: list[str] | tuple[str],
        terminal_output: bool = True
) -> dict:
    """
    获取有功无功电量
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :param terminal_output: 控制终端是否输出
    :return: dict(time:{items: values}) / dict(None)
    """

    spider_data = get_chart_data('ActiveReactiveElectricQuantity', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return {}

    electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_data1__total_positive_active_electric_quantity = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__total_positive_reactive_electric_quantity = ast.literal_eval(electricity_data['y_Data2'])
    y_data3__total_negative_active_electric_quantity = ast.literal_eval(electricity_data['y_Data3'])
    y_data4__total_negative_reactive_electric_quantity = ast.literal_eval(electricity_data['y_Data4'])

    y_data1__total_positive_active_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data1__total_positive_active_electric_quantity))
    )
    y_data2__total_positive_reactive_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data2__total_positive_reactive_electric_quantity))
    )
    y_data3__total_negative_active_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data3__total_negative_active_electric_quantity))
    )
    y_data4__total_negative_reactive_electric_quantity.extend(
        [0] * (len(x_axis__time) - len(y_data4__total_negative_reactive_electric_quantity))
    )

    return_data = {}

    for i in range(len(x_axis__time)):
        return_data[x_axis__time[i]] = {
            'total_positive_active_electric_quantity': y_data1__total_positive_active_electric_quantity[i],
            'total_positive_reactive_electric_quantity': y_data2__total_positive_reactive_electric_quantity[i],
            'total_negative_active_electric_quantity': y_data3__total_negative_active_electric_quantity[i],
            'total_negative_reactive_electric_quantity': y_data4__total_negative_reactive_electric_quantity[i]
        }

    show_data = {
        'time': x_axis__time,
        'total_positive_active_electric_quantity': y_data1__total_positive_active_electric_quantity,
        'total_positive_reactive_electric_quantity': y_data2__total_positive_reactive_electric_quantity,
        'total_negative_active_electric_quantity': y_data3__total_negative_active_electric_quantity,
        'total_negative_reactive_electric_quantity': y_data4__total_negative_reactive_electric_quantity
    }

    if terminal_output:
        print(tabulate(show_data, headers='keys', tablefmt='simple', showindex=False))

    return return_data

def active_power2csv(time_range: list[str] | tuple[str]) -> None:
    """
    获取有功功率并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: None
    """

    spider_data = get_chart_data('ActivePower', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return

    electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_datatotal__total_active_power = ast.literal_eval(electricity_data['y_DataTotal'])
    y_data1__a_phase_active_power = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__b_phase_active_power = ast.literal_eval(electricity_data['y_Data2'])
    y_data3__c_phase_active_power = ast.literal_eval(electricity_data['y_Data3'])

    y_datatotal__total_active_power.extend(['-'] * (len(x_axis__time) - len(y_datatotal__total_active_power)))
    y_data1__a_phase_active_power.extend(['-'] * (len(x_axis__time) - len(y_data1__a_phase_active_power)))
    y_data2__b_phase_active_power.extend(['-'] * (len(x_axis__time) - len(y_data2__b_phase_active_power)))
    y_data3__c_phase_active_power.extend(['-'] * (len(x_axis__time) - len(y_data3__c_phase_active_power)))

    df = pd.DataFrame(
        {
            '时间': x_axis__time,
            '总有功功率': y_datatotal__total_active_power,
            'A相有功功率': y_data1__a_phase_active_power,
            'B相有功功率': y_data2__b_phase_active_power,
            'C相有功功率': y_data3__c_phase_active_power
        }
    )

    df.to_csv('./Save/ActivePower.csv', index=False)

def get_active_power_data(time_range: list[str] | tuple[str], terminal_output: bool = True) -> dict:
    """
    获取有功功率
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :param terminal_output: 控制终端是否输出
    :return: dict(time:{items: values}) / dict(None)
    """

    spider_data = get_chart_data('ActivePower', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return {}

    electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_datatotal__total_active_power = ast.literal_eval(electricity_data['y_DataTotal'])
    y_data1__a_phase_active_power = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__b_phase_active_power = ast.literal_eval(electricity_data['y_Data2'])
    y_data3__c_phase_active_power = ast.literal_eval(electricity_data['y_Data3'])

    y_datatotal__total_active_power.extend(['-'] * (len(x_axis__time) - len(y_datatotal__total_active_power)))
    y_data1__a_phase_active_power.extend(['-'] * (len(x_axis__time) - len(y_data1__a_phase_active_power)))
    y_data2__b_phase_active_power.extend(['-'] * (len(x_axis__time) - len(y_data2__b_phase_active_power)))
    y_data3__c_phase_active_power.extend(['-'] * (len(x_axis__time) - len(y_data3__c_phase_active_power)))

    return_data = {}

    for i in range(len(x_axis__time)):
        return_data[x_axis__time[i]] = {
            'total_active_power': y_datatotal__total_active_power[i],
            'a_phase_active_power': y_data1__a_phase_active_power[i],
            'b_phase_active_power': y_data2__b_phase_active_power[i],
            'c_phase_active_power': y_data3__c_phase_active_power[i]
        }

    show_data = {
        'time': x_axis__time,
        'total_active_power': y_datatotal__total_active_power,
        'a_phase_active_power': y_data1__a_phase_active_power,
        'b_phase_active_power': y_data2__b_phase_active_power,
        'c_phase_active_power': y_data3__c_phase_active_power
    }

    if terminal_output:
        print(tabulate(show_data, headers='keys', tablefmt='simple', showindex=False))

    return return_data

def reactive_power2csv(time_range: list[str] | tuple[str]) -> None:
    """
    获取无功功率并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: None
    """

    spider_data = get_chart_data('ReactivePower', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return

    electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_datatotal__total_reactive_power = ast.literal_eval(electricity_data['y_DataTotal'])
    y_data1__a_phase_reactive_power = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__b_phase_reactive_power = ast.literal_eval(electricity_data['y_Data2'])
    y_data3__c_phase_reactive_power = ast.literal_eval(electricity_data['y_Data3'])

    y_datatotal__total_reactive_power.extend(['-'] * (len(x_axis__time) - len(y_datatotal__total_reactive_power)))
    y_data1__a_phase_reactive_power.extend(['-'] * (len(x_axis__time) - len(y_data1__a_phase_reactive_power)))
    y_data2__b_phase_reactive_power.extend(['-'] * (len(x_axis__time) - len(y_data2__b_phase_reactive_power)))
    y_data3__c_phase_reactive_power.extend(['-'] * (len(x_axis__time) - len(y_data3__c_phase_reactive_power)))

    df = pd.DataFrame(
        {
            '时间': x_axis__time,
            '总无功功率': y_datatotal__total_reactive_power,
            'A相无功功率': y_data1__a_phase_reactive_power,
            'B相无功功率': y_data2__b_phase_reactive_power,
            'C相无功功率': y_data3__c_phase_reactive_power
        }
    )

    df.to_csv('./Save/ReactivePower.csv', index=False)

def get_reactive_power_data(time_range: list[str] | tuple[str], terminal_output: bool = True) -> dict:
    """
    获取无功功率
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :param terminal_output: 控制终端是否输出
    :return: dict(time:{items: values}) / dict(None)
    """

    spider_data = get_chart_data('ReactivePower', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return {}

    electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_datatotal__total_reactive_power = ast.literal_eval(electricity_data['y_DataTotal'])
    y_data1__a_phase_reactive_power = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__b_phase_reactive_power = ast.literal_eval(electricity_data['y_Data2'])
    y_data3__c_phase_reactive_power = ast.literal_eval(electricity_data['y_Data3'])

    y_datatotal__total_reactive_power.extend(['-'] * (len(x_axis__time) - len(y_datatotal__total_reactive_power)))
    y_data1__a_phase_reactive_power.extend(['-'] * (len(x_axis__time) - len(y_data1__a_phase_reactive_power)))
    y_data2__b_phase_reactive_power.extend(['-'] * (len(x_axis__time) - len(y_data2__b_phase_reactive_power)))
    y_data3__c_phase_reactive_power.extend(['-'] * (len(x_axis__time) - len(y_data3__c_phase_reactive_power)))

    return_data = {}

    for i in range(len(x_axis__time)):
        return_data[x_axis__time[i]] = {
            'total_reactive_power': y_datatotal__total_reactive_power[i],
            'a_phase_reactive_power': y_data1__a_phase_reactive_power[i],
            'b_phase_reactive_power': y_data2__b_phase_reactive_power[i],
            'c_phase_reactive_power': y_data3__c_phase_reactive_power[i]
        }

    show_data = {
        'time': x_axis__time,
        'total_reactive_power': y_datatotal__total_reactive_power,
        'a_phase_reactive_power': y_data1__a_phase_reactive_power,
        'b_phase_reactive_power': y_data2__b_phase_reactive_power,
        'c_phase_reactive_power': y_data3__c_phase_reactive_power
    }

    if terminal_output:
        print(tabulate(show_data, headers='keys', tablefmt='simple', showindex=False))

    return return_data

def active_reactive_power2csv(time_range: list[str] | tuple[str]) -> None:
    """
    获取有功无功功率并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: None
    """

    spider_data = get_chart_data('ActiveReactivePower', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return

    electricity_data1 = spider_data['data'][0]
    electricity_data2 = spider_data['data'][1]

    x_axis__time = ast.literal_eval(electricity_data1['x_Axis'])
    y_datatotal__total_active_power = ast.literal_eval(electricity_data1['y_DataTotal'])
    y_data1__a_phase_active_power = ast.literal_eval(electricity_data1['y_Data1'])
    y_data2__b_phase_active_power = ast.literal_eval(electricity_data1['y_Data2'])
    y_data3__c_phase_active_power = ast.literal_eval(electricity_data1['y_Data3'])
    y_datatotal__total_reactive_power = ast.literal_eval(electricity_data2['y_DataTotal'])
    y_data1__a_phase_reactive_power = ast.literal_eval(electricity_data2['y_Data1'])
    y_data2__b_phase_reactive_power = ast.literal_eval(electricity_data2['y_Data2'])
    y_data3__c_phase_reactive_power = ast.literal_eval(electricity_data2['y_Data3'])

    y_datatotal__total_active_power.extend(['-'] * (len(x_axis__time) - len(y_datatotal__total_active_power)))
    y_data1__a_phase_active_power.extend(['-'] * (len(x_axis__time) - len(y_data1__a_phase_active_power)))
    y_data2__b_phase_active_power.extend(['-'] * (len(x_axis__time) - len(y_data2__b_phase_active_power)))
    y_data3__c_phase_active_power.extend(['-'] * (len(x_axis__time) - len(y_data3__c_phase_active_power)))
    y_datatotal__total_reactive_power.extend(['-'] * (len(x_axis__time) - len(y_datatotal__total_reactive_power)))
    y_data1__a_phase_reactive_power.extend(['-'] * (len(x_axis__time) - len(y_data1__a_phase_reactive_power)))
    y_data2__b_phase_reactive_power.extend(['-'] * (len(x_axis__time) - len(y_data2__b_phase_reactive_power)))
    y_data3__c_phase_reactive_power.extend(['-'] * (len(x_axis__time) - len(y_data3__c_phase_reactive_power)))

    df = pd.DataFrame(
        {
            '时间': x_axis__time,
            '总有功功率': y_datatotal__total_active_power,
            'A相有功功率': y_data1__a_phase_active_power,
            'B相有功功率': y_data2__b_phase_active_power,
            'C相有功功率': y_data3__c_phase_active_power,
            '总无功功率': y_datatotal__total_reactive_power,
            'A相无功功率': y_data1__a_phase_reactive_power,
            'B相无功功率': y_data2__b_phase_reactive_power,
            'C相无功功率': y_data3__c_phase_reactive_power
        }
    )

    df.to_csv('./Save/ActiveReactivePower.csv', index=False)

def get_active_reactive_power_data(time_range: list[str] | tuple[str], terminal_output: bool = True) -> dict:
    """
    获取有功无功功率
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :param terminal_output: 控制终端是否输出
    :return: dict(time:{items: values}) / dict(None)
    """

    spider_data = get_chart_data('ActiveReactivePower', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return {}

    electricity_data1 = spider_data['data'][0]
    electricity_data2 = spider_data['data'][1]

    x_axis__time = ast.literal_eval(electricity_data1['x_Axis'])
    y_datatotal__total_active_power = ast.literal_eval(electricity_data1['y_DataTotal'])
    y_data1__a_phase_active_power = ast.literal_eval(electricity_data1['y_Data1'])
    y_data2__b_phase_active_power = ast.literal_eval(electricity_data1['y_Data2'])
    y_data3__c_phase_active_power = ast.literal_eval(electricity_data1['y_Data3'])
    y_datatotal__total_reactive_power = ast.literal_eval(electricity_data2['y_DataTotal'])
    y_data1__a_phase_reactive_power = ast.literal_eval(electricity_data2['y_Data1'])
    y_data2__b_phase_reactive_power = ast.literal_eval(electricity_data2['y_Data2'])
    y_data3__c_phase_reactive_power = ast.literal_eval(electricity_data2['y_Data3'])

    return_data = {}

    for i in range(len(x_axis__time)):
        return_data[x_axis__time[i]] = {
            'total_active_power': y_datatotal__total_active_power[i],
            'a_phase_active_power': y_data1__a_phase_active_power[i],
            'b_phase_active_power': y_data2__b_phase_active_power[i],
            'c_phase_active_power': y_data3__c_phase_active_power[i],
            'total_reactive_power': y_datatotal__total_reactive_power[i],
            'a_phase_reactive_power': y_data1__a_phase_reactive_power[i],
            'b_phase_reactive_power': y_data2__b_phase_reactive_power[i],
            'c_phase_reactive_power': y_data3__c_phase_reactive_power[i]
        }

    show_data = {
        'time': x_axis__time,
        'total_active_power': y_datatotal__total_active_power,
        'a_phase_active_power': y_data1__a_phase_active_power,
        'b_phase_active_power': y_data2__b_phase_active_power,
        'c_phase_active_power': y_data3__c_phase_active_power,
        'total_reactive_power': y_datatotal__total_reactive_power,
        'a_phase_reactive_power': y_data1__a_phase_reactive_power,
        'b_phase_reactive_power': y_data2__b_phase_reactive_power,
        'c_phase_reactive_power': y_data3__c_phase_reactive_power
    }

    if terminal_output:
        print(tabulate(show_data, headers='keys', tablefmt='simple', showindex=False))

    return return_data

def apparent_power2csv(time_range: list[str] | tuple[str]) -> None:
    """
    获取视在功率并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: None
    """

    spider_data = get_chart_data('ApparentPower', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return

    electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_datatotal__total_apparent_power = ast.literal_eval(electricity_data['y_DataTotal'])
    y_data1__a_phase_apparent_power = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__b_phase_apparent_power = ast.literal_eval(electricity_data['y_Data2'])
    y_data3__c_phase_apparent_power = ast.literal_eval(electricity_data['y_Data3'])

    y_datatotal__total_apparent_power.extend(['-'] * (len(x_axis__time) - len(y_datatotal__total_apparent_power)))
    y_data1__a_phase_apparent_power.extend(['-'] * (len(x_axis__time) - len(y_data1__a_phase_apparent_power)))
    y_data2__b_phase_apparent_power.extend(['-'] * (len(x_axis__time) - len(y_data2__b_phase_apparent_power)))
    y_data3__c_phase_apparent_power.extend(['-'] * (len(x_axis__time) - len(y_data3__c_phase_apparent_power)))

    df = pd.DataFrame(
        {
            '时间': x_axis__time,
            '总视在功率': y_datatotal__total_apparent_power,
            'A相视在功率': y_data1__a_phase_apparent_power,
            'B相视在功率': y_data2__b_phase_apparent_power,
            'C相视在功率': y_data3__c_phase_apparent_power
        }
    )

    df.to_csv('./Save/ApparentPower.csv', index=False)

def get_apparent_power_data(time_range: list[str] | tuple[str], terminal_output: bool = True) -> dict:
    """
    获取视在功率
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :param terminal_output: 控制终端是否输出
    :return: dict(time:{items: values}) / dict(None)
    """

    spider_data = get_chart_data('ApparentPower', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return {}

    electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_datatotal__total_apparent_power = ast.literal_eval(electricity_data['y_DataTotal'])
    y_data1__a_phase_apparent_power = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__b_phase_apparent_power = ast.literal_eval(electricity_data['y_Data2'])
    y_data3__c_phase_apparent_power = ast.literal_eval(electricity_data['y_Data3'])

    y_datatotal__total_apparent_power.extend(['-'] * (len(x_axis__time) - len(y_datatotal__total_apparent_power)))
    y_data1__a_phase_apparent_power.extend(['-'] * (len(x_axis__time) - len(y_data1__a_phase_apparent_power)))
    y_data2__b_phase_apparent_power.extend(['-'] * (len(x_axis__time) - len(y_data2__b_phase_apparent_power)))
    y_data3__c_phase_apparent_power.extend(['-'] * (len(x_axis__time) - len(y_data3__c_phase_apparent_power)))

    return_data = {}

    for i in range(len(x_axis__time)):
        return_data[x_axis__time[i]] = {
            'total_apparent_power': y_datatotal__total_apparent_power[i],
            'a_phase_apparent_power': y_data1__a_phase_apparent_power[i],
            'b_phase_apparent_power': y_data2__b_phase_apparent_power[i],
            'c_phase_apparent_power': y_data3__c_phase_apparent_power[i]
        }

    show_data = {
        'time': x_axis__time,
        'total_apparent_power': y_datatotal__total_apparent_power,
        'a_phase_apparent_power': y_data1__a_phase_apparent_power,
        'b_phase_apparent_power': y_data2__b_phase_apparent_power,
        'c_phase_apparent_power': y_data3__c_phase_apparent_power
    }

    if terminal_output:
        print(tabulate(show_data, headers='keys', tablefmt='simple', showindex=False))

    return return_data

def power_factor2csv(time_range: list[str] | tuple[str]) -> None:
    """
    获取功率因数并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: None
    """

    spider_data = get_chart_data('PowerFactor', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return

    electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_datatotal__total_power_factor = ast.literal_eval(electricity_data['y_DataTotal'])
    y_data1__a_phase_power_factor = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__b_phase_power_factor = ast.literal_eval(electricity_data['y_Data2'])
    y_data3__c_phase_power_factor = ast.literal_eval(electricity_data['y_Data3'])

    y_datatotal__total_power_factor.extend(['-'] * (len(x_axis__time) - len(y_datatotal__total_power_factor)))
    y_data1__a_phase_power_factor.extend(['-'] * (len(x_axis__time) - len(y_data1__a_phase_power_factor)))
    y_data2__b_phase_power_factor.extend(['-'] * (len(x_axis__time) - len(y_data2__b_phase_power_factor)))
    y_data3__c_phase_power_factor.extend(['-'] * (len(x_axis__time) - len(y_data3__c_phase_power_factor)))

    df = pd.DataFrame(
        {
            '时间': x_axis__time,
            '总功率因数': y_datatotal__total_power_factor,
            'A相功率因数': y_data1__a_phase_power_factor,
            'B相功率因数': y_data2__b_phase_power_factor,
            'C相功率因数': y_data3__c_phase_power_factor
        }
    )

    df.to_csv('./Save/PowerFactor.csv', index=False)

def get_power_factor_data(time_range: list[str] | tuple[str], terminal_output: bool = True) -> dict:
    """
    获取功率因数
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :param terminal_output: 控制终端是否输出
    :return: dict(time:{items: values}) / dict(None)
    """

    spider_data = get_chart_data('PowerFactor', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return {}

    electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_datatotal__total_power_factor = ast.literal_eval(electricity_data['y_DataTotal'])
    y_data1__a_phase_power_factor = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__b_phase_power_factor = ast.literal_eval(electricity_data['y_Data2'])
    y_data3__c_phase_power_factor = ast.literal_eval(electricity_data['y_Data3'])

    y_datatotal__total_power_factor.extend(['-'] * (len(x_axis__time) - len(y_datatotal__total_power_factor)))
    y_data1__a_phase_power_factor.extend(['-'] * (len(x_axis__time) - len(y_data1__a_phase_power_factor)))
    y_data2__b_phase_power_factor.extend(['-'] * (len(x_axis__time) - len(y_data2__b_phase_power_factor)))
    y_data3__c_phase_power_factor.extend(['-'] * (len(x_axis__time) - len(y_data3__c_phase_power_factor)))

    return_data = {}

    for i in range(len(x_axis__time)):
        return_data[x_axis__time[i]] = {
            'total_power_factor': y_datatotal__total_power_factor[i],
            'a_phase_power_factor': y_data1__a_phase_power_factor[i],
            'b_phase_power_factor': y_data2__b_phase_power_factor[i],
            'c_phase_power_factor': y_data3__c_phase_power_factor[i]
        }

    show_data = {
        'time': x_axis__time,
        'total_power_factor': y_datatotal__total_power_factor,
        'a_phase_power_factor': y_data1__a_phase_power_factor,
        'b_phase_power_factor': y_data2__b_phase_power_factor,
        'c_phase_power_factor': y_data3__c_phase_power_factor
    }

    if terminal_output:
        print(tabulate(show_data, headers='keys', tablefmt='simple', showindex=False))

    return return_data

def maximum_demand2csv(time_range: list[str] | tuple[str]) -> None:
    """
    获取最大需量并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: None
    """

    spider_data = get_chart_data('MaximumDemand', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return

    electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_datatotal__maximum_demand = ast.literal_eval(electricity_data['y_DataTotal'])

    y_datatotal__maximum_demand.extend(['-'] * (len(x_axis__time) - len(y_datatotal__maximum_demand)))

    df = pd.DataFrame({'时间': x_axis__time, '最大需量': y_datatotal__maximum_demand})

    df.to_csv('./Save/MaximumDemand.csv', index=False)

def get_maximum_demand_data(time_range: list[str] | tuple[str], terminal_output: bool = True) -> dict:
    """
    获取最大需量
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :param terminal_output: 控制终端是否输出
    :return: dict(time:{items: values}) / dict(None)
    """

    spider_data = get_chart_data('MaximumDemand', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return {}

    electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_datatotal__maximum_demand = ast.literal_eval(electricity_data['y_DataTotal'])

    y_datatotal__maximum_demand.extend(['-'] * (len(x_axis__time) - len(y_datatotal__maximum_demand)))

    return_data = {}

    for i in range(len(x_axis__time)):
        return_data[x_axis__time[i]] = {'maximum_demand': y_datatotal__maximum_demand[i]}

    show_data = {'time': x_axis__time, 'maximum_demand': y_datatotal__maximum_demand}

    if terminal_output:
        print(tabulate(show_data, headers='keys', tablefmt='simple', showindex=False))

    return return_data

def voltage2csv(time_range: list[str] | tuple[str]) -> None:
    """
    获取电压并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: None
    """

    spider_data = get_chart_data('Voltage', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return

    electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_data1__a_phase_voltage = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__b_phase_voltage = ast.literal_eval(electricity_data['y_Data2'])
    y_data3__c_phase_voltage = ast.literal_eval(electricity_data['y_Data3'])
    y_data_total__three_phase_voltage_imbalance = ast.literal_eval(electricity_data['y_DataTotal'])

    y_data1__a_phase_voltage.extend(['-'] * (len(x_axis__time) - len(y_data1__a_phase_voltage)))
    y_data2__b_phase_voltage.extend(['-'] * (len(x_axis__time) - len(y_data2__b_phase_voltage)))
    y_data3__c_phase_voltage.extend(['-'] * (len(x_axis__time) - len(y_data3__c_phase_voltage)))
    y_data_total__three_phase_voltage_imbalance.extend(
        ['-'] * (len(x_axis__time) - len(y_data_total__three_phase_voltage_imbalance))
    )

    df = pd.DataFrame(
        {
            '时间': x_axis__time,
            'A相电压': y_data1__a_phase_voltage,
            'B相电压': y_data2__b_phase_voltage,
            'C相电压': y_data3__c_phase_voltage,
            '三相电压不平衡度（%）': y_data_total__three_phase_voltage_imbalance
        }
    )

    df.to_csv('./Save/Voltage.csv', index=False)

def get_voltage_data(time_range: list[str] | tuple[str], terminal_output: bool = True) -> dict:
    """
    获取电压
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :param terminal_output: 控制终端是否输出
    :return: dict(time:{items: values}) / dict(None)
    """

    spider_data = get_chart_data('Voltage', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return {}

    electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_data1__a_phase_voltage = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__b_phase_voltage = ast.literal_eval(electricity_data['y_Data2'])
    y_data3__c_phase_voltage = ast.literal_eval(electricity_data['y_Data3'])
    y_data_total__three_phase_voltage_imbalance = ast.literal_eval(electricity_data['y_DataTotal'])

    y_data1__a_phase_voltage.extend(['-'] * (len(x_axis__time) - len(y_data1__a_phase_voltage)))
    y_data2__b_phase_voltage.extend(['-'] * (len(x_axis__time) - len(y_data2__b_phase_voltage)))
    y_data3__c_phase_voltage.extend(['-'] * (len(x_axis__time) - len(y_data3__c_phase_voltage)))
    y_data_total__three_phase_voltage_imbalance.extend(
        ['-'] * (len(x_axis__time) - len(y_data_total__three_phase_voltage_imbalance))
    )

    return_data = {}

    for i in range(len(x_axis__time)):
        return_data[x_axis__time[i]] = {
            'a_phase_voltage': y_data1__a_phase_voltage[i],
            'b_phase_voltage': y_data2__b_phase_voltage[i],
            'c_phase_voltage': y_data3__c_phase_voltage[i],
            'three_phase_voltage_imbalance': y_data_total__three_phase_voltage_imbalance[i]
        }

    show_data = {
        'time': x_axis__time,
        'a_phase_voltage': y_data1__a_phase_voltage,
        'b_phase_voltage': y_data2__b_phase_voltage,
        'c_phase_voltage': y_data3__c_phase_voltage,
        'three_phase_voltage_imbalance(%)': y_data_total__three_phase_voltage_imbalance
    }

    if terminal_output:
        print(tabulate(show_data, headers='keys', tablefmt='simple', showindex=False))

    return return_data

def current2csv(time_range: list[str] | tuple[str]) -> None:
    """
    获取电流并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: None
    """

    spider_data = get_chart_data('Current', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return

    electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_data1__a_phase_current = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__b_phase_current = ast.literal_eval(electricity_data['y_Data2'])
    y_data3__c_phase_current = ast.literal_eval(electricity_data['y_Data3'])
    y_data_total__three_phase_current_imbalance = ast.literal_eval(electricity_data['y_DataTotal'])

    y_data1__a_phase_current.extend(['-'] * (len(x_axis__time) - len(y_data1__a_phase_current)))
    y_data2__b_phase_current.extend(['-'] * (len(x_axis__time) - len(y_data2__b_phase_current)))
    y_data3__c_phase_current.extend(['-'] * (len(x_axis__time) - len(y_data3__c_phase_current)))
    y_data_total__three_phase_current_imbalance.extend(
        ['-'] * (len(x_axis__time) - len(y_data_total__three_phase_current_imbalance))
    )

    df = pd.DataFrame(
        {
            '时间': x_axis__time,
            'A相电流': y_data1__a_phase_current,
            'B相电流': y_data2__b_phase_current,
            'C相电流': y_data3__c_phase_current,
            '三相电流不平衡度（%）': y_data_total__three_phase_current_imbalance
        }
    )

    df.to_csv('./Save/Current.csv', index=False)

def get_current_data(time_range: list[str] | tuple[str], terminal_output: bool = True) -> dict:
    """
    获取电流
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :param terminal_output: 控制终端是否输出
    :return: dict(time:{items: values}) / dict(None)
    """

    spider_data = get_chart_data('Current', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return {}

    electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_data1__a_phase_current = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__b_phase_current = ast.literal_eval(electricity_data['y_Data2'])
    y_data3__c_phase_current = ast.literal_eval(electricity_data['y_Data3'])
    y_data_total__three_phase_current_imbalance = ast.literal_eval(electricity_data['y_DataTotal'])

    y_data1__a_phase_current.extend(['-'] * (len(x_axis__time) - len(y_data1__a_phase_current)))
    y_data2__b_phase_current.extend(['-'] * (len(x_axis__time) - len(y_data2__b_phase_current)))
    y_data3__c_phase_current.extend(['-'] * (len(x_axis__time) - len(y_data3__c_phase_current)))
    y_data_total__three_phase_current_imbalance.extend(
        ['-'] * (len(x_axis__time) - len(y_data_total__three_phase_current_imbalance))
    )

    return_data = {}

    for i in range(len(x_axis__time)):
        return_data[x_axis__time[i]] = {
            'a_phase_current': y_data1__a_phase_current[i],
            'b_phase_current': y_data2__b_phase_current[i],
            'c_phase_current': y_data3__c_phase_current[i],
            'three_phase_current_imbalance': y_data_total__three_phase_current_imbalance[i]
        }

    show_data = {
        'time': x_axis__time,
        'a_phase_current': y_data1__a_phase_current,
        'b_phase_current': y_data2__b_phase_current,
        'c_phase_current': y_data3__c_phase_current,
        'three_phase_current_imbalance(%)': y_data_total__three_phase_current_imbalance
    }

    if terminal_output:
        print(tabulate(show_data, headers='keys', tablefmt='simple', showindex=False))

    return return_data

def voltage_current2csv(time_range: list[str] | tuple[str]) -> None:
    """
    获取电压电流并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: None
    """

    spider_data = get_chart_data('VoltageCurrentHz', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return

    electricity_data1 = spider_data['data'][0]
    electricity_data2 = spider_data['data'][1]

    x_axis__time = ast.literal_eval(electricity_data1['x_Axis'])
    y_data1__a_phase_voltage = ast.literal_eval(electricity_data1['y_Data1'])
    y_data2__b_phase_voltage = ast.literal_eval(electricity_data1['y_Data2'])
    y_data3__c_phase_voltage = ast.literal_eval(electricity_data1['y_Data3'])
    y_data1__a_phase_current = ast.literal_eval(electricity_data2['y_Data1'])
    y_data2__b_phase_current = ast.literal_eval(electricity_data2['y_Data2'])
    y_data3__c_phase_current = ast.literal_eval(electricity_data2['y_Data3'])

    y_data1__a_phase_voltage.extend(['-'] * (len(x_axis__time) - len(y_data1__a_phase_voltage)))
    y_data2__b_phase_voltage.extend(['-'] * (len(x_axis__time) - len(y_data2__b_phase_voltage)))
    y_data3__c_phase_voltage.extend(['-'] * (len(x_axis__time) - len(y_data3__c_phase_voltage)))
    y_data1__a_phase_current.extend(['-'] * (len(x_axis__time) - len(y_data1__a_phase_current)))
    y_data2__b_phase_current.extend(['-'] * (len(x_axis__time) - len(y_data2__b_phase_current)))
    y_data3__c_phase_current.extend(['-'] * (len(x_axis__time) - len(y_data3__c_phase_current)))

    df = pd.DataFrame(
        {
            '时间': x_axis__time,
            'A相电压': y_data1__a_phase_voltage,
            'B相电压': y_data2__b_phase_voltage,
            'C相电压': y_data3__c_phase_voltage,
            'A相电流': y_data1__a_phase_current,
            'B相电流': y_data2__b_phase_current,
            'C相电流': y_data3__c_phase_current,
        }
    )

    df.to_csv('./Save/VoltageCurrentHz.csv', index=False)

def get_voltage_current_data(time_range: list[str] | tuple[str], terminal_output: bool = True) -> dict:
    """
    获取电压电流
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :param terminal_output: 控制终端是否输出
    :return: dict(time:{items: values}) / dict(None)
    """

    spider_data = get_chart_data('VoltageCurrentHz', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return {}

    electricity_data1 = spider_data['data'][0]
    electricity_data2 = spider_data['data'][1]

    x_axis__time = ast.literal_eval(electricity_data1['x_Axis'])
    y_data1__a_phase_voltage = ast.literal_eval(electricity_data1['y_Data1'])
    y_data2__b_phase_voltage = ast.literal_eval(electricity_data1['y_Data2'])
    y_data3__c_phase_voltage = ast.literal_eval(electricity_data1['y_Data3'])
    y_data1__a_phase_current = ast.literal_eval(electricity_data2['y_Data1'])
    y_data2__b_phase_current = ast.literal_eval(electricity_data2['y_Data2'])
    y_data3__c_phase_current = ast.literal_eval(electricity_data2['y_Data3'])

    y_data1__a_phase_voltage.extend(['-'] * (len(x_axis__time) - len(y_data1__a_phase_voltage)))
    y_data2__b_phase_voltage.extend(['-'] * (len(x_axis__time) - len(y_data2__b_phase_voltage)))
    y_data3__c_phase_voltage.extend(['-'] * (len(x_axis__time) - len(y_data3__c_phase_voltage)))
    y_data1__a_phase_current.extend(['-'] * (len(x_axis__time) - len(y_data1__a_phase_current)))
    y_data2__b_phase_current.extend(['-'] * (len(x_axis__time) - len(y_data2__b_phase_current)))
    y_data3__c_phase_current.extend(['-'] * (len(x_axis__time) - len(y_data3__c_phase_current)))

    return_data = {}

    for i in range(len(x_axis__time)):
        return_data[x_axis__time[i]] = {
            'a_phase_voltage': y_data1__a_phase_voltage[i],
            'b_phase_voltage': y_data2__b_phase_voltage[i],
            'c_phase_voltage': y_data3__c_phase_voltage[i],
            'a_phase_current': y_data1__a_phase_current[i],
            'b_phase_current': y_data2__b_phase_current[i],
            'c_phase_current': y_data3__c_phase_current[i],
        }

    show_data = {
        'time': x_axis__time,
        'a_phase_voltage': y_data1__a_phase_voltage,
        'b_phase_voltage': y_data2__b_phase_voltage,
        'c_phase_voltage': y_data3__c_phase_voltage,
        'a_phase_current': y_data1__a_phase_current,
        'b_phase_current': y_data2__b_phase_current,
        'c_phase_current': y_data3__c_phase_current,
    }

    if terminal_output:
        print(tabulate(show_data, headers='keys', tablefmt='simple', showindex=False))

    return return_data

def electricity_bill2csv(time_range: list[str] | tuple[str]) -> None:
    """
    获取电费并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: None
    """

    spider_data = get_chart_data('ElectricityBill', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return

    electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_data1__sharp_electricity_bill = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__peak_electricity_bill = ast.literal_eval(electricity_data['y_Data2'])
    y_data3__flat_electricity_bill = ast.literal_eval(electricity_data['y_Data3'])
    y_data4__valley_electricity_bill = ast.literal_eval(electricity_data['y_Data4'])
    y_data_total__total_real_electricity_bill = ast.literal_eval(electricity_data['y_DataTotal'])

    y_data1__sharp_electricity_bill.extend([0] * (len(x_axis__time) - len(y_data1__sharp_electricity_bill)))
    y_data2__peak_electricity_bill.extend([0] * (len(x_axis__time) - len(y_data2__peak_electricity_bill)))
    y_data3__flat_electricity_bill.extend([0] * (len(x_axis__time) - len(y_data3__flat_electricity_bill)))
    y_data4__valley_electricity_bill.extend([0] * (len(x_axis__time) - len(y_data4__valley_electricity_bill)))
    y_data_total__total_real_electricity_bill.extend(
        [0] * (len(x_axis__time) - len(y_data_total__total_real_electricity_bill))
    )

    df = pd.DataFrame(
        {
            '时间': x_axis__time,
            '尖电费（元）': y_data1__sharp_electricity_bill,
            '峰电费（元）': y_data2__peak_electricity_bill,
            '平电费（元）': y_data3__flat_electricity_bill,
            '谷电费（元）': y_data4__valley_electricity_bill,
            '实际总电费（元）': y_data_total__total_real_electricity_bill
        }
    )

    df.to_csv('./Save/ElectricityBill.csv', index=False)

def get_electricity_bill_data(time_range: list[str] | tuple[str], terminal_output: bool = True) -> dict:
    """
    获取冻结电费并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :param terminal_output: 控制终端是否输出
    :return: dict(time:{items: values}) / dict(None)
    """

    spider_data = get_chart_data('ElectricityBill', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return {}

    electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_data1__sharp_electricity_bill = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__peak_electricity_bill = ast.literal_eval(electricity_data['y_Data2'])
    y_data3__flat_electricity_bill = ast.literal_eval(electricity_data['y_Data3'])
    y_data4__valley_electricity_bill = ast.literal_eval(electricity_data['y_Data4'])
    y_data_total__total_real_electricity_bill = ast.literal_eval(electricity_data['y_DataTotal'])

    y_data1__sharp_electricity_bill.extend([0] * (len(x_axis__time) - len(y_data1__sharp_electricity_bill)))
    y_data2__peak_electricity_bill.extend([0] * (len(x_axis__time) - len(y_data2__peak_electricity_bill)))
    y_data3__flat_electricity_bill.extend([0] * (len(x_axis__time) - len(y_data3__flat_electricity_bill)))
    y_data4__valley_electricity_bill.extend([0] * (len(x_axis__time) - len(y_data4__valley_electricity_bill)))
    y_data_total__total_real_electricity_bill.extend(
        [0] * (len(x_axis__time) - len(y_data_total__total_real_electricity_bill))
    )

    return_data = {}

    for i in range(len(x_axis__time)):
        return_data[x_axis__time[i]] = {
            'sharp_electricity_bill': y_data1__sharp_electricity_bill[i],
            'peak_electricity_bill': y_data2__peak_electricity_bill[i],
            'flat_electricity_bill': y_data3__flat_electricity_bill[i],
            'valley_electricity_bill': y_data4__valley_electricity_bill[i],
            'total_real_electricity_bill': y_data_total__total_real_electricity_bill[i]
        }

    show_data = {
        'time': x_axis__time,
        'sharp_electricity_bill': y_data1__sharp_electricity_bill,
        'peak_electricity_bill': y_data2__peak_electricity_bill,
        'flat_electricity_bill': y_data3__flat_electricity_bill,
        'valley_electricity_bill': y_data4__valley_electricity_bill,
        'total_real_electricity_bill': y_data_total__total_real_electricity_bill
    }

    if terminal_output:
        print(tabulate(show_data, headers='keys', tablefmt='simple', showindex=False))

    return return_data

# ======================================================================================================================
def summary_active_electric_quantity2csv(time_range: list[str] | tuple[str]) -> None:
    """
    获取有功电量汇总并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: None
    """

    spider_data = get_summary_data('SummaryActiveElectricQuantity', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return

    summary_electricity_data1 = spider_data['data'][0]
    summary_electricity_data2 = spider_data['data'][1]

    x__time = time_range[0] + '--' + time_range[1]
    total_positive_active_electric_quantity = summary_electricity_data1['Total']
    total_negative_active_electric_quantity = summary_electricity_data2['Total']

    spider_data = get_chart_data('ActiveElectricQuantity', time_range)  # 傻逼网站，页面明明有最值不写在返回数据里
    electricity_data = spider_data['data'][0]  # 还要他妈自己算

    y_data1__total_positive_active_electric_quantity = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__total_negative_active_electric_quantity = ast.literal_eval(electricity_data['y_Data2'])

    try:
        for i in range(len(y_data1__total_positive_active_electric_quantity)):
            if y_data1__total_positive_active_electric_quantity[i] == '-' \
                or y_data1__total_positive_active_electric_quantity[i] is None:

                y_data1__total_positive_active_electric_quantity[i] = 0

            else:
                y_data1__total_positive_active_electric_quantity[i] = float(
                    y_data1__total_positive_active_electric_quantity[i]
                )

        for i in range(len(y_data2__total_negative_active_electric_quantity)):
            if y_data2__total_negative_active_electric_quantity[i] == '-' \
                or y_data2__total_negative_active_electric_quantity[i] is None:

                y_data2__total_negative_active_electric_quantity[i] = 0

            else:
                y_data2__total_negative_active_electric_quantity[i] = float(
                    y_data2__total_negative_active_electric_quantity[i]
                )

    except ValueError as e:
        print('数据转换错误，我他妈怎么知道这傻逼网站给我什么东西，自己看：', e)
        return
    except TypeError as e:
        print('数据转换错误，我他妈怎么知道这傻逼网站给我什么东西，自己看：', e)
        return

    positive_active_electric_quantity_maximum = max(y_data1__total_positive_active_electric_quantity)
    positive_active_electric_quantity_minimum = min(y_data1__total_positive_active_electric_quantity)
    negative_active_electric_quantity_maximum = max(y_data2__total_negative_active_electric_quantity)
    negative_active_electric_quantity_minimum = min(y_data2__total_negative_active_electric_quantity)

    df = pd.DataFrame(
        {
            '时间': [x__time],
            '正向有功总电量': [total_positive_active_electric_quantity],
            '正向有功总电量最大值': [positive_active_electric_quantity_maximum],
            '正向有功总电量最小值': [positive_active_electric_quantity_minimum],
            '反向有功总电量': [total_negative_active_electric_quantity],
            '反向有功总电量最大值': [negative_active_electric_quantity_maximum],
            '反向有功总电量最小值': [negative_active_electric_quantity_minimum]
        }
    )

    df.to_csv('./Save/SummaryActiveElectricQuantity.csv', index=False)

def get_summary_active_electric_quantity_data(time_range: list[str] | tuple[str], terminal_output: bool = True) -> dict:
    """
    获取有功电量汇总
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :param terminal_output: 控制终端是否输出
    :return: dict(items: values) / dict(None)
    """

    spider_data = get_summary_data('SummaryActiveElectricQuantity', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return {}

    summary_electricity_data1 = spider_data['data'][0]
    summary_electricity_data2 = spider_data['data'][1]

    x__time = time_range[0] + '--' + time_range[1]
    total_positive_active_electric_quantity = summary_electricity_data1['Total']
    total_negative_active_electric_quantity = summary_electricity_data2['Total']

    spider_data = get_chart_data('ActiveElectricQuantity', time_range)  # 傻逼网站，页面明明有最值不写在返回数据里
    electricity_data = spider_data['data'][0]  # 还要他妈自己算

    y_data1__total_positive_active_electric_quantity = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__total_negative_active_electric_quantity = ast.literal_eval(electricity_data['y_Data2'])

    try:
        for i in range(len(y_data1__total_positive_active_electric_quantity)):
            if y_data1__total_positive_active_electric_quantity[i] == '-' \
                    or y_data1__total_positive_active_electric_quantity[i] is None:

                y_data1__total_positive_active_electric_quantity[i] = 0

            else:
                y_data1__total_positive_active_electric_quantity[i] = float(
                    y_data1__total_positive_active_electric_quantity[i]
                )

        for i in range(len(y_data2__total_negative_active_electric_quantity)):
            if y_data2__total_negative_active_electric_quantity[i] == '-' \
                    or y_data2__total_negative_active_electric_quantity[i] is None:

                y_data2__total_negative_active_electric_quantity[i] = 0

            else:
                y_data2__total_negative_active_electric_quantity[i] = float(
                    y_data2__total_negative_active_electric_quantity[i]
                )

    except ValueError as e:
        print('数据转换错误，我他妈怎么知道这傻逼网站给我什么东西，自己看：', e)
        return {}
    except TypeError as e:
        print('数据转换错误，我他妈怎么知道这傻逼网站给我什么东西，自己看：', e)
        return {}

    positive_active_electric_quantity_maximum = max(y_data1__total_positive_active_electric_quantity)
    positive_active_electric_quantity_minimum = min(y_data1__total_positive_active_electric_quantity)
    negative_active_electric_quantity_maximum = max(y_data2__total_negative_active_electric_quantity)
    negative_active_electric_quantity_minimum = min(y_data2__total_negative_active_electric_quantity)

    return_data = {
        'total_positive_electric_quantity': total_positive_active_electric_quantity,
        'positive_electric_quantity_maximum': positive_active_electric_quantity_maximum,
        'positive_electric_quantity_minimum': positive_active_electric_quantity_minimum,
        'total_negative_electric_quantity': total_negative_active_electric_quantity,
        'negative_electric_quantity_maximum': negative_active_electric_quantity_maximum,
        'negative_electric_quantity_minimum': negative_active_electric_quantity_minimum
    }

    show_data = {
        'time': [x__time],
        'total_positive_electric_quantity': [total_positive_active_electric_quantity],
        'positive_electric_quantity_maximum': [positive_active_electric_quantity_maximum],
        'positive_electric_quantity_minimum': [positive_active_electric_quantity_minimum],
        'total_negative_electric_quantity': [total_negative_active_electric_quantity],
        'negative_electric_quantity_maximum': [negative_active_electric_quantity_maximum],
        'negative_electric_quantity_minimum': [negative_active_electric_quantity_minimum]
    }

    if terminal_output:
        print(tabulate(show_data, headers='keys', tablefmt='simple', showindex=False))

    return return_data

def summary_frozen_electric_quantity2csv(time_range: list[str] | tuple[str]) -> None:
    """
    获取冻结电量汇总并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: None
    """

    spider_data = get_summary_data('SummaryFrozenElectricQuantity', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return

    summary_electricity_data = spider_data['data']

    x__time = time_range[0] + '--' + time_range[1]
    totalkwh__total_electric_quantity = summary_electricity_data['TotalKwh']
    usekwh1__sharp_electric_quantity = summary_electricity_data['UseKwh1']
    usekwh2__peak_electric_quantity = summary_electricity_data['UseKwh2']
    usekwh3__flat_electric_quantity = summary_electricity_data['UseKwh3']
    usekwh4__valley_electric_quantity = summary_electricity_data['UseKwh4']


    df = pd.DataFrame(
        {
            '时间': [x__time],
            '日冻结电量': [totalkwh__total_electric_quantity],
            '尖电量': [usekwh1__sharp_electric_quantity],
            '峰电量': [usekwh2__peak_electric_quantity],
            '平电量': [usekwh3__flat_electric_quantity],
            '谷电量': [usekwh4__valley_electric_quantity]
        }
    )

    df.to_csv('./Save/SummaryFrozenElectricQuantity.csv', index=False)

def get_summary_frozen_electric_quantity_data(time_range: list[str] | tuple[str], terminal_output: bool = True) -> dict:
    """
    获取冻结电量汇总
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :param terminal_output: 控制终端是否输出
    :return: dict(time:{items: values}) / dict(None)
    """

    spider_data = get_summary_data('SummaryFrozenElectricQuantity', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return {}

    summary_electricity_data = spider_data['data']

    x__time = time_range[0] + '--' + time_range[1]
    totalkwh__total_frozen_electric_quantity = summary_electricity_data['TotalKwh']
    usekwh1__sharp_frozen_electric_quantity = summary_electricity_data['UseKwh1']
    usekwh2__peak_frozen_electric_quantity = summary_electricity_data['UseKwh2']
    usekwh3__flat_frozen_electric_quantity = summary_electricity_data['UseKwh3']
    usekwh4__valley_frozen_electric_quantity = summary_electricity_data['UseKwh4']

    return_data = {
        'total_frozen_electric_quantity': totalkwh__total_frozen_electric_quantity,
        'sharp_frozen_electric_quantity': usekwh1__sharp_frozen_electric_quantity,
        'peak_frozen_electric_quantity': usekwh2__peak_frozen_electric_quantity,
        'flat_frozen_electric_quantity': usekwh3__flat_frozen_electric_quantity,
        'valley_frozen_electric_quantity': usekwh4__valley_frozen_electric_quantity
    }

    show_data = {
        'time': [x__time],
        'total_frozen_electric_quantity': [totalkwh__total_frozen_electric_quantity],
        'sharp_frozen_electric_quantity': [usekwh1__sharp_frozen_electric_quantity],
        'peak_frozen_electric_quantity': [usekwh2__peak_frozen_electric_quantity],
        'flat_frozen_electric_quantity': [usekwh3__flat_frozen_electric_quantity],
        'valley_frozen_electric_quantity': [usekwh4__valley_frozen_electric_quantity]
    }

    if terminal_output:
        print(tabulate(show_data, headers='keys', tablefmt='simple', showindex=False))

    return return_data

def summary_anti_frozen_electric_quantity2csv(time_range: list[str] | tuple[str]) -> None:
    """
    获取反冻结电量汇总并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: None
    """

    spider_data = get_summary_data('SummaryAntiFrozenElectricQuantity', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return

    summary_electricity_data = spider_data['data']

    x__time = time_range[0] + '--' + time_range[1]
    totalkwh__total_anti_frozen_electric_quantity = summary_electricity_data['TotalKwh']
    usekwh1__sharp_anti_frozen_electric_quantity = summary_electricity_data['UseKwh1']
    usekwh2__peak_anti_frozen_electric_quantity = summary_electricity_data['UseKwh2']
    usekwh3__flat_anti_frozen_electric_quantity = summary_electricity_data['UseKwh3']
    usekwh4__valley_anti_frozen_electric_quantity = summary_electricity_data['UseKwh4']

    df = pd.DataFrame(
        {
            '时间': [x__time],
            '日冻结电量': [totalkwh__total_anti_frozen_electric_quantity],
            '尖电量': [usekwh1__sharp_anti_frozen_electric_quantity],
            '峰电量': [usekwh2__peak_anti_frozen_electric_quantity],
            '平电量': [usekwh3__flat_anti_frozen_electric_quantity],
            '谷电量': [usekwh4__valley_anti_frozen_electric_quantity]
        }
    )

    df.to_csv('./Save/SummaryAntiFrozenElectricQuantity.csv', index=False)

def get_summary_anti_frozen_electric_quantity_data(
        time_range: list[str] | tuple[str],
        terminal_output: bool = True
) -> dict:
    """
    获取反冻结电量汇总
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :param terminal_output: 控制终端是否输出
    :return: dict(items: values) / dict(None)
    """

    spider_data = get_summary_data('SummaryAntiFrozenElectricQuantity', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return {}

    summary_electricity_data = spider_data['data']

    x__time = time_range[0] + '--' + time_range[1]
    totalkwh__total_anti_frozen_electric_quantity = summary_electricity_data['TotalKwh']
    usekwh1__sharp_anti_frozen_electric_quantity = summary_electricity_data['UseKwh1']
    usekwh2__peak_anti_frozen_electric_quantity = summary_electricity_data['UseKwh2']
    usekwh3__flat_anti_frozen_electric_quantity = summary_electricity_data['UseKwh3']
    usekwh4__valley_anti_frozen_electric_quantity = summary_electricity_data['UseKwh4']

    return_data = {
        'total_anti_frozen_electric_quantity': totalkwh__total_anti_frozen_electric_quantity ,
        'sharp_anti_frozen_electric_quantity': usekwh1__sharp_anti_frozen_electric_quantity,
        'peak_anti_frozen_electric_quantity': usekwh2__peak_anti_frozen_electric_quantity,
        'flat_anti_frozen_electric_quantity': usekwh3__flat_anti_frozen_electric_quantity,
        'valley_anti_frozen_electric_quantity': usekwh4__valley_anti_frozen_electric_quantity
    }

    show_data = {
        'time': [x__time],
        'total_anti_frozen_electric_quantity': [totalkwh__total_anti_frozen_electric_quantity],
        'sharp_anti_frozen_electric_quantity': [usekwh1__sharp_anti_frozen_electric_quantity],
        'peak_anti_frozen_electric_quantity': [usekwh2__peak_anti_frozen_electric_quantity],
        'flat_anti_frozen_electric_quantity': [usekwh3__flat_anti_frozen_electric_quantity],
        'valley_anti_frozen_electric_quantity': [usekwh4__valley_anti_frozen_electric_quantity]
    }

    if terminal_output:
        print(tabulate(show_data, headers='keys', tablefmt='simple', showindex=False))

    return return_data

def summary_reactive_electric_quantity2csv(time_range: list[str] | tuple[str]) -> None:
    """
    获取无功电量汇总并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: None
    """

    spider_data = get_summary_data('SummaryReactiveElectricQuantity', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return

    summary_electricity_data1 = spider_data['data'][0]
    summary_electricity_data2 = spider_data['data'][1]

    x__time = time_range[0] + '--' + time_range[1]
    total_positive_reactive_electric_quantity = summary_electricity_data1['Total']
    total_negative_reactive_electric_quantity = summary_electricity_data2['Total']

    spider_data = get_chart_data('ReactiveElectricQuantity', time_range)
    electricity_data = spider_data['data'][0]

    y_data1__total_positive_reactive_electric_quantity = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__total_negative_reactive_electric_quantity = ast.literal_eval(electricity_data['y_Data2'])

    try:
        for i in range(len(y_data1__total_positive_reactive_electric_quantity)):
            if y_data1__total_positive_reactive_electric_quantity[i] == '-' \
                or y_data1__total_positive_reactive_electric_quantity[i] is None:

                y_data1__total_positive_reactive_electric_quantity[i] = 0

            else:
                y_data1__total_positive_reactive_electric_quantity[i] = float(
                    y_data1__total_positive_reactive_electric_quantity[i]
                )

        for i in range(len(y_data2__total_negative_reactive_electric_quantity)):
            if y_data2__total_negative_reactive_electric_quantity[i] == '-' \
                or y_data2__total_negative_reactive_electric_quantity[i] is None:

                y_data2__total_negative_reactive_electric_quantity[i] = 0

            else:
                y_data2__total_negative_reactive_electric_quantity[i] = float(
                    y_data2__total_negative_reactive_electric_quantity[i]
                )

    except ValueError as e:
        print('数据转换错误，我他妈怎么知道这傻逼网站给我什么东西，自己看：', e)
        return
    except TypeError as e:
        print('数据转换错误，我他妈怎么知道这傻逼网站给我什么东西，自己看：', e)
        return

    positive_reactive_electric_quantity_maximum = max(y_data1__total_positive_reactive_electric_quantity)
    positive_reactive_electric_quantity_minimum = min(y_data1__total_positive_reactive_electric_quantity)
    negative_reactive_electric_quantity_maximum = max(y_data2__total_negative_reactive_electric_quantity)
    negative_reactive_electric_quantity_minimum = min(y_data2__total_negative_reactive_electric_quantity)

    df = pd.DataFrame(
        {
            '时间': [x__time],
            '正向无功总电量': [total_positive_reactive_electric_quantity],
            '正向无功总电量最大值': [positive_reactive_electric_quantity_maximum],
            '正向无功总电量最小值': [positive_reactive_electric_quantity_minimum],
            '反向无功总电量': [total_negative_reactive_electric_quantity],
            '反向无功总电量最大值': [negative_reactive_electric_quantity_maximum],
            '反向无功总电量最小值': [negative_reactive_electric_quantity_minimum]
        }
    )

    df.to_csv('./Save/SummaryReactiveElectricQuantity.csv', index=False)

def get_summary_reactive_electric_quantity_data(
        time_range: list[str] | tuple[str],
        terminal_output: bool = True
) -> dict:
    """
    获取无功电量汇总
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :param terminal_output: 控制终端是否输出
    :return: dict(items: values) / dict(None)
    """

    spider_data = get_summary_data('SummaryReactiveElectricQuantity', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return {}

    summary_electricity_data1 = spider_data['data'][0]
    summary_electricity_data2 = spider_data['data'][1]

    x__time = time_range[0] + '--' + time_range[1]
    total_positive_reactive_electric_quantity = summary_electricity_data1['Total']
    total_negative_reactive_electric_quantity = summary_electricity_data2['Total']

    spider_data = get_chart_data('ReactiveElectricQuantity', time_range)
    electricity_data = spider_data['data'][0]

    y_data1__total_positive_reactive_electric_quantity = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__total_negative_reactive_electric_quantity = ast.literal_eval(electricity_data['y_Data2'])

    try:
        for i in range(len(y_data1__total_positive_reactive_electric_quantity)):
            if y_data1__total_positive_reactive_electric_quantity[i] == '-' \
                or y_data1__total_positive_reactive_electric_quantity[i] is None:

                y_data1__total_positive_reactive_electric_quantity[i] = 0

            else:
                y_data1__total_positive_reactive_electric_quantity[i] = float(
                    y_data1__total_positive_reactive_electric_quantity[i]
                )

        for i in range(len(y_data2__total_negative_reactive_electric_quantity)):
            if y_data2__total_negative_reactive_electric_quantity[i] == '-' \
                or y_data2__total_negative_reactive_electric_quantity[i] is None:

                y_data2__total_negative_reactive_electric_quantity[i] = 0

            else:
                y_data2__total_negative_reactive_electric_quantity[i] = float(
                    y_data2__total_negative_reactive_electric_quantity[i]
                )

    except ValueError as e:
        print('数据转换错误，我他妈怎么知道这傻逼网站给我什么东西，自己看：', e)
        return {}
    except TypeError as e:
        print('数据转换错误，我他妈怎么知道这傻逼网站给我什么东西，自己看：', e)
        return {}

    positive_reactive_electric_quantity_maximum = max(y_data1__total_positive_reactive_electric_quantity)
    positive_reactive_electric_quantity_minimum = min(y_data1__total_positive_reactive_electric_quantity)
    negative_reactive_electric_quantity_maximum = max(y_data2__total_negative_reactive_electric_quantity)
    negative_reactive_electric_quantity_minimum = min(y_data2__total_negative_reactive_electric_quantity)

    return_data = {
        'total_positive_reactive_electric_quantity': total_positive_reactive_electric_quantity,
        'positive_reactive_electric_quantity_maximum': positive_reactive_electric_quantity_maximum,
        'positive_reactive_electric_quantity_minimum': positive_reactive_electric_quantity_minimum,
        'total_negative_reactive_electric_quantity': total_negative_reactive_electric_quantity,
        'negative_reactive_electric_quantity_maximum': negative_reactive_electric_quantity_maximum,
        'negative_reactive_electric_quantity_minimum': negative_reactive_electric_quantity_minimum
    }

    show_data = {
        'time': [x__time],
        'total_positive_reactive_electric_quantity': [total_positive_reactive_electric_quantity],
        'positive_reactive_electric_quantity_maximum': [positive_reactive_electric_quantity_maximum],
        'positive_reactive_electric_quantity_minimum': [positive_reactive_electric_quantity_minimum],
        'total_negative_reactive_electric_quantity': [total_negative_reactive_electric_quantity],
        'negative_reactive_electric_quantity_maximum': [negative_reactive_electric_quantity_maximum],
        'negative_reactive_electric_quantity_minimum': [negative_reactive_electric_quantity_minimum]
    }

    if terminal_output:
        print(tabulate(show_data, headers='keys', tablefmt='simple', showindex=False))

    return return_data

def summary_active_reactive_electric_quantity2csv(time_range: list[str] | tuple[str]) -> None:
    """
    获取有功无功电能汇总并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: None
    """

    spider_data = get_summary_data('SummaryActiveReactiveElectricQuantity', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return

    summary_electricity_data1 = spider_data['data'][0]
    summary_electricity_data2 = spider_data['data'][1]
    summary_electricity_data3 = spider_data['data'][2]
    summary_electricity_data4 = spider_data['data'][3]

    x__time = time_range[0] + '--' + time_range[1]
    total_positive_active_electric_quantity = summary_electricity_data1['Total']
    total_positive_reactive_electric_quantity = summary_electricity_data2['Total']
    total_negative_active_electric_quantity = summary_electricity_data3['Total']
    total_negative_reactive_electric_quantity = summary_electricity_data4['Total']
    positive_active_electric_quantity_maximum = summary_electricity_data1['ItemA']
    positive_reactive_electric_quantity_maximum = summary_electricity_data2['ItemA']
    negative_active_electric_quantity_maximum = summary_electricity_data3['ItemA']
    negative_reactive_electric_quantity_maximum = summary_electricity_data4['ItemA']
    positive_active_electric_quantity_minimum = summary_electricity_data1['ItemB']
    positive_reactive_electric_quantity_minimum = summary_electricity_data2['ItemB']
    negative_active_electric_quantity_minimum = summary_electricity_data3['ItemB']
    negative_reactive_electric_quantity_minimum = summary_electricity_data4['ItemB']
    positive_active_electric_quantity_peak_valley_difference = summary_electricity_data1['ItemC']
    positive_reactive_electric_quantity_peak_valley_difference = summary_electricity_data2['ItemC']
    negative_active_electric_quantity_peak_valley_difference = summary_electricity_data3['ItemC']
    negative_reactive_electric_quantity_peak_valley_difference = summary_electricity_data4['ItemC']
    positive_active_electric_quantity_average = summary_electricity_data1['ExplainValue']
    positive_reactive_electric_quantity_average = summary_electricity_data2['ExplainValue']
    negative_active_electric_quantity_average = summary_electricity_data3['ExplainValue']
    negative_reactive_electric_quantity_average = summary_electricity_data4['ExplainValue']

    # 不得不吐槽一句真神奇，Data1、Data2、Data3、Data4也就算了，你妈平均值这些放ExplainValue里
    # 知道是统一的，所有表最后一项都是'Explain': 'xxxx', 'ExplainValue': 'xxxx'
    # 但是你妈其它项目的解释为什么没有最大值最小值呢。
    # 来看看有多逆天：
    # {'keyword': 'ZY', 这个是正向有功总电能（表的横向标头）
    # 'Total': 83.07,   这是正向有功总电能
    # 'ItemA': 1.35,    这是正向有功总电能最大值
    # 'ItemB': 0.13,    这是正向有功总电能最小值
    # 'ItemC': 1.22,    这是正向有功总电能峰谷差
    # 'Explain': '正向有功总电能(平均电能)',
    # 'ExplainValue': '0.3171'}  这他妈是正向有功总电能的均值

    df = pd.DataFrame(
        {
            '时间': [x__time],
            '正向有功总电能': [total_positive_active_electric_quantity],
            '正向有功总电能最大值': [positive_active_electric_quantity_maximum],
            '正向有功总电能最小值': [positive_active_electric_quantity_minimum],
            '正向有功总电能峰谷差': [positive_active_electric_quantity_peak_valley_difference],
            '正向有功总电能平均值': [positive_active_electric_quantity_average],
            '正向无功总电能': [total_positive_reactive_electric_quantity],
            '正向无功总电能最大值': [positive_reactive_electric_quantity_maximum],
            '正向无功总电能最小值': [positive_reactive_electric_quantity_minimum],
            '正向无功总电能峰谷差': [positive_reactive_electric_quantity_peak_valley_difference],
            '正向无功总电能平均值': [positive_reactive_electric_quantity_average],
            '反向有功总电能': [total_negative_active_electric_quantity],
            '反向有功总电能最大值': [negative_active_electric_quantity_maximum],
            '反向有功总电能最小值': [negative_active_electric_quantity_minimum],
            '反向有功总电能峰谷差': [negative_active_electric_quantity_peak_valley_difference],
            '反向有功总电能平均值': [negative_active_electric_quantity_average],
            '反向无功总电能': [total_negative_reactive_electric_quantity],
            '反向无功总电能最大值': [negative_reactive_electric_quantity_maximum],
            '反向无功总电能最小值': [negative_reactive_electric_quantity_minimum],
            '反向无功总电能峰谷差': [negative_reactive_electric_quantity_peak_valley_difference],
            '反向无功总电能平均值': [negative_reactive_electric_quantity_average]
        }
     )

    df.to_csv('./Save/SummaryActiveReactiveElectricQuantity.csv', index=False)

def get_summary_active_reactive_electric_quantity_data(
        time_range: list[str] | tuple[str],
        terminal_output: bool = True
) -> dict:
    """
    获取有功无功电能汇总
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :param terminal_output: 控制终端是否输出
    :return: dict(items: values) / dict(None)
    """

    spider_data = get_summary_data('SummaryActiveReactiveElectricQuantity', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return {}

    summary_electricity_data1 = spider_data['data'][0]
    summary_electricity_data2 = spider_data['data'][1]
    summary_electricity_data3 = spider_data['data'][2]
    summary_electricity_data4 = spider_data['data'][3]

    x__time = time_range[0] + '--' + time_range[1]
    total_positive_active_electric_quantity = summary_electricity_data1['Total']
    total_positive_reactive_electric_quantity = summary_electricity_data2['Total']
    total_negative_active_electric_quantity = summary_electricity_data3['Total']
    total_negative_reactive_electric_quantity = summary_electricity_data4['Total']
    positive_active_electric_quantity_maximum = summary_electricity_data1['ItemA']
    positive_reactive_electric_quantity_maximum = summary_electricity_data2['ItemA']
    negative_active_electric_quantity_maximum = summary_electricity_data3['ItemA']
    negative_reactive_electric_quantity_maximum = summary_electricity_data4['ItemA']
    positive_active_electric_quantity_minimum = summary_electricity_data1['ItemB']
    positive_reactive_electric_quantity_minimum = summary_electricity_data2['ItemB']
    negative_active_electric_quantity_minimum = summary_electricity_data3['ItemB']
    negative_reactive_electric_quantity_minimum = summary_electricity_data4['ItemB']
    positive_active_electric_quantity_peak_valley_difference = summary_electricity_data1['ItemC']
    positive_reactive_electric_quantity_peak_valley_difference = summary_electricity_data2['ItemC']
    negative_active_electric_quantity_peak_valley_difference = summary_electricity_data3['ItemC']
    negative_reactive_electric_quantity_peak_valley_difference = summary_electricity_data4['ItemC']
    positive_active_electric_quantity_average = summary_electricity_data1['ExplainValue']
    positive_reactive_electric_quantity_average = summary_electricity_data2['ExplainValue']
    negative_active_electric_quantity_average = summary_electricity_data3['ExplainValue']
    negative_reactive_electric_quantity_average = summary_electricity_data4['ExplainValue']

    return_data = {
        'total_positive_active_electric_quantity': total_positive_active_electric_quantity,
        'total_positive_reactive_electric_quantity': total_positive_reactive_electric_quantity,
        'total_negative_active_electric_quantity': total_negative_active_electric_quantity,
        'total_negative_reactive_electric_quantity': total_negative_reactive_electric_quantity,
        'positive_active_electric_quantity_maximum': positive_active_electric_quantity_maximum,
        'positive_reactive_electric_quantity_maximum': positive_reactive_electric_quantity_maximum,
        'negative_active_electric_quantity_maximum': negative_active_electric_quantity_maximum,
        'negative_reactive_electric_quantity_maximum': negative_reactive_electric_quantity_maximum,
        'positive_active_electric_quantity_minimum': positive_active_electric_quantity_minimum,
        'positive_reactive_electric_quantity_minimum': positive_reactive_electric_quantity_minimum,
        'negative_active_electric_quantity_minimum': negative_active_electric_quantity_minimum,
        'negative_reactive_electric_quantity_minimum': negative_reactive_electric_quantity_minimum,
        'positive_active_electric_quantity_peak_valley_difference':
            positive_active_electric_quantity_peak_valley_difference,
        'positive_reactive_electric_quantity_peak_valley_difference':
            positive_reactive_electric_quantity_peak_valley_difference,
        'negative_active_electric_quantity_peak_valley_difference':
            negative_active_electric_quantity_peak_valley_difference,
        'negative_reactive_electric_quantity_peak_valley_difference':
            negative_reactive_electric_quantity_peak_valley_difference,
        'positive_active_electric_quantity_average': positive_active_electric_quantity_average,
        'positive_reactive_electric_quantity_average': positive_reactive_electric_quantity_average,
        'negative_active_electric_quantity_average': negative_active_electric_quantity_average,
        'negative_reactive_electric_quantity_average': negative_reactive_electric_quantity_average
    }

    show_data = {
        'time': [x__time],
        'total_positive_active_electric_quantity': [total_positive_active_electric_quantity],
        'positive_active_electric_quantity_maximum': [positive_active_electric_quantity_maximum],
        'positive_active_electric_quantity_minimum': [positive_active_electric_quantity_minimum],
        'positive_active_electric_quantity_peak_valley_difference':
            [positive_active_electric_quantity_peak_valley_difference],
        'positive_active_electric_quantity_average': [positive_active_electric_quantity_average],
        'total_positive_reactive_electric_quantity': [total_positive_reactive_electric_quantity],
        'positive_reactive_electric_quantity_maximum': [positive_reactive_electric_quantity_maximum],
        'positive_reactive_electric_quantity_minimum': [positive_reactive_electric_quantity_minimum],
        'positive_reactive_electric_quantity_peak_valley_difference':
            [positive_reactive_electric_quantity_peak_valley_difference],
        'positive_reactive_electric_quantity_average': positive_reactive_electric_quantity_average,
        'total_negative_active_electric_quantity': [total_negative_active_electric_quantity],
        'negative_active_electric_quantity_maximum': [negative_active_electric_quantity_maximum],
        'negative_active_electric_quantity_minimum': [negative_active_electric_quantity_minimum],
        'negative_active_electric_quantity_peak_valley_difference':
            [negative_active_electric_quantity_peak_valley_difference],
        'negative_active_electric_quantity_average': [negative_active_electric_quantity_average],
        'total_negative_reactive_electric_quantity': [total_negative_reactive_electric_quantity],
        'negative_reactive_electric_quantity_maximum': [negative_reactive_electric_quantity_maximum],
        'negative_reactive_electric_quantity_minimum': [negative_reactive_electric_quantity_minimum],
        'negative_reactive_electric_quantity_peak_valley_difference':
            [negative_reactive_electric_quantity_peak_valley_difference],
        'negative_reactive_electric_quantity_average': [negative_reactive_electric_quantity_average]
    }

    if terminal_output:
        print(tabulate(show_data, headers='keys', tablefmt='simple', showindex=False))

    return return_data

def summary_active_reactive_power2csv(time_range: list[str] | tuple[str]) -> None:
    """
    获取有功无功功率汇总并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: None
    """

    spider_data = get_summary_data('SummaryActiveReactivePower', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return

    summary_electricity_data1 = spider_data['data'][0]
    summary_electricity_data2 = spider_data['data'][1]

    x__time = time_range[0] + '--' + time_range[1]
    real_time_active_power = summary_electricity_data1['Value']
    real_time_active_power_read_time = summary_electricity_data1['ValueReadTime']
    active_power_maximum = summary_electricity_data1['MaxValue']
    active_power_minimum = summary_electricity_data1['MinValue']
    active_power_peak_valley_difference = summary_electricity_data1['ValleyPeakDiff']
    active_power_average = summary_electricity_data1['AverageLoad']
    active_power_load_rate = summary_electricity_data1['LoadRate']
    active_power_load_rate_minimum = summary_electricity_data1['MinLoadRate']
    real_time_reactive_power = summary_electricity_data2['Value']
    real_time_reactive_power_read_time = summary_electricity_data2['ValueReadTime']
    reactive_power_maximum = summary_electricity_data2['MaxValue']
    reactive_power_minimum = summary_electricity_data2['MinValue']
    reactive_power_peak_valley_difference = summary_electricity_data2['ValleyPeakDiff']
    reactive_power_average = summary_electricity_data2['AverageLoad']
    reactive_power_load_rate = summary_electricity_data2['LoadRate']
    reactive_power_load_rate_minimum = summary_electricity_data2['MinLoadRate']

    df = pd.DataFrame(
        {
            '时间': [x__time],
            f'实时有功功率（{real_time_active_power_read_time}）': [real_time_active_power],
            '有功功率最大值': [active_power_maximum],
            '有功功率最小值': [active_power_minimum],
            '有功功率峰谷差': [active_power_peak_valley_difference],
            '有功功率平均负荷': [active_power_average],
            '有功功率负荷系数': [active_power_load_rate],
            '有功功率最小负荷率': [active_power_load_rate_minimum],
            f'实时无功功率（{real_time_reactive_power_read_time}）': [real_time_reactive_power],
            '无功功率最大值': [reactive_power_maximum],
            '无功功率最小值': [reactive_power_minimum],
            '无功功率峰谷差': [reactive_power_peak_valley_difference],
            '无功功率平均负荷': [reactive_power_average],
            '无功功率负荷系数': [reactive_power_load_rate],
            '无功功率最小负荷率': [reactive_power_load_rate_minimum]
        }
    )

    df.to_csv('./Save/SummaryActiveReactivePower.csv', index=False)

def get_summary_active_reactive_power_data(time_range: list[str] | tuple[str], terminal_output: bool = True) -> dict:
    """
    获取有功无功功率汇总数据
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :param terminal_output: 控制终端是否输出
    :return: dict(items: values) / dict(None)
    """

    spider_data = get_summary_data('SummaryActiveReactivePower', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return {}

    summary_electricity_data1 = spider_data['data'][0]
    summary_electricity_data2 = spider_data['data'][1]

    x__time = time_range[0] + '--' + time_range[1]
    real_time_active_power = summary_electricity_data1['Value']
    real_time_active_power_read_time = summary_electricity_data1['ValueReadTime']
    active_power_maximum = summary_electricity_data1['MaxValue']
    active_power_minimum = summary_electricity_data1['MinValue']
    active_power_peak_valley_difference = summary_electricity_data1['ValleyPeakDiff']
    active_power_average = summary_electricity_data1['AverageLoad']
    active_power_load_rate = summary_electricity_data1['LoadRate']
    active_power_load_rate_minimum = summary_electricity_data1['MinLoadRate']
    real_time_reactive_power = summary_electricity_data2['Value']
    real_time_reactive_power_read_time = summary_electricity_data2['ValueReadTime']
    reactive_power_maximum = summary_electricity_data2['MaxValue']
    reactive_power_minimum = summary_electricity_data2['MinValue']
    reactive_power_peak_valley_difference = summary_electricity_data2['ValleyPeakDiff']
    reactive_power_average = summary_electricity_data2['AverageLoad']
    reactive_power_load_rate = summary_electricity_data2['LoadRate']
    reactive_power_load_rate_minimum = summary_electricity_data2['MinLoadRate']

    return_data = {
        'real_time_active_power': real_time_active_power,
        'real_time_active_power_read_time': real_time_active_power_read_time,
        'active_power_maximum': active_power_maximum,
        'active_power_minimum': active_power_minimum,
        'active_power_peak_valley_difference': active_power_peak_valley_difference,
        'active_power_average': active_power_average,
        'active_power_load_rate': active_power_load_rate,
        'active_power_load_rate_minimum': active_power_load_rate_minimum,
        'real_time_reactive_power': real_time_reactive_power,
        'real_time_reactive_power_read_time': real_time_reactive_power_read_time,
        'reactive_power_maximum': reactive_power_maximum,
        'reactive_power_minimum': reactive_power_minimum,
        'reactive_power_peak_valley_difference': reactive_power_peak_valley_difference,
        'reactive_power_average': reactive_power_average,
        'reactive_power_load_rate': reactive_power_load_rate,
        'reactive_power_load_rate_minimum': reactive_power_load_rate_minimum
    }

    show_data = {
        'time': [x__time],
        f'real_time_active_power({real_time_active_power_read_time})': [real_time_active_power],
        'active_power_maximum': [active_power_maximum],
        'active_power_minimum': [active_power_minimum],
        'active_power_peak_valley_difference': [active_power_peak_valley_difference],
        'active_power_average': [active_power_average],
        'active_power_load_rate': [active_power_load_rate],
        'active_power_load_rate_minimum': [active_power_load_rate_minimum],
        f'real_time_reactive_power({real_time_reactive_power_read_time})': [real_time_reactive_power],
        'reactive_power_maximum': [reactive_power_maximum],
        'reactive_power_minimum': [reactive_power_minimum],
        'reactive_power_peak_valley_difference': [reactive_power_peak_valley_difference],
        'reactive_power_average': [reactive_power_average],
        'reactive_power_load_rate': [reactive_power_load_rate],
        'reactive_power_load_rate_minimum': [reactive_power_load_rate_minimum]
    }

    if terminal_output:
        print(tabulate(show_data, headers='keys', tablefmt='simple', showindex=False))

    return return_data

def summary_apparent_power2csv(time_range: list[str] | tuple[str]) -> None:
    """
    获取视在功率汇总并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: None
    """

    spider_data = get_chart_data('ApparentPower', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return

    summary_electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(summary_electricity_data['x_Axis'])
    x__time = time_range[0] + '--' + time_range[1]
    y_datatotal__total_apparent_power = ast.literal_eval(summary_electricity_data['y_DataTotal'])
    y_data1__a_phase_apparent_power = ast.literal_eval(summary_electricity_data['y_Data1'])
    y_data2__b_phase_apparent_power = ast.literal_eval(summary_electricity_data['y_Data2'])
    y_data3__c_phase_apparent_power = ast.literal_eval(summary_electricity_data['y_Data3'])

    y_datatotal__total_apparent_power.extend(['-'] * (len(x_axis__time) - len(y_datatotal__total_apparent_power)))
    y_data1__a_phase_apparent_power.extend(['-'] * (len(x_axis__time) - len(y_data1__a_phase_apparent_power)))
    y_data2__b_phase_apparent_power.extend(['-'] * (len(x_axis__time) - len(y_data2__b_phase_apparent_power)))
    y_data3__c_phase_apparent_power.extend(['-'] * (len(x_axis__time) - len(y_data3__c_phase_apparent_power)))

    try:
        for i in range(len(y_datatotal__total_apparent_power)):
            if y_datatotal__total_apparent_power[i] == '-' or y_datatotal__total_apparent_power[i] is None:

                y_datatotal__total_apparent_power[i] = 0

            else:
                y_datatotal__total_apparent_power[i] = float(y_datatotal__total_apparent_power[i])

        for i in range(len(y_data1__a_phase_apparent_power)):
            if y_data1__a_phase_apparent_power[i] == '-' or y_data1__a_phase_apparent_power[i] is None:

                y_data1__a_phase_apparent_power[i] = 0

            else:
                y_data1__a_phase_apparent_power[i] = float(y_data1__a_phase_apparent_power[i])

        for i in range(len(y_data2__b_phase_apparent_power)):
            if y_data2__b_phase_apparent_power[i] == '-' or y_data2__b_phase_apparent_power[i] is None:

                y_data2__b_phase_apparent_power[i] = 0

            else:
                y_data2__b_phase_apparent_power[i] = float(y_data2__b_phase_apparent_power[i])

        for i in range(len(y_data3__c_phase_apparent_power)):
            if y_data3__c_phase_apparent_power[i] == '-' or y_data3__c_phase_apparent_power[i] is None:

                y_data3__c_phase_apparent_power[i] = 0

            else:
                y_data3__c_phase_apparent_power[i] = float(y_data3__c_phase_apparent_power[i])

    except ValueError as e:
        print('数据转换错误，我他妈怎么知道这傻逼网站给我什么东西，自己看：', e)
        return
    except TypeError as e:
        print('数据转换错误，我他妈怎么知道这傻逼网站给我什么东西，自己看：', e)
        return

    total_apparent_power = round(sum(y_datatotal__total_apparent_power), 5)
    apparent_power_maximum = max(y_datatotal__total_apparent_power)
    apparent_power_minimum = min(y_datatotal__total_apparent_power)
    apparent_power_peak_valley_difference = round(apparent_power_maximum - apparent_power_minimum, 5)
    apparent_power_average = round(total_apparent_power / len(y_datatotal__total_apparent_power), 5)
    apparent_power_load_rate = round(apparent_power_average / apparent_power_maximum, 5)
    apparent_power_load_rate_minimum = round(apparent_power_minimum / apparent_power_maximum, 5)

    df = pd.DataFrame(
        {
            '时间': [x__time],
            '总视在功率': [y_datatotal__total_apparent_power],
            '视在功率最大值': [apparent_power_maximum],
            '视在功率最小值': [apparent_power_minimum],
            '视在功率峰谷差': [apparent_power_peak_valley_difference],
            '视在功率平均值': [apparent_power_average],
            '视在功率负载率': [apparent_power_load_rate],
            '视在功率最小负荷系数': [apparent_power_load_rate_minimum],
        }
    )

    df.to_csv('./Save/SummaryApparentPower.csv', index=False)

def get_summary_apparent_power_data(time_range: list[str] | tuple[str], terminal_output: bool = True) -> dict:
    """
    获取视在功率汇总数据
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :param terminal_output: 控制终端是否输出
    :return: dict: dict(time:{items: values}) / dict(None)
    """

    spider_data = get_chart_data('ApparentPower', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return {}

    summary_electricity_data = spider_data['data'][0]

    x_axis__time = ast.literal_eval(summary_electricity_data['x_Axis'])
    x__time = time_range[0] + '--' + time_range[1]
    y_datatotal__total_apparent_power = ast.literal_eval(summary_electricity_data['y_DataTotal'])
    y_data1__a_phase_apparent_power = ast.literal_eval(summary_electricity_data['y_Data1'])
    y_data2__b_phase_apparent_power = ast.literal_eval(summary_electricity_data['y_Data2'])
    y_data3__c_phase_apparent_power = ast.literal_eval(summary_electricity_data['y_Data3'])

    y_datatotal__total_apparent_power.extend(['-'] * (len(x_axis__time) - len(y_datatotal__total_apparent_power)))
    y_data1__a_phase_apparent_power.extend(['-'] * (len(x_axis__time) - len(y_data1__a_phase_apparent_power)))
    y_data2__b_phase_apparent_power.extend(['-'] * (len(x_axis__time) - len(y_data2__b_phase_apparent_power)))
    y_data3__c_phase_apparent_power.extend(['-'] * (len(x_axis__time) - len(y_data3__c_phase_apparent_power)))

    try:
        for i in range(len(y_datatotal__total_apparent_power)):
            if y_datatotal__total_apparent_power[i] == '-' or y_datatotal__total_apparent_power[i] is None:

                y_datatotal__total_apparent_power[i] = 0

            else:
                y_datatotal__total_apparent_power[i] = float(y_datatotal__total_apparent_power[i])

        for i in range(len(y_data1__a_phase_apparent_power)):
            if y_data1__a_phase_apparent_power[i] == '-' or y_data1__a_phase_apparent_power[i] is None:

                y_data1__a_phase_apparent_power[i] = 0

            else:
                y_data1__a_phase_apparent_power[i] = float(y_data1__a_phase_apparent_power[i])

        for i in range(len(y_data2__b_phase_apparent_power)):
            if y_data2__b_phase_apparent_power[i] == '-' or y_data2__b_phase_apparent_power[i] is None:

                y_data2__b_phase_apparent_power[i] = 0

            else:
                y_data2__b_phase_apparent_power[i] = float(y_data2__b_phase_apparent_power[i])

        for i in range(len(y_data3__c_phase_apparent_power)):
            if y_data3__c_phase_apparent_power[i] == '-' or y_data3__c_phase_apparent_power[i] is None:

                y_data3__c_phase_apparent_power[i] = 0

            else:
                y_data3__c_phase_apparent_power[i] = float(y_data3__c_phase_apparent_power[i])

    except ValueError as e:
        print('数据转换错误，我他妈怎么知道这傻逼网站给我什么东西，自己看：', e)
        return {}
    except TypeError as e:
        print('数据转换错误，我他妈怎么知道这傻逼网站给我什么东西，自己看：', e)
        return {}

    total_apparent_power = round(sum(y_datatotal__total_apparent_power), 5)
    apparent_power_maximum = max(y_datatotal__total_apparent_power)
    apparent_power_minimum = min(y_datatotal__total_apparent_power)
    apparent_power_peak_valley_difference = round(apparent_power_maximum - apparent_power_minimum, 5)
    apparent_power_average = round(total_apparent_power / len(y_datatotal__total_apparent_power), 5)
    apparent_power_load_rate = round(apparent_power_average / apparent_power_maximum, 5)
    apparent_power_load_rate_minimum = round(apparent_power_minimum / apparent_power_maximum, 5)

    return_data = {
        'total_apparent_power': total_apparent_power,
        'apparent_power_maximum': apparent_power_maximum,
        'apparent_power_minimum': apparent_power_minimum,
        'apparent_power_peak_valley_difference': apparent_power_peak_valley_difference,
        'apparent_power_average': apparent_power_average,
        'apparent_power_load_rate': apparent_power_load_rate,
        'apparent_power_load_rate_minimum': apparent_power_load_rate_minimum
    }

    show_data = {
        'time': [x__time],
        'total_apparent_power': [total_apparent_power],
        'apparent_power_maximum': [apparent_power_maximum],
        'apparent_power_minimum': [apparent_power_minimum],
        'apparent_power_peak_valley_difference': [apparent_power_peak_valley_difference],
        'apparent_power_average': [apparent_power_average],
        'apparent_power_load_rate': [apparent_power_load_rate],
        'apparent_power_load_rate_minimum': [apparent_power_load_rate_minimum]
    }

    if terminal_output:
        print(tabulate(show_data, headers='keys', tablefmt='simple', showindex=False))

    return return_data

def summary_power_factor2csv(time_range: list[str] | tuple[str]) -> None:
    """
    获取功率因数汇总数据并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: None
    """

    spider_data = get_chart_data('PowerFactor', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return

    electricity_data = spider_data['data'][0]
    x__time = time_range[0] + '--' + time_range[1]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_datatotal__total_power_factor = ast.literal_eval(electricity_data['y_DataTotal'])
    y_data1__a_phase_power_factor = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__b_phase_power_factor = ast.literal_eval(electricity_data['y_Data2'])
    y_data3__c_phase_power_factor = ast.literal_eval(electricity_data['y_Data3'])

    y_datatotal__total_power_factor.extend(['-'] * (len(x_axis__time) - len(y_datatotal__total_power_factor)))
    y_data1__a_phase_power_factor.extend(['-'] * (len(x_axis__time) - len(y_data1__a_phase_power_factor)))
    y_data2__b_phase_power_factor.extend(['-'] * (len(x_axis__time) - len(y_data2__b_phase_power_factor)))
    y_data3__c_phase_power_factor.extend(['-'] * (len(x_axis__time) - len(y_data3__c_phase_power_factor)))

    try:
        for i in range(len(y_datatotal__total_power_factor)):
            if y_datatotal__total_power_factor[i] == '-' or y_datatotal__total_power_factor[i] is None:

                y_datatotal__total_power_factor[i] = 0

            else:
                y_datatotal__total_power_factor[i] = float(y_datatotal__total_power_factor[i])

        for i in range(len(y_data1__a_phase_power_factor)):
            if y_data1__a_phase_power_factor[i] == '-' or y_data1__a_phase_power_factor[i] is None:

                y_data1__a_phase_power_factor[i] = 0

            else:
                y_data1__a_phase_power_factor[i] = float(y_data1__a_phase_power_factor[i])

        for i in range(len(y_data2__b_phase_power_factor)):
            if y_data2__b_phase_power_factor[i] == '-' or y_data2__b_phase_power_factor[i] is None:

                y_data2__b_phase_power_factor[i] = 0

            else:
                y_data2__b_phase_power_factor[i] = float(y_data2__b_phase_power_factor[i])

        for i in range(len(y_data3__c_phase_power_factor)):
            if y_data3__c_phase_power_factor[i] == '-' or y_data3__c_phase_power_factor[i] is None:

                y_data3__c_phase_power_factor[i] = 0

            else:
                y_data3__c_phase_power_factor[i] = float(y_data3__c_phase_power_factor[i])

    except ValueError as e:
        print('数据转换错误，我他妈怎么知道这傻逼网站给我什么东西，自己看：', e)
        return
    except TypeError as e:
        print('数据转换错误，我他妈怎么知道这傻逼网站给我什么东西，自己看：', e)
        return


    total_power_factor_maximum = max(y_datatotal__total_power_factor)
    total_power_factor_minimum = min(y_datatotal__total_power_factor)
    total_power_factor_average = round(sum(y_datatotal__total_power_factor) / len(y_datatotal__total_power_factor), 5)
    a_phase_power_factor_maximum = round(max(y_data1__a_phase_power_factor), 2)
    a_phase_power_factor_minimum = round(min(y_data1__a_phase_power_factor), 2)
    a_phase_power_factor_average = round(sum(y_data1__a_phase_power_factor) / len(y_data1__a_phase_power_factor), 5)
    b_phase_power_factor_maximum = round(max(y_data2__b_phase_power_factor), 2)
    b_phase_power_factor_minimum = round(min(y_data2__b_phase_power_factor), 2)
    b_phase_power_factor_average = round(sum(y_data2__b_phase_power_factor) / len(y_data2__b_phase_power_factor), 5)
    c_phase_power_factor_maximum = round(max(y_data3__c_phase_power_factor), 2)
    c_phase_power_factor_minimum = round(min(y_data3__c_phase_power_factor), 2)
    c_phase_power_factor_average = round(sum(y_data3__c_phase_power_factor) / len(y_data3__c_phase_power_factor), 5)

    df = pd.DataFrame(
        {
            '时间': [x__time],
            '总功率因数最大值': [total_power_factor_maximum],
            '总功率因数最小值': [total_power_factor_minimum],
            '总功率因数平均值': [total_power_factor_average],
            'A相功率因数最大值': [a_phase_power_factor_maximum],
            'A相功率因数最小值': [a_phase_power_factor_minimum],
            'A相功率因数平均值': [a_phase_power_factor_average],
            'B相功率因数最大值': [b_phase_power_factor_maximum],
            'B相功率因数最小值': [b_phase_power_factor_minimum],
            'B相功率因数平均值': [b_phase_power_factor_average],
            'C相功率因数最大值': [c_phase_power_factor_maximum],
            'C相功率因数最小值': [c_phase_power_factor_minimum],
            'C相功率因数平均值': [c_phase_power_factor_average]
        }
    )

    df.to_csv('./Save/SummaryPowerFactor.csv', index=False)

def get_summary_power_factor_data(time_range: list[str] | tuple[str], terminal_output: bool = True) -> dict:
    """
    获取功率因数汇总数据
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :param terminal_output: 控制终端是否输出
    :return: dict: dict(time:{items: values}) / dict(None)
    """

    spider_data = get_chart_data('PowerFactor', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return {}

    electricity_data = spider_data['data'][0]
    x__time = time_range[0] + '--' + time_range[1]

    x_axis__time = ast.literal_eval(electricity_data['x_Axis'])
    y_datatotal__total_power_factor = ast.literal_eval(electricity_data['y_DataTotal'])
    y_data1__a_phase_power_factor = ast.literal_eval(electricity_data['y_Data1'])
    y_data2__b_phase_power_factor = ast.literal_eval(electricity_data['y_Data2'])
    y_data3__c_phase_power_factor = ast.literal_eval(electricity_data['y_Data3'])

    y_datatotal__total_power_factor.extend(['-'] * (len(x_axis__time) - len(y_datatotal__total_power_factor)))
    y_data1__a_phase_power_factor.extend(['-'] * (len(x_axis__time) - len(y_data1__a_phase_power_factor)))
    y_data2__b_phase_power_factor.extend(['-'] * (len(x_axis__time) - len(y_data2__b_phase_power_factor)))
    y_data3__c_phase_power_factor.extend(['-'] * (len(x_axis__time) - len(y_data3__c_phase_power_factor)))

    try:
        for i in range(len(y_datatotal__total_power_factor)):
            if y_datatotal__total_power_factor[i] == '-' or y_datatotal__total_power_factor[i] is None:

                y_datatotal__total_power_factor[i] = 0

            else:
                y_datatotal__total_power_factor[i] = float(y_datatotal__total_power_factor[i])

        for i in range(len(y_data1__a_phase_power_factor)):
            if y_data1__a_phase_power_factor[i] == '-' or y_data1__a_phase_power_factor[i] is None:

                y_data1__a_phase_power_factor[i] = 0

            else:
                y_data1__a_phase_power_factor[i] = float(y_data1__a_phase_power_factor[i])

        for i in range(len(y_data2__b_phase_power_factor)):
            if y_data2__b_phase_power_factor[i] == '-' or y_data2__b_phase_power_factor[i] is None:

                y_data2__b_phase_power_factor[i] = 0

            else:
                y_data2__b_phase_power_factor[i] = float(y_data2__b_phase_power_factor[i])

        for i in range(len(y_data3__c_phase_power_factor)):
            if y_data3__c_phase_power_factor[i] == '-' or y_data3__c_phase_power_factor[i] is None:

                y_data3__c_phase_power_factor[i] = 0

            else:
                y_data3__c_phase_power_factor[i] = float(y_data3__c_phase_power_factor[i])

    except ValueError as e:
        print('数据转换错误，我他妈怎么知道这傻逼网站给我什么东西，自己看：', e)
        return {}
    except TypeError as e:
        print('数据转换错误，我他妈怎么知道这傻逼网站给我什么东西，自己看：', e)
        return {}

    total_power_factor_maximum = max(y_datatotal__total_power_factor)
    total_power_factor_minimum = min(y_datatotal__total_power_factor)
    total_power_factor_average = round(sum(y_datatotal__total_power_factor) / len(y_datatotal__total_power_factor), 5)
    a_phase_power_factor_maximum = round(max(y_data1__a_phase_power_factor), 2)
    a_phase_power_factor_minimum = round(min(y_data1__a_phase_power_factor), 2)
    a_phase_power_factor_average = round(sum(y_data1__a_phase_power_factor) / len(y_data1__a_phase_power_factor), 5)
    b_phase_power_factor_maximum = round(max(y_data2__b_phase_power_factor), 2)
    b_phase_power_factor_minimum = round(min(y_data2__b_phase_power_factor), 2)
    b_phase_power_factor_average = round(sum(y_data2__b_phase_power_factor) / len(y_data2__b_phase_power_factor), 5)
    c_phase_power_factor_maximum = round(max(y_data3__c_phase_power_factor), 2)
    c_phase_power_factor_minimum = round(min(y_data3__c_phase_power_factor), 2)
    c_phase_power_factor_average = round(sum(y_data3__c_phase_power_factor) / len(y_data3__c_phase_power_factor), 5)

    return_data = {
        'total_power_factor_maximum': total_power_factor_maximum,
        'total_power_factor_minimum': total_power_factor_minimum,
        'total_power_factor_average': total_power_factor_average,
        'a_phase_power_factor_maximum': a_phase_power_factor_maximum,
        'a_phase_power_factor_minimum': a_phase_power_factor_minimum,
        'a_phase_power_factor_average': a_phase_power_factor_average,
        'b_phase_power_factor_maximum': b_phase_power_factor_maximum,
        'b_phase_power_factor_minimum': b_phase_power_factor_minimum,
        'b_phase_power_factor_average': b_phase_power_factor_average,
        'c_phase_power_factor_maximum': c_phase_power_factor_maximum,
        'c_phase_power_factor_minimum': c_phase_power_factor_minimum,
        'c_phase_power_factor_average': c_phase_power_factor_average
     }

    show_data = {
        'time': [x__time],
        'total_power_factor_maximum': [total_power_factor_maximum],
        'total_power_factor_minimum': [total_power_factor_minimum],
        'total_power_factor_average': [total_power_factor_average],
        'a_phase_power_factor_maximum': [a_phase_power_factor_maximum],
        'a_phase_power_factor_minimum': [a_phase_power_factor_minimum],
        'a_phase_power_factor_average': [a_phase_power_factor_average],
        'b_phase_power_factor_maximum': [b_phase_power_factor_maximum],
        'b_phase_power_factor_minimum': [b_phase_power_factor_minimum],
        'b_phase_power_factor_average': [b_phase_power_factor_average],
        'c_phase_power_factor_maximum': [c_phase_power_factor_maximum],
        'c_phase_power_factor_minimum': [c_phase_power_factor_minimum],
        'c_phase_power_factor_average': [c_phase_power_factor_average]
    }

    if terminal_output:
        print(tabulate(show_data, headers='keys', tablefmt='simple', showindex=False))

    return return_data

def summary_voltage_current2csv(time_range: list[str] | tuple[str]) -> None:
    """
    获取电压电流汇总数据并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: None
    """

    spider_data = get_summary_data('SummaryVoltageCurrentHz', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return

    summary_electricity_data1 = spider_data['data'][0]
    summary_electricity_data2 = spider_data['data'][1]

    # ???这企业怎么沟通的，一个页面换一个数据结构，各自做各自的是吧，我已经懒得喷了
    x__time = time_range[0] + '--' + time_range[1]
    # 你妈明明统计了各相电压最大值最小值峰谷差，页面上显示的竟然是A相的，还不能切换，真他妈牛逼
    a_phase_voltage_maximum = summary_electricity_data1['MaxData']['ValueA']
    b_phase_voltage_maximum = summary_electricity_data1['MaxData']['ValueB']
    c_phase_voltage_maximum = summary_electricity_data1['MaxData']['ValueC']
    a_phase_voltage_minimum = summary_electricity_data1['MinData']['ValueA']
    b_phase_voltage_minimum = summary_electricity_data1['MinData']['ValueB']
    c_phase_voltage_minimum = summary_electricity_data1['MinData']['ValueC']
    a_phase_voltage_peak_valley_difference = summary_electricity_data1['DiffData']['ValueA']
    b_phase_voltage_peak_valley_difference = summary_electricity_data1['DiffData']['ValueB']
    c_phase_voltage_peak_valley_difference = summary_electricity_data1['DiffData']['ValueC']
    a_phase_current_maximum = summary_electricity_data2['MaxData']['ValueA']
    b_phase_current_maximum = summary_electricity_data2['MaxData']['ValueB']
    c_phase_current_maximum = summary_electricity_data2['MaxData']['ValueC']
    a_phase_current_minimum = summary_electricity_data2['MinData']['ValueA']
    b_phase_current_minimum = summary_electricity_data2['MinData']['ValueB']
    c_phase_current_minimum = summary_electricity_data2['MinData']['ValueC']
    a_phase_current_peak_valley_difference = summary_electricity_data2['DiffData']['ValueA']
    b_phase_current_peak_valley_difference = summary_electricity_data2['DiffData']['ValueB']
    c_phase_current_peak_valley_difference = summary_electricity_data2['DiffData']['ValueC']

    df = pd.DataFrame(
        {
            '时间': [x__time],
            'A相电压最大值': [a_phase_voltage_maximum],
            'B相电压最大值': [b_phase_voltage_maximum],
            'C相电压最大值': [c_phase_voltage_maximum],
            'A相电压最小值': [a_phase_voltage_minimum],
            'B相电压最小值': [b_phase_voltage_minimum],
            'C相电压最小值': [c_phase_voltage_minimum],
            'A相电压峰谷差': [a_phase_voltage_peak_valley_difference],
            'B相电压峰谷差': [b_phase_voltage_peak_valley_difference],
            'C相电压峰谷差': [c_phase_voltage_peak_valley_difference],
            'A相电流最大值': [a_phase_current_maximum],
            'B相电流最大值': [b_phase_current_maximum],
            'C相电流最大值': [c_phase_current_maximum],
            'A相电流最小值': [a_phase_current_minimum],
            'B相电流最小值': [b_phase_current_minimum],
            'C相电流最小值': [c_phase_current_minimum],
            'A相电流峰谷差': [a_phase_current_peak_valley_difference],
            'B相电流峰谷差': [b_phase_current_peak_valley_difference],
            'C相电流峰谷差': [c_phase_current_peak_valley_difference]
        }
    )

    df.to_csv('./Save/SummaryVoltageCurrent.csv', index=False)

def get_summary_voltage_current_data(time_range: list[str] | tuple[str], terminal_output: bool = True) -> dict:
    """
    获取电压电流汇总数据
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :param terminal_output: 控制终端是否输出
    :return: dict: dict(time:{items: values}) / dict(None)
    """

    spider_data = get_summary_data('SummaryVoltageCurrentHz', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return {}

    summary_electricity_data1 = spider_data['data'][0]
    summary_electricity_data2 = spider_data['data'][1]

    x__time = time_range[0] + '--' + time_range[1]
    a_phase_voltage_maximum = summary_electricity_data1['MaxData']['ValueA']
    b_phase_voltage_maximum = summary_electricity_data1['MaxData']['ValueB']
    c_phase_voltage_maximum = summary_electricity_data1['MaxData']['ValueC']
    a_phase_voltage_minimum = summary_electricity_data1['MinData']['ValueA']
    b_phase_voltage_minimum = summary_electricity_data1['MinData']['ValueB']
    c_phase_voltage_minimum = summary_electricity_data1['MinData']['ValueC']
    a_phase_voltage_peak_valley_difference = summary_electricity_data1['DiffData']['ValueA']
    b_phase_voltage_peak_valley_difference = summary_electricity_data1['DiffData']['ValueB']
    c_phase_voltage_peak_valley_difference = summary_electricity_data1['DiffData']['ValueC']
    a_phase_current_maximum = summary_electricity_data2['MaxData']['ValueA']
    b_phase_current_maximum = summary_electricity_data2['MaxData']['ValueB']
    c_phase_current_maximum = summary_electricity_data2['MaxData']['ValueC']
    a_phase_current_minimum = summary_electricity_data2['MinData']['ValueA']
    b_phase_current_minimum = summary_electricity_data2['MinData']['ValueB']
    c_phase_current_minimum = summary_electricity_data2['MinData']['ValueC']
    a_phase_current_peak_valley_difference = summary_electricity_data2['DiffData']['ValueA']
    b_phase_current_peak_valley_difference = summary_electricity_data2['DiffData']['ValueB']
    c_phase_current_peak_valley_difference = summary_electricity_data2['DiffData']['ValueC']

    return_data = {
        'a_a_phase_voltage_maximum': a_phase_voltage_maximum,
        'b_b_phase_voltage_maximum': b_phase_voltage_maximum,
        'c_c_phase_voltage_maximum': c_phase_voltage_maximum,
        'a_a_phase_voltage_minimum': a_phase_voltage_minimum,
        'b_b_phase_voltage_minimum': b_phase_voltage_minimum,
        'c_c_phase_voltage_minimum': c_phase_voltage_minimum,
        'a_a_phase_voltage_peak_valley_difference': a_phase_voltage_peak_valley_difference,
        'b_b_phase_voltage_peak_valley_difference': b_phase_voltage_peak_valley_difference,
        'c_c_phase_voltage_peak_valley_difference': c_phase_voltage_peak_valley_difference,
        'a_a_phase_current_maximum': a_phase_current_maximum,
        'b_b_phase_current_maximum': b_phase_current_maximum,
        'c_c_phase_current_maximum': c_phase_current_maximum,
        'a_a_phase_current_minimum': a_phase_current_minimum,
        'b_b_phase_current_minimum': b_phase_current_minimum,
        'c_c_phase_current_minimum': c_phase_current_minimum,
        'a_a_phase_current_peak_valley_difference': a_phase_current_peak_valley_difference,
        'b_b_phase_current_peak_valley_difference': b_phase_current_peak_valley_difference,
        'c_c_phase_current_peak_valley_difference': c_phase_current_peak_valley_difference
    }

    show_data = {
        'time': [x__time],
        'a_phase_voltage_maximum': [a_phase_voltage_maximum],
        'b_phase_voltage_maximum': [b_phase_voltage_maximum],
        'c_phase_voltage_maximum': [c_phase_voltage_maximum],
        'a_phase_voltage_minimum': [a_phase_voltage_minimum],
        'b_phase_voltage_minimum': [b_phase_voltage_minimum],
        'c_phase_voltage_minimum': [c_phase_voltage_minimum],
        'a_phase_voltage_peak_valley_difference': [a_phase_voltage_peak_valley_difference],
        'b_phase_voltage_peak_valley_difference': [b_phase_voltage_peak_valley_difference],
        'c_phase_voltage_peak_valley_difference': [c_phase_voltage_peak_valley_difference],
        'a_phase_current_maximum': [a_phase_current_maximum],
        'b_phase_current_maximum': [b_phase_current_maximum],
        'c_phase_current_maximum': [c_phase_current_maximum],
        'a_phase_current_minimum': [a_phase_current_minimum],
        'b_phase_current_minimum': [b_phase_current_minimum],
        'c_phase_current_minimum': [c_phase_current_minimum],
        'a_phase_current_peak_valley_difference': [a_phase_current_peak_valley_difference],
        'b_phase_current_peak_valley_difference': [b_phase_current_peak_valley_difference],
        'c_phase_current_peak_valley_difference': [c_phase_current_peak_valley_difference]
    }

    if terminal_output:
        print(tabulate(show_data, headers='keys', tablefmt='simple', showindex=False))

    return return_data

def summary_electricity_bill2csv(time_range: list[str] | tuple[str]) -> None:
    """
    获取电费并保存为csv文件
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: None
    """

    spider_data = get_summary_data('SummaryElectricityBill', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return

    summary_electricity_data = spider_data['data']

    x__time = time_range[0] + '--' + time_range[1]
    total_electricity_bill = summary_electricity_data['TotalKwh']
    sharp_electricity_bill = summary_electricity_data['UseKwh1']
    peak_electricity_bill = summary_electricity_data['UseKwh2']
    flat_electricity_bill = summary_electricity_data['UseKwh3']
    valley_electricity_bill = summary_electricity_data['UseKwh4']

    df = pd.DataFrame(
        {
            '时间': [x__time],
            '总电费': [total_electricity_bill],
            '尖电费': [sharp_electricity_bill],
            '峰电费': [peak_electricity_bill],
            '平电费': [flat_electricity_bill],
            '谷电费': [valley_electricity_bill]
        }
    )

    df.to_csv('./Save/SummaryElectricityBill.csv', index=False)

def get_summary_electricity_bill_data(time_range: list[str] | tuple[str], terminal_output: bool = True) -> dict:
    """
    获取电费数据汇总
    :param time_range: 时间范围，如果时间需要精确到分钟，格式为yyyy-MM-dd HH:mm，如果需要精确到天，格式为yyyy-MM-dd
    :return: dict: dict(time:{items: values}) / dict(None)
    """

    spider_data = get_summary_data('SummaryElectricityBill', time_range)
    if spider_data['status'] != 'success':
        print(spider_data['message'])
        return {}

    summary_electricity_data = spider_data['data']

    x__time = time_range[0] + '--' + time_range[1]
    total_electricity_bill = summary_electricity_data['TotalKwh']
    sharp_electricity_bill = summary_electricity_data['UseKwh1']
    peak_electricity_bill = summary_electricity_data['UseKwh2']
    flat_electricity_bill = summary_electricity_data['UseKwh3']
    valley_electricity_bill = summary_electricity_data['UseKwh4']

    return_data = {
        'total_electricity_bill': total_electricity_bill,
        'sharp_electricity_bill': sharp_electricity_bill,
        'peak_electricity_bill': peak_electricity_bill,
        'flat_electricity_bill': flat_electricity_bill,
        'valley_electricity_bill': valley_electricity_bill
    }

    show_data = {
        'time': [x__time],
        'total_electricity_bill': [total_electricity_bill],
        'sharp_electricity_bill': [sharp_electricity_bill],
        'peak_electricity_bill': [peak_electricity_bill],
        'flat_electricity_bill': [flat_electricity_bill],
        'valley_electricity_bill': [valley_electricity_bill]
    }

    if terminal_output:
        print(tabulate(show_data, headers='keys', tablefmt='simple', showindex=False))

    return return_data