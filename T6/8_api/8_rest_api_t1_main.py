import rest_api_t1_functions as raf
import json, csv


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
        # ############### # ################ ################ ###############

        pokemon_list = raf.get_available_pokemons_list()
        pokemon_stats = []
        pokemon_stats_list_grouped = []
        pokemon_column_names = []
        is_keys = True

        for pokemon_s in pokemon_list:
            ps_dict = raf.get_pokemon_info(pokemon_s)
            ps_dict_specific = raf.show_pokemon_specific_info(ps_dict)
            for key, spec_data in ps_dict_specific.items():
                pokemon_column_names.append(key)
                pokemon_stats.append(spec_data)
            if is_keys:
                pokemon_stats_list = list(pokemon_column_names)
            else:
                pokemon_stats_list = list(pokemon_stats)
            is_keys = False
            pokemon_stats_list_grouped.append(pokemon_stats_list)
            pokemon_column_names.clear()
            pokemon_stats.clear()

        print(pokemon_stats_list_grouped)

        with open("7_j_pokemon.csv", "w", newline="") as fileobj:
            writer = csv.writer(fileobj)
            for line in pokemon_stats_list_grouped:
                writer.writerow(line)

        # ############### # ################ ################ ###############

        # ############### # ################ ################ ###############
        # csv_raws = []
        # with open("7_j_file_pokemon_csv.txt", "w") as f:
        #     csv_first_raw = []
        #     pokemon_list = raf.get_available_pokemons_list()[0:10]
        #     # print(len(pokemon_list))
        #     c_i = 0
        #     for pokemon_s in pokemon_list:
        #         ps_dict = raf.get_pokemon_info(pokemon_s)
        #         ps_dict_specific = raf.show_pokemon_specific_info(ps_dict)
        #         if c_i == 0:
        #             for k in ps_dict_specific:
        #                 f.write(str(k))
        #                 f.write(" ")
        #             f.write("\n")
        #         for v in ps_dict_specific.values():
        #             csv_raws.append(v)
        #         for item in csv_raws:
        #             f.write(str(item))
        #             f.write(" ")
        #         f.write("\n")
        #         csv_raws.clear()
        #         c_i = 1
        # ############### # ################ ################ ###############

        # csv_rows = []
        #
        # with open("7_j_file_pokemon_csv.txt", "r") as f:
        #     for line in f:
        #         csv_rows.append(line)
        #
        # print(csv_rows)
        #
        # # new_list = []
        # # with open("7_j_file_pokemon_csv.txt", "r") as f:
        # #     for item in f:
        # #         new_list.append(item)
        # #
        #
        # with open("7_j_pokemon.csv", "w", newline="") as fileobj:
        #     writer = csv.writer(fileobj)
        #     writer.writerow(csv_rows)

        # with open("7_j_file_pokemon_csv.txt", "r") as f:
        #     with open("7_j_pokemon.csv", "w", newline="") as fileobj:
        #         writer = csv.writer(fileobj)
        #         writer.writerow(f)

if __name__ == '__main__':
    main()

