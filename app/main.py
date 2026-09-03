from app.db.db import SessionLocal
from app.db import crud

def main():
    db = SessionLocal()
    
    try:
        print("Книги по категориям:")
        
        categories = crud.get_categories(db)
        
        if not categories:
            print("Категории не найдены")
        else:
            for category in categories:
                print(f"\nКатегория: {category.title}")
                print("---------------------------------------------------")
                
                books = crud.get_books_by_category(db, category.id)
                if books:
                    for book in books:
                        print(f" • {book.title}")
                        print(f"   Описание: {book.description}")
                        print(f"   Цена: {book.price} ₽")
                        print()
                else:
                    print("  Книг в этой категории нет\n")
        
        print("Книги без категорий:")
        
        books_without = crud.get_books_without_category(db)
        if books_without:
            for book in books_without:
                print(f" • {book.title}")
                print(f"   Описание: {book.description}")
                print(f"   Цена: {book.price} ₽")
                print()
        else:
            print(" Нет книг без категории")
                
    finally:
        db.close()

if __name__ == "__main__":
    main()