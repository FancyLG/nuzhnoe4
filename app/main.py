from app.db.db import SessionLocal
from app.db.crud import get_categories, get_books

def main():
    db = SessionLocal()
    
    try:
        categories = get_categories(db)
        print("\nКатегории книг")
        for category in categories:
            print(f"ID: {category.id}, Название: {category.title}")
        
        books = get_books(db)
        print("\nВсе книги")
        for book in books:
            print(f"ID: {book.id}, Название: {book.title}, Цена: {book.price} руб., Категория: {book.category.title if book.category else 'Без категории'}")
        
        print("\nКниги по категориям")
        for category in categories:
            print(f"\nКатегория: {category.title}")
            for book in category.books:
                print(f"  - {book.title} ({book.price} руб.)")
        
    finally:
        db.close()

if __name__ == "__main__":
    main()