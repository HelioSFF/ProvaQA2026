import pytest
from tech.heliosff.UniDiasUp.operacoes.calcular_desconto import calcular_desconto

class TestCalculadoraDesconto:

    def test_compra_menor_100_comum(self):
        assert calcular_desconto(99.99, "COMUM") == 0.00

    def test_compra_exatamente_100_comum(self):
        assert calcular_desconto(100.00, "COMUM") == 10.00

    def test_compra_entre_100_e_500_comum(self):
        assert calcular_desconto(300.00, "COMUM") == 30.00

    def test_compra_exatamente_500_comum(self):
        assert calcular_desconto(500.00, "COMUM") == 100.00

    def test_compra_menor_100_vip_maiusculo(self):
        assert calcular_desconto(50.00, "VIP") == 2.50

    def test_compra_entre_100_e_500_vip_minusculo(self):
        assert calcular_desconto(200.00, "vip") == 30.00

    def test_compra_maior_500_vip_misto(self):
        assert calcular_desconto(600.00, "vIp") == 150.00

    def test_teto_200_cliente_vip(self):
        assert calcular_desconto(1000.00, "VIP") == 200.00

    def test_teto_200_cliente_comum(self):
        assert calcular_desconto(1500.00, "COMUM") == 200.00