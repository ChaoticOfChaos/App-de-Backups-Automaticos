import pandas as pd
import os 
import datetime as dt
import zipfile
from time import sleep

def Backup(Tempo,dataframe,Diretorio):
    originaldr = os.path.dirname(Diretorio)
    dataframe.to_csv(f"{originaldr}\Backup.csv",index = False)
    Bp = f"Backup.csv"
    Zip = f"{originaldr}\Backup.zip"
    
    match Tempo:
        case 1:
            with zipfile.ZipFile(Zip, 'w') as zipf:
                zipf.write(Bp)
            sleep(dt.timedelta(days=1).total_seconds())
                
        case 2:
            with zipfile.ZipFile(Zip, 'w') as zipf:
                zipf.write(Bp)  
            sleep(dt.timedelta(days=30).total_seconds())
                
        case 3:
            with zipfile.ZipFile(Zip, 'w') as zipf:
                zipf.write(Bp)
            sleep(dt.timedelta(days=365).total_seconds())
                

while True:
    Diretorio = input("Digite o diretório do arquivo>>")
    try:
        Arquivo = pd.read_csv(Diretorio)
        break
    except:
        print("Arquivo não encontrado")
    Tempo = int(input("Em quanto tempo deseja fazer o backup? |1-24h|2-30 dias|3-365 dias >>"))

    Backup(True,Tempo,Arquivo,Diretorio)