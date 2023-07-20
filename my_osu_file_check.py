import os

def search(bsid="0", dirname="o:/osu!원본/songs"):
    bsid = bsid
    dirname = dirname

    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        if filename.startswith(bsid):
            print(f"filtered ({bsid}) {full_filename}")
            return bsid