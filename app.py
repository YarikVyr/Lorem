from flask import Flask, render_template, request
import lorem

app = Flask(__name__)

# Обрабатывает запросы GET (для отображения формы) и POST (для обработки данных формы)
@app.route('/', methods=['GET', 'POST'])
def index():
    lorem_paragraphs = []
    # Проверка, был ли отправлен POST-запрос
    if request.method == 'POST':
        try:
            # Получение количества абзацев из формы
            paragraphs = int(request.form.get('paragraphs', 1))
            # Генерация указанного количества случайных абзацев
            for _ in range(paragraphs):
                lorem_paragraphs.append(lorem.paragraph())
        except (ValueError, IndexError):
            # Обработка ошибок, если введено некорректное значение
            lorem_paragraphs = ["Ошибка: введите корректное число."]

    return render_template('index.html', lorem_text="\n\n".join(lorem_paragraphs))

if __name__ == '__main__':
    app.run(debug=True)
