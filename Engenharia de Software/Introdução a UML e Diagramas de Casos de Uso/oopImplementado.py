class Livro:
    def __init__(self, titulo, autor):
        self.titulo    = titulo
        self.autor     = autor
        self.disponivel = True

    def __repr__(self):
        status = "✅" if self.disponivel else "❌"
        return f"[{status}] {self.titulo} — {self.autor}"


class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.emprestimos = {}  # { leitor: [livros] }

    def cadastrar(self, titulo, autor):
        self.catalogo.append(Livro(titulo, autor))
        print(f"📚 '{titulo}' cadastrado!")

    def listar(self):
        print("\n📖 Catálogo:")
        for livro in self.catalogo:
            print(f"  {livro}")

    # UC-03
    def emprestar(self, titulo, leitor):
        livro_encontrado = None

        for livro in self.catalogo:
            if livro.titulo == titulo:
                livro_encontrado = livro
                break

        if livro_encontrado is None:
            print("❌ Livro não encontrado.")
            return

        if not livro_encontrado.disponivel:
            print(f"⚠️ '{titulo}' já está emprestado!")
            return

        # fluxo principal
        livro_encontrado.disponivel = False

        if leitor not in self.emprestimos:
            self.emprestimos[leitor] = []

        self.emprestimos[leitor].append(livro_encontrado)
        print(f"✅ '{titulo}' emprestado para {leitor}")

    # UC-04
    def devolver(self, titulo, leitor):
        if leitor not in self.emprestimos:
            print("❌ Nenhum empréstimo para esse leitor.")
            return

        livro_encontrado = None

        for livro in self.emprestimos[leitor]:
            if livro.titulo == titulo:
                livro_encontrado = livro
                break

        if livro_encontrado is None:
            print("❌ Livro não encontrado nos empréstimos.")
            return

        # devolver
        livro_encontrado.disponivel = True
        self.emprestimos[leitor].remove(livro_encontrado)

        print(f"✅ '{titulo}' devolvido por {leitor}")

        # <<extend>> multa
        atraso = True  # simulação
        if atraso:
            print("📋 Multa aplicada!")
