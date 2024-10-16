import os
import joblib
from django.shortcuts import render
from .forms import ReviewForm

# Получаем абсолютный путь к папке проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath("C:/Users/dasha/Desktop/stagirovka/movie_reviews")))

# Пути к сохранённой модели и векторизатору
model_path = os.path.join(BASE_DIR, 'reviews', 'models', 'model.pkl')
vectorizer_path = os.path.join(BASE_DIR, 'reviews', 'models', 'vectorizer.pkl')

# Загрузка модели и векторизатора
model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)


# Функция для предсказания настроения отзыва
def predict_sentiment(review):
    review_vec = vectorizer.transform([review])  # Преобразуем текст отзыва в вектор
    sentiment = model.predict(review_vec)[0]  # Предсказываем
    return "positive" if sentiment == 1 else "negative"


# Функция для предсказания рейтинга
def predict_rating(review):
    # Простое правило: высокий рейтинг для положительных отзывов и низкий для отрицательных
    return 8 if predict_sentiment(review) == "positive" else 3


# Представление для обработки формы отзыва
def review_view(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_text = form.cleaned_data['review']
            sentiment = predict_sentiment(review_text)
            rating = predict_rating(review_text)

            # Отображаем результат
            return render(request, 'result.html', {'sentiment': sentiment, 'rating': rating})
    else:
        form = ReviewForm()

    return render(request, 'review_form.html', {'form': form})

