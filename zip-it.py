from os import listdir, path, system, name
from shutil import make_archive


def zipit(wd: str, ze: tuple):
    """This function compresses all folders found in 'wd' except the ones in 'ze'."""
    for i in listdir(wd):
        if not path.isfile(wd + "/" + i) and i not in ze:
            print(f"-> {i}.zip")
            try:
                make_archive(i, "zip", i)
                print("\tComplete!")
            except:
                print("\tError!")


def clear():
    # Windows
    if name == "nt":
        system("cls")
    # GNU/Linux
    else:
        system("clear")


def main():
    # get file working directory
    fp = path.abspath(__file__)
    wd = path.dirname(fp)
    print("Current working directory:", wd)
    # read exceptions file
    try:
        fe = open(wd + "/zip-itExceptions.txt", "r", encoding="utf-8")
        ze = fe.read().splitlines()
        fe.close()
        print("zip-itExceptions.txt file found.")
    except:
        ze = ()
    print("\nThe following folders will be compressed:")
    # list folders to compress
    for i in listdir(wd):
        if not path.isfile(wd + "/" + i) and i not in ze:
            print(f"-> {i}")
    proceed = input("\nDo you want to proceed? [Y/n] ")
    if proceed not in ("n", "N", "No", "NO"):
        clear()
        print("Compressing:")
        zipit(wd, ze)
    # finish
    input("\nPress Enter to finish the program or close this window ")


main()
