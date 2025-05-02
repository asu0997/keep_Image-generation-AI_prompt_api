from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ImagePrompt(Base):
    __tablename__ = 'image_prompts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    image_url = Column(String(255), nullable=False)  # 画像の保存URL
    model_name = Column(String(100), nullable=False)  # モデル名
    prompt = Column(Text, nullable=False)             # プロンプト
    negative_prompt = Column(Text, nullable=True)     # ネガティブプロンプト

    def __repr__(self):
        return f"<ImagePrompt(id={self.id}, model_name='{self.model_name}')>"
