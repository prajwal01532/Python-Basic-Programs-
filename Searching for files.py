from pathlib import Path

path=Path()
print("Shows all files exists inside the directories:")
for file in path.glob('*'):
    print(file)