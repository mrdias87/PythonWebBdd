Feature: Pesquisa de Produto
  Eu como usuário,
  quero realizar uma pesquisa de um produto,
  para poder realizar a compra dele no site.

  Background:
    Given A pagina Petz é mostrada

  Scenario: Realizar a pesquisa do produto no site
    When digito o produto a ser pesquisado
     And clico no botão de pesquisa
     And clico para selecionar o produto
     And verifico se as informações do produto estão corretas
     And adiciono o produto ao carrinho
    Then verifico se o produto foi adicionado ao carrinho
