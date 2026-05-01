## 🔐 Security Essentials: Hardening e Defesa

Nesta seção, o foco sai da "funcionalidade" e entra na "proteção". Um sistema que funciona mas não é seguro é um risco.

### 🛡️ 1. SSH Hardening (Blindagem de Acesso)

O SSH (porta 22) é a porta de entrada para o seu servidor. Se deixá-lo padrão, ele será alvo de ataques brute-force constantes.

- **Desativar Login de Root:** Obriga o uso de um usuário comum com sudo para tarefas administrativas.  
- **Autenticação por Chaves:** Substitui senhas por chaves criptográficas (muito mais seguro).  
- **Mudar a Porta Padrão:** Mover da 22 para uma porta alta (ex: 2222) para evitar bots simples.

### 🧱 2. Firewall: A Primeira Linha

O Firewall decide quem entra e quem sai.

- **Conceito:** Filtragem de pacotes baseada em IP e Porta.  
- **Na Nuvem:** Chamado de Security Groups (AWS). A regra de ouro é: Negar tudo por padrão e liberar apenas o estritamente necessário.

### 🔍 3. Auditoria e Monitoramento de Acesso

Saber quem entrou no seu sistema é crucial para detectar invasões.

- **last:** Exibe informações sobre os últimos logins no sistema (IP, data e hora).  
- **lastlog:** Mostra o último login de todos os usuários cadastrados.  
- **id:** Verifica o UID e GID para garantir que um usuário não tem privilégios que não deveria.