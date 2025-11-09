import httpx

async def fetchi(time):
    print(f"Fetching data for {time} seconds...")
    await asyncio.sleep(time)
    print("The real Data!")
    return f"Fetched data after {time} seconds"

async def main():
    task = await asyncio.create_task(fetchi(10))
    print(task)

asyncio.run(main())