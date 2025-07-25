from fastapi import FastAPI,Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from schemas import session,DragonBall
from pydantic import BaseModel,Field

templates = Jinja2Templates(directory="templates")

app = FastAPI()

app.add_middleware(
   CORSMiddleware,
   allow_origins=['*'],
   allow_credentials=True,
   allow_methods=['*'],
   allow_headers=['*']
)

class User(BaseModel):
    nombre: str


@app.get('/')
def home(request:Request):

    return templates.TemplateResponse('index.html',{'request':request})

@app.post('/sajayin')
def sajayins_v2(dato: User):
    try:
        pedido = dato.nombre.capitalize()
       
        respuesta = session.query(DragonBall).filter(
            DragonBall.nombre.like(f'%{pedido}%')
        ).all()
        
        return {
            "resultados": [{'id': r.id, 'nombre': r.nombre, 'imagen': r.imagen} for r in respuesta]
          
        }
        
    except Exception as e:
        print(f"Error en el endpoint: {str(e)}")
        return {
            "error": f"Error interno: {str(e)}",
            "pedido": "",
            "resultados": []
        }




