{{
    config(
        schema = 'integration',
        alias = 'order_items',
    )
}}

WITH

order_item_extracted AS (
    SELECT
        -- ID
        order_item_id,

        -- References
        order_id,
        product_id
    FROM
        {{ ref('base__order_items') }}
),

order_extracted AS (
    SELECT
        -- ID
        order_id,

        -- Times
        order_time
    FROM
        {{ ref('base__orders') }}
),

product_extracted AS (
    SELECT
        -- ID
        product_id,

        -- Texts
        product_name,
        product_description,

        -- Enumerations
        product_type,

        -- Numerics
        product_price
    FROM
        {{ ref('integration__products') }}
),

joined AS (
    SELECT
        -- ID
        order_item_extracted.order_item_id,

        -- References
        order_item_extracted.order_id,
        order_item_extracted.product_id,

        -- Texts
        product_extracted.product_name,
        product_extracted.product_description,

        -- Enumerations
        product_extracted.product_type,

        -- Numerics
        product_extracted.product_price,

        -- Times
        order_extracted.order_time
    FROM
        order_item_extracted
    LEFT JOIN
        order_extracted
        ON
            order_item_extracted.order_id = order_extracted.order_id
    LEFT JOIN
        product_extracted
        ON
            order_item_extracted.product_id = product_extracted.product_id
)

SELECT * FROM joined
