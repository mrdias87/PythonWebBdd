from pytest_bdd import scenarios, when, then
from screen_actions.acoes_site_realizar_pesquisa import Acoes_Realizar_Pesquisa
from screen_actions.acoes_site_verifica_dados_produto import Acoes_Verifica_Dados_Produto
from screen_actions.acoes_site_seleciona_produto import Acoes_Seleciona_Produto
from screen_actions.acoes_site_verifica_produtos_carrinho import Acoes_Produtos_Carrinho

scenarios('../features/pesquisa_petz.feature')


@when('digito o produto a ser pesquisado')
def preenche_pesquisa(browser):
    preenche_pesquisa_produto = Acoes_Realizar_Pesquisa(browser)
    preenche_pesquisa_produto.escreve_pesquisa_produto('Ração')


@when('clico no botão de pesquisa')
def clica_pesquisa(browser):
    clica_botao_procura = Acoes_Realizar_Pesquisa(browser)
    clica_botao_procura.clicar_botao_procura()


@when('clico para selecionar o produto')
def seleciona_item(browser):
    clica_para_selecionar_produto = Acoes_Seleciona_Produto(browser)
    clica_para_selecionar_produto.clicar_seleciona_produto()


@when('verifico se as informações do produto estão corretas')
def verifica_produto(browser):
    verifica_dados_produto = Acoes_Verifica_Dados_Produto(browser)
    assert verifica_dados_produto.verificar_texto_nome_produto() == 'Ração Royal Canin 15kg Maxi Junior Cães Filhotes ' \
                                                                    'de Raças Grandes '
    assert verifica_dados_produto.verificar_texto_nome_fornecedor() == 'Royal Canin'
    assert verifica_dados_produto.verificar_texto_valor_produto() == 'R$ 248,89'
    assert verifica_dados_produto.verificar_texto_valor_assinante() == 'R$ 224,00'


@when('adiciono o produto ao carrinho')
def adicionar_carrinho(browser):
    verifica_dados_produto = Acoes_Verifica_Dados_Produto(browser)
    verifica_dados_produto.clicar_adicionar_ao_carrinho()


@then('verifico se o produto foi adicionado ao carrinho')
def verifica_dados_carrinho(browser):
    verifica_produtos_carrinho = Acoes_Produtos_Carrinho(browser)
    assert verifica_produtos_carrinho.verificar_nome_produto_carrinho() == 'Ração Royal Canin 15kg Maxi Junior Cães ' \
                                                                           'Filhotes de Raças Grandes '
    assert verifica_produtos_carrinho.verificar_nome_fornecedor_carrinho() == 'Royal Canin'
    assert verifica_produtos_carrinho.verificar_valor_produto_carrinho() == 'R$ 248,89'
