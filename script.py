import json
import os
from datetime import datetime

def load_json(file_path):
    if not os.path.exists(file_path):
        print(f"⚠️ Файл {file_path} не найден. Создаю примерный JSON.")
        example_data = {
            "name": "json-tools",
            "version": "1.0",
            "description": "Utility scripts for working with JSON data in Python",
            "last_updated": datetime.now().isoformat(),
            "features": [
                "Read JSON files",
                "Pretty print JSON data",
                "Basic validation"
            ]
        }
        with open(file_path, 'w') as f:
            json.dump(example_data, f, indent=4)
        return example_data
    else:
        with open(file_path, 'r') as f:
            return json.load(f)

def pretty_print_json(data):
    print(json.dumps(data, indent=4, ensure_ascii=False))

def main():
    json_file = "example.json"
    data = load_json(json_file)
    print(f"📂 Загружен файл: {json_file}")
    print("✨ Содержимое JSON:")
    pretty_print_json(data)

if __name__ == "__main__":
    main()
# fix 5238
# optimize 9852
# optimize 1260
# fix 3105
# optimize 3626
# optimize 3399
# optimize 8621
# fix 1748
# refactor 1130
# fix 4969
# optimize 4485
# optimize 8670
# optimize 8384
# fix 7636
# refactor 5551
# refactor 5489
# refactor 9574
# refactor 9905
# fix 2277
# refactor 4769
# fix 2831
# optimize 1457
# fix 5119
# refactor 6762
# optimize 3429
# fix 7233
# optimize 4413
# fix 7530
# fix 6095
# fix 4810
# refactor 7943
# fix 6756
# fix 6085
# fix 7169
# optimize 6251
# fix 2975
# fix 7519
# optimize 8680
# optimize 9037
# fix 2798
# fix 7102
# optimize 9331
# optimize 3224
# refactor 9810
# fix 6670
# fix 7800
# fix 2071
