import rest_api_t1_functions as raf
import json


def main():
        """
        with open("7_j_file_pokemon_csv.txt", "w") as f:
            for pokemon_s in raf.get_available_pokemons_list()[0:6]:
                ps = raf.get_pokemon_info(pokemon_s)
                raf_str = str(raf.show_pokemon_specific_info(ps))
                f.write(raf_str)
                f.write("\n")
        """

        """
        {'name': 'bulbasaur', 'id': 1, 'order': 1, 'weight': 69, 'base_experience': 64}
        {'name': 'ivysaur', 'id': 2, 'order': 2, 'weight': 130, 'base_experience': 142}
        {'name': 'venusaur', 'id': 3, 'order': 3, 'weight': 1000, 'base_experience': 236}
        {'name': 'charmander', 'id': 4, 'order': 5, 'weight': 85, 'base_experience': 62}
        {'name': 'charmeleon', 'id': 5, 'order': 6, 'weight': 190, 'base_experience': 142}
        {'name': 'charizard', 'id': 6, 'order': 7, 'weight': 905, 'base_experience': 240}
        """
        csv_raws = [[]]

        with open("7_j_file_pokemon_csv.txt", "w") as f:
            csv_first_raw = []
            pokemon_list = raf.get_available_pokemons_list()[0:6]
            print(len(pokemon_list))
            for pokemon_s in pokemon_list:
                ps_dict = raf.get_pokemon_info(pokemon_s)
                ps_dict_specific = raf.show_pokemon_specific_info(ps_dict)
                # {'name': 'bulbasaur', 'id': 1, 'order': 1, 'weight': 69, 'base_experience': 64}
                # [[name, id, order, weight, base_experience],
                #  [bulbasaur, 1, 1, 69,64]
                # for k in ps_dict_specific.keys():
                #     csv_first_raw.append(k)
                for i in range(len(pokemon_list)):
                    for v in ps_dict_specific.values():
                        csv_raws[i].append(v)
            # f.write(raf_str)
            # f.write("\n")

        print(csv_raws)


if __name__ == '__main__':
    main()

