{{ config(materialized='table') }}

select
  c.customer_id,
  concat(c.first_name, ' ', c.last_name) as full_name,
  c.email              as email,
  c.is_active          as active_flag,
  c.created_at         as signup_date,
  c.updated_at         as last_updated
from {{ ref('stg_customer') }} c