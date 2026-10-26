from abc import ABC, abstractmethod

class Conta:

  def __init__(self, saldo: float, tipo: str, bloqueada_judicialmente: bool):
    self.saldo = saldo
    self.tipo = tipo  # "Comum" ou "Premium"
    self.bloqueada_judicialmente = bloqueada_judicialmente



class Transacao:

  def __init__(self, conta: Conta, valor: float):
    self.conta = conta
    self.valor = valor


class ValidadorTransacao(ABC):

  def __init__(self, proximo: "ValidadorTransacao" = None):
    self._proximo = proximo

  def set_proximo(self, proximo: "ValidadorTransacao") -> "ValidadorTransacao":
    self._proximo = proximo
    return proximo  # Permite encadeamento fluído


  @abstractmethod
  def validar(self, transacao: Transacao) -> bool:
    pass


class ValidadorSaldo(ValidadorTransacao):

  def validar(self, transacao: Transacao) -> bool:
    print(
        f" -> [Validando] Regra de Saldo (Saldo: R$"
        f" {transacao.conta.saldo:.2f}, Valor: R$ {transacao.valor:.2f})..."
    )
    if transacao.conta.saldo < transacao.valor:
      print("REJEITADO: Saldo insuficiente para realizar a transação.\n")
      return False

    print(" APROVADO: Saldo suficiente.")
    if self._proximo:
      return self._proximo.validar(transacao)
    return True



class ValidadorValorMaximo(ValidadorTransacao):

  def validar(self, transacao: Transacao) -> bool:
    tipo_conta = transacao.conta.tipo.lower()
    limite = 1000.0 if tipo_conta == "comum" else 10000.0

    print(
        f" -> [Validando] Regra de Valor Máximo (Conta {transacao.conta.tipo},"
        f" Limite: R$ {limite:.2f})..."
    )
    if transacao.valor > limite:
      print(
          f"REJEITADO: Valor R$ {transacao.valor:.2f} excede o limite"
          f" permitido para o tipo de conta (R$ {limite:.2f}).\n"
      )
      return False

    print(f" APROVADO: Valor dentro do limite de R$ {limite:.2f}.")
    if self._proximo:
      return self._proximo.validar(transacao)
    return True



class ValidadorBloqueioJudicial(ValidadorTransacao):

  def validar(self, transacao: Transacao) -> bool:
    print(" -> [Validando] Regra de Bloqueio Judicial...")
    if transacao.conta.bloqueada_judicialmente:
      print(" REJEITADO: A conta possui bloqueio judicial ativo.\n")
      return False

    print(" APROVADO: Conta sem bloqueios judiciais.")
    if self._proximo:
      return self._proximo.validar(transacao)
    return True



class Principal:

  @staticmethod
  def processar_transacao(
      validador_inicial: ValidadorTransacao,
      transacao: Transacao,
      descricao: str,
  ):
    print("=" * 70)
    print(f"SIMULAÇÃO: {descricao}")
    print(
        "Detalhes da Conta -> Tipo:"
        f" {transacao.conta.tipo} | Saldo: R$ {transacao.conta.saldo:.2f} |"
        f" Bloqueio: {transacao.conta.bloqueada_judicialmente}"
    )
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
    Principal.processar_transacao(
        validador_saldo, transacao_1, "Cenário 1 - Transação Válida (Conta Comum)"
    )

    conta_2 = Conta(saldo=200.0, tipo="Comum", bloqueada_judicialmente=False)
    transacao_2 = Transacao(conta=conta_2, valor=300.0)
    Principal.processar_transacao(
        validador_saldo, transacao_2, "Cenário 2 - Falha por Saldo Insuficiente"
    )

    conta_3 = Conta(saldo=5000.0, tipo="Comum", bloqueada_judicialmente=False)
    transacao_3 = Transacao(conta=conta_3, valor=1200.0)
    Principal.processar_transacao(
        validador_saldo,
        transacao_3,
        "Cenário 3 - Falha por Ultrapassar o Limite de Conta Comum",
    )
    
    conta_4 = Conta(
        saldo=10000.0, tipo="Premium", bloqueada_judicialmente=True
    )
    transacao_4 = Transacao(conta=conta_4, valor=1500.0)
    Principal.processar_transacao(
        validador_saldo,
        transacao_4,
        "Cenário 4 - Falha por Bloqueio Judicial Ativo",
    )


if __name__ == "__main__":
  Principal.main()