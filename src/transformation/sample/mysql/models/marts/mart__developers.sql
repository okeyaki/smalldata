{{
    config(
        schema='mart__mysql',
        alias='developers',
    )
}}

WITH

sources AS (
    SELECT
        id,
        name,
        email,
        role_name
    FROM
        {{ ref('integration__developers') }}
)

SELECT * FROM sources
