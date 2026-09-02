from app.db.db import engine, SessionLocal
from app.db import models
from app.db.crud import create_category, create_book

def init_database():
    models.Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        category1 = create_category(db, "Художественная литература")
        category2 = create_category(db, "Научная литература")
        category3 = create_category(db, "Детская литература")
        
        print(f"Созданы категории: {category1.title}, {category2.title}, {category3.title}")
        
        books1 = [
            ("Война и мир", "Роман Льва Толстого", 599.99, category1.id),
            ("Преступление и наказание", "Роман Фёдора Достоевского", 499.99, category1.id),
            ("Анна Каренина", "Роман Льва Толстого", 549.99, category1.id),
        ]
        
        for title, desc, price, cat_id in books1:
            create_book(db, title, desc, price, cat_id)
        
        books2 = [
            ("Краткая история времени", "Стивен Хокинг", 789.99, category2.id),
            ("Эгоистичный ген", "Ричард Докинз", 659.99, category2.id),
            ("Структура научных революций", "Томас Кун", 699.99, category2.id),
        ]
        
        for title, desc, price, cat_id in books2:
            create_book(db, title, desc, price, cat_id)
        
        books3 = [
            ("Маленький принц", "Философская сказка Антуана де Сент-Экзюпери", 399.99, category3.id),
            ("Гарри Поттер и философский камень", "Джоан Роулинг", 899.99, category3.id),
        ]
        
        for title, desc, price, cat_id in books3:
            create_book(db, title, desc, price, cat_id)
        
        print("База данных успешно инициализирована!")
        
    finally:
        db.close()

if __name__ == "__main__":
    init_database()