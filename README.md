# keep_Image-generation-AI_prompt_api

# 移動
cd keep_Image-generation-AI_prompt_api

# 仮想環境を作成
python3 -m venv [仮想環境名]

# 仮想環境を立ち上げる
source [仮想環境名]/bin/activate

# パッケージのインストール
pip install -r app/requirements.txt

# 開始
sh start.sh

# mysql-container内のMySQLに接続する
docker exec -it mysql-container mysql -u root -p

# 終了
sh stop.sh
