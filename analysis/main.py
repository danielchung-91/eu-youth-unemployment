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
    total_unemployment_df = load_file("D:\Documents\GitHub\eu-youth-unemployment\data\API_SL.UEM.1524.ZS_DS2_en_csv_v2_6300644.csv", 4)
    # print(total_unemployment_df)
    tertiary_education_df = load_file("D:\Documents\GitHub\eu-youth-unemployment\data\API_SE.XPD.TERT.PC.ZS_DS2_en_csv_v2_6300612.csv",4)
    # print(tertiary_education_df)
    secondary_education_df = load_file("D:\Documents\GitHub\eu-youth-unemployment\data\API_SE.XPD.SECO.PC.ZS_DS2_en_csv_v2_6301549.csv",4)
    # print (secondary_education_df)
    total_education_df = load_file("D:\Documents\GitHub\eu-youth-unemployment\data\API_SE.XPD.TOTL.GB.ZS_DS2_en_csv_v2_6303332.csv", 4)
    # print (total_education_df

    # Selecting EU countries from the data. EU countries defined as: Austria, Belgium, Bulgaria, Croatia, Republic of Cyprus,
    # Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Latvia, Lithuania, Luxembourg,
    # Malta, Netherlands, Norway, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden, Switzerland and the UK.

    eu_trigrams = ["AUT", "BEL", "BGR", "HRV", "CHE", "CYP", "CZE", "DNK", "EST", "FIN", "FRA", "DEU", "GRC", "HUN",
                   "IRL", "ITA", "LVA", "LTU", "LUX", "MLT", "NLD", "NOR", "POL", "PRT", "ROU", "SVK", "SVN", "ESP",
                   "SWE", "GBR"]
    eu_male_unemployment_df = filter_data_by_column_value(male_unemployment_df,"Country Code", eu_trigrams)
    print(eu_male_unemployment_df)
    eu_female_unemployment_df = filter_data_by_column_value(female_unemployment_df, "Country Code", eu_trigrams)
    print(eu_female_unemployment_df)
    eu_total_unemployment_df = filter_data_by_column_value(total_unemployment_df,"Country Code", eu_trigrams)
    print(eu_total_unemployment_df)
    eu_secondary_education_df = filter_data_by_column_value(secondary_education_df, "Country Code", eu_trigrams)
    print(eu_secondary_education_df)
    eu_tertiary_education_df = filter_data_by_column_value(tertiary_education_df, "Country Code", eu_trigrams)
    print(eu_tertiary_education_df)
    eu_total_education_df = filter_data_by_column_value(total_education_df,"Country Code", eu_trigrams)
    print(eu_total_education_df)

    #Dropping data values prior to 1991 and removing non numerical data values.
    columns_to_drop = ["Country Code", "Indicator Name", "Indicator Code", "1960", "1961", "1962", "1963", "1964",
                       "1965", "1966", "1967", "1968", "1969", "1970", "1971", "1972", "1973", "1974", "1975", "1976",
                       "1977", "1978", "1979", "1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988",
                       "1989", "1990", "Unnamed: 67"]
    eu_male_unemployment_1991_2022_df = eu_male_unemployment_df.drop(columns=columns_to_drop)
    eu_female_unemployment_1991_2022_df = eu_female_unemployment_df.drop(columns=columns_to_drop)
    eu_total_unemployment_1991_2022_df = eu_total_unemployment_df.drop(columns=columns_to_drop)
    eu_secondary_education_1991_2022_df = eu_secondary_education_df.drop(columns=columns_to_drop)
    eu_tertiary_education_1991_2022_df = eu_tertiary_education_df.drop(columns=columns_to_drop)
    eu_total_education_1991_2022_df = eu_total_education_df.drop(columns=columns_to_drop)

    #Cleaning and reshaping the dataset for timeseries analysis.

    melt_eu_male_unemployment_1991_2022_df = eu_male_unemployment_1991_2022_df.melt(id_vars="Country Name",
                                                                                    var_name="Year",
                                                                                    value_name="Unemployment Rate")
    melt_eu_female_unemployment_1991_2022_df = eu_female_unemployment_1991_2022_df.melt(id_vars="Country Name",
                                                                                        var_name="Year",
                                                                                        value_name="Unemployment Rate")
    melt_eu_total_unemployment_1991_2022_df = eu_female_unemployment_1991_2022_df.melt(id_vars="Country Name",
                                                                                        var_name="Year",
                                                                                        value_name="Unemployment Rate")
    melt_eu_secondary_education_1991_2022_df = eu_secondary_education_1991_2022_df.melt(id_vars="Country Name",
                                                                                        var_name="Year",
                                                                                        value_name="Education Expenditure (%GDP per Capita)")
    melt_eu_tertiary_education_1991_2022_df = eu_tertiary_education_1991_2022_df.melt(id_vars="Country Name",
                                                                                        var_name="Year",
                                                                                        value_name="Education Expenditure (%GDP per Capita)")
    melt_eu_total_education_1991_2022_df = eu_total_education_1991_2022_df.melt(id_vars="Country Name",
                                                                                        var_name="Year",
                                                                                        value_name="Education Expenditure (% Government Expenditure)")

    # Merging Government Total Education Expenditure (% of GDP) with total youth unemployment

    merged_eu_total_youth_unemployment_total_government_expenditure_df = pd.merge(melt_eu_total_unemployment_1991_2022_df,
                                                                                 melt_eu_total_education_1991_2022_df,
                                                                                 how='right', on=['Country Name','Year'])
    print(merged_eu_total_youth_unemployment_total_government_expenditure_df)
    merged_eu_total_youth_unemployment_total_government_expenditure_df.to_csv('eu_total_unemployment_and_education_expenditure.csv', index=True)

    # Export Initial Data Clean to CSV
    # eu_male_unemployment_df.to_csv('eu_male_unemployment.csv', index=True)
    # eu_female_unemployment_df.to_csv('eu_female_unemployment.csv', index=True)
    # eu_secondary_education_df.to_csv('eu_secondary_education.csv', index=True)
    # eu_tertiary_education_df.to_csv('eu_tertiary_education.csv', index=True)
    # eu_total_education_df.to_csv('eu_total_education.csv', index=True)

    #Export Melted Datasets to CSV

    # melt_eu_male_unemployment_1991_2022_df.to_csv('melt_eu_male_unemployment.csv', index=True)
    # melt_eu_female_unemployment_1991_2022_df.to_csv('melt_eu_female_unemployment.csv', index=True)
    # melt_eu_secondary_education_1991_2022_df.to_csv('melt_eu_secondary_education.csv', index=True)
    # melt_eu_tertiary_education_1991_2022_df.to_csv('melt_eu_tertiary_education.csv', index=True)
