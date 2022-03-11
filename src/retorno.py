from collections import namedtuple


def minha_lista() -> dict:
    """_summary_

    Returns:
        dict: dicionario
    """
    my_list = namedtuple("compra", "frutas local supermercados extras")
    return my_list(
        frutas=["maça", "uva", "abacate"],
        local="rua das laranjas",
        supermercados=2,
        extras={"doces": "chocolates", "sucos": "morango"},
    )
