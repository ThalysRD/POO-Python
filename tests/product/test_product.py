from inventory_report.inventory.product import Product


def test_cria_produto():
    start = '21-12-2010'
    end = '21-12-2023'
    product = Product(325, 'Tinta', 'Armazém', start, end, '1', 'bla')

    assert product.id == 325
    assert product.nome_do_produto == 'Tinta'
    assert product.nome_da_empresa == 'Armazém'
    assert product.data_de_fabricacao == start
    assert product.data_de_validade == end
    assert product.numero_de_serie == '1'
    assert product.instrucoes_de_armazenamento == 'bla'
