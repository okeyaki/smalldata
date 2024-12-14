{{
    config(
        schema = 'base',
        alias = 'order_items',
    )
}}

WITH

extracted AS (
    SELECT
        -- ID
        id AS order_item_id,

        -- References
        order_id,
        sku AS product_id
    FROM
        {{ source('default', 'items') }}
)

SELECT * FROM extracted
