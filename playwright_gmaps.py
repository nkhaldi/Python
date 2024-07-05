"""Reservation on Google Maps using Playwright."""

import asyncio
import datetime

from playwright.async_api import async_playwright


async def book_table(number_of_guests: str, reserve_date: str, reserve_time: str):
    """Reserve a table on Google Maps."""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Открываем ссылку на бронирование
        await page.goto("https://www.google.com/maps/reserve/v/dine/c/5tHzSy086ZM?hl=en-US")

        # Ждем появления элементов для выбора количества людей, даты и времени
        await page.wait_for_selector('div[aria-label="Party"]')
        await page.wait_for_selector('div[aria-label="Date"]')
        await page.wait_for_selector('div[aria-label="Time"]')

        # Вводим количество людей
        await page.click('div[aria-label="Party"]')
        await page.click(f'text="{number_of_guests}"')

        # Вводим дату
        await page.click('div[aria-label="Date"]')
        await page.click(f'text="{reserve_date}"')

        # Вводим время
        await page.click('div[aria-label="Time"]')
        await page.click(f'text="{reserve_time}"')

        # Ждем появления кнопки "Continue"
        await page.wait_for_selector('button[aria-label="Continue"]')

        # Нажимаем кнопку "Continue"
        await page.click('button[aria-label="Continue"]')

        # Ждем появления элемента подтверждения бронирования (например, сообщение о подтверждении)
        await page.wait_for_selector("text=Your reservation is confirmed")

        print("Бронирование успешно выполнено!")

        await browser.close()


if __name__ == "__main__":
    number_of_guests = input("Введите количество гостей: ") or "2"

    today = datetime.date.today()
    reserve_date = input("Введите дату бронирования (гггг-мм-дд): ") or today.strftime("%Y-%m-%d")
    reserve_time = input("Введите время бронирования: ") or "7:00 PM"

    asyncio.run(book_table(number_of_guests, reserve_date, reserve_time))
