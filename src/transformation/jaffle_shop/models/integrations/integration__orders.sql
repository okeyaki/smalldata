{{
    config(
        schema='integration',
        alias='orders',
    )
}}

WITH

order_extracted AS (
    SELECT
        -- ID
        order_id
    FROM
        {{ ref('base__orders') }}
),

order_item_aggregated AS (
    SELECT
        -- ID
        order_id,

        -- Numerics
        COUNT(order_item_id) AS num_order_items
    FROM
        {{ ref('base__order_items') }}
    GROUP BY
        order_id
),

joined AS (
    SELECT
        -- ID
        order_extracted.order_id,

        -- Numerics
        order_item_aggregated.num_order_items
    FROM
        order_extracted
    LEFT JOIN
        order_item_aggregated
        ON
            order_extracted.order_id = order_item_aggregated.order_id
)

SELECT * FROM joined
