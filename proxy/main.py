
class Main:

  @staticmethod
  def main():
    print("=" * 60)
    print(" SISTEMA DE GERENCIAMENTO DE USUÁRIOS - CONFORMIDADE LGPD ")
    print("=" * 60)

    
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

    print("=" * 60)


if __name__ == "__main__":
  Main.main()