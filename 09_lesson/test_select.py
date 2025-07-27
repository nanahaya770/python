from sqlalchemy import create_engine, text


def test_insert():
    engine = create_engine("postgresql://postgres:770@localhost:5432/postgres")
    with engine.connect() as connection:
        sql = "INSERT INTO subject (subject_id, subject_title" \
            ") VALUES (21, 'Geometry')"  # строка с sql запросом
        connection.execute(text(sql))  # выполнение срокового sql запроса к БД

        sql = "select * from subject where subject_id = 21"
        result = connection.execute(text(sql))

        subject_id, subject_title = list(result)[0]
        assert subject_id == 21
        assert subject_title == 'Geometry'

        sql = "DELETE FROM subject WHERE subject_id = 21"
        connection.execute(text(sql))


def test_update():
    # подключение к БД
    engine = create_engine("postgresql://postgres:770@localhost:5432/postgres")
    with engine.connect() as connection:
        # update изменить
        sql = "UPDATE subject SET subject_title='Physics' WHERE subject_id=5"
        connection.execute(text(sql))

        # select
        sql = "select * from subject where subject_id = 5"
        result = connection.execute(text(sql))

        # assert
        subject_id, subject_title = list(result)[0]
        assert subject_id == 5
        assert subject_title == 'Physics'

        # update вернуть обратно
        sql = "UPDATE subject SET subject_title='Chess' WHERE subject_id=5"
        connection.execute(text(sql))


def test_delete():
    # delete существующую строку
    engine = create_engine("postgresql://postgres:770@localhost:5432/postgres")
    with engine.connect() as connection:
        # update изменить
        sql = "DELETE FROM subject WHERE subject_id = 1"
        connection.execute(text(sql))

        # select
        sql = "select * from subject where subject_id = 1"
        result = connection.execute(text(sql))

        # assert
        assert list(result) == []

        # insert вернуть удаленную строку
        sql = "INSERT INTO subject (" \
            "subject_id, subject_title) VALUES (1, 'English')"
        connection.execute(text(sql))
