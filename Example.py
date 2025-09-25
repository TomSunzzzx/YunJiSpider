from ElectricityData import (
    active_electric_quantity_data2csv,
    get_active_electric_quantity_data,
    frozen_electric_quantity2csv,
    get_frozen_electric_quantity_data,
    anti_frozen_electric_quantity2csv,
    get_anti_frozen_electric_quantity_data,
    reactive_electric_quantity2csv,
    get_reactive_electric_quantity_data,
    active_reactive_electric_quantity2csv,
    get_active_reactive_electric_quantity_data,
    active_power2csv,
    get_active_power_data,
    reactive_power2csv,
    get_reactive_power_data,
    active_reactive_power2csv,
    get_active_reactive_power_data,
    apparent_power2csv,
    get_apparent_power_data,
    power_factor2csv,
    get_power_factor_data,
    maximum_demand2csv,
    get_maximum_demand_data,
    voltage2csv,
    get_voltage_data,
    current2csv,
    get_current_data,
    voltage_current2csv,
    get_voltage_current_data,
    electricity_bill2csv,
    get_electricity_bill_data,

    summary_active_electric_quantity2csv,
    get_summary_active_electric_quantity_data,
    summary_frozen_electric_quantity2csv,
    get_summary_frozen_electric_quantity_data,
    summary_anti_frozen_electric_quantity2csv,
    get_summary_anti_frozen_electric_quantity_data,
    summary_reactive_electric_quantity2csv,
    get_summary_reactive_electric_quantity_data,
    summary_active_reactive_electric_quantity2csv,
    get_summary_active_reactive_electric_quantity_data,
    summary_active_reactive_power2csv,
    get_summary_active_reactive_power_data,
    summary_apparent_power2csv,
    get_summary_apparent_power_data,
    summary_power_factor2csv,
    get_summary_power_factor_data,
    summary_voltage_current2csv,
    get_summary_voltage_current_data,
    summary_electricity_bill2csv,
    get_summary_electricity_bill_data
)

# 以上是所有获取数据的方法

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
