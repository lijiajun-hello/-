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

cursor.execute("""
    SELECT TABLE_NAME, TABLE_COMMENT, TABLE_ROWS
    FROM information_schema.TABLES
    WHERE TABLE_SCHEMA = 'kunyun-prod-new-52'
    AND TABLE_TYPE = 'BASE TABLE'
    ORDER BY TABLE_NAME
""")

tables = cursor.fetchall()

with open(r'd:\Grid++Report 6\tables_list.txt', 'w', encoding='utf-8') as f:
    f.write(f"数据库共有 {len(tables)} 张表\n")
    f.write("=" * 100 + "\n")
    f.write(f"{'表名':<55} {'行数':<12} {'注释'}\n")
    f.write("=" * 100 + "\n")
    for t in tables:
        name = (t[0] or '')
        rows = str(t[2] or '')
        comment = (t[1] or '')
        f.write(f"{name:<55} {rows:<12} {comment}\n")

print(f"已保存 {len(tables)} 张表到 tables_list.txt")

cursor.close()
conn.close()
