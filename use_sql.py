import mysql.connector


def use_sql(sql: int):
    # コネクションの作成
    conn = mysql.connector.connect(
        host='localhost',
        port='43306',
        user='root',
        password='mysql',
        database='imagegen_db'
    )
    # コネクションが切れた時に再接続してくれるよう設定
    conn.ping(reconnect=True)
    # 接続できているかどうか確認
    print(conn.is_connected())
    # DB操作用にカーソルを作成
    cur = conn.cursor()
    cur.execute(sql)
    print(cur.fetchall())
    # カーソルとコネクションを閉じる
    cur.close()
    conn.close()


create_table_image_prompts_sql = """
CREATE TABLE image_prompts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    image_url VARCHAR(255) NOT NULL,
    model_name VARCHAR(100) NOT NULL,
    prompt TEXT NOT NULL,
    negative_prompt TEXT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""

use_sql(create_table_image_prompts_sql)
