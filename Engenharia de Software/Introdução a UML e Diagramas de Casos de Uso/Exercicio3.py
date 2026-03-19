print("\n🔍 Buscando livro...")
busca = "clean"

for livro in catalogo:
    if busca.lower() in livro["titulo"].lower():
        status = "✅" if livro["disponivel"] else "❌"
        print(f"  {status} {livro['titulo']} — {livro['autor']}")

print("\n🔄 Devolução:")
leitor_devolvendo = "Ana Silva"
titulo_devolvendo = "Clean Code"

registro_encontrado = None

# 1. Procurar empréstimo
for emp in emprestimos:
    if emp["leitor"] == leitor_devolvendo and emp["livro"] == titulo_devolvendo:
        registro_encontrado = emp
        break

if registro_encontrado:
    # 2. Marcar livro como disponível
    for livro in catalogo:
        if livro["titulo"] == titulo_devolvendo:
            livro["disponivel"] = True
            break
    
    # remover empréstimo
    emprestimos.remove(registro_encontrado)
    
    print(f"✅ '{titulo_devolvendo}' devolvido por {leitor_devolvendo}")
    
    # <<extend>> — multa (opcional)
    atraso = True  # simulação
    if atraso:
        print("📋 Multa aplicada!")
else:
    # 3. erro
    print("❌ Empréstimo não encontrado.")
