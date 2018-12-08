cd crawlers
docker-compose up -d
sleep 10
echo "Running crawlers"

cd ../services
docker-compose up -d
sleep 5
echo "Running server"

cd ../client
docker-compose up -d
sleep 5
echo "Running client"

docker ps