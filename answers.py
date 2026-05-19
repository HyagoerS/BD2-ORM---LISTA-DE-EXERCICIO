from sqlalchemy import create_engine, desc
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
    print(f"Email: {pedido.usuario.email}")

#Função Filter()
#Questão 10

usuarios_intervalo = session.query(Usuario).filter(Usuario.idade >= 25, Usuario.idade <= 35).all()

if usuarios_intervalo:
    for usuario in usuarios_intervalo:
        print(f"Nome: {usuario.nome} Idade: {usuario.idade} anos")

#Questão 11

pedidos = session.query(Pedido).filter(
    Pedido.status.in_(['cancelado', 'pendente']),
    Pedido.data_pedido >= datetime(2025, 1, 1)
).all()

for pedido in pedidos:
    print(f"Pedido ID: {pedido.id} | Status: {pedido.status} | Data: {pedido.data_pedido}")

produtos = session.query(Produto).join(Pedido).filter(
    Produto.preco > 500.0
).distinct().all()

for produto in produtos:
    print(f"Produto: {produto.nome} | Preço: R$ {produto.preco}")

#Função: filter_by()
#Questão 13

usuarios_inativos = session.query(Usuario).filter(Usuario.ativo == False).all()

for usuario in usuarios_inativos:
    print(f"Nome: {usuario.nome} | Ativo: {usuario.ativo}")

#Questão 14

livros_baratos = session.query(Produto).filter(
    Produto.categoria == 'livros',
    Produto.preco < 100.0).all()

for livro in livros_baratos:
    print(f"Livro: {livro.nome} | Preço: R$ {livro.preco}")

#Questão 15

''produtos_caros = session.query(Produto).filter(
    Produto.estoque > 0
).order_by(desc(Produto.preco)).limit(3).all()

for produto in produtos_caros:
    print(f"Produto: {produto.nome} | Preço: R$ {produto.preco} | Estoque: {produto.estoque}")''

#Função: order_by()
#Questão 16

usuarios_alfabetica = session.query(Usuario).order_by(Usuario.nome).all()

for usuario in usuarios_alfabetica:
    print(f"Nome: {usuario.nome}")

#Questão 17

produtos_decrescente = session.query(Produto).order_by(desc(Produto.preco)).all()

for produto in produtos_decrescente:
    print(f"Produto: {produto.nome} | Preço: R$ {produto.preco}")

#Questão 18

pedidos_ordenados = session.query(Pedido).order_by(
    Pedido.status, 
    desc(Pedido.data_pedido)
).all()

for pedido in pedidos_ordenados:
    print(f"Status: {pedido.status} | Data: {pedido.data_pedido} | ID: {pedido.id}")

#Função: limit(n)
#Questão 19

primeiros_usuarios = session.query(Usuario).order_by(Usuario.id).limit(6).all()

for usuario in primeiros_usuarios:
    print(f"ID: {usuario.id} | Nome: {usuario.nome}")

#Questão 20

produtos_baratos = session.query(Produto).filter(
    Produto.estoque > 0
).order_by(Produto.preco).limit(5).all()

for produto in produtos_baratos:
    print(f"Produto: {produto.nome} | Preço: R$ {produto.preco} | Estoque: {produto.estoque}")

#Questão 21

pedidos_recentes = session.query(Pedido).join(Usuario).filter(
    Usuario.idade > 30
).order_by(desc(Pedido.data_pedido)).limit(3).all()

for pedido in pedidos_recentes:
    print(f"Data: {pedido.data_pedido} | Usuário: {pedido.usuario.nome} ({pedido.usuario.idade} anos) | Status: {pedido.status}")

#Função: offset(n)
#Questão 22

usuarios_paginados = session.query(Usuario).order_by(Usuario.id).offset(5).all()

for usuario in usuarios_paginados:
    print(f"ID: {usuario.id} | Nome: {usuario.nome}")

#Questão 23

produtos_pulados = session.query(Produto).order_by(desc(Produto.preco)).offset(3).all()

for produto in produtos_pulados:
    print(f"Produto: {produto.nome} | Preço: R$ {produto.preco}")

#Questão 24

pedidos_antigos = session.query(Pedido).order_by(desc(Pedido.data_pedido)).offset(8).all()

for pedido in pedidos_antigos:
    print(f"ID: {pedido.id} | Data: {pedido.data_pedido} | Status: {pedido.status}")'''