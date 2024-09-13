import asyncio
from fastapi import APIRouter
from time import monotonic

from schemas import TestResponse

router = APIRouter()
lock = asyncio.Lock()
task = asyncio.Queue()

async def work() -> None:
    await asyncio.sleep(3)

@router.get("/test", response_model=TestResponse)
async def handler() -> TestResponse:
    ts1 = monotonic()
    async with lock:
        await work()
    ts2 = monotonic()
    result = ts2 - ts1
    return TestResponse(elapsed=result)
