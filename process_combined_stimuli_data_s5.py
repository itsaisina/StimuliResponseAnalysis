import json
import os
import sys


def update_stimuli_values_final(combine_stimuli, mikhail_data):
    for slide_number, stimuli_list in combine_stimuli.items():
        slide_key = f"Slide {slide_number}"
        if slide_key in mikhail_data:
            if "не в силах" in stimuli_list:
                keys_to_sum = ["не_1", "в_3", "силах_1"]
                sum_value = sum(mikhail_data[slide_key].get(key, 0) for key in keys_to_sum)
                mikhail_data[slide_key]["не в силах"] = sum_value
                for key in keys_to_sum:
                    del mikhail_data[slide_key][key]

            if "в моей" in stimuli_list:
                keys_to_sum = ["в_1", "моей_1"]
                sum_value = sum(mikhail_data[slide_key].get(key, 0) for key in keys_to_sum)
                mikhail_data[slide_key]["в моей_1"] = sum_value
                for key in keys_to_sum:
                    del mikhail_data[slide_key][key]

                keys_to_sum = ["в_2", "моей_2"]
                sum_value = sum(mikhail_data[slide_key].get(key, 0) for key in keys_to_sum)
                mikhail_data[slide_key]["в моей_2"] = sum_value
                for key in keys_to_sum:
                    del mikhail_data[slide_key][key]

            if slide_key == 'Slide 17':
                temp_values = {}
                for stimulus_index, combined_stimulus in enumerate(stimuli_list):
                    if combined_stimulus == "не в силах":
                        continue
                    words = combined_stimulus.split()
                    first_word, second_word = words[0], words[1]
                    for key, value in mikhail_data[slide_key].items():
                        if first_word in key:
                            first_key_index = key.split('_')[-1]
                            second_key = f"{second_word}_{first_key_index}"
                            if second_key in mikhail_data[slide_key]:
                                sum_value = value + mikhail_data[slide_key][second_key]
                                new_key = f"{combined_stimulus}_{first_key_index}"
                                temp_values[new_key] = sum_value

                for new_key, value in temp_values.items():
                    mikhail_data[slide_key][new_key] = value

            else:
                for combined_stimulus in stimuli_list:
                    if combined_stimulus == "не в силах":
                        continue
                    words = combined_stimulus.split()
                    first = words[0]
                    ls = list(mikhail_data[slide_key].keys())
                    sum_value = 0.0
                    for key in ls:
                        if key == ls[-1]:
                            break
                        key_temp = key.split('_')[0]
                        if first == key_temp:
                            sum_value += mikhail_data[slide_key][key]
                            second = words[1]
                            index = ls.index(key)
                            key_2 = ls[index + 1]
                            if second == key_2.split("_")[0]:
                                sum_value += mikhail_data[slide_key][key_2]
                                mikhail_data[slide_key][combined_stimulus] = sum_value
                                del mikhail_data[slide_key][key]
                                del mikhail_data[slide_key][key_2]

    return mikhail_data


def combine_stimuli_data(path, result_path, combine_stimuli):
    os.makedirs(result_path, exist_ok=True)

    for filename in os.listdir(path):
        if not filename.endswith('.json'):
            continue
        file_path = os.path.join(path, filename)
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        updated_data = update_stimuli_values_final(combine_stimuli, data.copy())
        res_path = os.path.join(result_path, filename)
        with open(res_path, 'w', encoding='utf-8') as new_file:
            json.dump(updated_data, new_file, ensure_ascii=False, indent=4)


def main():
    if len(sys.argv) < 3:
        print("Usage: python process_combined_stimuli_data_s5.py <source_folder> <result_folder>")
        sys.exit(1)

    source_folder = sys.argv[1]
    result_folder = sys.argv[2]

    combine_stimuli = {
        2: ["не могу", "не говорить", "на самом", "или бсд", "я просто", "не понимаю"],
        3: ["с РПП", "в истерику", "не в силах"],
        8: ["из собственных"],
        9: ["надо мной", "в моей", "как клубок", "в моей", "что я", "Мой замок", "моя замкнутость", "и недоверие"],
        10: ["в голове", "их беспорядочность", "и недоверие"],
        12: ["— детям"],
        13: ["от оков", "к мыслям", "о смерти", "от настигающих"],
        16: ["с одиночеством", "и непониманием", "их любовь", "и доброты", "В сенсорном", "и тактильны"],
        17: ["от этого", "от этого"],
        18: ["у детей", "с пограничным", "«в больничку»", "с ПРЛ", "и поддержка", "и тепло"],
    }

    combine_stimuli_data(source_folder, result_folder, combine_stimuli)


if __name__ == "__main__":
    main()
