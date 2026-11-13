
print("=== CONVERSOR DE KB PARA MB ===")
kb = float(input("Quantidade de kb: "))
mb = kb / 1024
print(f"{kb} kb = {mb: .2f} mb")

print("=== CONVERSOR DE MB PARA GB ===")
mb = float(input("Quantidade de mb: "))
gb = mb / 1024
print(f"{mb} mb = {gb: .2f} gb")


print("=== CONVERSOR DE ARMAZENAMENTO ===")

bytes = float(input("Digite a quantidade de bytes: "))
kb = float(input("Quantidade de kb: "))
mb = float(input("Quantidade de mb: "))

resultado_kb = bytes / 1024
resultado_mb = kb / 1024
resultado_gb = mb / 1024

print("\n=== RESULTADOS ===")

print(f"(bytes) Bytes = {resultado_kb: .2f} KB")
print(f"(kb) KB = {resultado_mb: .2f} MB")
print(f"(mb) MB = {resultado_gb: .2f} GB")
