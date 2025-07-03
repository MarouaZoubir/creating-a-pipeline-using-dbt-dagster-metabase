-- models/marts/reports/monthly_revenue_by_store.sql

{{ config(materialized='view') }}

with payments_enriched as (
    select
        p.payment_id,
        p.customer_id,
        p.staff_id,
        p.amount,
        date_trunc('month', p.paid_at) as month,  -- ✅ use alias 'paid_at'
        s.store_id
    from {{ ref('stg_payment') }} p
    join {{ ref('stg_staff') }} s on p.staff_id = s.staff_id
)

select
    month,
    store_id,
    sum(amount) as total_revenue
from payments_enriched
group by month, store_id
order by month, store_id