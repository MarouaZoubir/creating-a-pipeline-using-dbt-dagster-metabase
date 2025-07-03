{{ config(materialized = 'view') }}

select
  film_id,
  title
from public.film