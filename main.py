from fastapi import FastAPI, UploadFile, File, Form, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List
import os

from . import models, schemas, crud
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

UPLOAD_DIR = "app/images"


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/upload", response_model=schemas.ImageDataOut)
async def upload_image(
    file: UploadFile = File(...),
    model_name: str = Form(...),
    prompt: str = Form(...),
    negative_prompt: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        image_data = schemas.ImageDataCreate(
            model_name=model_name,
            prompt=prompt,
            negative_prompt=negative_prompt
        )
        db_image = crud.create_image(db, file, image_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return schemas.ImageDataOut(
        id=db_image.id,
        filename=db_image.filename,
        model_name=db_image.model_name,
        prompt=db_image.prompt,
        negative_prompt=db_image.negative_prompt,
        image_url=f"/images/files/{db_image.filename}"
    )


@app.get("/images", response_model=List[schemas.ImageDataOut])
def read_images(db: Session = Depends(get_db)):
    images = crud.get_images(db)
    return [
        schemas.ImageDataOut(
            id=image.id,
            filename=image.filename,
            model_name=image.model_name,
            prompt=image.prompt,
            negative_prompt=image.negative_prompt,
            image_url=f"/images/files/{image.filename}"
        )
        for image in images
    ]


@app.delete("/images/{image_id}")
def delete_image(image_id: int, db: Session = Depends(get_db)):
    try:
        deleted = crud.delete_image(db, image_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Image not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"ok": True}


@app.get("/images/files/{filename}")
def get_image_file(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Image not found")
    return FileResponse(file_path)
