{{
    config(
        schema = 'mart__default',
        alias = 'supply_costs',
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

        -- Numerics
        supply_cost
    FROM
        {{ ref('integration__supply_costs') }}
)

SELECT * FROM extracted
