from fastapi import FastAPI
import asyncio

app = FastAPI()


@app.get('/wait')
async def wait_example():
    await asyncio.sleep(2)
    return {"this message will delsyed by 2 second"}


async def fake_db_call():
    await asyncio.sleep(1)
    return {"data": "User data from DB"}

@app.get("/user")
async def get_user():
    result = await fake_db_call()
    return result

@app.get("/parallel")
async def run_parallel():
    async def task(n):
        await asyncio.sleep(n)
        return f"Task {n} done"

    
    results = await asyncio.gather(
        task(1),
        task(2),
        task(3)
    )
    return {"results": results}
