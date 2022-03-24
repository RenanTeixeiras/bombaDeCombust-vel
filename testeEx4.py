from ex4 import bombaCombustível

diesels500 = bombaCombustível ('diesels500', 6.20, 70)
diesels10 = bombaCombustível ('diesels10', 6.5, 70)
gasolina = bombaCombustível ('gasolina', 7.1, 70)
etanol = bombaCombustível ('etanol', 5.3, 70)

#print(diesels10.tipoCombustivel)
#diesels10.__tipoCombustivel='gasolina'
#print(diesels10.tipoCombustivel)

diesels10.abastecerPorLitro()