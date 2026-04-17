import rest_api_t1_functions as raf
import json


def main():

    for pokemon_s in raf.get_available_pokemons_list()[0:6]:
        ps = raf.get_pokemon_info(pokemon_s)
        with open("7_j_file_pokemon_csv.txt", "a") as f:
            # raf_str = str(raf.show_pokemon_specific_info(ps))
            # f.write(raf_str)
            json.load(fp=f)


if __name__ == '__main__':
    main()

