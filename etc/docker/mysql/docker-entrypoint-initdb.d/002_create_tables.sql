USE `example`;

CREATE TABLE IF NOT EXISTS `user_roles` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `name` VARCHAR(255) NOT NULL
)
COMMENT = 'User roles'
;

INSERT INTO `user_roles` (
    `name`
) VALUES
    ('administrator'),
    ('developer')
;

CREATE TABLE IF NOT EXISTS `users` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `role_id` INT NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255) NOT NULL,

    FOREIGN KEY (`role_id`) REFERENCES `user_roles` (`id`)
        ON DELETE RESTRICT
        ON UPDATE RESTRICT
)
COMMENT = 'Users'
;

INSERT INTO `users` (
    `role_id`,
    `name`,
    `email`
) VALUES
    (1, 'Alice', 'alice@localhost'),
    (1, 'Bob', 'bob@localhost'),
    (1, 'Charlie', 'charlie@localhost'),
    (2, 'David', 'david@localhost'),
    (2, 'Eve',  'eve@localhost'),
    (2, 'Frank', 'frank@localhost'),
    (2, 'Grace', 'grace@localhost'),
    (2, 'Heidi', 'heidi@localhost'),
    (2, 'Ivan', 'ivan@localhost'),
    (2, 'Judy', 'judy@localhost')
;
