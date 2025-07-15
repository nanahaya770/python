# db_connection_string = (postgresql://qa:skyqa@localhost:5432/x_clients)
from sqlalchemy import create_engine, text

try:
    engine = create_engine("postgresql://postgres:770@localhost:5432/postgres")
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("✅ Соединение с БД успешно!", list(result))
except Exception as e:
    print("❌ Ошибка подключения:", e)


