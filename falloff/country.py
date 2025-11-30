#!/usr/bin/python

# What is the relative falloff in population for the cities in each country?
# using dataset https://public.opendatasoft.com/explore/assets/geonames-all-cities-with-a-population-1000/export/

import pandas
import plotly

pandas.options.plotting.backend = "plotly"
country = "Country name EN"
city = "ASCII Name"
population = "Population"
normalized_population = "Normalized Population"
group_index = "Group Index"


def validate(row: pandas.Series):
    if not isinstance(row[city], str) or not isinstance(row[country], str):
        print(row)
        return None
    return row


def normalize(df_in: pandas.DataFrame):
    normal = 1e2 / df_in.Population.iloc[0]
    df_in[normalized_population] = df_in[population].apply(lambda x: x * normal)
    df_in[group_index] = range(len(df_in))
    return df_in


df = (pandas.read_csv("cities.csv", delimiter=";")
      [[city, country, population]]
      .sort_values([population], ascending=False)
      .apply(validate, axis=1))

countries = (df.groupby(country)
             .head(10)
             .groupby(country)
             .apply(normalize)
             .reset_index(drop=True))

fig = plotly.graph_objs.Figure()
(countries.groupby(country)
 .apply(lambda x:
        fig.add_trace(
            plotly.graph_objs.Line(
                name=x[country].iloc[0],
                x=x[group_index],
                y=x[normalized_population],
                text=x[city],
                mode="lines+text"))
        )
 )
fig.show()
