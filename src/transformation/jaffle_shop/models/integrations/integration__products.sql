{{
    config(
        schema = 'integration',
        alias = 'products',
    )
}}

WITH

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
        {{ ref('base__products') }}
),

supply_cost_extracted AS (
    SELECT
        -- ID
        supply_cost_id,

        -- References
        product_id,
        supply_id,

        -- Numerics
        supply_cost
    FROM
        {{ ref('base__supply_costs') }}
),

supply_cost_aggregated AS (
    SELECT
        -- ID
        product_id,

        -- Numerics
        CAST(SUM(supply_cost) AS INTEGER) AS product_supply_cost
    FROM
        supply_cost_extracted
    GROUP BY
        product_id
),

joined AS (
    SELECT
        -- ID
        product_extracted.product_id,

        -- Texts
        product_extracted.product_name,
        product_extracted.product_description,

        -- Enumerations
        product_extracted.product_type,

        -- Numerics
        product_extracted.product_price,
        supply_cost_aggregated.product_supply_cost
    FROM
        product_extracted
    LEFT JOIN
        supply_cost_aggregated
        ON
            product_extracted.product_id = supply_cost_aggregated.product_id
)

SELECT * FROM joined
