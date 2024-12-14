{{
    config(
        schema = 'integration',
        alias = 'supplies',
    )
}}

WITH

extracted AS (
    SELECT
        -- References
        supply_id,

        -- Texts
        supply_name,

        -- Flags
        is_supply_perishable
    FROM
        {{ ref('base__supply_costs') }}
),

filtered AS (
    SELECT DISTINCT
        -- ID
        supply_id,

        -- Texts
        supply_name,

        -- Flags
        is_supply_perishable
    FROM
        extracted
)

SELECT * FROM filtered
