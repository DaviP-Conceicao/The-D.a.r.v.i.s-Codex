# 🐧 Linux Essentials: Operações, Processos e Segurança

> **Módulo:** 01 - Linux Fundamental
> **Gerenciado por:** D.A.R.V.I.S. Codex Engine
> **Fontes:** Documentação e Experiência Prática

Este guia compila os comandos essenciais para sobrevivência no terminal, focando em eficiência (DevOps) e proteção do sistema (Security).

---

## 📂 1. Navegação e Manipulação de Arquivos
Comandos para se mover e organizar o sistema com agilidade.

| Comando | Descrição | Diferencial DARVIS |
| :--- | :--- | :--- |
| `ls -la` | Lista tudo, incluindo arquivos ocultos (Git/Python). | Essencial para auditar arquivos `.env` ou `.git`.[cite: 1] |
| `cd -` | Volta para a pasta anterior instantaneamente. | Atalho de produtividade para alternar diretórios longos.[cite: 1] |
| `mkdir -p` | Cria pastas em cascata (ex: `mkdir -p projeto/src/bin`). | Permite criar estruturas complexas de uma só vez.[cite: 1] |
| `grep -r` | Busca um texto específico dentro de arquivos recursivamente. | Localize funções perdidas em milhares de linhas de código.[cite: 1] |
| `man [comando]` | Abre o manual detalhado de qualquer comando. | O "professor" nativo do seu terminal.[cite: 1] |

---

## ⚙️ 2. Gerenciamento de Processos (The Engine Room)
Monitorar e controlar o que está "comendo" os recursos do seu sistema.[cite: 3]

### Monitoramento em Tempo Real
*   **`top`**: Exibe lista em tempo real de CPU e Memória.[cite: 3]
    *   `top -p [PID]`: Monitora um processo específico.[cite: 3]
*   **`htop`**: Versão visual e interativa do top. Perfeito para monitorar o peso de IDEs como o Android Studio.[cite: 1]
*   **`pstree -p`**: Exibe a hierarquia de processos em formato de árvore com seus PIDs.[cite: 3]

### Controle de Execução
*   **`ps -ef`**: Exibe informações detalhadas de todos os processos ativos.[cite: 3]
*   **`kill [PID]`**: Encerra um processo.[cite: 3]
    *   `kill -9 [PID]`: Força o encerramento imediato (use com cautela).[cite: 3]
*   **`pkill [nome]` / `killall [nome]`**: Encerra processos pelo nome (ex: `pkill firefox`).[cite: 3]
*   **`nice -n [valor] comando`**: Define a prioridade de um comando (-20 a 19).[cite: 3]
*   **`renice`**: Altera a prioridade de um processo que já está rodando.[cite: 3]

#### 🔍 Códigos de Estado do Processo (STAT)
Ao usar `ps`, preste atenção no status:[cite: 3]
*   **R**: Running (Em execução).
*   **S**: Interruptible Sleep (Aguardando evento).
*   **Z**: Zombie (Encerrado, mas não coletado pelo pai).
*   **D**: Uninterruptible Sleep (Geralmente aguardando I/O de disco).

---

## 🔐 3. Contas e Permissões (The Gatekeeper)
A base da segurança no Linux reside em quem pode ler, escrever ou executar.[cite: 4]

### Gestão de Usuários e Grupos
*   **`id [usuário]`**: Mostra IDs de usuário (UID) e grupo (GID).[cite: 4]
*   **`adduser [nome]`**: Cria um novo usuário com diretório home.[cite: 4]
*   **`usermod -aG [grupo] [user]`**: Adiciona um usuário a um grupo extra (ex: grupo `docker` ou `sudo`).[cite: 4]
*   **`su -l [usuário]`**: Muda para outra conta reiniciando o ambiente.[cite: 4]
*   **`sudo [comando]`**: Executa tarefas com privilégios de root.[cite: 4]

### Propriedade e Acesso
*   **`chmod`**: Define permissões.
    *   Ex: `chmod 755 arquivo` (Dono: rwx | Grupo/Outros: r-x).[cite: 4]
*   **`chown [user]:[group] [arquivo]`**: Altera o dono e o grupo de um arquivo.[cite: 4]
    *   `-R`: Aplica recursivamente a pastas e subpastas.[cite: 4]

---

## 🛠️ 4. Manutenção e Infraestrutura Moderna
Comandos para manter o sistema saudável e integrar com ferramentas de containers.

### Manutenção do Sistema (MX Linux / Debian)
*   **`sudo apt update`**: Atualiza a lista de repositórios.[cite: 1]
*   **`sudo apt autoremove`**: Remove dependências inúteis de programas desinstalados.[cite: 1]
*   **`sudo apt clean`**: Limpa o cache de pacotes baixados para liberar espaço.[cite: 1]
*   **`rm -rf ~/.cache/*`**: Limpa o cache de aplicativos (navegadores, etc.).[cite: 1]

### Comandos de Infra e Dev
*   **`python -m http.server`**: Cria um servidor web instantâneo na porta 8000.[cite: 2]
*   **`docker run -it ubuntu bash`**: Sobe um container Ubuntu e te joga direto no terminal.[cite: 2]
*   **`inxi -Fxz`**: Gera um relatório completo do hardware do seu computador.[cite: 1]
*   **`df -h`**: Mostra o uso do disco em formato legível (Gigas/Megas).[cite: 1]

---

## 🚀 5. Produtividade no Terminal
*   **`history`**: Mostra os últimos comandos. Use `!numero` para repetir um comando sem digitar.[cite: 1]
*   **`alias [nome]='[comando]'`**: Cria atalhos (ex: `alias att='sudo apt update && sudo apt upgrade'`).[cite: 1]

---