-- models/marts/facts/fact_rental.sql
{{ config(
    materialized='incremental',
    unique_key='rental_id'
) }}

select
  r.rental_id,
  r.rental_date::timestamp      as rental_datetime,
  r.return_date::timestamp      as return_datetime,
  r.customer_id,
  i.film_id,
  i.store_id,
  r.staff_id
from {{ ref('stg_rental') }} r
join {{ ref('stg_inventory') }} i on r.inventory_id = i.inventory_id

{% if is_incremental() %}
where r.rental_date > (
    select max(rental_datetime) from {{ this }}
)
{% endif %}
