docker build -t quiz-prod:quiz_prod_staging -f Dockerfile .
docker push registry.digitalocean.com/daphne-registry/quiz-prod:quiz_prod_staging