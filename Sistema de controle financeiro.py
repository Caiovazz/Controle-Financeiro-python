import re
import json

def zerar_arquivo(arquivo):
    with open(arquivo, 'w', encoding='utf-8') as arquivo_dados:
        json.dump([], arquivo_dados)



def saldo(receita, despesa):
    total = receita - despesa
    print('========= SALDO =========')
    print('Total Receita R$ {:.2f}'.format(receita))
    print('Total Despesa: R$ {:.2f}'.format(despesa))
    print('Saldo Atual: R$ {:.2f}'.format(total))
    print('========= SALDO =========')



def carregar_dados(nome_arquivo):
    try:
       with open (nome_arquivo, 'r', encoding='utf-8') as arquivo:
          return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
       return []



receitas = carregar_dados('receitas.json')
despesas = carregar_dados('despesas.json')



def adcionar_receitas(receitas):
    try:
        with open('receitas.json', 'w', encoding='utf-8') as arquivo_receitas:
            json.dump(receitas, arquivo_receitas, ensure_ascii=False, indent=4)
            return True
    except FileNotFoundError as erro:
        return False


def adcionar_despesas(despesas):
    try:
        with open('despesas.json', 'w', encoding='utf-8') as arquivo_despesas:
            json.dump(despesas, arquivo_despesas, ensure_ascii=False, indent=4)
            return True
    except FileNotFoundError as erro:
        return False



while True:
    print('\n==== CONTROLE FINANCEIRO ===')
    print('1 - ADCIONAR RECEITA ')
    print('2 - ADCIONAR DESPESA ')
    print('3 - MOSTRAR SALDO')
    print('4 - MOSTRAR RELATORIO')
    print('5 - APAGAR TODOS OS DADOS')
    print('6 - SAIR')
    try:
      opcao_texto = input('Escolha uma opção: ')
      if re.search(r'[a-zA-ZáàâãéèêíïóôõöúçÁÀÂÃÉÈÍÏÓÔÕÖÚÇ]', opcao_texto):
          raise ValueError('Campo invalido. No menu, apenas são aceito numeros de 1 a 6!!! Tente novamente')

      opcao = int(opcao_texto)

    except ValueError as erro:
        print(f'Erro {erro}')
        continue
    if opcao == 1:
        nova_receita = {
            'descricao': '',
            'valor': 0
        }
        while True:
           try:
              descricao = input('Qual a descrição da receita: ')

              if re.search(r'[\d]', descricao):
                  raise ValueError('campo invalido por favor tente novamente')
              print('Concluido')
              nova_receita['descricao'] = descricao
              break
           except ValueError as erro:
              print('Campo incorreto!!')
        while True:
            try:
                valor = float(input('Digite o valor do receita: '))

                if valor <= 0:
                    raise ValueError()
                print('Concluido')
                nova_receita['valor'] = valor
                break
            except ValueError as erro:
                if 'could not convert string to float' in str(erro):
                    print('Aceito apenas numeros, tente novamente')
                else:
                    print('Campo incorreto, tente novamente!!')
        receitas.append(nova_receita)
        adcionar_receitas(receitas)

    elif opcao == 2:
        nova_despesa = {
            'descricao': '',
            'valor': 0
        }
        while True:
            try:
               descricao = input('Qual a descrição da despesa: ')

               if re.search(r'[\d]', descricao):
                  raise ValueError('campo invalido por favor tente novamente')

               print('Concluido')
               nova_despesa['descricao'] = descricao
               break
            except ValueError as erro:
                if 'could not convert string to float' in str(erro):
                    print('Campo incorreto!!')
                else:
                    print('Campo incorreto, tente novamente!!')

        while True:
            try:
                valor = float(input('Digite o valor da despesa: '))
                if valor <= 0:
                    raise ValueError('O valor deve ser maior que 0!')

                print('Concluido')
                nova_despesa['valor'] = valor
                break
            except ValueError as erro:
                if 'could not convert string to float' in str(erro):
                    print('Campo incorreto!!')
                else:
                    print('Campo incorreto, tente novamente!!')
        despesas.append(nova_despesa)
        adcionar_despesas(despesas)
    elif opcao == 3:
        if len(receitas) != 0 or len(despesas) != 0:

            total_receita = 0
            total_despesa = 0
            for r in receitas:
                total_receita += r['valor']
            for d in despesas:
                total_despesa += d['valor']

            saldo(total_receita, total_despesa)
        else:
            print('Saldo R$ 0,00 ')
            print('Arquivos vazios ')

    elif opcao == 4:
        print('\n========= RELATORIO GERAL =========')
        print('--------- RECEITAS --------')
        if len(receitas) == 0:
            print('Nenhuma receita cadastrada!!')
        else:
            for r in receitas:
                print(f'- {r['descricao']}: R$ {r['valor']:.2f}')
        print('\n-------- DESPESAS ---------')
        if len(despesas) == 0:
            print('Nenhuma despesa cadastrada!!')
        else:
            for d in despesas:
                print(f'- {d['descricao']}: R$ {d['valor']:.2f}')
        print('==================================')


    elif opcao == 5:
        comfirmacao = input('Deseja Apagar todos os dados do progama? [S/N] ').upper()
        if comfirmacao == 'S':

            receitas = []
            despesas = []

            zerar_arquivo('receitas.json')
            zerar_arquivo('despesas.json')

            print('Todos os dados foram apagados com sucesso!!')

        elif comfirmacao == 'N':
            print('Ação cancelada!!')

        else:
            print('Opção invalida! Tente novamente!')

    elif opcao == 6:
        print('Saindo do programa...')
        break

    else:
        print('Opção invalida! Tente novamente!')