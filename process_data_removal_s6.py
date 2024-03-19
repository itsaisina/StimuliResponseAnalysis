import json
import os


def process_data_removal(source_path, result_path, removal_keys):
    os.makedirs(result_path, exist_ok=True)
    for filename in os.listdir(source_path):
        file_path = os.path.join(source_path, filename)
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        for slide_key, words_to_remove in removal_keys.items():
            for word in words_to_remove:
                if word in data[slide_key]:
                    del data[slide_key][word]

        result_file_path = os.path.join(result_path, filename)
        with open(result_file_path, 'w', encoding='utf-8') as new_file:
            json.dump(data, new_file, ensure_ascii=False, indent=4)


def main():
    file_type_input = int(input('Введите 1 (группа нормы) или 2 (контрольная группа): '))
    if file_type_input == 1:
        source_path = "/path/to/final_results_группа_нормы"
        result_path = "/path/to/finally_final_results_группа_нормы"
    elif file_type_input == 2:
        source_path = "/path/to/final_results_контрольная_группа"
        result_path = "/path/to/finally_final_results_контрольная_группа"
    else:
        print("Неверный ввод. Завершение программы.")
        return

    removal_keys = {
        "Slide 17": ["от_1", "этого_1", "от_2", "этого_2"]
    }

    process_data_removal(source_path, result_path, removal_keys)


if __name__ == "__main__":
    main()
