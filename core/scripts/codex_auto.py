import os 
from datetime import datetime

def generate_entry():
    
    print("--- D.A.R.V.I.S. Codex Automation ---")
    
    category = input("Pasta (linux/networking/cloud/security): ").lower()
    title = input("Título do Conhecimento: ")
    content = input("Conteúdo (Texto puro): ")
    
    filename = f"{title.lower().replace(' ', '-')}.md"
    path = f"knowledge/{category}/{filename}"
    
    template = f"""# {title}
> 📥 **Ingerido por:** D.A.R.V.I.S Engine
> 📅 **Data:** {datetime.now().strftime('%d/%m/%Y %H:%M')}

## 📝 Conteúdo Analisado
{content}

---
*Nota: Este documento foi gerado automaticamente e aguarda revisão técnica.*
"""

    try:
        if not os.path.exists(f"knowledge/{category}"):
            os.makedirs(f"knowledge/{category}")
            
        with open(path, "w", encoding="utf-8") as f:
            f.write(template)
            
        print(f"\n  Sucesso! O conhecimento foi mapeado em: {path}")
    except Exception as e:
        print(f"\n Erro na ingestão: {e}")

if __name__ == "__main__":
    generate_entry()
