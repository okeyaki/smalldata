{{
    config(
        schema = 'mart__default',
        alias = 'supplies',
    )
}}

WITH

extracted AS (
    SELECT
        -- ID
        supply_id,

        -- Texts
        supply_name,

        -- Flags
        is_supply_perishable
    FROM
        {{ ref('integration__supplies') }}
)

SELECT * FROM extracted
