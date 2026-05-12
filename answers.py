from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import Usuario, Produto, Pedido, Avaliacao


engine = create_engine('sqlite:///exercicios.db')
Session = sessionmaker(bind=engine)
session = Session()

#Função: all()
'''#Questão 1

produtos = session.query(Produto).all()

for produto in produtos:
    print(produto)


#Questão 2

usuarios_ativos = session.query(Usuario).filter(
    Usuario.ativo == True, 
    Usuario.idade > 18
).all()

for usuario in usuarios_ativos:
    print(usuario)

#Questão 3

pedidos = session.query(Pedido).where(
#deposis
    Pedido.quantidade > 5
).all()

for pedido in pedidos:
    print(pedido) 

#Função: first()
#Questão 4

primeiro_usuario = session.query(Usuario).filter(Usuario.id == 1).first()

if primeiro_usuario:
    print(f"Primeiro usuário encontrado: {primeiro_usuario.nome}")
else:
    print("Nenhum usuário encontrado.")


#Questão 5
produto_mais_barato = session.query(Produto).filter(Produto.categoria == 'eletrônicos').order_by(Produto.preco.asc()).first()

if produto_mais_barato:
    print(f"O produto mais barato de eletrônicos é: {produto_mais_barato.nome}")
    print(f"Preço: R$ {produto_mais_barato.preco}")

#Questão 6

ultimo_pedido = session.query(Pedido).filter(Pedido.data_pedido.desc()).first()

if ultimo_pedido:
    print(f"Ultimo pedido feito por {ultimo_pedido.usuario.nome} em {ultimo_pedido.data_pedido}")

#Função Get(PK)
#Questão 7

usuario_7 = session.get(Usuario, 7)

if usuario_7:
    print(f"Dados do Usuário ID 7:")
    print(f"Nome: {usuario_7.nome}")
    print(f"Email: {usuario_7.email}")
    print(f"Idade: {usuario_7.idade}")
    print(f"Ativo: {'Sim' if usuario_7.ativo else 'Não'}")
else:
    print("Usuário com ID 7 não encontrado.")

#Questão 8

produto = session.query(Produto).filter(Produto.id == 5, Produto.estoque > 0).first()

if produto == True:
    print(f"Sim! O produto '{produto.nome}' (ID 5) tem {produto.estoque} unidades em estoque.")

#Questão 9

pedido = session.query(Pedido).filter(Pedido.id == 3).first()

if pedido:
    print(f"Status: {pedido.status}")
    print(f"Quantidade: {pedido.quantidade}")
    print(f"Data: {pedido.data_pedido}")
    print("Dados do Usuário")
    print(f"Nome: {pedido.usuario.nome}")
    print(f"Email: {pedido.usuario.email}")'''

#Função Filter()
#Questão 10

usuarios_intervalo = session.query(Usuario).filter(Usuario.idade >= 25, Usuario.idade <= 35).all()

if usuarios_intervalo:
    for usuario in usuarios_intervalo:
        print(f"Nome: {usuario.nome} Idade: {usuario.idade} anos")