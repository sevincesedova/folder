

# import os
# import shutil
# from pathlib import Path
# import fnmatch

# os.makedirs("Example", exist_ok=True)
# os.makedirs("Example/subdirect", exist_ok=True)
# # shutil.move("sekil/sekil.jpg","Example/subdirect")
# # shutil.move("sekil/text.txt","Example/subdirect")

# axtarilan_yol=Path(os.getcwd())/ "Example" / "subdirect"
# uzanti="*.txt"
# for file in axtarilan_yol.iterdir():
#     if file.is_file() and fnmatch.fnmatch(file.name,uzanti):
#         shutil.move(str(file), "Example/",file.name)





# task2
def yerler_(xallar):
    xallar_yerler = [(xallar[i], i) for i in range(len(xallar))]
    
    xallar_yerler.sort(reverse=True, key=lambda item: item[0])
    yerler = [0] * len(xallar)
    
    sira = 1
    for item in xallar_yerler:
        xal, indeks = item
        if sira == 1 or sira == 2 or sira == 5:
            yerler[indeks] = f"{sira}-ci"
        elif sira == 3 or sira == 4:
            yerler[indeks] = f"{sira}-cü"
        sira += 1
    
    return yerler

xallar = [2, 3, 5, 4, 1]
print(yerler_(xallar))