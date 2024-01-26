import pandas as pd
import matplotlib.pyplot as plt

# Loading file function
def load_file(path, skip_rows):
    df = pd.read_csv(path, skiprows=skip_rows)
    return df

# Defining the filter function
def filter_data_by_column_value(df, column, filter_list):
    filter = df[column].isin(filter_list)
    filtered_df = df[filter]
    return filtered_df


if __name__ == "__main__":
    male_unemployment_df = load_file("D:\Documents\GitHub\eu-youth-unemployment\data\API_SL.UEM.1524.MA.ZS_DS2_en_csv_v2_6302083.csv", 4)
    # print(male_unemployment_df)
    female_unemployment_df = load_file("D:\Documents\GitHub\eu-youth-unemployment\data\API_SL.UEM.1524.FE.ZS_DS2_en_csv_v2_6301222.csv", 4)
    # print(female_unemployment_df)
    tertiary_education_df = load_file("D:\Documents\GitHub\eu-youth-unemployment\data\API_SE.XPD.TERT.PC.ZS_DS2_en_csv_v2_6300612.csv",4)
    # print(tertiary_education_df)
    secondary_education_df = load_file("D:\Documents\GitHub\eu-youth-unemployment\data\API_SE.XPD.SECO.PC.ZS_DS2_en_csv_v2_6301549.csv",4)

    # Selecting EU countries from the data. EU countries defined as: Austria, Belgium, Bulgaria, Croatia, Republic of Cyprus,
    # Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Latvia, Lithuania, Luxembourg,
    # Malta, Netherlands, Norway, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden, Switzerland and the UK.

    eu_trigrams = ["AUT", "BEL", "BGR", "HRV", "CHE", "CYP", "CZE", "DNK", "EST", "FIN", "FRA", "DEU", "GRC", "HUN", "IRL", "ITA", "LVA", "LTU", "LUX", "MLT", "NLD", "NOR", "POL", "PRT", "ROU", "SVK", "SVN", "ESP", "SWE", "GBR"]
    eu_male_unemployment_df = filter_data_by_column_value(male_unemployment_df,"Country Code", eu_trigrams)
    print(eu_male_unemployment_df)
    eu_female_unemployment_df = filter_data_by_column_value(female_unemployment_df, "Country Code", eu_trigrams)
    print(eu_female_unemployment_df)
    eu_secondary_education_df = filter_data_by_column_value(secondary_education_df, "Country Code", eu_trigrams)
    print(eu_secondary_education_df)
    eu_tertiary_education_df = filter_data_by_column_value(tertiary_education_df, "Country Code", eu_trigrams)
    print(eu_tertiary_education_df)

    #Preparing dataset for timeseries

    # Export to CSV
    # eu_male_unemployment_df.to_csv('eu_male_unemployment.csv', index=True)
    # eu_female_unemployment_df.to_csv('eu_female_unemployment.csv', index=True)
    # eu_secondary_education_df.to_csv('eu_secondary_education.csv', index=True)
    # eu_tertiary_education_df.to_csv('eu_tertiary_education.csv', index=True)

