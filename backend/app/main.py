from fastapi import FastAPI
from routes import veiculos  # Importando o arquivo de rotas

app = FastAPI()

# Registrar as rotas
app.include_router(veiculos.router)
