import os
import logging
from flask import Flask, jsonify, make_response, request
from datetime import datetime

# Создаем приложение Flask
app = Flask(__name__)

# Настраиваем логирование
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

# Читаем токен из переменной окружения или задаем значение по умолчанию
API_TOKEN = os.getenv('API_TOKEN', 'default_token')

@app.route('/')
def get_time():
    try:
        # Проверяем наличие токена в заголовке Authorization
        auth_header = request.headers.get('Authorization')
        if not auth_header or auth_header != f"Bearer {API_TOKEN}":
            logger.warning("Неверный или отсутствующий токен авторизации")
            raise ValueError("Unauthorized access")

        # Получаем текущее время
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logger.info("Запрос успешен, текущее время: %s", current_time)
        return jsonify({"status": 200, "time": current_time})
    except Exception as e:
        logger.error("Ошибка при обработке запроса: %s", str(e))
        response = jsonify({"status": 500, "error": "Internal Server Error"})
        response.status_code = 500
        return response

@app.errorhandler(404)
def not_found(error):
    response = jsonify({"status": 500, "error": "Internal Server Error"})
    response.status_code = 500
    return response

if __name__ == '__main__':
    # Читаем настройки из переменных окружения
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() in ('true', '1', 't')

    # Запускаем приложение
    app.run(host=host, port=port, debug=debug)

