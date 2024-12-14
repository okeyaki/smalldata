{{
    config(
        schema='mart__default',
        alias='supply_costs',
    )
}}

WITH

extracted AS (
    SELECT
        -- ID
        supply_cost_id,

        -- References
        supply_id,
        product_id,

        -- Texts
        supply_name,

        -- Numerics
        supply_cost,

        -- Flags
        is_supply_perishable
    FROM
        {{ ref('base__supply_costs') }}
)

SELECT * FROM extracted
