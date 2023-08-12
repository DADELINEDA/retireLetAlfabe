alfabe="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
rezilta=''
antreYonFraz=input("antre yon paragraf")
for karakte in antreYonFraz:
    if karakte in alfabe:
        rezilta += karakte

print(f"rete selman sa : {rezilta}, apre le m efase lot karakte")