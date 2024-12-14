{{
    config(
        schema = 'base',
        alias = 'orders',
    )
}}

WITH

extracted AS (
    SELECT
        -- ID
        id AS order_id,

        -- References
        store_id,
        customer AS customer_id,

        -- Numerics
        CAST(order_total AS INTEGER) AS order_price,
        CAST(subtotal AS INTEGER) AS order_subtotal_price,
        CAST(tax_paid AS INTEGER) AS order_tax,

        -- Times
        ordered_at AT TIME ZONE 'UTC' AS order_time
    FROM
        {{ source('default', 'orders') }}
)

SELECT * FROM extracted
