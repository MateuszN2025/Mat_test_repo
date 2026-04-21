import requests, json

def get_available_pokemons_list () -> list:

    url_p = f"https://pokeapi.co/api/v2/pokemon"
    poke_info = requests.request(method='GET', url=url_p)
    poke_info_dict = poke_info.json()
    # print(type(poke_info_dict))
    ava_poke_list = poke_info_dict["results"]
    # print(type(ava_poke_list))
    ava_poke_list_less = []
    for item in ava_poke_list:
        item = item["name"]
        ava_poke_list_less.append(item)
    # ava_poke_json_str = json.dumps(ava_poke_list_less, indent=4) # dump: python obj -> str
    # return ava_poke_json_str
    return ava_poke_list_less

def get_pokemon_info(name: str) -> dict:
    pokemons_url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    poke_info = requests.request(method='GET', url=pokemons_url)
    poke_info_dict = poke_info.json()
    # print(type(poke_info_dict))
    # print(poke_info_dict)
    return poke_info_dict

def show_pokemon_specific_info(poke_dict: dict) -> dict:
    poke_spec_dict = {}
    poke_spec_dict["name"] = poke_dict["name"]
    poke_spec_dict["id"] = poke_dict["id"]
    poke_spec_dict["order"] = poke_dict["order"]
    poke_spec_dict["weight"] = poke_dict["weight"]
    poke_spec_dict["base_experience"] = poke_dict["base_experience"]

    # print("------------------------------------------")
    # print(f'name: {poke_dict["name"]}')
    # print(f'order: {poke_dict["order"]}')
    # print(f'weight: {poke_dict["weight"]}')
    # print(f'base_experience: {poke_dict["base_experience"]}')
    # print(f'id: {poke_dict["id"]}')

    return poke_spec_dict
