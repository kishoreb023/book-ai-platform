from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book

import requests
from bs4 import BeautifulSoup


# ----------------------------------------
# 🔹 SCRAPE BOOKS API
# ----------------------------------------
@api_view(['GET'])
def scrape_books(request):
    url = "http://books.toscrape.com/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").text

        rating_class = book.find("p", class_="star-rating")["class"][1]

        rating_map = {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5
        }

        rating = rating_map.get(rating_class, 0)

        Book.objects.create(
            title=title,
            author=None,
            description=price,
            rating=rating,
            url=url
        )

    return Response({"message": "Books scraped successfully"})


# ----------------------------------------
# 🔹 GET ALL BOOKS
# ----------------------------------------
@api_view(['GET'])
def get_books(request):
    books = Book.objects.all().values()

    return Response(list(books))


# ----------------------------------------
# 🔹 GET SINGLE BOOK (DETAIL PAGE)
# ----------------------------------------
@api_view(['GET'])
def get_book_detail(request, id):
    try:
        book = Book.objects.get(id=id)

        data = {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "description": book.description,
            "rating": book.rating,
            "url": book.url,
        }

        return Response(data)

    except Book.DoesNotExist:
        return Response({"error": "Book not found"})


# ----------------------------------------
# 🔹 ASK AI (DUMMY - SAFE)
# ----------------------------------------
@api_view(['POST'])
def ask_question(request):
    question = request.data.get("question")

    books = Book.objects.all()

    # simple logic: return top 3 books
    top_books = books.order_by("-rating")[:3]

    book_titles = [book.title for book in top_books]

    answer = f"Based on your question '{question}', you can check these books: {', '.join(book_titles)}"

    return Response({
        "answer": answer
    })


# ----------------------------------------
# 🔹 RECOMMEND BOOKS
# ----------------------------------------
@api_view(['GET'])
def recommend_books(request):
    books = Book.objects.all().order_by("-rating")[:5]

    data = list(books.values())

    return Response(data)