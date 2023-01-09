from inventory_report.inventory.product import Product


def test_cria_produto():
    start = '21-12-2010'
    end = '21-12-2023'
    product = Product(325, 'Tinta', 'Trybe', start, end, '1', 'bla')

    print(type(product.id))
    assert isinstance(product.id, int)
    assert isinstance(product.nome_do_produto, str)
    assert isinstance(product.nome_da_empresa, str)
    assert isinstance(product.data_de_fabricacao, str)
    assert isinstance(product.data_de_validade, str)
    assert isinstance(product.numero_de_serie, str)
    assert isinstance(product.instrucoes_de_armazenamento, str)
