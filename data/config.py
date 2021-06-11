from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

data = {"date": env.str("date"),
        "api_key": env.str("api_key"),
        "main_admin_id": env.int("main_admin_id"),
        "who_need_notify": env.list("who_need_notify"),
        "chat_link": env.str("chat_link"),
        "bot_github_pages": env.str("bot_github_pages")}

