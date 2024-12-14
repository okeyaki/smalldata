{{
    config(
        schema='base__mysql',
        alias='users',
    )
}}

WITH

sources AS (
    SELECT *
    FROM
        {{ source('mysql', 'users') }}
)

SELECT * FROM sources
