import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(5):
        print(f'Силач {name} поднял шар №{i+1}.')
        await asyncio.sleep(i+10/power)
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    print('Начали!')
    task_1 = asyncio.create_task(start_strongman('Федор', 7))
    task_2 = asyncio.create_task(start_strongman('Билл', 6))
    task_3 = asyncio.create_task(start_strongman('Свомпи', 4))
    await task_1
    await task_2
    await task_3


asyncio.run(start_tournament())