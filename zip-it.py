from os import listdir, path
from shutil import make_archive


def zipit(wd: str, ze: tuple):
    for i in listdir(wd):
        if not path.isfile(i) and i not in ze:
            print(f"Compressing '{i}' to '{i}.zip'")
            try:
                make_archive(i, "zip", i)
                print(" Complete!")
            except:
                print(" Error!")


def main():
    # get executable working directory
    fp = path.abspath(__file__)
    wd = path.dirname(fp)
    # proceed check
    print("This is the current working directory: ")
    print(wd)
    proceed = input("Do you want to proceed? [Y/n] ")
    if proceed not in ("n", "N", "No", "NO"):
        # read exceptions file
        try:
            fe = open(wd + "/zip-itExceptions.txt", "r", encoding="utf-8")
            ze = fe.read().splitlines()
            fe.close()
        except:
            ze = ()
        # zip-it!
        zipit(wd, ze)
        # finish
        input("Press Enter to finish the program or close this window ")


main()
