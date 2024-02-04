import csv

file=open("series_offres_difusees.csv",'r', encoding="utf-8-sig")
csvreader=csv.DictReader(file, delimiter=",")

valeurs= dict()
for row in csvreader:
    # print(row["Année"])
    if row["Année"]=="2022":
        print(row["Nombre d'offres diffusées"])
    try:
        try:

            valeurs[row["Année"]]+= int(row["Nombre d'offres diffusées"].replace(",", ""))
        except:
            valeurs[row["Année"]]+= int(row["Nombre d'offres diffusées"].replace(",", ""))
    except:
        try:
            valeurs[row["Année"]]= int(row["Nombre d'offres diffusées"].replace(",", ""))
        except:
            valeurs[row["Année"]]= int(row["Nombre d'offres diffusées"].replace(",", ""))

print(valeurs)

tab= """<!DOCTYPE html><html lang="fr"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><link rel="stylesheet" href="tableau.css"><title> Tableau</title> <body><table>\n<tr> <th style='text-align: left;' style='height: 50px;'>Annee</th> <th style='height: 50px;'>Nombre d'offres dans l'annee</th> </tr></body></html>\n"""

for k,v in valeurs.items():
    tab += f"<tr><td style='height: 25px;'>{k}</td><td style='height: 25px;'>{v}</td></tr>\n"

tab += "</table>"

with open("table.html", "w") as file:
    file.write(tab)
