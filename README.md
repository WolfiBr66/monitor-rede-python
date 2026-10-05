# Monitor de Rede - Python

Script em Python para monitoramento de ativos de rede via ping e verificação de portas TCP. Ideal para ambientes de suporte que precisam acompanhar disponibilidade de servidores e estações, gerando logs para auditoria.

## Funcionalidades

- Lê lista de hosts a partir de `hosts.txt`
- Realiza ping em cada host
- Verifica se portas específicas estão abertas (ex: 3389 - RDP)
- Gera log com status de cada ativo em `log_rede.txt`
- Pode ser agendado via Task Scheduler ou cron

## Tecnologias

- Python 3.10+
- Bibliotecas: `subprocess`, `socket`, `datetime`

## Como executar

1. Clone o repositório:
```bash
git clone https://github.com/WolfiBr66/monitor-rede-python.git
cd monitor-rede-python
```

2. Edite o arquivo `hosts.txt` com os IPs ou hostnames que deseja monitorar:
```
8.8.8.8
192.168.0.1
servidor01.local
```

3. Execute o script:
```bash
python monitor.py
```

4. Verifique o resultado em `log_rede.txt`.

## Estrutura do projeto
```
monitor-rede-python/
├── monitor.py
├── hosts.txt
├── log_rede.txt
└── README.md
```

## Aprendizados

- Monitoramento de ativos de rede
- Verificação de portas TCP com Python
- Geração de logs para auditoria de infraestrutura

## Autor

Marcelo Junio Siqueira Gonçalo
[LinkedIn](https://www.linkedin.com/in/marcelogoncalo/) | [GitHub](https://github.com/WolfiBr66)