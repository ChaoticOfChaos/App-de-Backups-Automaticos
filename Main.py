import datetime as dt
import json
import os
import time as tm
import zipfile
import sys

def Backup():
    with open(".config.json", 'r') as file:
        jsonData = json.load(file)
        lastBKPDate = jsonData.get("lastbkp")
        if lastBKPDate == None:
            return
        else:
            lastBKPDate = dt.datetime.strptime(lastBKPDate, "%Y-%m-%d")

        while 1:
            if ((dt.datetime.today().date() - lastBKPDate.date()).days >= jsonData.get("interval")):
                dirs = jsonData.get("dirs")
                outp = jsonData.get("output")
                if dirs == None or outp == None:
                    return
                for dr in dirs:
                    zip_path = os.path.join(outp, f"{os.path.basename(dr)}.zip")
                    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                        for root, _, files in os.walk(dr):
                            for file in files:
                                file_path = os.path.join(root, file)
                                arcname = os.path.relpath(file_path, start=dr)
                                zipf.write(file_path, arcname=arcname)

                today_str = dt.datetime.today().strftime("%Y-%m-%d")
                jsonData["lastbkp"] = today_str
                with open(".config.json", 'w') as file:
                    json.dump(jsonData, file, indent=4)
                lastBKPDate = dt.datetime.strptime(today_str, "%Y-%m-%d")

                print("Backup Concluido!")

            else:
                print("...")

            tm.sleep(1000)

def configure():
    print("__________Backup Automátio (Config)__________")
    configs = {"lastbkp": "2001-12-31", "dirs": [], "output": "", "interval": 30}
    dirs = "none"
    while 1:
        dirs = input("Diretório Para Backup (Vazio Para Próximo) >>> ")
        if dirs == "":
            break
        configs["dirs"].append(dirs)

    output = input("Local de Salvamento do Backup >>> ")
    configs["output"] = output

    interval = int(input("Intervalo Entre Backups (Dias) >>> "))
    configs["interval"] = interval
    with open(".config.json", 'w') as nJson:
        json.dump(configs, nJson, indent=4)

    os.system("cls")


if __name__ == '__main__':
    os.system("cls")
    if (len(sys.argv) > 1 and sys.argv[1] == "--config"):
        configure()
        Backup()

    elif (".config.json" in os.listdir(".")):
        Backup()

    else:
        configure()
        Backup()