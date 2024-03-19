import json
import os
from collections import defaultdict


def calculate_average_delay(input_path, output_file):
    values_sum = defaultdict(lambda: defaultdict(lambda: [0, 0]))

    for filename in os.listdir(input_path):
        if filename.endswith(".json"):
            file_path = os.path.join(input_path, filename)
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                for slide, values in data.items():
                    for key, value in values.items():
                        values_sum[slide][key][0] += value
                        values_sum[slide][key][1] += 1

    average_values = {
        slide: {key: sum_count[0] / sum_count[1] for key, sum_count in values.items()}
        for slide, values in values_sum.items()
    }

    with open(output_file, 'w', encoding='utf-8') as result_file:
        json.dump(average_values, result_file, ensure_ascii=False, indent=4)


def main():
    file_type_input = int(input('Введите 1 (группа нормы) или 2 (контрольная группа): '))
    if file_type_input == 1:
        input_path = "finally_final_results_группа_нормы"
        output_file = "summary_results_normal.json"
    elif file_type_input == 2:
        input_path = "finally_final_results_контрольная_группа"
        output_file = "summary_results_control.json"
    else:
        print("Неверный ввод. Завершение программы.")
        return

    calculate_average_delay(input_path, output_file)


if __name__ == "__main__":
    main()
