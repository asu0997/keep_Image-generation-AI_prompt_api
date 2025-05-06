# keep_Image-generation-AI_prompt_api
![Image](https://github.com/user-attachments/assets/45aa0643-1242-411f-a6d3-cd0931f9a80f)
![Image](https://github.com/user-attachments/assets/a8a1e4bd-9fea-4cf0-8ffe-0c47cf19194c)
![Image](https://github.com/user-attachments/assets/8cf021e0-e832-47dd-8ffa-df1178622b40)
![Image](https://github.com/user-attachments/assets/6d3ae4eb-7b7d-42fe-8927-3156277cb89c)
![Image](https://github.com/user-attachments/assets/ace4be7a-da68-44b6-8142-73cb72e6f990)
![Image](https://github.com/user-attachments/assets/e3cc1545-0862-4577-bea2-d9cc81a8b2bd)

# 移動
cd keep_Image-generation-AI_prompt_api

# 仮想環境を作成
python3 -m venv [仮想環境名]

# 仮想環境を立ち上げる
source [仮想環境名]/bin/activate

# パッケージのインストール
pip install -r app/requirements.txt

# ボリュームを作成
docker volume create --name=volume-mysql

# 開始
sh start.sh

# mysql-container内のMySQLに接続する
docker exec -it mysql-container mysql -u root -p
# データベースimagegen_dbを作成
CREATE DATABASE imagegen_db;

# テーブルimage_promptsを作成
python use_sql.py

# 下記URLでAPIを使用
http://localhost:8000/docs

# 終了
sh stop.sh
