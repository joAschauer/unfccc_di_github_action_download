import datetime
from pathlib import Path

import tqdm
from unfccc_di_api import UNFCCCApiReader

OUTDIR = Path(__file__).parent / "downloaded_data"
OUTDIR.mkdir()

TS = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")


def main():
    print(TS)
    print("downloading data from UNFCCC")
    r = UNFCCCApiReader()
    data = []
    for party in tqdm.tqdm(r.parties["code"], desc="parties"):
        df = r.query(party_code=party, progress=True)
        df["download_date"] = TS
        data.append(df)

    # encode non numerical year values:
    data.loc[data["year"] == "Base year", "year"] = 9999
    # save in csv and parquet format
    df.to_csv(OUTDIR / f"{TS}_data.csv.gz", compression="gzip")
    df.to_parquet(OUTDIR / f"{TS}_data.parquet", compression="brotli")


if __name__ == "__main__":
    main()
