import os
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Путь к папкам с данными
train_data_path = "C:/Users/dasha/Desktop/stagirovka/aclImdb/train"
test_data_path = "C:/Users/dasha/Desktop/stagirovka/aclImdb/test"

# Функция для загрузки данных из папки
def load_data(folder_path, label):
    reviews = []
    for filename in os.listdir(folder_path):
        with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
            reviews.append(f.read())
    return pd.DataFrame({'review': reviews, 'label': label})

# Загрузка обучающих данных (игнорируем папку unsup)
train_pos_reviews = load_data(os.path.join(train_data_path, 'pos'), 1)  # Положительные отзывы
train_neg_reviews = load_data(os.path.join(train_data_path, 'neg'), 0)  # Отрицательные отзывы

# Загрузка тестовых данных
test_pos_reviews = load_data(os.path.join(test_data_path, 'pos'), 1)  # Положительные отзывы
test_neg_reviews = load_data(os.path.join(test_data_path, 'neg'), 0)  # Отрицательные отзывы

# Объединение данных
train_reviews_df = pd.concat([train_pos_reviews, train_neg_reviews])
test_reviews_df = pd.concat([test_pos_reviews, test_neg_reviews])

# Преобразование текста в векторную форму
vectorizer = TfidfVectorizer(max_features=5000)
X_train = vectorizer.fit_transform(train_reviews_df['review'])
X_test = vectorizer.transform(test_reviews_df['review'])

y_train = train_reviews_df['label']
y_test = test_reviews_df['label']

# Обучение модели
model = MultinomialNB()
model.fit(X_train, y_train)

# Оценка модели
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)