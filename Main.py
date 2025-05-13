import pandas as pd
import os
import datetime as dt
import zipfile
from time import sleep


def Backup(Tempo, dataframe, Diretorio):

    with open("lastbp.txt", "r") as arquivo:
        date = arquivo.readline().strip()
        if date == ' ':
            lastbp = dt.datetime.now().date()
        else:
            lastbp = dt.datetime.strptime(date,"%Y-%m-%d")
    originaldr = os.path.dirname(Diretorio)
    dataframe.to_csv(f"{originaldr}\Backup.csv", index=False)
    Bp = f"{originaldr}\Backup.csv"
    Zip = f"{originaldr}\Backup.zip"
    while True:
        match Tempo:
            case 1:
                nextbp = lastbp + dt.timedelta(days=1)
                if dt.datetime.now() >= nextbp:
                    with zipfile.ZipFile(Zip, 'w') as zipf:
                        zipf.write(Bp)
                    with open("lastbp.txt", "w") as arquivo:
                        arquivo.write(dt.datetime.now().date().strftime("%Y-%m-%d"))

            case 2:
                nextbp = lastbp + dt.timedelta(days=30)
                if dt.datetime.now() >= nextbp:
                    with zipfile.ZipFile(Zip, 'w') as zipf:
                        zipf.write(Bp)
                    with open("lastbp.txt", "w") as arquivo:
                        arquivo.write(dt.datetime.now().date().strftime("%Y-%m-%d"))

            case 3:
                nextbp = lastbp + dt.timedelta(days=365)
                if dt.datetime.now() >= nextbp:
                    with zipfile.ZipFile(Zip, 'w') as zipf:
                        zipf.write(Bp)
                    with open("lastbp.txt", "w") as arquivo:
                        arquivo.write(dt.datetime.now().date().strftime("%Y-%m-%d"))
            case 0:
                with zipfile.ZipFile(Zip, 'w') as zipf:
                    zipf.write(Bp)
                with open("lastbp.txt", "w") as arquivo:
                    arquivo.write(dt.datetime.now().date().strftime("%Y-%m-%d"))
        sleep(3600)

while True:
    Diretorio = input("Digite o diretório do arquivo>>")
    try:
        Arquivo = pd.read_csv(Diretorio)
        break
    except:
        print("Arquivo não encontrado")
Tempo = int(
    input("Em quanto tempo deseja fazer o backup? |1-24h|2-30 dias|3-365 dias >>"))
print(dt.datetime.now().date())
Backup(Tempo, Arquivo, Diretorio)
