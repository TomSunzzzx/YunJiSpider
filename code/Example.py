from ElectricityData import (
    active_electric_quantity_data2csv,
    get_active_electric_quantity_data,
    get_frozen_electric_quantity_data
)


if __name__ == '__main__':
    # 获取有功电量并保存csv文件，到./Save/{name}.csv
    active_electric_quantity_data2csv(['2025-09-24 10:00', '2025-09-24 10:15'])
    # 获取有功电量数据，不打印表格
    data = get_active_electric_quantity_data(['2025-09-24 10:00', '2025-09-24 10:15'], terminal_output=False)
    print(data)
    # 默认打印表格
    get_frozen_electric_quantity_data(['2025-09-23', '2025-09-24'])

    # 错误范例
    active_electric_quantity_data2csv(['2025-09-24 11:00', '2025-09-24 10:15'])
