endpoints = ["/login", "/produtos", "/pedidos"]
status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]
# print(endpoints[0])
# print(endpoints[0][2])
# FUNÇÃO QUE VERIFICA SE UM STATUS CODE HTTP É SUCESSO
#200-299 = sucesso
def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299

# print(eh_sucesso(404)) 

# Função que detecta 2 erros seguidos nos codigos http de
#um endpoint
#[200, 200, 401, 200, 500] --> /login >> false
#[201, 500, 502, 201, 500] --> /pedidos >> true

def erros_seguidos(codigos_http):
    for i in range(len(codigos_http) - 1):
        codigo_atual = codigos_http[i]
        prox_codigo = codigos_http[i+1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True
    return False

#print(erros_seguidos(status[2]))

def analisar_endpoint(codigos_http):
    qtd_sucessos = 0

    for codigo in codigos_http:
        if eh_sucesso(codigo):
            qtd_sucessos += 1

    qtd_requisicoes = len(codigos_http)
    qtd_erros = qtd_requisicoes - qtd_sucessos

    percentual_sucesso = (qtd_sucessos / qtd_requisicoes) *100

    tem_erros_seguidos = erros_seguidos(codigos_http)

    if tem_erros_seguidos:
        classificacao = "CRÍTICO"
    elif percentual_sucesso >= 80:
        classificacao = "Estavel"
    else:
        classificacao = "Instavel"
        
    return (qtd_sucessos, qtd_erros,percentual_sucesso, classificacao)

#print(analisar_endpoints(status[2]))

#Percorrendo a matriz

maior_qtd_erros = -1
endpoint_maior_erro = ""
for i in range(len(endpoints)):
    nome_endpoint = endpoints [i]
    codigos_endpoint = status[i]

    sucessos, erros, percentual, classificacao = analisar_endpoint(codigos_endpoint)
    print(f"Endpoint: {nome_endpoint}")
    print(f"Códigos HTTP: {codigos_endpoint}")
    print(f"Sucessos: {sucessos}")
    print(f"Erros: {erros}")
    print(f"% de sucesso: {percentual}")
    print(f"Classificação: {classificacao}")
    print("-" * 30)
    print()

    if erros > maior_qtd_erros:
        maior_qtd_erros = erros
        endpoint_maior_erro == nome_endpoint
    elif erros == maior_qtd_erros:
        endpoint_maior_erro += " " + nome_endpoint

print(f"Endpoint(s) com + erros: {endpoint_maior_erro} ({maior_qtd_erros})")