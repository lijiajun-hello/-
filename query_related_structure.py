import pymysql

conn = pymysql.connect(
    host='10.1.1.75',
    user='beta',
    password='WTk$Xgrrqs&#',
    database='kunyun-prod-new-52',
    charset='utf8mb4',
    connect_timeout=10
)

cursor = conn.cursor()

target_tables = [
    'system_warehouse',
    'oms_shipping_order',
    'oms_shipping_order_package',
    'wms_dimensions_data',
    'oms_shipping_fbx_order',
]

with open(r'd:\Grid++Report 6\related_tables_structure.txt', 'w', encoding='utf-8') as f:
    for tbl in target_tables:
        cursor.execute("""
            SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_COMMENT
            FROM information_schema.COLUMNS
            WHERE TABLE_SCHEMA = 'kunyun-prod-new-52' AND TABLE_NAME = %s
            ORDER BY ORDINAL_POSITION
        """, (tbl,))
        cols = cursor.fetchall()

        cursor.execute("""
            SELECT TABLE_COMMENT FROM information_schema.TABLES
            WHERE TABLE_SCHEMA = 'kunyun-prod-new-52' AND TABLE_NAME = %s
        """, (tbl,))
        tcomment = cursor.fetchone()[0] or ''

        f.write(f"\n{'='*100}\n")
        f.write(f"表名: {tbl}  (注释: {tcomment})  字段数: {len(cols)}\n")
        f.write(f"{'='*100}\n")
        f.write(f"{'字段名':<40} {'类型':<25} {'可空':<6} {'键':<6} {'注释'}\n")
        f.write(f"{'-'*100}\n")
        for c in cols:
            f.write(f"{(c[0] or ''):<40} {(c[1] or ''):<25} {(c[2] or ''):<6} {(c[3] or ''):<6} {c[4] or ''}\n")

print("已保存关联表结构到 related_tables_structure.txt")

cursor.close()
conn.close()
