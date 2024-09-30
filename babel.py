from random import randint
import os
from pathlib import Path

def create_text_file(base_filename="babel"):
    a = ""
    base_path = Path(base_filename+".txt")

    if not base_path.exists():
        base_path = Path(base_filename+".txt")
        with open(base_path, "w") as f:
            for i in range(16):
                b = randint(65,91)
                a += chr(b)
            f.write(a+"\n")
            f.write(""+"\n")
            for i in range(26):
                a = ""
                for i in range(16):
                    b = randint(65,91)
                    if b == 91:
                        a += chr(32)
                    else:
                        a += chr(b)
                f.write(a+"\n")
        return str(base_path)

    i = 1
    while True:
        new_filename = f"{base_filename}_{i}"
        new_path = Path(new_filename+".txt")
        if not new_path.exists():
            new_path = Path(new_filename+".txt")
            with open(new_path, "w") as f:
                for i in range(16):
                    b = randint(65,91)
                    a += chr(b)
                f.write(a+"\n")
                f.write(""+"\n")
                for i in range(26):
                    a = ""
                    for i in range(16):
                        b = randint(65,91)
                        if b == 91:
                            a += chr(32)
                        else:
                            a += chr(b)
                    f.write(a+"\n")
            return str(new_path)
        i += 1

created_file = create_text_file()
print(f"制作完了 {created_file}")