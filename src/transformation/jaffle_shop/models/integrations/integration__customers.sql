{{
    config(
        schema='integration',
        alias='customers',
    )
}}

WITH

customer_extracted AS (
    SELECT
        -- ID
        customer_id,

        -- Texts
        customer_name
    FROM
        {{ ref('base__customers') }}
),

customer_order_aggregated AS (
    SELECT
        -- ID
        customer_id,

        -- Numerics
        COUNT(order_id) AS num_customer_lifetime_orders,

        -- Times
        MIN(order_time) AS customer_first_order_time,
        MAX(order_time) AS customer_last_order_time
    FROM
        {{ ref('base__orders') }}
    GROUP BY
        customer_id
),

joined AS (
    SELECT
        -- ID
        customer_extracted.customer_id,

        -- Texts
        customer_extracted.customer_name,

        -- Numerics
        customer_order_aggregated.num_customer_lifetime_orders,

        -- Times
        customer_order_aggregated.customer_first_order_time,
        customer_order_aggregated.customer_last_order_time
    FROM
        customer_extracted
    LEFT JOIN
        customer_order_aggregated
        ON
            customer_extracted.customer_id
            = customer_order_aggregated.customer_id
)

SELECT * FROM joined
