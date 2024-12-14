{{
    config(
        schema = 'base',
        alias = 'customers',
    )
}}

WITH

extracted AS (
    SELECT
        -- ID
        id AS customer_id,

        -- Texts
        name AS customer_name
    FROM
        {{ source('default', 'customers') }}
)

SELECT * FROM extracted
