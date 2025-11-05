# TeskaLabs | Test Task
JSON parser (async approach)

## STEPS
- download repo (git clone -b async https://github.com/I-antiva-I/teskalabs_test_task.git)
- open repo
- create .env (based on .env.example)
- open cmd
- run docker compose up --build
- run docker exec -it python_app_container python /app/main.py
- select JSON file
- check with phpMyAdmin (http://localhost:2222/)

## IDEA
- Insertion of lxc_item --> should be awaited
- Insertion of lxc_item's networks --> fire and forget (as tasks)
