import asyncio
from asyncio import Future
from datetime import datetime


async def fetch_data(input_data: int, *, delay: int) -> dict:
    """Simulates fetching data asynchronously, returns timing info."""
    print(f'Fetching Data for input {input_data} ...')

    # Simulate a network call or long computation
    start_time = datetime.now()
    await asyncio.sleep(delay)
    end_time = datetime.now()

    print(f'Data Retrieved for input {input_data}.')

    return {
        'input_data': input_data,
        'start_time': f'{start_time:%H:%M:%S}',
        'end_time': f'{end_time:%H:%M:%S}'
    }


async def main():
    """Runs multiple asynchronous fetch_data tasks and prints their results."""

    # tasks: list[Task] = [
    #     asyncio.create_task(fetch_data(1, delay=1)),
    #     asyncio.create_task(fetch_data(5, delay=5)),
    # ]

    # Await all tasks concurrently
    # results = await asyncio.gather(*tasks)

    # for idx, data in enumerate(results, 1):
    #     print(f'Input Data {idx}: {data}')

    tasks: Future[tuple] = asyncio.gather(
        fetch_data(4, delay=4),
        fetch_data(6, delay=6),
        fetch_data(3, delay=3),
        return_exceptions=True  # Allows gathering to continue even if one fails
    )

    results: list[dict] = await tasks
    print('Results:')
    for idx, data in enumerate(results, 1):
        print(f'Input Data {idx}: {data}')


if __name__ == '__main__':
    asyncio.run(main=main())
