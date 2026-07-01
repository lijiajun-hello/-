---
name: "gridpp-report"
description: "锐浪报表(Grid++ Report)设计与开发助手。当用户需要设计报表、创建.grf模板文件、编写报表脚本、解决锐浪报表相关问题时调用此技能。"
---

# 锐浪报表(Grid++ Report)设计与开发助手

## 一、产品概述

锐浪报表(Grid++ Report)是一款高性能报表工具，支持C/S和B/S架构。核心是COM组件，提供可视化设计器生成.grf模板文件。模板文件本质是JSON格式文本。

- 版本：Grid++ Report 6
- 安装目录：`d:\Grid++Report 6`
- 示例报表目录：`d:\Grid++Report 6\Samples\Reports\`
- 示例数据：`d:\Grid++Report 6\Samples\Data\Northwind.mdb`
- 多语言开发支持：C#、VB.NET、VB、VC++、Delphi、C++Builder
- COM组件名：`gregn6Lib.GridppReport`

## 二、.grf文件结构(JSON格式)

### 顶层结构
```json
{
    "Version": "6.8.9.1",
    "Title": "报表标题",
    "Author": "作者",
    "Description": "描述",
    "Font": { "Name":"宋体", "Size":90000, "Weight":400, "Charset":134 },
    "Printer": { "Size":256, "LeftMargin":1.5, "TopMargin":1.5, "RightMargin":1.5, "BottomMargin":1.5 },
    "PageHeader": { "Height":1.3, "Control":[...] },
    "PageFooter": { "Height":1.3, "Control":[...] },
    "ReportHeader": [ { "Name":"...", "Height":3, "Control":[...] } ],
    "ReportFooter": [ { "Name":"...", "Height":3, "Control":[...] } ],
    "DetailGrid": { ... },
    "Parameter": [ { "Name":"参数名", "DataType":"Integer" } ],
    "ConnectionString": "...",
    "QuerySQL": "...",
    "PageStartScript": "...",
    "Watermark": "..."
}
```

### 报表区域说明
| 区域 | 属性名 | 说明 |
|------|--------|------|
| 报表头 | ReportHeader | 报表开头显示的内容(可多个节) |
| 页眉 | PageHeader | 每页顶部重复显示 |
| 明细网格 | DetailGrid | 核心表格数据区域 |
| 页脚 | PageFooter | 每页底部重复显示 |
| 报表尾 | ReportFooter | 报表末尾显示的内容(可多个节) |

### Font属性说明
- Size单位是1/1000磅，90000=9pt，105000=10.5pt，120000=12pt，180000=18pt
- Charset: 134=GB2312简体中文

### Printer属性说明
- Size: 256=A4, 9=A3, 1=Letter
- Oriention: 默认纵向，"Landscape"=横向
- 边距单位：厘米

## 三、DetailGrid(明细网格)结构

```json
{
    "DetailGrid": {
        "CenterView": true,
        "ShowColLine": true,
        "ShowRowLine": true,
        "ColLine": { "Color":"000000" },
        "RowLine": { "Color":"000000" },
        "PrintAdaptMethod": "ResizeToFit",
        "IsCrossTab": false,
        "FixCols": 0,
        "PageColumnCount": 1,
        "Border": { "Styles":"[DrawLeft|DrawTop|DrawRight|DrawBottom]" },
        "Recordset": { ... },
        "Column": [ ... ],
        "ColumnTitle": { ... },
        "ColumnContent": { ... },
        "Group": [ ... ],
        "CrossTab": { ... }
    }
}
```

### Recordset(记录集)
```json
{
    "Recordset": {
        "ConnectionString": "Provider=Microsoft.Jet.OLEDB.4.0;User ID=Admin;Data Source=..\\Data\\Northwind.mdb",
        "QuerySQL": "SELECT * FROM Customers",
        "BeforePostRecordScript": "脚本代码",
        "Field": [
            { "Name":"CustomerID" },
            { "Name":"OrderDate", "Type":"DateTime", "Format":"yyyy年MM月dd日" },
            { "Name":"Amount", "Type":"Float", "Format":"#,##0.00" },
            { "Name":"Discount", "Type":"Float", "Format":"0.00%" },
            { "Name":"ProductID", "Type":"Integer" },
            { "Name":"Price", "Type":"Currency" }
        ]
    }
}
```
字段Type取值：String(默认)、Integer、Float、DateTime、Currency、Boolean

### Column(列定义)
```json
{
    "Column": [
        { "Name":"CustomerID", "Width":2.38125 },
        { "Name":"CompanyName", "Width":3.175, "Visible":false }
    ]
}
```
宽度单位：厘米

### ColumnTitle(列标题行)
```json
{
    "ColumnTitle": {
        "BackColor": "C0C0C0",
        "Height": 0.79375,
        "RepeatStyle": "OnPage",
        "Font": { "Name":"宋体", "Size":90000, "Bold":true, "Charset":134 },
        "ColumnTitleCell": [
            { "GroupTitle":false, "Column":"CustomerID", "Text":"客户编号", "TextAlign":"MiddleCenter" },
            { "GroupTitle":true, "Name":"Group1", "ColumnTitleCell":[
                { "GroupTitle":false, "Column":"ContactName", "Text":"姓名" },
                { "GroupTitle":false, "Column":"ContactTitle", "Text":"称谓" }
            ]}
        ]
    }
}
```
- GroupTitle:true 表示合并表头组，其子标题在ColumnTitleCell数组中
- RepeatStyle:"OnPage" 表示每页重复标题行

### ColumnContent(列内容行)
```json
{
    "ColumnContent": {
        "Height": 0.79375,
        "ColumnContentCell": [
            { "Column":"CustomerID", "DataField":"CustomerID" },
            { "Column":"Amount", "DataField":"Amount", "TextAlign":"MiddleRight", "ForeColor":"0000FF" },
            { "Column":"OnlyOne", "FreeCell":true, "Control":[
                { "Type":"FieldBox", "Name":"Field1", "DataField":"ProductName" },
                { "Type":"Barcode", "Name":"Barcode1", "BarcodeType":"QRCode", "DataField":"CustomerID" }
            ]}
        ]
    }
}
```
- FreeCell:true 表示自由格，格内可放多个部件框
- TextAlign取值：MiddleLeft, MiddleCenter, MiddleRight

### Group(分组)
```json
{
    "Group": [
        {
            "Name": "Group1",
            "ByFields": "OrderID",
            "GroupHeader": {
                "Height": 0.79375,
                "Control": [
                    { "Type":"MemoBox", "Name":"MemoBox1", "Text":"订单号：[#OrderID#]  客户：[#CompanyName#]  日期：[#OrderDate#]" }
                ]
            },
            "GroupFooter": {
                "Height": 0.582083,
                "Control": [
                    { "Type":"SummaryBox", "Name":"Summary1", "DataField":"Amount", "AlignColumn":"Amount", "TextAlign":"MiddleRight" },
                    { "Type":"StaticBox", "Name":"StaticBox1", "Text":"小计" }
                ]
            }
        }
    ]
}
```
- ByFields: 分组依据字段，多个字段用逗号分隔
- 不设ByFields或留空则全表一个分组(用于合计)

### CrossTab(交叉表)
```json
{
    "CrossTab": {
        "PercentFormat": "0.##%",
        "HCrossFields": "ProductID",
        "VCrossFields": "CustomerId",
        "ListCols": 2
    }
}
```
- 需设置DetailGrid.IsCrossTab=true
- HCrossFields: 横向交叉字段
- VCrossFields: 纵向交叉字段
- ListCols: 纵向交叉列数(前N列为纵向固定列)

## 四、部件框类型(Control Type)

### StaticBox(静态文字框)
```json
{ "Type":"StaticBox", "Name":"TitleBox", "Left":5.6, "Top":0.2, "Width":6.7, "Height":0.6,
  "Center":"Horizontal", "Text":"标题文字", "ForeColor":"FF0000",
  "Font":{ "Name":"宋体", "Size":180000, "Bold":true, "Charset":134 },
  "Border":{ "Styles":"[DrawLeft|DrawTop|DrawRight|DrawBottom]" }
}
```

### FieldBox(字段框)
```json
{ "Type":"FieldBox", "Name":"FieldBox1", "Dock":"Fill", "DataField":"ProductName", "TextAlign":"MiddleCenter" }
```

### MemoBox(综合文字框)
```json
{ "Type":"MemoBox", "Name":"MemoBox1", "Left":0.2, "Top":0.4, "Width":6, "Height":0.6,
  "Text":"第[#SystemVar(PageNumber)#]页/共[#SystemVar(PageCount)#]页"
}
```

### SummaryBox(统计框)
```json
{ "Type":"SummaryBox", "Name":"Summary1", "AlignColumn":"Amount", "DataField":"Amount",
  "TextAlign":"MiddleRight", "Left":9.5, "Width":2.8, "Height":0.58
}
```

### Chart(图表)
```json
{ "Type":"Chart", "Name":"Chart1", "Left":0.2, "Top":0.2, "Width":8.5, "Height":5.5,
  "Title":"柱图", "GroupCount":4, "SeriesCount":3,
  "GroupLabel":"一\r二\r三\r四",
  "SeriesLabel":"张三\r李四\r王五",
  "Value":"1000,1200,1500,800,1500,1800,2000,1200,800,1000,700,500",
  "XAxis":{ "Label":"季度" },
  "YAxis":{ "Label":"销售额", "Max":2000, "Space":500 },
  "ChartSeries":[ { "ValueFormat":"0.##" } ]
}
```

### Barcode(条形码/二维码)
```json
{ "Type":"Barcode", "Name":"Barcode1", "Left":0.4, "Top":2.2, "Width":4, "Height":2,
  "BarcodeType":"QRCode", "DataField":"CustomerID"
}
```
BarcodeType取值：QRCode(二维码)、Code128、Code39、EAN13、ITF14等

### SubReport(子报表)
```json
{ "Type":"SubReport", "Name":"srCustomerList", "Dock":"Fill",
  "Report": { 完整的报表定义对象 }
}
```

### FreeGrid(自由表格)
```json
{ "Type":"FreeGrid", "Name":"FreeGrid1", "Left":0.2, "Top":1.2,
  "Border":{ "Styles":"[DrawLeft|DrawTop|DrawRight|DrawBottom]", "Pen":{ "Width":2 } },
  "ColumnCount":7, "RowCount":8,
  "FreeGridColumn":[ { "index":1, "Width":1.35 }, { "index":2, "Width":1.85 } ],
  "FreeGridRow":[ { "index":1, "Height":0.95 }, { "index":2, "Height":0.95 } ],
  "FreeGridCell":[
      { "row":1, "col":1, "TextAlign":"MiddleCenter", "Text":"姓 名" },
      { "row":1, "col":2, "Text":"[#{LastName}#][#{FirstName}#]" }
  ]
}
```

### Image(图像框)
```json
{ "Type":"Image", "Name":"Image1", "Left":0.2, "Top":0.2, "Width":2, "Height":2,
  "DataField":"图片字段", "Stretch":"True"
}
```

### Line(线条)
```json
{ "Type":"Line", "Name":"Line1", "Anchor":"[Left|Top|Right]", "Top":1, "Width":18, "Pen":{ "Width":2 } }
```

## 五、部件框通用属性

| 属性 | 说明 | 常用值 |
|------|------|--------|
| Left/Top/Width/Height | 位置和大小 | 单位：厘米 |
| Dock | 停靠方式 | Fill(充满), Left, Top, Right, Bottom |
| Anchor | 锚定 | [Left\|Top\|Right], [Top\|Right] |
| Center | 居中 | Horizontal(水平居中) |
| DataField | 绑定数据字段 | 字段名 |
| Text | 显示文字 | 直接文字或表达式 |
| TextAlign | 对齐 | MiddleLeft, MiddleCenter, MiddleRight |
| ForeColor | 前景色 | "FF0000"(红色), "0000FF"(蓝色) |
| BackColor | 背景色 | "C0C0C0"(灰色), "FFFFCC"(浅黄) |
| Font | 字体 | { Name, Size, Bold, Charset } |
| Visible | 是否可见 | true/false |
| CanGrow | 可伸展 | true(内容多时自动变高) |
| ShrinkFontToFit | 字体缩小适应 | true |
| Border | 边框 | { Styles:"[DrawLeft\|DrawTop\|DrawRight\|DrawBottom]" } |

## 六、表达式语法

在MemoBox和StaticBox的Text属性中使用：

```
[#字段名#]                          ← 引用明细字段值
[#{参数名}#]                        ← 引用报表参数
[#SystemVar(PageNumber)#]          ← 当前页码
[#SystemVar(PageCount)#]           ← 总页数
[#SystemVar(RecordCount)#]         ← 记录总数
[#SystemVar(CurrentDateTime):yyyy年MM月dd日#] ← 当前日期格式化
```

在FreeGrid单元格中使用参数：
```
[#{参数名}#]   ← 引用参数值
```

## 七、脚本编程

### 脚本位置
| 脚本属性 | 所属对象 | 触发时机 |
|----------|----------|----------|
| BeforePostRecordScript | Recordset | 每条记录提交前 |
| PageStartScript | Report主对象 | 每页开始生成时 |
| ProcessBeginScript | Report主对象 | 报表处理开始时 |
| ProcessRecordScript | Report主对象 | 每条记录处理时 |

### 常用脚本示例

#### 计算字段
```javascript
// 在Recordset.BeforePostRecordScript中
var AmtFld = Sender.Fields.Item("Amount");
var QtyFld = Sender.Fields.Item("Quantity");
var PriceFld = Sender.Fields.Item("UnitPrice");
AmtFld.AsFloat = QtyFld.AsFloat * PriceFld.AsFloat;
```

#### 电子印章(只在最后一页显示)
```javascript
// 在Report.PageStartScript中
Report.ControlByName("pbMark").Visible = (Report.SystemVarValue(3) == Report.SystemVarValue(2));
// SystemVarValue(2)=总页数, SystemVarValue(3)=当前页码
```

#### 条件隐藏行
```javascript
// 在ColumnContent的格式化脚本中
if (Sender.ControlByName("FieldName").AsFloat == 0) {
    Sender.Section.Visible = false;
}
```

#### 追加空白记录
```javascript
// 在Report.ProcessBeginScript中
var rs = Report.DetailGrid.Recordset;
var desiredRows = 20;
while (rs.RecordCount < desiredRows) {
    rs.Append();
    rs.Post();
}
```

## 八、设计器操作指南

### 两种视图
| 视图 | 切换方式 | 用途 |
|------|----------|------|
| 报表视图 | 菜单→视图→报表视图 | 设计明细网格、分组、交叉表 |
| 页面视图 | 菜单→视图→页面视图 | 设计页眉页脚、报表头尾、自由布局、套打定位 |

### 新建报表流程
1. 文件→新建→选择"明细报表"或"自由表格"
2. 设置数据源：对象浏览器→明细网格→记录集→设置ConnectionString和QuerySQL
3. 定义列：对象浏览器→明细网格→右键→插入列
4. 设计列标题：在报表视图中点击列标题行输入文字
5. 绑定数据：选中内容格→设置DataField属性
6. 添加页眉页脚：切换到页面视图操作

### 常用操作
- 插入分组：对象浏览器→明细网格→右键→插入分组→设置ByFields
- 制作交叉表：设置DetailGrid.IsCrossTab=true→配置CrossTab节点
- 套打：页面视图→设置BackgroundImage→在背景图上定位部件框
- 电子印章：页面视图→右键→"显示浮动节"→插入图像框→用脚本控制显示
- 多层表头：选中列标题格→右键→"列标题布局"

## 九、C#编程接口

```csharp
using gregn6Lib;

// 创建报表对象
GridppReport Report = new GridppReport();

// 加载模板
Report.LoadFromFile("模板路径.grf");

// 设置数据源连接
Report.DetailGrid.Recordset.ConnectionString = "连接字符串";

// 打印预览
Report.PrintPreview(true);

// 直接打印
Report.Print(true);

// 导出
Report.ExportDirect(GRExportType.gretPDF, "输出.pdf", true, false);
// 导出类型：gretXLS, gretRTF, gretPDF, gretHTM, gretIMG, gretTXT, gretCSV

// 事件
Report.ExportBegin += new _IGridppReportEvents_ExportBeginEventHandler(Handler);
```

## 十、报表功能分类与参考示例

| 编号 | 类别 | 示例文件 | 典型功能 |
|------|------|----------|----------|
| 1a | 简单表格 | 1a.简单表格.grf | 基本列列表 |
| 1b | 双层表头 | 1b.双层表头.grf | 多层列标题 |
| 1c | 锁定列 | 1c.锁定列.grf | 固定左侧列 |
| 1d | 多栏报表 | 1d.多栏报表.grf | 多栏显示 |
| 1e | 图像 | 1e.图像.grf | 图片显示 |
| 1g | 条码二维码 | 1g.条形码与二维码.grf | 条码/二维码 |
| 1h | RTF文本 | 1h.RTF格式文本.grf | 富文本 |
| 1l | 交替色 | 1l.交替色显示明细行.grf | 奇偶行不同色 |
| 1n | 追加空白行 | 1n.追加空白行.grf | 补空行满页 |
| 1o | 文字绕行 | 1o.文字绕行与自动伸展.grf | 自动换行 |
| 1p | 文字缩小 | 1p.文字缩小适应.grf | ShrinkFontToFit |
| 2a | 基本分组 | 2a.基本分组.grf | 分组+小计 |
| 2c | 多级分组 | 2c.多级分组.grf | 多层分组 |
| 2d | 单元格合并 | 2d.分组单元格合并.grf | 分组合并 |
| 2g | 页分组 | 2g.页分组.grf | 按页分组 |
| 3a | 交叉表起步 | 3a.交叉表起步.grf | 基本交叉表 |
| 4a | 子报表 | 4a.演示子报表.grf | 子报表嵌入 |
| 5a | 表达式 | 5a.表达式运算.grf | 计算表达式 |
| 5j | 财务金额线 | 5j.财务金额线.grf | 金额位线 |
| 5m | 电子印章 | 5m.电子印章.grf | 浮动印章 |
| 5n | 水印背景 | 5n.水印背景.grf | 水印图 |
| 6e | 发票套打 | 6e.发票套打.grf | 套打定位 |
| 7-2a | 计算字段 | 7-2a.脚本.计算字段.grf | 脚本计算 |
| 8a | 图表 | 8a.图表.序列组柱图.grf | 柱图饼图折线图 |
| 9a | 自由表格 | 9a.自由表格.grf | FreeGrid |

## 十一、常见问题解决

| 问题 | 解决方法 |
|------|----------|
| 看不到数据 | 检查ConnectionString和QuerySQL |
| 列标题不每页重复 | ColumnTitle.RepeatStyle = OnPage |
| 表格太宽打印不下 | DetailGrid.PrintAdaptMethod = ResizeToFit |
| 合并单元格 | 分组中用GroupTitle或用FreeGrid |
| 套打位置不准 | 页面视图+BackgroundImage精确定位 |
| 金额显示格式 | Type=Float/Currency, Format=#,##0.00 |
| 行号自动生成 | BeforePostRecordScript中 Field.AsInteger = Sender.RecordNo |
| 条件控制显示 | 脚本中设置Control.Visible或Section.Visible |
| 最后一页才显示内容 | PageStartScript中判断当前页==总页数 |
| 空白行补满页 | ProcessBeginScript中追加空白记录 |

## 十二、创建报表模板的工作流程

当用户提供报表截图或需求时，按以下步骤操作：

1. **分析报表结构**：识别报表头、明细表格、分组、合计、报表尾、页眉页脚等区域
2. **确定数据字段**：根据表格列确定需要的字段名和类型
3. **选择报表类型**：简单表格/分组报表/交叉表/套打/自由表格
4. **编写.grf文件**：按照JSON结构生成完整模板
5. **关键注意事项**：
   - Font.Size单位是1/1000磅
   - 位置和宽度单位是厘米
   - 颜色用6位十六进制(无#号)
   - 换行用\r\n
   - 表达式用[#...#]包裹
   - 参数用[#{...}#]包裹
6. **提供使用说明**：告知用户需要修改的ConnectionString和QuerySQL

## 十三、数据库信息

数据库连接信息和表结构详见独立文件：[database.md](file:///d:/Grid++Report 6/.trae/skills/gridpp-report/database.md)

### 快速参考

- 数据库：MySQL 10.1.1.75 / kunyun-prod-new-52 / beta
- 连接字符串（ODBC）：`Provider=MSDASQL;Driver={MySQL ODBC 8.0 UNICODE Driver};Server=10.1.1.75;Database=kunyun-prod-new-52;User=beta;Password=WTk$Xgrrqs&#;Option=3;Charset=utf8mb4;`
- 所有表查询必须加 `deleted=0` 过滤
- 画报表时需要查新表，用Python脚本 `d:\Grid++Report 6\query_inbound_structure.py` 查询表结构，结果追加到 database.md

## 十四、项目业务代码参考

画报表时，**优先参考业务代码写SQL**，确保字段名和查询逻辑与代码一致。

### 项目索引

| 项目名 | 文件 | 说明 |
|--------|------|------|
| 鲲运(kunyun-api) | [projects/kunyun.md](file:///d:/Grid++Report 6/.trae/skills/gridpp-report/projects/kunyun.md) | Spring Boot项目，含架构、模块对应、查找步骤 |
| 鲲运-表结构 | [projects/kunyun-tables.md](file:///d:/Grid++Report 6/.trae/skills/gridpp-report/projects/kunyun-tables.md) | DO字段映射 |
| 鲲运-SQL | [projects/kunyun-sql.md](file:///d:/Grid++Report 6/.trae/skills/gridpp-report/projects/kunyun-sql.md) | SQL模板 |

### 使用方式

1. 用户发报表截图 → 判断涉及哪个业务系统
2. 读取对应项目文件（如 `projects/kunyun.md`）
3. 按文件中的查找步骤，去项目代码中搜索 DO/Mapper
4. 结合 DO 字段映射和 Mapper 查询逻辑，编写准确的SQL
5. 如果项目文件中没有对应的表信息，用Python脚本查数据库，结果追加到 database.md 和项目文件

### 新增项目

当有新项目需要对接时，在 `projects/` 目录下创建对应的 `.md` 文件，格式参考 kunyun.md
