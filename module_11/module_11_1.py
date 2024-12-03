import requests
import pandas as pd


github_token = "Токен авторизации GitHub"  

reposit_name = "Репозиторий на GitHub"
url = f"https://api.github.com/repos/{reposit_name}"
headers = {
    "Authorization": f"token {github_token}",
    "Accept": "application/vnd.github+json"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    reposit_data = response.json()
    reposit_df = pd.DataFrame([reposit_data])
    print(reposit_df)

except requests.exceptions.RequestException as e:
    print(f"Произошла ошибка: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")

# выполняем запрос к API сайта, проверяем наличие ошибок, преобразуем ответ с сайта в формат JSON, далее в Data Frame и выводим. 