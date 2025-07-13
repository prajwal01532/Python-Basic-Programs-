from pathlib import Path

path=Path("Ecommerce")
'''Here,ecommerce package(folder)or dir
 exists so it prints True '''

print(path.exists())

#Making Dir(PrajwalDirectory) or folder
path=Path("PrajwalDirectory")
print(path.mkdir())

#Removing Dir(PrajwalDirectory) or folder
path=Path("PrajwalDirectory")
print(path.rmdir())


