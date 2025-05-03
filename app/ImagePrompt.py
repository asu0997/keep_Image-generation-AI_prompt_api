import traceback
from logging import getLogger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import model


logger = getLogger(__name__)


def get_db_session(echo_mode=False):
    '''
    データベースセッション作成
    Returns
    -------
    session
        データベースセッション
    '''
    rds_host = 'mysql'
    rds_port = '3306'
    database_name = 'imagegen_db'
    rds_user = 'root'
    rds_password = 'mysql'
    # 接続文字列作成
    db_url = f'mysql+mysqlconnector://{rds_user}:{rds_password}@{rds_host}:{rds_port}/{database_name}?charset=utf8'
    engine = create_engine(db_url, echo=echo_mode)
    # DBセッション取得
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def get_ImagePrompt():
    '''
    ImagePromptを取得
    Parameters
    ----------
    session: object
        データベースセッション
    Returns
    -------
    list
        ImagePromptのデータを辞書形式で返す
    '''
    try:
        session = get_db_session()
        model_object = model.ImagePrompt
        # クエリ実行
        q = session.query(
            model_object.id,
            model_object.image_url,
            model_object.model_name,
            model_object.prompt,
            model_object.negative_prompt
        )
        results = [
            {
                "id": row.id,
                "image_url": row.image_url,
                "model_name": row.model_name,
                "prompt": row.prompt,
                "negative_prompt": row.negative_prompt
            }
            for row in q.all()
        ]
        return results
    except Exception as e:
        logger.error(traceback.format_exc())
        logger.error(e)
        return []


def insert_ImagePrompt(image_url, model_name, prompt, negative_prompt):
    '''
    ImagePromptに新しいデータを追加
    Parameters
    ----------
    session: object
        データベースセッション
    image_url: str
        画像のURL
    prompt: str
        プロンプト
    negative_prompt: str
        ネガティブプロンプト
    Returns
    -------
    bool
        成功すればTrue、失敗すればFalse
    '''
    try:
        session = get_db_session()
        model_object = model.ImagePrompt
        data_dict = {
            "image_url": image_url,
            "model_name": model_name,
            "prompt": prompt,
            "negative_prompt": negative_prompt
        }
        session.execute(model_object.__table__.insert(), [data_dict])
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        logger.error(traceback.format_exc())
        logger.error(e)
        return False


def delete_ImagePrompt_by_id(id):
    '''
    指定したIDのImagePromptを削除
    Parameters
    ----------
    session: object
        データベースセッション
    id: int
        削除したいImagePromptのID
    Returns
    -------
    bool
        成功すればTrue、失敗すればFalse
    '''
    try:
        session = get_db_session()
        record = session.query(model.ImagePrompt).filter_by(id=id).first()
        if record:
            session.delete(record)
            session.commit()
            return True
        else:
            logger.warning(f"ID {id} のデータは見つかりませんでした。")
            return False
    except Exception as e:
        session.rollback()
        logger.error(traceback.format_exc())
        logger.error(e)
        return False
