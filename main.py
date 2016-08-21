from app import app, db, bot, config

from DB.models import *

from webserver import *

from bot_events import *

if __name__ == '__main__':

    bot.remove_webhook()
    bot.set_webhook(url=config.WEBHOOK_URL_BASE + config.WEBHOOK_URL_PATH,
                    certificate=open(config.WEBHOOK_SSL_CERT, 'r'))

    app.run(host=config.WEBHOOK_LISTEN,
            port=config.WEBHOOK_PORT,
            ssl_context=(config.WEBHOOK_SSL_CERT, config.WEBHOOK_SSL_PRIV),
            debug=False)