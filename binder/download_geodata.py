from pathlib import Path
import requests
import io
from zipfile import ZipFile

RAW_DATA_PATH = Path("exercises/data/raw/counties/")

url = "https://www2.census.gov/geo/tiger/TIGER2018/COUNTY/tl_2018_us_county.zip"
site = requests.get(url)

z = ZipFile(io.BytesIO(site.content))
z.extractall(RAW_DATA_PATH)