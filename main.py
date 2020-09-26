from fastapi import FastAPI, Request,Form
from fastapi.templating import Jinja2Templates

app = FastAPI()



templates = Jinja2Templates(directory="templates")


@app.get("/items/")
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request,  "id": "hai"})

@app.post("/getform")
async def getdata(nama:str = Form(...)):
	return  {"namanya":nama}
