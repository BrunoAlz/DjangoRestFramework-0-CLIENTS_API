from rest_framework import serializers
from clientes.models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    """VALIDANDO TAMANHO DO CPF"""

    def validade_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError('O CPF deve ter 11 digitos.')
        return cpf

    def validade_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError('O nome só pode conter letras.')
        return nome

    def validade_rg(self, rg):
        if len(rg) != 9:
            raise serializers.ValidationError('O RG só poderá ter 9 digitos.')
        return rg

    def validade_celular(self, celular):
        if len(celular) < 11:
            raise serializers.ValidationError(
                'O celular deverá possuir 11 digitos. DDD e Numero.')
        return celular
