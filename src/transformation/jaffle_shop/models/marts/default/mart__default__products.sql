{{
    config(
        schema='mart__default',
        alias='products',
    )
}}

WITH

extracted AS (
    SELECT
        -- ID
        product_id,

        -- Texts
        product_name,
        product_description,

        -- Enumerations
        product_type,

        -- Numerics
        product_price
    FROM
        {{ ref('base__products') }}
)

SELECT * FROM extracted
