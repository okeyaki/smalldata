{{
    config(
        schema = 'mart__default',
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
        {{ ref('integration__stores') }}
)

SELECT * FROM extracted
