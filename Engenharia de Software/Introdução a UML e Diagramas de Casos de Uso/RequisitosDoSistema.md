UC-02: Emprestar Livro
Ator: Leitor

Pré-condições:

O catálogo deve estar carregado

O leitor deve estar cadastrado

O livro deve existir no catálogo

Fluxo Principal:

O leitor informa o título do livro

O sistema verifica a disponibilidade do livro (<<include>>)

O sistema registra o empréstimo e marca o livro como indisponível

Fluxo de Exceção:

Livro não encontrado → exibe erro

Livro indisponível → informa que já está emprestado

Pós-condições:

O livro fica indisponível no catálogo

O empréstimo é registrado na lista
