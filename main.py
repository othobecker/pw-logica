

print("=== CALCULADORA DE DESCONTO ===")

preco = float(input("preço R$: "))
desconto= float(input("Desconto (%): "))
produto = (input("Nome do produto: "))
valor_desconto = preco * (desconto - 100)
preco_final = preco - valor_desconto

print(f"\nProduto: {produto}")
print(f"Preço Original: R$ = {preco: .2f}")
print(f"Desconto: R$ {valor_desconto: .2f}")
print(f"preço final: R$ {preco_final: .2f}")
