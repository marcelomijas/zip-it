from os import listdir, path, system, name
from shutil import make_archive


def zipit(wd: str, ze: list[str]):
    """This function compresses all folders found in 'wd' except the ones in 'ze'."""
    for i in listdir(wd):
        if not path.isfile(path.join(wd, i)) and i not in ze:
            print(f"-> {i}.zip")
            try:
                make_archive(path.join(wd, i), "zip", wd, i)
                print("\tComplete!")
            except Exception as e:
                print("\tError: {e}")


def main():
    # get file working directory
    fp = path.abspath(__file__)
    wd = path.dirname(fp)
    print("Current working directory:", wd)

    # read exceptions file
    ze = []
    exceptions_file = path.join(wd, "zip-itExceptions.txt")
    if path.exists(exceptions_file):
        with open(exceptions_file, "r", encoding="utf-8") as fe:
            ze = fe.read().splitlines()
        print("zip-itExceptions.txt file found.")

    # list folders to compress
    print("\nThe following folders will be compressed:")
    for i in listdir(wd):
        if not path.isfile(path.join(wd, i)) and i not in ze:
            print(f"-> {i}")

    proceed = input("\nDo you want to proceed? [Y/n] ").strip().lower()
    if proceed not in ("n", "no"):
        system("cls" if name == "nt" else "clear")
        print("Compressing:")
        zipit(wd, ze)

    # finish
    input("\nPress Enter to finish the program or close this window ")


if __name__ == "__main__":
    main()
