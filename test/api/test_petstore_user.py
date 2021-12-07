# bibliotecas

import pytest  # Framework de Teste Unitário - Engine

import requests  # Framework de teste de API - Resquest / Response

# Endereço da API
base_url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}


# Os teste
def test_criar_usuario():
    # Configura
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '1002'

    # Executa
    resposta = requests.post(  # Faz a requisição , passando :
        # O endpont da API
        url=base_url,  # O BODY jSON
        data=open('C:/Users/55119/PycharmProjects/pythonProject/fts132_inicial1/test/db/user1.json', 'rb'),
        headers=headers
    )

    # Valida/ Formatação

    corpo_da_resposta = resposta.json()
    print(resposta)  # Respota Bruta
    print(resposta.status_code)  # Satus Code
    print(corpo_da_resposta)  # Resposta Formatada

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada


def testar_consultar_usuario():
    # Configura
    status_code = 200
    id = 1002
    username = 'GSOBREIRA'
    firstName = 'Gustavo'
    lastName = 'Sobreira'
    email = 'gsobreira@teste.com.br'
    password = '123456'
    phone = '971380287'
    userStatus = 0

    # Executa
    # Executa

    resposta = requests.get(
        url=f'{base_url}/{username}',
        headers=headers
    )

    # Formata

    corpo_da_resposta = resposta.json()
    print(resposta)  # Respota Bruta
    print(resposta.status_code)  # Satus Code
    print(corpo_da_resposta)  # Resposta Formatada

    # Valida
    assert resposta.status_code == status_code
    assert corpo_da_resposta['id'] == id
    assert corpo_da_resposta['username'] == username
    assert corpo_da_resposta['email'] == email


def testar_alterar_usuario():
    # Configura
    username = 'GSOBREIRA'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '1002'

    # Executa
    resposta = requests.put(
        url=f'{base_url}/{username}',
        data=open('C:/Users/55119/PycharmProjects/pythonProject/fts132_inicial1/test/db/user2.json', 'rb'),
        headers=headers
    )
    # Formatação
    corpo_da_resposta = resposta.json()
    print(resposta)  # Respota Bruta
    print(resposta.status_code)  # Satus Code
    print(corpo_da_resposta)  # Resposta Formatada

    # Validação
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada


  def testar_excluir_usuario():
    # Configura
    username = 'GSOBREIRA'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = 'GSOBREIRA'

    # Executa
    resposta = requests.delete(
        url=f'{base_url}/{username}',
        headers=headers
    )
    # Formatação
    match resposta.status_code:
        case 200:  # Apagar usuário que foi encontrado
            corpo_da_resposta = resposta.json()
            print(resposta)  # Respota Bruta
            print(resposta.status_code)  # Satus Code
            print(corpo_da_resposta)  # Resposta Formatada

            # Validação
            assert resposta.status_code == status_code_esperado
            assert corpo_da_resposta['code'] == codigo_esperado
            assert corpo_da_resposta['type'] == tipo_esperado
            assert corpo_da_resposta['message'] == mensagem_esperada

        case 400:
            print('username fornecido incorretamente')

        case 404:
            print('usuário não encontrado')