verifica_email = True
verifica_senha = True

login = verifica_email and verifica_senha
print(login)

if login:
    print("Entrar no programa")

logica_ou = False or False or True
print(logica_ou)

negacao = not False
print(negacao)

if not login:
    print("loga certo ai...")