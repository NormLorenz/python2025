import asyncio
from asyncio import Future
from datetime import datetime
import requests
from requests import Response


async def check_status(url: str) -> dict[str, int | str]:

    start_time = datetime.now()
    response: Response = await asyncio.to_thread(requests.get, url, None)
    end_time = datetime.now()

    return {
        'url': url,
        'status': response.status_code,
        'start_time': f'{start_time:%H:%M:%S}',
        'end_time': f'{end_time:%H:%M:%S}'
    }


async def main():
    tasks: Future[tuple] = asyncio.gather(
        check_status('https://www.example.com'),
        check_status('https://www.python.org'),
        check_status('https://www.github.com'),
        check_status('https:www.nonexistentwebsite.com'),
        return_exceptions=True
    )

    results: list[dict] = await tasks
    print('Results:')
    for result in results:
        print(result)


if __name__ == '__main__':
    asyncio.run(main=main())
