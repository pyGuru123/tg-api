# TG-API [![Telegram Badge](https://img.shields.io/badge/-Telegram-0088cc?style=flat-square&logo=Telegram&logoColor=white)](https://t.me/itspyguru)

Few APIs for [@pyguru](https://t.me/pyguru) telegram channel.

## We are participating in Hacktoberfest 2023.
Looking for a way to contribute to this project. Its kinda easy. We just expect an api endpoint which can be helpful for our telegram bot. You can discuss your ideas in our group here [@pyguru](https://t.me/pyguru)

## API Endpoints

Base Endpoint : [https://tgapi-7d0b0583d985.herokuapp.com](https://tgapi-7d0b0583d985.herokuapp.com) \
Documentation : [https://tgapi-7d0b0583d985.herokuapp.com/docs](https://tgapi-7d0b0583d985.herokuapp.com/docs)

## Basic Example

Here's a simple python requests based example of our ```/gpt``` endpoint

```python
import requests

url = "https://tgapi-7d0b0583d985.herokuapp.com/api/v1/llmodels/gpt"
payload = {
	"prompt": "hello. How are you ?"
}
response = requests.post(url, json=payload)
print(response.json())
```

## Contributions are welcome

Create a new issue about what you want to implement. The API is written in FastAPI and python so a basic knowledge of both is expected. Also we directly integrate this api with our telegram bot, so make sure your feature should be compatible with our bot. Contact admins for the same.

#### How to setup the project

* Create a fork and a new branch
* Clone the repository
* Create virtual environment ```python -m venv venv```
* install requirements.txt file ```pip install -r requirements.txt```
* Run main.py ```python main.py```
* Open the localhost port 8000 in browser ```http://localhost:8000/docs```

### Heroku Deployment

* Procfile   -> web: uvicorn app.api:app --host=0.0.0.0 --port=$PORT
* heroku-cli -> heroku ps:scale web=1 --app tgapi

#### How to contribute

* Once your issue gets a thumbsup 👍, setup the project
* Now go to app folder & create a new folder as per your issue
* Write python code for your issue in ```main.py``` in your newly created folder
* Create a router with endpoints in ```router.py```, refer to other folder codes for help
* If your api endpoint is expecting a body, write the base model for it in ```model.py```
* Finally include your newly created router in ```api.py```
* Test your code on localhost for all possible cases, do add exception handling
* Push the code and create a PR.

#

<div align="center">

### Show some ❤️ by starring this repository!

</div>
