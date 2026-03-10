with source_data as (
    select *
    from {{ source('chicago_crime_source', 'crime_aggregated') }}
),

renamed as (

    select
        id,
        case_number,
        cast(date as timestamp) as crime_date,
        block,
        iucr,
        primary_type,
        description,
        location_description,
        cast(arrest as boolean) as arrest,
        cast(domestic as boolean) as domestic,
        beat,
        district,
        ward,
        community_area,
        fbi_code,
        x_coordinate,
        y_coordinate,
        arrest_int,
        domestic_int,
        year,
        cast(updated_on as timestamp) as updated_on,
        cast(latitude as double precision) as latitude,
        cast(longitude as double precision) as longitude,
        location
    from source_data

),

filtered as (
    select *
    from renamed
    where id is not null
      and case_number is not null
      and crime_date is not null
      and primary_type is not null
      and year >= 2000

)

select *
from filtered