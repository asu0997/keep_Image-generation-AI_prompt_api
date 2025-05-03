# keep_Image-generation-AI_prompt_api

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
