{{
    config(
        schema = 'base',
        alias = 'products',
    )
}}

WITH

extracted AS (
    SELECT
        -- ID
        sku AS product_id,

        -- Texts
        name AS product_name,
        description AS product_description,

        -- Enumerations
        type AS product_type,

        -- Numerics
        CAST(price AS INTEGER) AS product_price
    FROM
        {{ source('default', 'products') }}
)

SELECT * FROM extracted
