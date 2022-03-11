from .retorno import minha_lista


def test_minha_lista():
    """Teste minha lista"""
    assert list == type(minha_lista().frutas)
    assert str == type(minha_lista().local)
    assert int == type(minha_lista().supermercados)
    assert dict == type(minha_lista().extras)
