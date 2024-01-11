from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DB_CONFIG = "mysql+mysqlconnector://root:admin@localhost/vitrine"

#{
#    'host': 'localhost',
#    'user': 'root',
#    'password': 'admin',
#    'database': 'MySQL82'
#}

engine = create_engine(DB_CONFIG)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()

Base = declarative_base()

class Veiculo(Base):
    __tablename__ = 'VEICULOS'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=True)
    nome = Column(String(50), index=True)
    marca = Column(String(50))
    ano = Column(Integer)
    modelo = Column(String(20))
    km = Column(Integer)
    valor = Column(Float)
    transmissao = Column(String(20))
    foto = Column(String(255))

Base.metadata.create_all(bind=engine)