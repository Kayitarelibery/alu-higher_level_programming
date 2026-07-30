-- Lists all privileges of the MySQL users user_0d_1 and user_0d_2
SELECT
    CONCAT(grantee, ' ---> ', privilege_type) AS Grants
FROM
    information_schema.user_privileges
WHERE
    grantee LIKE "%user_0d_1%" OR grantee LIKE "%user_0d_2%";
