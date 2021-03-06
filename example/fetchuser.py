import asyncio

from enkapy import Enka

client = Enka()


async def main():
    await client.load_lang()
    user = await client.fetch_user(104267816)
    print(f"Nickname: {user.player.nickname}")
    print(f"Level: {user.player.level}")
    for character in user.characters:
        print(f'Name: {character.name}')
        print(f'Weapon: {character.weapon.nameText}')
        print('Artifacts:')
        for artifact in character.artifacts:
            print(f'\t{artifact.setNameText} {artifact.nameText}:')
            print(f'\t{artifact.main_stat.prop}:{artifact.main_stat.value}')
            for sub_stats in artifact.sub_stats:
                print(f'\t\t{sub_stats.prop}:{sub_stats.value}')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
