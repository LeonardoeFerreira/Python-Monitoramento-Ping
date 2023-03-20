import platform
import subprocess

def myping(host):
    parameter = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', parameter, '4', host]
    response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
    output = response.stdout.decode('latin1')  # Usando o codec latin1
    if response.returncode == 0:
        with open("output-UP.txt", "a", encoding="utf-8") as f:  # Usando o codec utf-8 para escrever no arquivo
            f.write("")
            f.write("\n\n_____________________________________________________________________________________\n\n")
            f.write(f"{command} - UP\n")
            f.write(output)
        return True
    else:
        with open("output-DOWN.txt", "a", encoding="utf-8") as f:  # Usando o codec utf-8 para escrever no arquivo
            f.write(f"{command} - DOWN\n")
            f.write(output)
        return False

with open("listPing.txt", encoding="latin1") as file:  # Usando o codec latin1 para ler o arquivo
    lista = file.read()
    lista = lista.splitlines()

for ip in lista:
    myping(ip)
