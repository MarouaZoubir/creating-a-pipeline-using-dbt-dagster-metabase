{{ config(materialized = 'view') }}

select
  staff_id,
  first_name,
  last_name,
  store_id,
  email,
  username,
  active,
  last_update as updated_at
from public.staff
