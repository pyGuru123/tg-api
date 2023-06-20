# TG-API [![Telegram Badge](https://img.shields.io/badge/-Telegram-0088cc?style=flat-square&logo=Telegram&logoColor=white)](https://t.me/itspyguru)

Few APIs for [@pyguru](https://t.me/pyguru) telegram channel.

Base Endpoint : https://tg-api-pyguru123.vercel.app/ \
Documentation : https://tg-api-pyguru123.vercel.app/docs

## Contributions are welcome

Create a new issue about what you want to implement. The API is written in FastAPI and python so a basic knowledge of both is expected. Also we directly integrate this api with our telegram bot, so make sure your feature should be compatible with our bot. Contact admins for the same.

#### How to setup the project

* Create a fork and a new branch
* Clone the repository
* Create virtual environment ```python -m venv venv```
* install requirements.txt file ```pip install -r requirements.txt```
* Run main.py ```python main.py```
* Open the localhost port 8000 in browser ```http://localhost:8000/docs```

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