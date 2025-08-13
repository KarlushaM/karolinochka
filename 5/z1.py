import asyncio

async def fetch_url(url):
    await asyncio.sleep(1)
    return f"Data from {url}"

async def main():
    urls = [
        "Запрос 1",
        "Запрос 2",
        "Запрос 3",
        "Запрос 4",
        "Запрос 5",
    ]
 
    tasks = [fetch_url(url) for url in urls]
    results = await asyncio.gather(*tasks)
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
