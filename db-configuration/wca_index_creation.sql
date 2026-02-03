-- Index creation
/*
For creating indexes, we shall use the following name convention:
idx_<table_name>_<column_name>
*/

---------- wca.championships table ----------
CREATE INDEX IF NOT EXISTS idx_championships_competition_id
ON wca.championships (competition_id);

---------- wca.competitions table ----------

-- (this index already exists by default as a primary key)
-- CREATE INDEX IF NOT EXISTS idx_competitions_id
-- ON wca.competitions (id);

---------- wca.events table ----------

-- (this index already exists by default as a primary key)
-- CREATE INDEX IF NOT EXISTS idx_events_id
-- ON wca.events (id);

---------- wca.formats table ----------

-- (this index already exists by default as a primary key)
-- CREATE INDEX IF NOT EXISTS idx_formats_id
-- ON wca.formats (id);

---------- wca.persons table ----------

CREATE INDEX IF NOT EXISTS idx_persons_wca_id
ON wca.persons (wca_id);

---------- wca.ranks_average table ----------

CREATE INDEX IF NOT EXISTS idx_ranks_average_person_id
ON wca.ranks_average (person_id);

---------- wca.ranks_single table ----------

CREATE INDEX IF NOT EXISTS idx_ranks_single_person_id
ON wca.ranks_single (person_id);

---------- wca.result_attempts table ----------

CREATE INDEX IF NOT EXISTS idx_result_attempts_result_id
ON wca.result_attempts (result_id);

---------- wca.results table ----------

-- (this index already exists by default as a primary key)
-- CREATE INDEX IF NOT EXISTS idx_results_id
-- ON wca.results (id);

CREATE INDEX IF NOT EXISTS idx_results_person_id
ON wca.results (person_id);

---------- wca.scrambles table ----------

-- (this index already exists by default as a primary key)
-- CREATE INDEX IF NOT EXISTS idx_scrambles_id
-- ON wca.scrambles (id);

CREATE INDEX IF NOT EXISTS idx_scrambles_competition_id
ON wca.scrambles (competition_id);
