import asyncio as asc

async def goSlowly():
  await asc.sleep(3)
  return 15


async def asynchronous():

  print("Start")

  task = asc.create_task(goSlowly())

  result = await task
  print(result)

  print("End")

asc.run(asynchronous())
