import asyncio

async def set_async_timer(seconds, callback):
    await asyncio.sleep(seconds)
    callback()

async def main():
    print("Таймер сработал!")
    def on_timer_end():
        print("Таймер сработал!")
    await set_async_timer(3, on_timer_end)

if __name__ == "__main__":
    asyncio.run(main())