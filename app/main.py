from fastapi import FastAPI, Query
import ImagePrompt


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello!"}


@app.get("/get_ImagePrompt/")
def read_root():
    return ImagePrompt.get_ImagePrompt()


@app.post("/insert_ImagePrompt/")
def insert_image_prompt(
    image_url = Query(...),
    model_name = Query(...),
    prompt = Query(...),
    negative_prompt = Query(...)
):
    success = ImagePrompt.insert_ImagePrompt(image_url, model_name, prompt, negative_prompt)
    return {"result": "success" if success else "failure"}


@app.delete("/delete_ImagePrompt/")
def delete_image_prompt(id: int = Query(...)):
    success = ImagePrompt.delete_ImagePrompt_by_id(id)
    return {"result": "success" if success else "failure"}
