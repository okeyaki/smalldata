{{
    config(
        schema = 'integration',
        alias = 'stores',
    )
}}

WITH

extracted AS (
    SELECT
        -- ID
        store_id,

        -- Texts
        store_name,

        -- Numerics
        store_tax_rate,

        -- Times
        store_opening_time
    FROM
        {{ ref('base__stores') }}
)

SELECT * FROM extracted
