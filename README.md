# s30687

## Dataset Description
Chicago Crime Dataset

The dataset used in this project contains detailed records of reported crimes in the city of Chicago. It is maintained and published by the Chicago Police Department through the Chicago Data Portal. The dataset includes information about each reported crime incident such as the type of crime, location, time of occurrence, and other relevant attributes.

Each row in the dataset represents a single crime incident. The dataset includes structured attributes describing the event, administrative districts, and geospatial information.

Key variables included in the dataset:

- id – unique identifier of the crime record

- case_number – police case number assigned to the incident

- date – date and time when the incident occurred

- block – approximate block location where the crime occurred

- iucr – Illinois Uniform Crime Reporting code

- primary_type – main category of the crime (e.g., theft, burglary)

- description – detailed description of the crime type

- location_description – type of location where the crime occurred (e.g., residence, street, parking lot)

- arrest – indicates whether an arrest was made

- domestic – indicates whether the incident was classified as domestic-related

- beat – police beat where the crime occurred

- district – police district

- ward – city council ward

- community_area – community area in Chicago

- year – year of the incident

- latitude / longitude – geographic coordinates of the crime location

This dataset enables spatial and temporal analysis of crime patterns in Chicago and can be used for tasks such as crime trend analysis, geographic clustering of crime incidents, and public safety analytics.

Dataset URL

Chicago Data Portal – Crimes Dataset
https://data.cityofchicago.org/resource/ijzp-q8t2.csv

API query used in this project:

`https://data.cityofchicago.org/resource/ijzp-q8t2.csv?$limit=50000`