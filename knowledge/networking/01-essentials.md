# 🌐 Networking Essentials para DevOps & Sec

> **Módulo:** 02 - Redes e Conectividade
> **Status:** Base de Conhecimento Inicial

### 🏗️ O Modelo Mental: TCP vs UDP
*   **TCP (Transmission Control Protocol):** Focado em confiabilidade. Garante que os pacotes cheguem na ordem certa. Usado em SSH, HTTP e Bancos de Dados.
*   **UDP (User Datagram Protocol):** Focado em velocidade. Não garante entrega. Usado em Streamings e DNS.

### 🚪 Portas que você DEVE conhecer
| Porta | Serviço | Relevância Sec |
| :--- | :--- | :--- |
| **22** | SSH | O principal alvo de ataques brute-force.[cite: 4] |
| **80 / 443** | HTTP / HTTPS | Tráfego web padrão. |
| **53** | DNS | Crucial para resolução de nomes em clusters Kubernetes/Docker. |
| **8000** | Python Server | Porta padrão para testes rápidos de transferência de arquivos.[cite: 2] |

### 🛠️ Comandos de Diagnóstico
*   **`ip addr`**: Verifica suas interfaces e IPs atuais.
*   **`ping [ip/host]`**: Testa a conectividade básica.
*   **`netstat -tulpn`**: Mostra quais portas estão abertas e quais processos as estão usando.
*   **`python -m http.server`**: Comando instantâneo para testar se uma porta está acessível na rede.[cite: 2]