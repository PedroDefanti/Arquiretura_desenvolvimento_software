from abc import ABC, abstractmethod


class UsuarioServico(ABC):

  @abstractmethod
  def get_nome(self) -> str:
    pass

  @abstractmethod
  def get_cpf(self) -> str:
    pass

  @abstractmethod
  def get_endereco(self) -> str:
    pass


class Usuario(UsuarioServico):

  def __init__(self, nome: str, cpf: str, endereco: str):
    self._nome = nome
    self._cpf = cpf
    self._endereco = endereco

  def get_nome(self) -> str:
    return self._nome

  def get_cpf(self) -> str:
    return self._cpf

  def get_endereco(self) -> str:
    return self._endereco


class UsuarioProxy(UsuarioServico):

  def __init__(self, usuario: Usuario):
    self._usuario = usuario

  def get_nome(self) -> str:
    return self._usuario.get_nome()

  def get_cpf(self) -> str:
    cpf_original = self._usuario.get_cpf()
    digitos = "".join(filter(str.isdigit, cpf_original))

    if len(digitos) >= 5:
      # Oculta os 3 primeiros e os 2 últimos dígitos com '*'
      primeiros = "***"
      ultimos = "**"
      intermediarios = digitos[3:-2]
      return primeiros + intermediarios + ultimos

    return "***"

  def get_endereco(self) -> str:
    raise PermissionError(
        "Acesso Negado: O endereço do usuário é um dado sensível protegido "
        "pela LGPD e seu acesso é estritamente proibido."
    )


class Main:

  @staticmethod
  def main():
      
    print(" SISTEMA DE GERENCIAMENTO DE USUÁRIOS - CONFORMIDADE LGPD ")
      

    usuario_real = Usuario(
        nome="Ana Beatriz Souza",
        cpf="12345678901",
        endereco="Av. Paulista, 1000 - São Paulo/SP",
    )

    print("\n[DEMONSTRAÇÃO 1]: Acesso Direto (Sem Proxy - Exposição Indevida)")
    print(f"Nome     : {usuario_real.get_nome()}")
    print(f"CPF      : {usuario_real.get_cpf()} (Exposto por completo)")
    print(
        f"Endereço : {usuario_real.get_endereco()} (Exposto violando a LGPD)"
    )

    print("\n" + "-" * 60)

    print("\n[DEMONSTRAÇÃO 2]: Acesso via Proxy (Aplicando Regras da LGPD)")
    proxy_usuario = UsuarioProxy(usuario_real)

    print(f"Nome     : {proxy_usuario.get_nome()}")
    print(f"CPF      : {proxy_usuario.get_cpf()} (Mascarado conforme diretriz)")

    print("Endereço : Tentando acessar...")
    try:
      proxy_usuario.get_endereco()
    except PermissionError as e:
      print(f"[BLOQUEIO DE SEGURANÇA] -> {e}")

      


if __name__ == "__main__":
  Main.main()