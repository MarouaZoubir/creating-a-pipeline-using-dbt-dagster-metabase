{{ config(materialized = 'view') }}

select
  inventory_id,
  film_id,
  store_id,
  last_update
from public.inventory
