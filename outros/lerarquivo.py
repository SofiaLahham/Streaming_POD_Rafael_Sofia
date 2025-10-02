from pathlib import Path

p = Path("Exemplo Entrada - 1.md")
texto = p.read_text(encoding="utf-8")
print(texto)