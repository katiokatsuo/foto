import os

import PIL
from PIL import Image

#quantidade de arquivos na pasta
dateimage = os.listdir("fotos/")

print(len(dateimage))
#data atual
mes, dia = None, None


for data in dateimage:
    imagem = Image.open(f"fotos/{data}")
    exifdata = imagem.getexif()

    mes, dia, ano = exifdata.get(306)[5:7], exifdata.get(306)[8:10], exifdata.get(306)[0:4]

    print(exifdata.get(306))
    print(f"exifdata: {exifdata.get(306)[11:13]}")
    # horario hora
    #print(exifdata.get(306)[11:13])

    if 13 > int(exifdata.get(306)[11:13]) > 6:
        #if int(exifdata.get(306)[5:7]) == int(mes) and int(exifdata.get(306)[8:10]) == int(dia):
            try:
                os.makedirs(f"fotos_mandar/{dia}_{mes}_{ano}")
                imagem.close()
                os.rename(f"fotos/{data}", f"fotos_mandar/{dia}_{mes}_{ano}/{data}")
            except FileExistsError:
                print("existe")
                imagem.close()
                os.rename(f"fotos/{data}", f"fotos_mandar/{dia}_{mes}_{ano}/{data}")
