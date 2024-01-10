from typing import Optional

class Veiculo:
    def __init__(self, id: int, nome: str, marca: str, ano: int, modelo: str, km: int, valor: float, transmissao: str, foto: Optional[str]):
        self.id: int = id
        self.nome: str = nome
        self.marca: str = marca
        self.ano: int = ano
        self.modelo: str = modelo
        self.km: int = km
        self.valor: float = valor
        self.transmissao: str = transmissao # Manuel ou Automatico
        self.foto: Optional[str] = foto
    
    @staticmethod
    def create_veiculo(id, nome, marca, ano, modelo, km, valor, transmissao, foto):
        new_veiculo = Veiculo(id, nome, marca, ano, modelo, km, valor, transmissao, foto)
        # Ajustar depois para comunicação com o banco de dados
        return new_veiculo
    
    def search_veiculo(id):
        return Veiculo(id, 'Nome', 'Marca', 'Ano', 'Modelo', 'KM', 'Valor', 'Transmissao', 'Foto')
    
    def update_veiculo(self, nome, marca, ano, modelo, km, valor, transmissao, foto):
        self.nome = nome
        self.marca = marca
        self.ano = ano
        self.modelo = modelo
        self.km = km
        self.valor = valor
        self.transmissao = transmissao
        self.foto = foto
    
    def delete_veiculo(self):
        del self
