[no-cd]
[group("migration")]
[doc('Запуск миграций')]
run_migration tag="head":
    just docker up postgresql
    docker compose run --remove-orphans migrations alembic upgrade {{tag}}
    just docker down postgresql


[no-cd]
[group("migration")]
[doc('Создание миграции')]
make_migration message:
    just docker up postgresql
    docker compose run --remove-orphans migrations alembic revision --autogenerate -m "{{message}}"
    just docker down postgresql


DEFAULT_SERVICES := "telegram_bot postgresql redis"

[no-cd]
[group("docker")]
[doc("Сборка docker контейнера")]
build_container:
   docker build -t ivankirpichnikov/taglibro_bot .


[no-cd]
[group("docker")]
[doc("Старт docker сервисов")]
up_compose *services=DEFAULT_SERVICES: build_container
   docker compose up {{services}} -d --remove-orphans


[no-cd]
[group("docker")]
[doc("Остановка docker сервисов")]
down_compose *services=DEFAULT_SERVICES:
   docker compose down {{services}}


[no-cd]
[group("docker")]
[doc("Прочтение логов docker сервисов")]
logs_compose *services=DEFAULT_SERVICES:
   docker compose logs {{services}}


[no-cd]
[group("docker")]
[doc("Перезапуск docker сервисов")]
restart_compose *services=DEFAULT_SERVICES:
   just docker down {{services}}
   just docker up {{services}}


[no-cd]
[group("docker")]
[doc("Пуш docker контейнера")]
push_container:
   docker push ivankirpichnikov/taglibro_bot
