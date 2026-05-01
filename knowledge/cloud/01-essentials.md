# ☁️ Cloud Essentials: Modelos e AWS Base



## 🏗️ 1. Modelos de Serviço (A Pirâmide da Nuvem)

Entender isso é fundamental para saber até onde você, como DevOps, precisa configurar o sistema.

**IaaS (Infrastructure as a Service):** Você aluga o "ferro" virtual (servidor, rede, disco). Você é responsável pelo SO, segurança e apps.  
**Exemplo:** AWS EC2.

**PaaS (Platform as a Service):** A nuvem gerencia o SO e o servidor. Você foca apenas no código.  
**Exemplo:** AWS Elastic Beanstalk ou Heroku.

**SaaS (Software as a Service):** O software completo é entregue via web. Você só consome.  
**Exemplo:** Google Drive ou Slack.

---

## 🛡️ 2. O Modelo de Responsabilidade Compartilhada

Na nuvem, a segurança é um "trabalho em dupla":

- **A Nuvem (AWS):** Responsável pela segurança **DA nuvem** (data centers físicos, cabos, hardware).  
- **O Cliente (Você):** Responsável pela segurança **NA nuvem** (quem acessa o servidor, firewall/Security Groups, criptografia de dados).

---

## 🟠 3. Primeiros Passos na AWS

Para começar com o pé direito, foque nestes três serviços que são o "feijão com arroz" de qualquer infraestrutura:

- **IAM (Identity and Access Management):** Nunca use a conta Root para o dia a dia. Crie usuários com permissões específicas.  
- **EC2 (Elastic Compute Cloud):** Suas máquinas virtuais Linux na nuvem.  
- **S3 (Simple Storage Service):** Onde você guarda arquivos, backups e logs de forma segura e barata.  

---

## 🧪 Mini-Lab: Simulando Cloud Localmente

Como você está estudando para o portfólio, é vital mostrar que você sabe usar ferramentas que aproximam o seu PC de um ambiente de nuvem.

### A. Servidor Web Instantâneo

Uma tarefa comum na nuvem é disponibilizar arquivos rapidamente via HTTP. Você pode simular isso com um comando:

```bash
python -m http.server

Isso cria um servidor na porta 8000 do seu IP, permitindo transferência de arquivos na rede local.

---

A nuvem moderna roda em containers. Teste sua primeira imagem Linux isolada:

```bash
docker run -it ubuntu bash