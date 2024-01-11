from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from models.Veiculo import MyVeiculo

router = APIRouter()

# Definição do aplicativo FastAPI
#app = FastAPI()

# Modelo Pydantic para entrada de dados (Rotas POST e PUT)
class MyVeiculoCreate(BaseModel):
    nome: str
    marca: str
    ano: int
    modelo: str
    km: int
    valor: float
    transmissao: str
    foto: str

# Rota para criar novo veiculo
@router.post("/veiculos/", response_model=MyVeiculoCreate)
def create_veiculo(veiculo: MyVeiculoCreate): 
    return MyVeiculo.create_veiculo(**veiculo.dict())

# Rota para buscar um veiculo pelo ID
@router.get("/veiculos/{veiculo_id}", response_model=MyVeiculo)
def search_veiculo(veiculo_id: int):
    veiculo = MyVeiculo.search_veiculo(veiculo_id)
    if not veiculo:
        raise HTTPException(status_code=404, detail="Veiculo não encontrado")
    return veiculo