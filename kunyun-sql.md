# 鲲运项目(kunyun-api) SQL模板

## 入仓单明细查询

```sql
SELECT
    o.order_number AS 系统S0号,
    o.fba_no AS FBA,
    o.act_package_qty AS 件数,
    o.act_kg_value AS 重量,
    o.act_cbm_value AS 体积,
    o.dest_platform_code AS 仓库代码,
    o.remark AS 备注,
    o.customer_name AS 客户名称,
    o.recv_warehouse_name AS 收货仓库,
    o.act_inbound_time AS 入仓时间
FROM oms_shipping_order o
WHERE o.deleted = 0
  AND o.order_status IN (1, 2, 8)
  AND o.recv_warehouse_id = #{仓库ID}
  AND DATE(o.act_inbound_time) = #{入仓日期}
ORDER BY o.act_inbound_time DESC
```

## 入仓单按绑定号汇总

```sql
SELECT
    b.bing_number AS 入仓单绑定号,
    b.warehouse_name AS 仓库名称,
    o.order_number AS 系统S0号,
    o.fba_no AS FBA,
    o.act_package_qty AS 件数,
    o.act_kg_value AS 重量,
    o.act_cbm_value AS 体积,
    o.dest_platform_code AS 仓库代码,
    o.remark AS 备注
FROM wms_domestic_inbound_bind_order b
LEFT JOIN oms_shipping_order o ON o.order_number = b.order_number AND o.deleted = 0
WHERE b.deleted = 0
  AND b.bing_number = #{绑定号}
ORDER BY o.order_number
```

## 仓库信息查询

```sql
SELECT
    warehouse_name, warehouse_code, address1, address2,
    city, phone_number, leader_user_name, lat, lng
FROM system_warehouse
WHERE deleted = 0 AND id = #{仓库ID}
```

## 入仓预约查询

```sql
SELECT
    a.appointment_number AS 预约编号,
    a.driver_name AS 司机名,
    a.driver_phone_number AS 司机电话,
    a.plate_number AS 车牌号,
    a.car_type AS 车辆类型,
    a.appointment_date AS 预约日期,
    a.appointment_time_seg AS 预约时间段,
    a.warehouse_name AS 仓库名称,
    a.dock_name AS 道口名,
    a.appointment_status AS 预约状态,
    ao.order_number AS 订单号
FROM wms_domestic_appointment a
LEFT JOIN wms_domestic_appointment_order ao ON ao.domestic_appointment_id = a.id AND ao.deleted = 0
WHERE a.deleted = 0
  AND a.appointment_date = #{预约日期}
  AND a.warehouse_id = #{仓库ID}
ORDER BY a.appointment_time_seg
```
