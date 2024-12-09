{{
    config(
        schema='integration__mysql',
        alias='developers',
    )
}}

WITH

sources AS (
    SELECT
        users.id,
        users.name,
        users.email,
        user_roles.id AS role_id,
        user_roles.name AS role_name
    FROM
        {{ ref('base__users') }} AS users
    LEFT JOIN {{ ref('base__user_roles') }} AS user_roles
        ON users.role_id = user_roles.id
),

filtered AS (
    SELECT
        *
    FROM
        sources
    WHERE
        role_name = 'developer'
)

SELECT * FROM filtered
