import urllib.request
import os

URL = "https://www.ncei.noaa.gov/data/international-best-track-archive-for-climate-stewardship-ibtracs/v04r01/access/csv/ibtracs.since1980.list.v04r01.csv"
FILENAME = "ibtracs.since1980.list.v04r01.csv"

def download():
    if os.path.exists(FILENAME):
        print(f"{FILENAME} already exists, skipping download")
        return

    print("downloading IBTrACS data from NOAA...")
    print("file is ~50MB, may take a moment")

    def progress(count, block_size, total_size):
        percent = int(count * block_size * 100 / total_size)
        print(f"\r  {percent}% complete", end="", flush=True)

    urllib.request.urlretrieve(URL, FILENAME, reporthook=progress)
    print(f"\ndone — saved as {FILENAME}")

if __name__ == "__main__":
    download()
