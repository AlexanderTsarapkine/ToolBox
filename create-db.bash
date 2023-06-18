# Description: Create a local postgres database for development

# Create folder for postgres data
[ ! -d "${HOME}/postgres-data/" ] && mkdir "${HOME}/postgres-data/"

# Pull postgres image
docker pull ankane/pgvector

# Create postgres container
docker run --rm --name dev-postgres -e POSTGRES_PASSWORD=Pass2023! -v ${HOME}/postgres-data/:/var/lib/postgresql/data -p 5432:5432 -d ankane/pgvector

# Start postgres container
docker start dev-postgres
