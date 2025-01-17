from app.modelos import Entrada, TipoEntrada, GrupoEntrada
import pytest
def test_crear_entrada():
    entrada = Entrada(12)
    assert entrada.tipo == TipoEntrada.NIÑO
    assert entrada.precio == 14

    entrada = Entrada(35)
    assert entrada.tipo == TipoEntrada.ADULTO
    assert entrada.precio == 23

    entrada = Entrada(70)
    assert entrada.tipo == TipoEntrada.JUBILADO
    assert entrada.precio == 18

    entrada = Entrada(1)
    assert entrada.tipo == TipoEntrada.BEBE
    assert entrada.precio == 0

def test_crear_entrada_edad_negativa_error():
    with pytest.raises(ValueError):
        Entrada(-2)

def test_crear_entrada_edad_mayor100_error():
    with pytest.raises(ValueError):
        Entrada(100)        

def test_crear_grupo_entradas():
    grupo = GrupoEntrada()
    assert grupo.total == 0
    assert grupo.num_entradas == 0

def test_add_entradas_grupo():
    grupo = GrupoEntrada()
    grupo.agregar_entrada(35)
    assert grupo.num_entradas == 1
    assert grupo.total == 23
    
    grupo.agregar_entrada(12)
    assert grupo.num_entradas == 2
    assert grupo.total == 37

    grupo.agregar_entrada(72)
    assert grupo.num_entradas == 3
    assert grupo.total == 55

    grupo.agregar_entrada(2)
    assert grupo.num_entradas == 4
    assert grupo.total == 55

def test_cantidad_entradas_por_tipo():
    grupo = GrupoEntrada()
    grupo.agregar_entrada(10)
    assert grupo.cant_entradas_tipo(TipoEntrada.NIÑO) == 1
    grupo.agregar_entrada(16)
    assert grupo.cant_entradas_tipo(TipoEntrada.ADULTO) == 1
    grupo.agregar_entrada(23)
    assert grupo.cant_entradas_tipo(TipoEntrada.ADULTO) == 2
    grupo.agregar_entrada(75)
    assert grupo.cant_entradas_tipo(TipoEntrada.JUBILADO) == 1

def test_subtotal_por_tipo():
    grupo = GrupoEntrada()
    grupo.agregar_entrada(10)
    assert grupo.subtotal_tipo(TipoEntrada.NIÑO) == 14