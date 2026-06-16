# Задание 1. Выбор и реализация решения для пакетной обработки данных

## Выбор технологического решения

Для реализации системы пакетной обработки данных выбрана платформа Apache Airflow.

### Причины выбора

Система должна обеспечивать:

* построение сложных пайплайнов обработки данных;
* интеграцию с различными источниками данных;
* поддержку ветвлений и условной логики;
* обработку больших объёмов данных;
* мониторинг и уведомления;
* возможность развёртывания в облачной инфраструктуре.

Apache Airflow удовлетворяет всем перечисленным требованиям и является одним из наиболее распространённых инструментов оркестрации ETL/ELT процессов.

---

## Интеграция с внешними системами

### BigQuery

Поддерживается официальный пакет:

```
apache-airflow-providers-google
```

Доступны готовые операторы:

* BigQueryInsertJobOperator
* BigQueryCreateTableOperator
* BigQueryGetDataOperator

### Amazon Redshift

Поддерживается официальный пакет:

```
apache-airflow-providers-amazon
```

Доступны:

* RedshiftSQLOperator
* RedshiftDataOperator

### Kafka

Поддерживается официальный пакет:

```
apache-airflow-providers-apache-kafka
```

Доступны:

* ProduceToTopicOperator
* ConsumeFromTopicOperator

### Apache Spark

Поддерживается официальный пакет:

```
apache-airflow-providers-apache-spark
```

Доступны:

* SparkSubmitOperator
* SparkJDBCOperator

Таким образом, для всех требуемых систем существуют готовые модули, что существенно ускоряет разработку.

---

## Поддержка бизнес-логики

### Ветвления

Поддерживаются через:

* BranchPythonOperator
* @task.branch

### Условные операторы

Поддерживаются через:

* ShortCircuitOperator
* BranchPythonOperator

### Event Triggers

Поддерживаются:

* FileSensor
* ExternalTaskSensor
* Kafka Trigger
* Dataset Trigger

---

## Отказоустойчивость

### Retry

Поддерживается из коробки:

```python
retries=3,
retry_delay=timedelta(minutes=1)
```

### Fallback Logic

Реализуется через:

* Trigger Rules
* Branching
* отдельные DAG-задачи обработки ошибок

### Email-уведомления

Поддерживаются встроенно:

```python
email_on_failure=True
email_on_retry=True
email_on_success=True
```

---

## Развёртывание в облаке

Airflow хорошо масштабируется в Kubernetes.

Возможные варианты:

* Google Kubernetes Engine (GKE)
* Amazon EKS
* Azure AKS

Рекомендуемый способ:

* Kubernetes
* официальный Helm Chart
* PostgreSQL как metadata database
* Redis при использовании CeleryExecutor

Такой подход обеспечивает горизонтальное масштабирование воркеров и отказоустойчивость системы.

---

# POC

В рамках POC реализован простой DAG:

1. Чтение данных из CSV-файла.
2. Подсчёт количества записей.
3. Ветвление пайплайна:

   * если записей больше 5 → success branch;
   * иначе → fail branch.
4. Настроены retry-политики.
5. Настроены email-уведомления.

Демонстрация выполнена локально в Docker Compose.
