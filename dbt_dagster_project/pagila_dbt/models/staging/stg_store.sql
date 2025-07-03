{{ config(materialized = 'view') }}

-- Staging model for the raw Pagila store table, joined to its address
select
  s.store_id,
  s.manager_staff_id  as manager_id,
  s.address_id,
  a.address,
  a.address2,
  a.district,
  a.city_id,
  a.postal_code,
  a.phone,
  s.last_update       as updated_at
from public.store s
join public.address a
  on s.address_id = a.address_id
