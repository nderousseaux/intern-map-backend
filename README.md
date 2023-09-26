# internmap-backend
backend for the project "internmap"

## Development
Start up the database with `docker-compose up -d`.

Launch the server with `python src/main.py`.

### First time ?
If it's the first time, you need to create the databse from the file `structure.sql`
```bash
docker compose exec -T db mysql -u root -ppassword db < structure.sql
```

Now, you can import your data from the file `data.sql`
```bash
docker compose exec -T db mysql -u root -ppassword db < data.sql
```

