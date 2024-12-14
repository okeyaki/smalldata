{{
    config(
        schema = 'base',
        alias = 'stores',
    )
}}

WITH

extracted AS (
    SELECT
        -- ID
        id AS store_id,

        -- Texts
        name AS store_name,

        -- Numerics
        tax_rate AS store_tax_rate,

        -- Times
        opened_at AT TIME ZONE 'UTC' AS store_opening_time
    FROM
        {{ source('default', 'stores') }}
)

SELECT * FROM extracted
