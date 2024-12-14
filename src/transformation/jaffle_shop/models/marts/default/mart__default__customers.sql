{{
    config(
        schema = 'mart__default',
        alias = 'customers',
    )
}}

WITH

extracted AS (
    SELECT
        -- ID
        customer_id,

        -- Texts
        customer_name,

        -- Numerics
        num_customer_lifetime_orders,

        -- Times
        customer_first_order_time,
        customer_last_order_time
    FROM
        {{ ref('integration__customers') }}
)

SELECT * FROM extracted
