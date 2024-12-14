{{
    config(
        schema='mart__mysql',
        alias='administrators',
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
        {{ ref('integration__administrators') }}
)

SELECT * FROM sources
