from app.db.db import engine, SessionLocal
from app.db import models
from app.db import crud

def init_db():
    print("Пересоздание таблиц...")
    models.Base.metadata.drop_all(bind=engine)
    models.Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        categories = ["Программирование", "Художественная литература"]
        
        for cat_title in categories:
            existing = db.query(models.Category).filter(models.Category.title == cat_title).first()
            if not existing:
                crud.create_category(db, cat_title)
                print(f"Создана категория: {cat_title}")
        
        programming = db.query(models.Category).filter(models.Category.title == "Программирование").first()
        fiction = db.query(models.Category).filter(models.Category.title == "Художественная литература").first()
        
        books_programming = [
            {"title": "Python с нуля", "description": "Полное руководство по Python", "price": 1500, "url": ""},
            {"title": "Алгоритмы", "description": "Классический учебник по алгоритмам", "price": 2000, "url": ""},
            {"title": "SQL для начинающих", "description": "Основы работы с базами данных", "price": 1200, "url": ""},
        ]
        
        for book in books_programming:
            existing = db.query(models.Book).filter(
                models.Book.title == book["title"],
                models.Book.category_id == programming.id
            ).first()
            if not existing:
                crud.create_book(db, **book, category_id=programming.id)
                print(f"Добавлена книга: {book['title']} (Программирование)")
        
        books_fiction = [
            {"title": "Война и мир", "description": "Роман-эпопея Льва Толстого", "price": 800, "url": ""},
            {"title": "Преступление и наказание", "description": "Роман Достоевского", "price": 700, "url": ""},
            {"title": "Мастер и Маргарита", "description": "Роман Булгакова", "price": 900, "url": ""},
        ]
        
        for book in books_fiction:
            existing = db.query(models.Book).filter(
                models.Book.title == book["title"],
                models.Book.category_id == fiction.id
            ).first()
            if not existing:
                crud.create_book(db, **book, category_id=fiction.id)
                print(f"Добавлена книга: {book['title']} (Художественная литература)")
        
        print("\nДемонстрация: удаляем категорию 'Художественная литература'")
        crud.delete_category(db, fiction.id)
        print("Категория удалена! Книги остались, но без категории.")
        
        books_without_cat = crud.get_books_without_category(db)
        print(f"\nКниги без категории ({len(books_without_cat)} шт.):")
        for book in books_without_cat:
            print(f"  - {book.title} (цена: {book.price} ₽)")
        
        print("\nБаза данных успешно инициализирована!")
        
    except Exception as e:
        print(f"Ошибка: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_db()