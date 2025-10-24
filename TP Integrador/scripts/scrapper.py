import csv

CONTINENTES = ["África", "Asia", "Europa", "América", "Oceanía"]

def scrap_continent(continente):
    continente_formateado = continente.lower()
    with open("paises.csv", "r", encoding="utf-8-sig", newline="") as paises_archivo:
        with open(continente_formateado + ".csv", "w", encoding="utf-8-sig", newline="") as continente_archivo:
            paises_contenido = csv.reader(paises_archivo)
            cabecera = next(paises_contenido)
            indice_continente = cabecera.index("continente")
            for campo_pais in cabecera:
                continente_archivo.write(campo_pais)
                if campo_pais != "onu":
                    continente_archivo.write(",")
            for pais in paises_contenido:
                if (pais[indice_continente].lower() == continente_formateado):
                    continente_archivo.write("\n")
                    for campo_pais in pais:
                        continente_archivo.write(campo_pais)
                        if (len(cabecera)-1 != pais.index(campo_pais)):
                            continente_archivo.write(",")

for continente in CONTINENTES:
    scrap_continent(continente)