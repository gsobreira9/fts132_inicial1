import pytest

from main import somar_dois_numeros, calcular_area_do_circulo


def testar_somar_dois_numeros():
    # - 1ª Etapa: Configura / Prepara
    # Dados / Valores
    # Entrada / Input
    num1 = 4
    num2 = 5
    # Saída / Output
    resultado_esperado = 9

    # - 2ª Etapa: Executa
    resultado_atual = somar_dois_numeros(num1, num2)

    # - 3ª Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado


@pytest.mark.parametrize('raio, resultado_esperado',[
    #valores
                                     (1,3.14), #teste nº1
                                     (2,12.56), #teste nº2
                                     (3,28.26), #teste nº3
                                     (4,50.24), # test nº4
                                     ('a', "Falha no calculo - raio não é um número "), # test nº5
                                     (' ', "Falha no calculo - raio não é um número "),  # test nº6
                         ])
def testar_calcular_area_do_circulo(raio,resultado_esperado):
    # 1- configura / Comentamos para que os parametros sejam lidos
    # raio= 2
    # resutlado_esperado =12.56


    #2 - executa
    resultado_atual = calcular_area_do_circulo(raio)

    #3 Valida
    assert resultado_atual == resultado_esperado

