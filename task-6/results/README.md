1. Запустить инфраструктуру.

2. Запустить Spring Batch приложение.

3. Выполнить:

python client.py

или

curl -X POST http://localhost:8080/batch/run

4. Открыть Kibana.

5. Найти записи логов по полям:

traceId
spanId
uri

Пример URI:

/batch/run