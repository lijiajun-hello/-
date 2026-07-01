# 数据库表结构文档

## 一、数据库连接信息

| 项目 | 值 |
|------|-----|
| 数据库类型 | MySQL |
| 服务器 | 10.1.1.75 |
| 数据库名 | kunyun-prod-new-52 |
| 账号 | beta |
| 密码 | WTk$Xgrrqs&# |
| ODBC连接字符串 | Provider=MSDASQL;Driver={MySQL ODBC 8.0 UNICODE Driver};Server=10.1.1.75;Database=kunyun-prod-new-52;User=beta;Password=WTk$Xgrrqs&#;Option=3;Charset=utf8mb4; |

## 二、查询注意事项

- 所有表查询必须加 `deleted=0` 过滤已删除记录
- 所有表都有 `tenant_id` 字段，多租户隔离
- 所有表都有 `create_time`、`update_time`、`creator`、`updater` 基础字段
- 主键为雪花ID（BigInt）

## 三、核心业务表

### 3.1 oms_shipping_order（大货运单表）

共226个字段，核心字段：

| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | bigint | 主键(雪花ID) |
| order_number | varchar(50) | 系统S0号 |
| customer_order_number | varchar(100) | 客户单号 |
| company_name | varchar(100) | 主体名称 |
| company_id | bigint | 主体ID |
| customer_id | bigint | 客户ID |
| customer_name | varchar(100) | 客户名称 |
| customer_type | varchar(50) | 客户类型 |
| sales_user_name | varchar(50) | 营销人员 |
| sales_user_department_name | varchar(100) | 营销人员部门名称 |
| service_user_name | varchar(50) | 客服人员 |
| product_type | int | 产品类型(1海运,2空运,3陆运) |
| delivery_type | int | 派送方式(1卡车,2快递,3整柜直送) |
| express_type | varchar(50) | 快递类型 |
| master_tracking_number | varchar(100) | 快递主单号 |
| cntr_loading_order_number | varchar(100) | 装柜单号 |
| est_inbound_time | datetime | 预计送仓时间 |
| act_inbound_time | datetime | 实际入仓时间 |
| recv_warehouse_id | bigint | 收货仓库ID |
| recv_warehouse_name | varchar(100) | 收货仓库名称 |
| dest_warehouse_id | bigint | 海外仓库ID |
| dest_warehouse_name | varchar(100) | 海外仓库名称 |
| dest_country_code | varchar(10) | 目的地国家代码 |
| dest_platform_code | varchar(50) | FBA仓库代码(如CLT2/LAX9) |
| dest_platform_name | varchar(100) | 目的地平台名称 |
| est_package_qty | int | 预计包裹数量 |
| est_kg_value | decimal(10,2) | 预计重量(KG) |
| est_cbm_value | decimal(10,2) | 预计体积(CBM) |
| act_package_qty | int | 实际包裹数量(件数) |
| outbound_package_qty | int | 出库包裹数量 |
| act_kg_value | decimal(10,2) | 实计重量(KG) |
| act_cbm_value | decimal(10,2) | 实计体积(CBM) |
| act_vol_value | decimal(10,2) | 实际材积 |
| package_type | int | 包裹类型(1箱,2卡板) |
| declare_name | varchar(200) | 品名 |
| fba_no | varchar(100) | FBA号 |
| order_status | int | 订单状态 |
| order_source | varchar(50) | 订单来源 |
| remark | varchar(500) | 下单备注 |
| internal_remarks | varchar(500) | 内部备注 |
| driver_name | varchar(50) | 司机姓名 |
| driver_phone_number | varchar(50) | 司机电话 |
| plate_number | varchar(50) | 车牌号码 |

### 3.2 system_warehouse（仓库表）

共40个字段，核心字段：

| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | bigint | 主键 |
| warehouse_name | varchar(100) | 仓库名称 |
| warehouse_code | varchar(50) | 仓库编码 |
| address1 | varchar(200) | 地址1 |
| address2 | varchar(200) | 地址2 |
| city | varchar(50) | 城市 |
| phone_number | varchar(50) | 电话 |
| leader_user_name | varchar(50) | 负责人 |
| lat | decimal(10,6) | 纬度 |
| lng | decimal(10,6) | 经度 |

### 3.3 wms_domestic_inbound_order（入库单表）

共51个字段，核心字段：

| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | bigint | 主键 |
| warehouse_id | bigint | 仓库ID |
| shipping_order_id | bigint | 大货运单ID(关联oms_shipping_order.id) |
| order_number | varchar(50) | 入库单号 |
| mark_number | varchar(50) | 唛头短号 |
| inbound_package_qty | int | 入库包裹数量 |
| outbound_package_qty | int | 出库包裹数量 |
| inbound_time | datetime | 首次入仓时间 |
| sign_time | datetime | 签到时间 |
| outbound_time | datetime | 出仓时间 |
| location_code | varchar(50) | 库位号 |
| act_kg_value | decimal(10,2) | 实际重量(KG) |
| act_cbm_value | decimal(10,2) | 实际体积(CBM) |
| act_vol_value | decimal(10,2) | 实际材积 |
| target_warehouse_name | varchar(100) | 目标仓库名称 |
| source_warehouse_name | varchar(100) | 来源仓库名称 |
| inventory_status | int | 库存状态(1正常,2异常) |
| inbound_source | int | 入仓来源(1直接,2中转,3外配) |
| inbound_order_status | int | 入库单状态(0待入库,1已入库,2已出库) |
| inbound_type | int | 入库类型(1直送,2中转,3退仓,4外配) |

### 3.4 wms_domestic_inbound_bind_order（入仓单绑定关系表）

| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | bigint | 主键 |
| warehouse_id | bigint | 仓库ID |
| warehouse_name | varchar(100) | 仓库名称 |
| bing_number | varchar(50) | 入仓单绑定号 |
| order_number | varchar(50) | 订单号 |

### 3.5 wms_domestic_appointment（入仓预约表）

| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | bigint | 主键 |
| appointment_number | varchar(50) | 预约编号 |
| warehouse_id | bigint | 仓库ID |
| warehouse_name | varchar(100) | 仓库名称 |
| driver_name | varchar(50) | 司机姓名 |
| driver_phone_number | varchar(50) | 司机电话 |
| plate_number | varchar(50) | 车牌号 |
| car_type | varchar(50) | 车辆类型 |
| appointment_date | date | 预约日期 |
| appointment_time_seg | varchar(50) | 预约时间段 |
| dock_name | varchar(50) | 道口名 |
| appointment_status | int | 预约状态 |

### 3.6 wms_domestic_appointment_order（预约订单关联表）

| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | bigint | 主键 |
| domestic_appointment_id | bigint | 预约ID |
| order_number | varchar(50) | 订单号 |

### 3.7 wms_international_inbound_order（客户端入库预报表）

| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | bigint | 主键 |
| inbound_number | varchar(50) | 入库预报编号 |
| warehouse_id | bigint | 仓库ID |
| package_qty | int | 包裹数量 |
| received_qty | int | 已收数量 |

## 四、查询工具

查询表结构的Python脚本：`d:\Grid++Report 6\query_inbound_structure.py`

使用方式：
```bash
python d:\Grid++Report 6\query_inbound_structure.py <表名>
```
