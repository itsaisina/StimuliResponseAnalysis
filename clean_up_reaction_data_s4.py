import os
import json


def process_json_files(group_type, source_folder, target_folder):
    os.makedirs(target_folder, exist_ok=True)
    for filename in os.listdir(source_folder):
        if filename.endswith('.json'):
            file_path = os.path.join(source_folder, filename)
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)

            keys_to_delete = [
                ("Slide 2", ["я_2", "не_3", "моей_2", "на_2", "на_3"]),
                ("Slide 9", ["и_1", "как_1", "и_2", "и_3", "и_4", "и_6"]),
                ("Slide 10", ["и_1", "и_2", "в_1", "и_4"]),
                ("Slide 12", ["—_2"]),
                ("Slide 13", ["мира_1"]),
                ("Slide 16", ["и_1", "и_2", "и_3", "и_4", "и_5", "и_6"]),
                ("Slide 18", ["и_1", "и_2"])
            ]

            for slide, keys in keys_to_delete:
                for key in keys:
                    try:
                        del data[slide][key]
                    except KeyError:
                        pass

            new_file_path = os.path.join(target_folder, filename)
            with open(new_file_path, 'w', encoding='utf-8') as new_file:
                json.dump(data, new_file, ensure_ascii=False, indent=4)


file_type_input = int(input('Введите 1 (группа нормы) или 2 (контрольная группа): '))
if file_type_input == 1:
    process_json_files(
        group_type="группа_нормы",
        source_folder="/Users/alinaaisina/PythonProjects/Test/часть практики/results_группа_нормы",
        target_folder="/Users/alinaaisina/PythonProjects/Test/часть практики/almost_final_results_группа_нормы"
    )
elif file_type_input == 2:
    process_json_files(
        group_type="контрольная_группа",
        source_folder="/Users/alinaaisina/PythonProjects/Test/часть практики/results_контрольная_группа",
        target_folder="/Users/alinaaisina/PythonProjects/Test/часть практики/almost_final_results_контрольная_группа"
    )
