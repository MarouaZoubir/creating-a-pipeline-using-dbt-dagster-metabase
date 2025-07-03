{{ config(materialized = 'view') }}

-- Staging model for the raw Pagila customer table
select
  customer_id,
  store_id,
  first_name,
  last_name,
  email,
  address_id,
  active as is_active,
  create_date     as created_at,
  last_update     as updated_at
from public.customer