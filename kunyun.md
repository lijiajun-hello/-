# 鲲运项目(kunyun-api)业务代码参考

## 项目路径

`D:\code\kunyun-api`

## 项目架构

- Spring Boot 3.4.1，Java 17
- 基于 RuoYi-Vue-Pro 多模块架构
- MyBatis Plus、RocketMQ、Redis
- DO 用 `@TableName` + `@Data`；DTO/VO 用 `@Data`
- 依赖方向：`DO → Mapper → Service → Controller`
- BaseDO 基类包含：`createTime`, `updateTime`, `creator`, `updater`, `deleted`, `tenantId`

## 模块与业务对应

| 报表涉及业务 | 对应模块 | DO包路径 |
|-------------|---------|----------|
| 运单/大货运单 | module-oms | `modules/module-oms/module-oms-biz/src/main/java/com/link_trans/module/oms/dal/dataobject/shippingorder/` |
| 入仓/入库 | module-wms | `modules/module-wms/module-wms-biz/src/main/java/com/link_trans/module/wms/dal/dataobject/domesticinboundorder/` |
| 仓库信息 | module-system | 搜索 `WarehouseDO` |
| 费用/账单 | module-bill | `modules/module-bill/module-bill-biz/src/main/java/com/link_trans/module/bill/dal/dataobject/` |
| 报表 | module-report | `modules/module-report/module-report-biz/src/main/java/com/link_trans/module/report/dal/dataobject/` |
| 运输管理 | module-tms | `modules/module-tms/module-tms-biz/src/main/java/com/link_trans/module/tms/dal/dataobject/` |
| 采购供应链 | module-purchase | `modules/module-purchase-product-biz/` |
| 路由 | module-route | `modules/module-route/module-route-biz/` |

## 查找业务代码的步骤

### 1. 找DO（数据对象）
```
Glob **/dal/dataobject/**/*关键字*.java
```
- `@TableName("表名")` → 对应数据库表名
- 字段名驼峰 → 数据库列名下划线（MyBatis Plus自动转换）
- 例：`shippingOrderId` → `shipping_order_id`

### 2. 找Mapper（查询逻辑）
```
Glob **/dal/mysql/**/*关键字*Mapper.java
```
- 了解常用查询条件（eqIfPresent/betweenIfPresent/likeIfPresent）
- 了解JOIN关系（MPJLambdaWrapper）
- 了解排序方式

### 3. 找Service（业务逻辑）
```
Glob **/service/**/*关键字*Service*.java
```
- 了解状态枚举含义
- 了解计算字段逻辑
- 了解业务校验规则

### 4. 找枚举（状态值）
```
Glob **/enums/**/*关键字*.java
```
- 了解 order_status、warehouse_status 等数字含义

## DO字段映射

DO字段映射详见独立文件：[kunyun-tables.md](file:///d:/Grid++Report 6/.trae/skills/gridpp-report/projects/kunyun-tables.md)

新增DO时，追加到 kunyun-tables.md 中。

## SQL模板

SQL模板详见独立文件：[kunyun-sql.md](file:///d:/Grid++Report 6/.trae/skills/gridpp-report/projects/kunyun-sql.md)

画报表时需要新SQL，追加到 kunyun-sql.md 中。
