{{
    config(
        schema = 'mart__default',
        alias = 'orders',
    )
}}

WITH

extracted AS (
    SELECT
        -- ID
        order_id,

        -- Numerics
        num_order_items
    FROM
        {{ ref('integration__orders') }}
)

SELECT * FROM extracted
