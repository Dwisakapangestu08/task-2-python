from flask import Flask, request, jsonify
from collections import defaultdict

app = Flask(__name__)

def reformat_array(input_array):
    # Menggunakan defaultdict untuk otomatisasi nested dictionary
    result = defaultdict(lambda: defaultdict(list))
    
    # Iterasi setiap item dalam input_array
    for item in input_array:
        # Mengelompokkan berdasarkan kategori dan subkategori
        category = item.get("category")
        sub_category = item.get("sub_category")
        
        # Menambahkan item yang hanya berisi id dan name ke dalam hasil
        result[category][sub_category].append({
            "id": item.get("id"),
            "name": item.get("name")
        })
    
    # Mengubah defaultdict menjadi dictionary biasa untuk JSON output
    return {category: dict(sub_categories) for category, sub_categories in result.items()}

@app.route('/reformat', methods=['POST'])
def reformat():
    data = request.get_json()
    
    # Validasi apakah input berupa array dan berisi JSON
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        return jsonify({"error": "Input harus berupa array JSON"}), 400
    
    # Panggil fungsi reformat_array untuk memproses data
    result = reformat_array(data)
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
