from flask import Flask, request, jsonify
from collections import defaultdict

app = Flask(__name__)

def reformat_array(input_array):

# Menggunakan defaultdict untuk membuat otomasi nested dictionary
    result = defaultdict(lambda: defaultdict(list))

# iterasi setiap item dalam array
    for item in input_array:
        # mengelompokkan 
        category = item.get('category')
        subcategory = item.get('subcategory')
        # memasukkan item ke dalam nested dictionary
        result[category][subcategory].append(item)

# konversi nested dictionary menjadi array
    output = [
        [
            items
            for subcategory, items in subcategories.items()
        ]
        for category, subcategories in result.items()
    ]

    return output

@app.route('/reformat', methods=['POST'])
def reformat():
    data = request.get_json()

# validasi
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        return jsonify({'error': 'Invalid input format'}), 400


# panggil fungsi reformat array
    result = reformat_array(data)

    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)