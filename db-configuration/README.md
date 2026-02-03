# Database config

Requirements:
1. Intall MariaDB
2. Install PostgreSQL
3. Create an user for PostgreSQL

# Commands

1. Create WCA DB in MariaDB:
    ```shell
    mariadb -u <username> -p
    ```
    Then create db:
    ```sql
    CREATE DATABASE wca
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
    ```
2. Import the data:
    ```shell
    mariadb -u <username> -p wca < WCA_export.sql
    ```

3. Create WCA DB in PgSQL. Access to PgSQL:
    ```shell
    psql -U postgres
    ```

    Then create WCA DB:
    ```
    CREATE DATABASE wca
    OWNER <user>
    ENCODING 'UTF8';
    ```

4. Install `pgloader`:
    In MacOS:
    ```
    brew install pgloader

    pgloader --version
    ```

5. Create config file with the following content (if not exist), call it `import_db.load`:
    ```shell
    LOAD DATABASE
        FROM mysql://<user>:<password_mariaDB>@localhost/wca
        INTO postgresql://<user>:<password_Postgre>@localhost/wca

    WITH
        include drop,
        create tables,
        create indexes,
        reset sequences,
        batch rows = 50000,
        workers = 4,
        concurrency = 2

    SET
        maintenance_work_mem to '1GB',
        work_mem to '64MB'

    CAST
        type datetime to timestamptz,
        type date to date,
        type time to time

    BEFORE LOAD DO
        $$ DROP SCHEMA IF EXISTS public CASCADE; $$,
        $$ CREATE SCHEMA public; $$;
    ```
6. Run `import_db.load` with `pgload`:
    ```shell
    pgload import_db.load
    ```

7. For optimizing wca-db performance, you can create the indexes indicated in `wca_index_creation.sql`. You can run the script in terminal with:
    ```shell
    psql -U <you_user> -d wca -f db_optimization.sql
    ```

7. **(Optional, but not recommended for this project)** If you want to migrate wca data to public schema, run the following script:
    ```SQL
    DO $$
    DECLARE
        r RECORD;
    BEGIN
        FOR r IN
            SELECT tablename
            FROM pg_tables
            WHERE schemaname = 'wca'
        LOOP
            EXECUTE format(
                'ALTER TABLE wca.%I SET SCHEMA public;',
                r.tablename
            );
        END LOOP;
    END $$;

    DROP SCHEMA wca CASCADE;
    ```
