from pydantic import BaseModel
from config.database import session, Veiculo

class MyVeiculo(BaseModel):
    #id: int
    nome: str
    marca: str
    ano: int
    modelo: str
    km: int
    valor: float
    transmissao: str
    foto: str

    @classmethod
    def create_veiculo(cls, nome: str, marca: str, ano: int, modelo: str, km: int, valor: float, transmissao: str, foto: str):
        novo_veiculo = Veiculo(
            nome=nome, marca=marca, ano=ano, modelo=modelo, km=km, valor=valor, transmissao=transmissao, foto=foto
        )
        session.add(novo_veiculo)
        session.commit()
        return novo_veiculo
            
    @classmethod
    def search_veiculo(cls, id: int):
        # Lógica para buscar um veículo no banco de dados usando o ID
        # Suponha que get_veiculo_from_db é uma função que busca o veículo no banco de dados
        veiculo_from_db = session.query(Veiculo).filter(Veiculo.id == id).first()
        print("Veiculo from DB:", veiculo_from_db.__dict__)  # Adicione esta linha para inspecionar o conteúdo
        #veiculo_from_db = get_veiculo_fromn_db(id)
        if veiculo_from_db:
            veiculo_dict = {**veiculo_from_db.__dict__}
            veiculo_dict.pop("_sa_instance_state", None)  # Remover a chave que não é necessária
            return cls(**veiculo_dict)
        return None  # Retorna None se o veículo não for encontrado
    
    @classmethod
    def update_veiculo(cls, id: int, nome: str, marca: str, ano: int, modelo: str, km: int, valor: float, transmissao: str, foto: str):
        # Lógica para atualizar o veículo no banco de dados usando o ID
        # Suponha que update_veiculo_in_db é uma função que atualiza o veículo no banco de dados
        update_veiculo_in_db(id, nome, marca, ano, modelo, km, valor, transmissao, foto)
        return cls(id=id, nome=nome, marca=marca, ano=ano, modelo=modelo, km=km, valor=valor, transmissao=transmissao, foto=foto)

    @classmethod
    def delete_veiculo(cls, id: int):
        # Lógica para excluir o veículo no banco de dados usando o ID
        # Suponha que delete_veiculo_from_db é uma função que exclui o veículo no banco de dados
        delete_veiculo_from_db(id)
