"""Doc."""
from telegram import Update
from telegram.ext import ContextTypes
import datetime
from spy import log


async def hi_command(update: Update, context:
                     ContextTypes.DEFAULT_TYPE) -> None:
    """Doc."""
    log(update, context)
    await update.message.reply_text(f'Hi, {update.effective_user.first_name}!')


async def help_command(update: Update, context:
                       ContextTypes.DEFAULT_TYPE) -> None:
    """Doc."""
    log(update, context)
    await update.message.reply_text('/hi\n/time\n/help\nЧтобы '
                                    'посчитать сумму: "/sum number number"')


async def time_command(update: Update, context:
                       ContextTypes.DEFAULT_TYPE) -> None:
    """Doc."""
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def sum_command(update: Update, context:
                      ContextTypes.DEFAULT_TYPE) -> None:
    """Doc."""
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()  # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')
