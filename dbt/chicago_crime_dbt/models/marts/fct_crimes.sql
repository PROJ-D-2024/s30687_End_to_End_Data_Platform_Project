with crimes as (

    select *
    from {{ ref('stg_crimes') }}

),

final as (
    select
        id,
        case_number,
        crime_date,
        updated_on,
        year,
        district,
        ward,
        community_area,
        beat,
        primary_type,
        description,
        location_description,
        arrest,
        domestic,
        latitude,
        longitude,
        date_trunc('month', crime_date) as crime_month,

        case
            when arrest = true then 'arrested'
            else 'not_arrested'
        end as arrest_status,

        case
            when domestic = true then 'domestic'
            else 'non_domestic'
        end as domestic_flag

    from crimes
    where district is not null
      and primary_type <> ''

)

select *
from final