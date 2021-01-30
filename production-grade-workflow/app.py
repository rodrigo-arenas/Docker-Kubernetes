from fastapi import FastAPI
import aioredis

app = FastAPI(title="Hello World API", description="Dummy app for Docker exercises", version="1.0")

redis = None


@app.on_event('startup')
async def connect_redis():
    global redis
    redis = await aioredis.create_redis_pool(('redis-server', 6379))
    await redis.set('visits', 0)


@app.on_event('shutdown')
async def disconnect_redis():
    global redis
    redis.close()
    await redis.wait_closed()


@app.get('/', tags=["Home"])
async def greeting():
    global redis
    current_visits = int(await redis.get('visits', encoding='utf-8'))
    current_visits += 1
    redis.set('visits', current_visits)
    return {"message": f'Hi there!, you got {current_visits} visits so far'}

