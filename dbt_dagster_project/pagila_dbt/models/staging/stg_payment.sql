-- models/staging/stg_payment.sql

{{ config(materialized='view') }}

-- Stage the payment table
select
    payment_id,
    customer_id,
    staff_id,
    rental_id,
    amount,
    payment_date as paid_at  -- ✅ renamed to paid_at for consistency
from public.payment
