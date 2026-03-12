# ============================================================
# 🚀 SRS em Python — FIAP Marketplace
# ============================================================
from dataclasses import dataclass, field
from typing import List
from enum import Enum

class Prioridade(Enum):
    ALTA = "Alta"
    MEDIA = "Média"
    BAIXA = "Baixa"

@dataclass
class RequisitoFuncional:
    id: str
    nome: str
    descricao: str
    prioridade: Prioridade
    ator: str
    pre_condicao: str
    pos_condicao: str

@dataclass
class RequisitoNaoFuncional:
    id: str
    categoria: str
    descricao: str
    criterio_aceitacao: str

@dataclass
class SRS:
    projeto: str
    versao: str
    descricao: str
    requisitos_funcionais: List[RequisitoFuncional] = field(default_factory=list)
    requisitos_nao_funcionais: List[RequisitoNaoFuncional] = field(default_factory=list)

    def adicionar_rf(self, req: RequisitoFuncional):
        self.requisitos_funcionais.append(req)
        print(f"✅ RF '{req.id}' adicionado!")

    def adicionar_rnf(self, req: RequisitoNaoFuncional):
        self.requisitos_nao_funcionais.append(req)
        print(f"✅ RNF '{req.id}' adicionado!")

    def relatorio(self):
        print(f"\n{'='*50}")
        print(f"📋 SRS — {self.projeto} v{self.versao}")
        print(f"{'='*50}")
        print(f"📝 {self.descricao}\n")

        print(f"🔧 REQUISITOS FUNCIONAIS ({len(self.requisitos_funcionais)})")
        for rf in self.requisitos_funcionais:
            print(f"[{rf.id}] {rf.nome} — Prioridade: {rf.prioridade.value}")
            print(f"Ator: {rf.ator}")
            print(f"📌 {rf.descricao}\n")

        print(f"⚡ REQUISITOS NÃO-FUNCIONAIS ({len(self.requisitos_nao_funcionais)})")
        for rnf in self.requisitos_nao_funcionais:
            print(f"[{rnf.id}] {rnf.categoria}")
            print(f"📌 {rnf.descricao}")
            print(f"✔️ Critério: {rnf.criterio_aceitacao}\n")


# ============================================================
# 🛒 SRS — FIAP Marketplace
# ============================================================

srs = SRS(
    projeto="FIAP Marketplace",
    versao="1.0",
    descricao="Marketplace interno para alunos venderem produtos artesanais."
)

# ------------------------------------------------------------
# REQUISITOS FUNCIONAIS
# ------------------------------------------------------------

srs.adicionar_rf(RequisitoFuncional(
    id="RF-001",
    nome="Cadastro de Produto",
    descricao="O sistema deve permitir que alunos cadastrem produtos com nome, descrição, preço e categoria em até 30 segundos.",
    prioridade=Prioridade.ALTA,
    ator="Aluno vendedor",
    pre_condicao="Usuário autenticado no sistema",
    pos_condicao="Produto listado no marketplace"
))

srs.adicionar_rf(RequisitoFuncional(
    id="RF-002",
    nome="Busca por Categoria",
    descricao="O sistema deve permitir buscar produtos por categoria retornando resultados em até 2 segundos.",
    prioridade=Prioridade.ALTA,
    ator="Aluno comprador",
    pre_condicao="Produtos cadastrados na plataforma",
    pos_condicao="Lista de produtos exibida ao usuário"
))

srs.adicionar_rf(RequisitoFuncional(
    id="RF-003",
    nome="Avaliação de Vendedor",
    descricao="O sistema deve permitir que compradores avaliem vendedores com nota de 1 a 5 estrelas após a compra.",
    prioridade=Prioridade.MEDIA,
    ator="Aluno comprador",
    pre_condicao="Compra finalizada",
    pos_condicao="Avaliação registrada no perfil do vendedor"
))


# ------------------------------------------------------------
# REQUISITOS NÃO FUNCIONAIS
# ------------------------------------------------------------

srs.adicionar_rnf(RequisitoNaoFuncional(
    id="RNF-001",
    categoria="Disponibilidade",
    descricao="O sistema deve possuir disponibilidade mínima de 99.9% ao longo do mês.",
    criterio_aceitacao="Monitoramento via uptime robot comprovando disponibilidade >= 99.9%"
))

srs.adicionar_rnf(RequisitoNaoFuncional(
    id="RNF-002",
    categoria="Conformidade Legal",
    descricao="O sistema deve estar em conformidade com a LGPD para tratamento de dados pessoais.",
    criterio_aceitacao="Auditoria de segurança confirmando anonimização e consentimento de dados"
))


# ============================================================
# 🔍 Função de Validação de Requisitos
# ============================================================

def validar_requisito(rf: RequisitoFuncional) -> dict:
    """
    Valida se um requisito funcional segue boas práticas.
    """
    
    resultados = {}

    resultados["descricao_longa"] = len(rf.descricao) > 20
    resultados["tem_pre_condicao"] = rf.pre_condicao != ""
    resultados["criterio_mensuravel"] = any(char.isdigit() for char in rf.descricao)

    return resultados


# ============================================================
# ⭐ Exportar SRS em Markdown
# ============================================================

def exportar_markdown(srs: SRS):

    md = f"# SRS — {srs.projeto}\n"
    md += f"Versão: {srs.versao}\n\n"
    md += f"{srs.descricao}\n\n"

    md += "## Requisitos Funcionais\n\n"

    for rf in srs.requisitos_funcionais:
        md += f"### {rf.id} — {rf.nome}\n"
        md += f"- **Ator:** {rf.ator}\n"
        md += f"- **Prioridade:** {rf.prioridade.value}\n"
        md += f"- **Descrição:** {rf.descricao}\n"
        md += f"- **Pré-condição:** {rf.pre_condicao}\n"
        md += f"- **Pós-condição:** {rf.pos_condicao}\n\n"

    md += "## Requisitos Não Funcionais\n\n"

    for rnf in srs.requisitos_nao_funcionais:
        md += f"### {rnf.id} — {rnf.categoria}\n"
        md += f"- **Descrição:** {rnf.descricao}\n"
        md += f"- **Critério de aceitação:** {rnf.criterio_aceitacao}\n\n"

    return md


# ============================================================
# 📋 Teste
# ============================================================

srs.relatorio()

print("\nValidação RF-001:")
print(validar_requisito(srs.requisitos_funcionais[0]))

print("\nMarkdown gerado:\n")
print(exportar_markdown(srs))
