{{
    config(
        schema = 'mart__default',
        alias = 'order_items',
    )
}}

WITH

extracted AS (
    SELECT
        -- ID
        order_item_id,

        -- References
        order_id,
        product_id,

        -- Texts
        product_name,
        product_description,

        -- Enumerations
        product_type,

        -- Times
        order_time
    FROM
        {{ ref('integration__order_items') }}
)

SELECT * FROM extracted
