import dns.name
import dns.query
import dns.message
import dns.rdatatype
from ftplib import FTP
import paramiko

def perform_dns_query(): # DNS
    try:
        queryname = dns.name.from_text("amazon.com")
        q = dns.message.make_query(queryname, dns.rdatatype.NS)
        print("Запит має вигляд:")
        print(q)
        print(" ")
        r = dns.query.udp(q, "8.8.8.8")
        print("Відповідь на запит:")
        print(r)
    except Exception as e:
        print(f"Помилка DNS-запиту: {e}")

def perform_ftp(): # FTP
    try:
        ftp = FTP('ftp.us.debian.org')
        ftp.login()
        print("FTP Login successful.")
        ftp.cwd('debian')
        print("Directory listing:")
        ftp.retrlines('LIST')
        with open('README', 'wb') as fp:
            ftp.retrbinary('RETR README', fp.write)
            print("README file downloaded.")
        ftp.quit()
    except Exception as e:
        print(f"Помилка FTP-запиту: {e}")

def perform_ssh(): # SSH
    try:
        host = "192.168.56.101"
        username = "kali"
        password = "kali"

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=username, password=password)
        print(f"Підключення до SSH-сервера: {host}")

        stdin, stdout, stderr = ssh.exec_command("df -h")
        print("Вивід команди:")
        print(stdout.read().decode())
        ssh.close()
    except Exception as e:
        print(f"Помилка SSH-запиту: {e}")


if __name__ == "__main__":
    while True:
        print("Оберіть завдання: DNS, FTP, SSH")

        choice = input("Введіть Ваш вибір: ")

        if choice == "DNS":
            perform_dns_query()
        elif choice == "FTP":
            perform_ftp()
        elif choice == "SSH":
            perform_ssh()
        else:
            print("Неіснуючий вибір.")

        another = input("Ви хочете виконати ще одне завдання? (+/-): ")
        if another.lower() != '+':
            break