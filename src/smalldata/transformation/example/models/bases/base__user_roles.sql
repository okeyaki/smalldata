{{
    config(
        schema='base__mysql',
        alias='user_roles',
    )
}}

WITH

sources AS (
    SELECT *
    FROM
        {{ source('mysql', 'user_roles') }}
)

SELECT * FROM sources
