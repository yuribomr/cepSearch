import requests

print(f"#################\n###### CEP ######\n#################")

userCEP = input("Digite seu CEP: ")

if len(userCEP) != 8:
    print("Quantidade de digitos inválida")
    exit()

request = requests.get(f'https://viacep.com.br/ws/{userCEP}/json/')

addressData = request.json()

if 'erro' not in addressData:
    print('CEP: {}' .format(addressData['cep']))
    print('Logradouro: {}'.format(addressData['logradouro']))
    print('Cidade: {}'.format(addressData['localidade']))
    print('Estado: {}'.format(addressData['uf']))
else:
    print("CEP inválido")
