{{
    config(
        schema='base',
        alias='orders',
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
        order_total AS order_price,
        subtotal AS order_subtotal_price,
        tax_paid AS order_tax,

        -- Times
        ordered_at AS order_time
    FROM
        {{ source('default', 'orders') }}
)

SELECT * FROM extracted
