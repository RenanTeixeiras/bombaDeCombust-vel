#classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

#Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
#tipoCombustivel.
#valorLitro
#quantidadeCombustivel
#Possua no mínimo esses métodos:
#abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
#abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
#alterarValor( ) – altera o valor do litro do combustível.
#alterarCombustivel( ) – altera o tipo do combustível.
#alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
#OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.


class bombaCombustível ():
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustível):
        self.__tipoCombustivel = tipoCombustivel
        self.__valorLitro = valorLitro
        self.__quantidadeCombustível = quantidadeCombustível
    @property
    def tipoCombustivel(self):
        return self.__tipoCombustivel
    
    @tipoCombustivel.setter
    def tipoCombustível(self):
        raise ValueError('Utilize a função para alterar o tipo de combustível! ')
    
    @property
    def valorLitro(self):
        return self.__valorLitro
    
    @valorLitro.setter
    def valorLitro(self):
        raise ValueError('Utilize a função para alterar o valor do litro. ')
    
    @property
    def quantidadeCombustível(self):
        return self.__quantidadeCombustível
    
    @quantidadeCombustível.setter
    def quantidadeCombustível(self):
        raise ValueError('A quantidade de combustível é alterada automaticamente a cada abastecimento. ')
    
    def abastecerPorValor(self):
        valCliente = float(input('Quantos R$ você quer abastecer? '))
        print('A quantia de R$: ',valCliente, ' dá para colocar: ', valCliente/self.valorLitro, ' litros de: ', self.tipoCombustivel,'.')
        self.__quantidadeCombustível -= (valCliente/self.__valorLitro)
    
    def abastecerPorLitro(self):
        litrosCliente = float(input('Quantos litros você quer abastercer? '))
        print(litrosCliente, ' litros custam: R$', litrosCliente*self.__valorLitro,' para o combustível ',self.__tipoCombustivel,'.')
        self.__quantidadeCombustível -= litrosCliente
    
    def alterarValor(self):
        novoValor = float(input('Qual o novo valor para o combustível ' + self.__tipoCombustivel +'? '))
        self.__valorLitro = novoValor
        print('O valor do combustível ', self.__tipoCombustivel, ' foi alterado com sucesso para R$ ', self.__valorLitro, '.')

    def alterarTipo (self):
        novoTipo = input('Qual o novo tipo de combustível que estará nessa bomba? ')
        self.__tipoCombustivel = novoTipo
        print('O combustível dessa bomba agora é o(a) ', self.__tipoCombustivel,'.')
    
    def alterarQuantidadeCombustível (self):
        novaQtd = float(input('Qual a nova quantidade na bomba? '))
        self.__quantidadeCombustível = novaQtd
        print('A bomba de ', self.__tipoCombustivel, ' possui ', self.__quantidadeCombustível, ' litros.')
    
    