# internmap-backend
backend for the project "internmap"

## Development

Copy/paste the file `.env.example` to `.env` and fill the variables.

### Database
Start up the database with `docker-compose up -d`.

If it's the first time, you need to create the databse from the file `structure.sql`
```bash
docker compose -f bdd/docker-compose.yml exec -T db mysql -u root -ppassword db < bdd/structure.sql
```

Now, you can import your data from the file `data.sql`
```bash
docker compose -f bdd/docker-compose.yml exec -T db mysql -u root -ppassword db < $PATH_TO_DATA_FILE
```

### Server

Launch the server with `python src/main.py`.

If needed, you can install the dependencies with `pip install -r requirements.txt`.

## Deployment
For the deployment, `Dockerfile` and `gcloud-build.yml` are used.
It's necessary to indicate the environment variables in the Google Cloud Build configuration.
