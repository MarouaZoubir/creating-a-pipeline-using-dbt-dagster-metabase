-- models/marts/top_rented_films.sql

with rental_counts as (

    select
        f.film_id,
        f.title,
        count(*) as rental_count
    from {{ ref('stg_rental') }}   as r
    join {{ ref('stg_inventory') }}as i
      on r.inventory_id = i.inventory_id
    join {{ ref('stg_film') }}     as f
      on i.film_id = f.film_id
    group by f.film_id, f.title

)

select *
from rental_counts
order by rental_count desc
limit 10
