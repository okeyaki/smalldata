{{
    config(
        schema = 'integration',
        alias = 'supply_costs',
    )
}}

WITH

extracted AS (
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
)

SELECT * FROM extracted
