# Тестовое задание для стажера ML

Задание выполнил Чуфистов Георгий

В данном архиве лежит блокнот с содержанием исследования 
и код микросервиса, написанного с помощью **FastAPI**.

Для того, чтобы запустить проект (если нет Docker):
1. Создайте виртуальное окружение 

* ```python3 -m venv venv```

2. Активируйте виртуальное окружение

*  ```source venv/bin/activate```

3. Скачайте все зависимости

* ```pip install -r app/requirements.txt```

4. Запустить проект из папки app

* ```uvicorn main:app --host 0.0.0.0 --port 8000```

Если на вашем компьютере установлен Docker и Docker Compose, то запустите приложение следующей командой

* ```docker compose up```

P.S. Модели, полученные в результате исследования, можно скачать по
[этой](#https://drive.google.com/uc?export=download&id=1TLAEffY1Zzn2mfeVcrPOqpBLxtHzjKOq)
и [этой](https://drive.google.com/uc?export=download&id=1Gnm3yML2fdTCLY0FyXYrIPTKvYU9vjn9) ссылке.
Их нужно поместить в папку model внутри папки app.

[Ссылка на GitHub](#https://github.com/georgechufff/gazprombank_test_cv.git)
