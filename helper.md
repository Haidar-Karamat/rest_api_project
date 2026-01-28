# HOW TO Connect Environment Variable by using databasesite(supabase) connection string(DATABASE_URL=postgresql://postgres:[YOUR-PASSWORD]@db.zqnmfgsfjnjtqjtehyxp.supabase.co:5432/postgres) make sure network connection should be ipv4 because many deployment website like (render) support ipv4 network connection

## These are breifly following steps-'

```
1. 	In Supabase SQL editor for your Render project, run:
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

1. 	This wipes everything, including .
2. 	Locally, delete old migration files in .
rm migrations/versions/*.py
3. 	Generate a new migration:
flask db revision --autogenerate -m "Initial tables"

3. 	This should now include  for all your models.
4. 	Commit and push:
git add migrations
git commit -m "Fresh initial migration"
git push origin main

5. 	Redeploy on Render →  will create all tables cleanly by using command that store in render.yaml.
```
### Remember in environmnet option present in deployment website in render always paste suitable network connection string like ipv4 & ipv6 like key->DATABASE_URL value-> postgresql://postgres:[YOUR-PASSWORD]@db.zqnmfgsfjnjtqjtehyxp.supabase.co:5432/postgres