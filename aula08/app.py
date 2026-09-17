from model import model_lead
import control


def add_lead():
    name = input("Nome: ")
    email = input("E-mail: ")
    company = input("Empresa: ")
    step = input("Etapa de vendas: ")

    # validar as entradas do usuario
    # depois de validar, vamos modelar os dados

    print(model_lead(name, email, company, step))

    # depois de modelado, vamos enviar esse dicionario(dict)(leads) para o leads.json
    # para salvar vamos usar o modulo control
    control.create_lead(model_lead(name, email, company, step))
    print("Lead adicionado (func)")

def list_leads():
    leads = control.read_leads()
    if not leads:
        print("nenhum lead ainda")
        return

    print(f"#  | {'Nome':<10} | {'Email':<20} | company")
    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead["name"]:<10} | {lead["email"]:<10} | {lead["company"]}")

def search_leads():
    query = input("Buscar por: ").strip().lower()
    if not query:
        print("Consulta vazia")
        return

    leads_finded = control.read_leads_search(query)
    print(f"#  | {'Nome':<10} | {'Email':<20} | company")
    for i, lead in leads_finded:
        print(f"{i:02d} | {lead["name"]:<10} | {lead["email"]:<10} | {lead["company"]}")

def export_leads():
    path_csv = control.export_csv()

    if path_csv is None:
        print("Não foi possivel exportar os leads")
    else:
        print(f"Exportado para {path_csv}")

def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Buscar (nome/e-mail/empresa)")
        print("[4] Exportar CSV")
        print("[0] Sair do programa")

        opt = input("Escolha uma opção: ")

        if opt == "1":
            add_lead()
        elif opt == "2":
            print("Listar leads")
        elif opt == "3":
            search_leads()
        elif opt == "4":
            export_leads()
        elif opt == "0":
            print("Até mais...")
            break
        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()