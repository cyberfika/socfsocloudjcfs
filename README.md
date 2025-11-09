# 🧠 **Projeto II – Sistemas Operacionais em Cloud**

Este projeto demonstra, na prática, como **serviços PaaS (Platform as a Service)** abstraem o gerenciamento de **sistemas operacionais**, permitindo que desenvolvedores foquem apenas na aplicação.  
A aplicação foi desenvolvida em **Python + Flask**, hospedada no **Render.com**, e exibe métricas em tempo real de processo, memória e CPU.

---

## 👥 Integrantes
- **Jafte Carneiro Fagundes da Silva**

---

## ☁️ Objetivo do Projeto

O projeto faz parte do estudo de **Sistemas Operacionais e Computação em Nuvem**, demonstrando:
- Como as métricas do processo (PID, memória, CPU) ainda refletem o SO subjacente;
- Como o ambiente PaaS abstrai kernel, rede e hardware físico;
- Como Flask pode ser usado para expor informações do sistema operacional via rotas REST.

---

## 🧩 Estrutura do Projeto

```

socfsocloudjcfs/
│
├── app.py
├── requirements.txt
├── README.md

````

---

## ⚙️ Configuração do Ambiente (GitHub Codespaces ou Local)

### 1. Clonar o Repositório
```bash
git clone https://github.com/cyberfika/socfsocloudjcfs.git
cd socfsocloudjcfs
````

### 2. Criar e Ativar o Ambiente Virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as Dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a Aplicação Localmente

```bash
python app.py
```

Acesse no navegador:
👉 `http://127.0.0.1:5000`

---

## 🌐 Deploy no Render.com

### 1. Criar um novo Web Service

Acesse [https://render.com](https://render.com) e conecte seu repositório do GitHub.

### 2. Configurações

| Campo             | Valor                             |
| ----------------- | --------------------------------- |
| **Runtime**       | Python 3                          |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app`               |
| **Instance Type** | Free                              |
| **Branch**        | main                              |

### 3. Arquivo `render.yaml` (opcional)

```yaml
services:
  - type: web
    name: socfsocloudjcfs
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "gunicorn app:app"
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
```

---

## 🔍 Rotas da Aplicação

| Rota        | Descrição                             | Exemplo de Retorno                                           |
| ----------- | ------------------------------------- |--------------------------------------------------------------|
| `/`         | Exibe informações do sistema em HTML  | PID, memória, CPV, SO                                        |
| `/info`     | Retorna nomes dos integrantes em JSON | `{"integrantes": "Jafte Carneiro Fagundes da Silva"}`        |
| `/metricas` | Retorna métricas completas em JSON    | `{"pid": 1234, "memoria_mb": 25.4, "cpu_percent": 1.3, ...}` |

---

## 🧠 Conceito Central

Em um ambiente **PaaS**, o sistema operacional ainda existe (por exemplo, Linux), mas é completamente **abstraído** do desenvolvedor.
Você interage apenas com sua aplicação e métricas de alto nível, sem precisar configurar ou manter o SO.

Mesmo assim, é possível observar:

* PID (Process ID) do processo Python ativo;
* Consumo de memória e uso de CPV (CPU);
* Identificação do sistema operacional subjacente.

