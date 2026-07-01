# 鲲运项目(kunyun-api) DO字段映射

## ShippingOrderDO（大货运单）- 对应表 oms_shipping_order

| DO字段 | 数据库列 | 类型 | 说明 |
|--------|---------|------|------|
| id | id | Long | 雪花ID |
| orderNumber | order_number | String | 系统S0号 |
| customerOrderNumber | customer_order_number | String | 客户单号 |
| companyName | company_name | String | 主体名称 |
| companyId | company_id | Long | 主体ID |
| customerId | customer_id | Long | 客户ID |
| customerName | customer_name | String | 客户名称 |
| customerType | customer_type | String | 客户类型 |
| salesUserName | sales_user_name | String | 营销人员 |
| salesUserDepartmentName | sales_user_department_name | String | 营销人员部门名称 |
| serviceUserName | service_user_name | String | 客服人员 |
| productType | product_type | Integer | 产品类型(1海运,2空运,3陆运) |
| deliveryType | delivery_type | Integer | 派送方式(1卡车,2快递,3整柜直送) |
| expressType | express_type | String | 快递类型 |
| masterTrackingNumber | master_tracking_number | String | 快递主单号 |
| cntrLoadingOrderNumber | cntr_loading_order_number | String | 装柜单号 |
| estInboundTime | est_inbound_time | LocalDateTime | 预计送仓时间 |
| actInboundTime | act_inbound_time | LocalDateTime | 实际入仓时间 |
| recvWarehouseId | recv_warehouse_id | Long | 收货仓库ID |
| recvWarehouseName | recv_warehouse_name | String | 收货仓库名称 |
| destWarehouseId | dest_warehouse_id | Long | 海外仓库ID |
| destWarehouseName | dest_warehouse_name | String | 海外仓库名称 |
| destCountryCode | dest_country_code | String | 目的地国家代码 |
| destPlatformCode | dest_platform_code | String | FBA仓库代码(如CLT2/LAX9) |
| destPlatformName | dest_platform_name | String | 目的地平台名称 |
| estPackageQty | est_package_qty | Integer | 预计包裹数量 |
| estKgValue | est_kg_value | BigDecimal | 预计重量(KG) |
| estCbmValue | est_cbm_value | BigDecimal | 预计体积(CBM) |
| actPackageQty | act_package_qty | Integer | 实际包裹数量(件数) |
| outboundPackageQty | outbound_package_qty | Integer | 出库包裹数量 |
| actKgValue | act_kg_value | BigDecimal | 实计重量(KG) |
| actCbmValue | act_cbm_value | BigDecimal | 实计体积(CBM) |
| actVolValue | act_vol_value | BigDecimal | 实际材积 |
| packageType | package_type | Integer | 包裹类型(1箱,2卡板) |
| declareName | declare_name | String | 品名 |
| fbaNo | fba_no | String | FBA号 |
| orderStatus | order_status | Integer | 订单状态 |
| orderSource | order_source | String | 订单来源 |
| remark | remark | String | 下单备注 |
| internalRemarks | internal_remarks | String | 内部备注 |
| driverName | driver_name | String | 司机姓名 |
| driverPhoneNumber | driver_phone_number | String | 司机电话 |
| plateNumber | plate_number | String | 车牌号码 |

## DomesticInboundOrderDO（入库单）- 对应表 wms_domestic_inbound_order

| DO字段 | 数据库列 | 类型 | 说明 |
|--------|---------|------|------|
| id | id | Long | 雪花ID |
| warehouseId | warehouse_id | Long | 仓库编号 |
| shippingOrderId | shipping_order_id | Long | 大货运单编号(关联oms_shipping_order.id) |
| orderNumber | order_number | String | 入库单号 |
| markNumber | mark_number | String | 唛头短号 |
| inboundPackageQty | inbound_package_qty | Integer | 入库包裹数量 |
| outboundPackageQty | outbound_package_qty | Integer | 出库包裹数量 |
| inboundTime | inbound_time | LocalDateTime | 首次入仓时间 |
| signTime | sign_time | LocalDateTime | 签到时间 |
| outboundTime | outbound_time | LocalDateTime | 出仓时间 |
| locationCode | location_code | String | 库位号 |
| actKgValue | act_kg_value | BigDecimal | 实际重量(KG) |
| actCbmValue | act_cbm_value | BigDecimal | 实际体积(CBM) |
| actVolValue | act_vol_value | BigDecimal | 实际材积 |
| targetWarehouseName | target_warehouse_name | String | 目标仓库名称 |
| sourceWarehouseName | source_warehouse_name | String | 来源仓库名称 |
| inventoryStatus | inventory_status | Integer | 库存状态(1正常,2异常) |
| inboundSource | inbound_source | Integer | 入仓来源(1直接,2中转,3外配) |
| inboundOrderStatus | inbound_order_status | Integer | 入库单状态(0待入库,1已入库,2已出库) |
| inboundType | inbound_type | Integer | 入库类型(1直送,2中转,3退仓,4外配) |

## DomesticInboundBindOrderDO（入仓单绑定关系）- 对应表 wms_domestic_inbound_bind_order

| DO字段 | 数据库列 | 类型 | 说明 |
|--------|---------|------|------|
| id | id | Long | 雪花ID |
| warehouseId | warehouse_id | Long | 仓库id |
| warehouseName | warehouse_name | String | 仓库名称 |
| bingNumber | bing_number | String | 入仓单绑定号 |
| orderNumber | order_number | String | 订单号 |
