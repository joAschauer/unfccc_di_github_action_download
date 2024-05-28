import os
from pathlib import Path

import pandas as pd
import tqdm
from unfccc_di_api import UNFCCCApiReader

OUTDIR = Path(__file__).parent / "downloaded_data"
OUTDIR.mkdir()

TS = os.environ["DOWNLOAD_DATE"]

def main():
    print(TS)
    print("downloading data from UNFCCC")
    r = UNFCCCApiReader()
    data = []
    for party in tqdm.tqdm(r.parties["code"], desc="parties"):
        df = r.query(party_code=party, progress=False)
        data.append(df)

    data = pd.concat(data)
    data["download_date"] = TS
    # encode non numerical year values:
    data.loc[data["year"] == "Base year", "year"] = 9999
    data["year"] = data["year"].astype(int)
    # save in csv and parquet format
    data.to_csv(OUTDIR / f"{TS}_all_parties.csv.gz", compression="gzip")
    data.to_parquet(OUTDIR / f"{TS}_all_parties.parquet", compression="brotli")


if __name__ == "__main__":
    main()
