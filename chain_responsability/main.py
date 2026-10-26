
class Principal:

  @staticmethod
  def processar_transacao(validador_inicial: ValidadorTransacao, transacao: Transacao, descricao: str):
    print("=" * 70)
    print(f"SIMULAÇÃO: {descricao}")
    print(f"Detalhes da Conta -> Tipo: {transacao.conta.tipo} | Saldo: R$ {transacao.conta.saldo:.2f} | Bloqueio: {transacao.conta.bloqueada_judicialmente}")
    print(f"Valor da Transação -> R$ {transacao.valor:.2f}")


    autorizada = validador_inicial.validar(transacao)


    if autorizada:
      print(" RESULTADO: Transação AUTORIZADA com sucesso!")
    else:
      print(" RESULTADO: Transação NEGADA pela cadeia de validações.")
    print("=" * 70 + "\n")

  @staticmethod
  def main():

    validador_saldo = ValidadorSaldo()
    validador_limite = ValidadorValorMaximo()
    validador_bloqueio = ValidadorBloqueioJudicial()


    validador_saldo.set_proximo(validador_limite).set_proximo(validador_bloqueio)


    conta_1 = Conta(saldo=1500.0, tipo="Comum", bloqueada_judicialmente=False)
    transacao_1 = Transacao(conta=conta_1, valor=500.0)
    Principal.processar_transacao(validador_saldo, transacao_1, "Cenário 1 - Transação Válida (Conta Comum)")


    conta_2 = Conta(saldo=200.0, tipo="Comum", bloqueada_judicialmente=False)
    transacao_2 = Transacao(conta=conta_2, valor=300.0)
    Principal.processar_transacao(validador_saldo, transacao_2, "Cenário 2 - Falha por Saldo Insuficiente")


    conta_3 = Conta(saldo=5000.0, tipo="Comum", bloqueada_judicialmente=False)
    transacao_3 = Transacao(conta=conta_3, valor=1200.0)
    Principal.processar_transacao(validador_saldo, transacao_3, "Cenário 3 - Falha por Ultrapassar o Limite de Conta Comum")


    conta_4 = Conta(saldo=10000.0, tipo="Premium", bloqueada_judicialmente=True)
    transacao_4 = Transacao(conta=conta_4, valor=1500.0)
    Principal.processar_transacao(validador_saldo, transacao_4, "Cenário 4 - Falha por Bloqueio Judicial Ativo")


if __name__ == "__main__":
  Principal.main()