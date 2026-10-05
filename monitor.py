import subprocess
import socket
import platform
from datetime import datetime

def ping(host):
    sistema = platform.system().lower()
    if sistema == "windows":
        comando = ["ping", "-n", "1", "-w", "2000", host]
    else:
        comando = ["ping", "-c", "1", "-W", "2", host]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    return resultado.returncode == 0

def verificar_porta(host, porta, timeout=2):
    try:
        with socket.create_connection((host, porta), timeout=timeout):
            return True
    except Exception:
        return False

def monitorar():
    try:
        with open("hosts.txt", "r", encoding="utf-8") as f:
            hosts = [linha.strip() for linha in f if linha.strip() and not linha.startswith("#")]
    except FileNotFoundError:
        print("Arquivo hosts.txt não encontrado.")
        return

    if not hosts:
        print("Nenhum host para monitorar.")
        return

    with open("log_rede.txt", "a", encoding="utf-8") as log:
        log.write(f"\n--- Verificação em {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ---\n")
        for host in hosts:
            status = "ONLINE" if ping(host) else "OFFLINE"
            portas_verificar = [80, 443, 3389]
            portas_status = []
            for porta in portas_verificar:
                if verificar_porta(host, porta):
                    portas_status.append(f"{porta}:aberta")
                else:
                    portas_status.append(f"{porta}:fechada")
            linha = f"{host} - {status} - " + " | ".join(portas_status)
            print(linha)
            log.write(linha + "\n")
    print("\nMonitoramento concluído. Veja log_rede.txt")

if __name__ == "__main__":
    monitorar()