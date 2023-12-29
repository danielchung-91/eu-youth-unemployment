import pandas as pd


def load_file(path, skip_rows):
    df = pd.read_csv(path, skiprows=skip_rows)
    return df

if __name__ == "__main__":
    male_unemployment_df = load_file("D:\Documents\GitHub\eu-youth-unemployment\data\API_SL.UEM.1524.MA.ZS_DS2_en_csv_v2_6302083.csv", 4)
    print(male_unemployment_df)
    female_unemployment_df = load_file("D:\Documents\GitHub\eu-youth-unemployment\data\API_SL.UEM.1524.FE.ZS_DS2_en_csv_v2_6301222.csv", 4)
    print(female_unemployment_df)
