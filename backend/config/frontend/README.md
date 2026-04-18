# Book AI Platform

## Features
- Scrapes book data
- Stores in database
- AI-based question answering
- Book summary generation
- Recommendation system

## APIs
- GET /api/books/
- GET /api/scrape/
- POST /api/ask/
- GET /api/summary/<id>/
- GET /api/recommend/<id>/

## How to run
pip install -r requirements.txt
python manage.py runserver

cd frontend
npm install
npm start