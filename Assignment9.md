## 1. Create the docker-compose file under the ~/w205/flask-with-kafka/
## 2. Spin up the docker container
#### docker-compose up -d

## 3. Create the event using kafka 
#### docker-compose exec kafka kafka-topics --create --topic events --partitions 1 --replication-factor 1 --if-not-exists --zookeeper zookeeper:32181

## 4. Create the .py file with flask library, save under ~/w205/flask-with-kafka/

## 5. Run flask
#### docker-compose exec mids env FLASK_APP=/w205/flask-with-kafka/basic_game_api.py flask run

## 6. Open another SSH session to make the call to the API
#### docker-compose exec mids curl http://localhost:5000/purchase_a_sword
