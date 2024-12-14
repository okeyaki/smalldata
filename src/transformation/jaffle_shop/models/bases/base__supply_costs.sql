{{
    config(
        schema = 'base',
        alias = 'supply_costs',
    )
}}

WITH

extracted AS (
    SELECT
        -- ID
        {{ dbt_utils.generate_surrogate_key(['id', 'sku']) }} AS supply_cost_id,

        -- References
        sku AS product_id,
        id AS supply_id,

        -- Texts
        name AS supply_name,

        -- Numerics
        CAST(cost AS INTEGER) AS supply_cost,

        -- Flags
        perishable AS is_supply_perishable
    FROM
        {{ source('default', 'supplies') }}
)

SELECT * FROM extracted
