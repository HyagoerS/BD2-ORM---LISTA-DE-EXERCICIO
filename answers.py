from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import Usuario, Produto, Pedido, Avaliacao


engine = create_engine('sqlite:///exercicios.db')
Session = sessionmaker(bind=engine)
session = Session()

#Função: all()
'''print("Questão 1")

produtos = session.query(Produto).all()

for produto in produtos:
    print(produto)


print("Questão 2")

usuarios_ativos = session.query(Usuario).filter(
    Usuario.ativo == True, 
    Usuario.idade > 18
).all()

for usuario in usuarios_ativos:
    print(usuario)

print("Questão 3")

pedidos = session.query(Pedido).where(
#deposis
    Pedido.quantidade > 5
).all()

for pedido in pedidos:
    print(pedido) '''

#Função: first()
print("Questão 4")


primeiro_usuario = session.query(Usuario).filter_by(id=1).first(
    if primeiro_usuario:
        print(Usuario.nome)
)