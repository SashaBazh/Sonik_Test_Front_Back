import { Telegraf, Markup } from "telegraf"

const token = '7289282616:AAFDnBhtAm6zxoEjPKxM_SrWMfUecX3mqBk'
const webAppUrl = ''

const bot = new Telegraf(token)

bot.command('start', (ctx) => {
    ctx.reply(
    'привет',
    Markup.keyboard([
        Markup.button.webApp(
            'пока',
            webAppUrl
        )
    ])
    )
})

bot.launch()