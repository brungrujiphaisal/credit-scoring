from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
def credit_scoring_model(Dict):
    name = Dict['name']
    age = Dict['age']
    income = Dict['income']
    credit_score = age * 20 + income / 10000
    return name, credit_score

@app.route('/api/credit-score', methods=['POST'])
def credit_score():
    # Get request data
    data = request.get_json()

    # Call credit scoring model function with the data
    name, score = credit_scoring_model(data)

    # Return the credit score as a JSON response
    return jsonify({'name': name,'credit_score': score, 'Credit score formula':'age * 20 + income / 10000'})

if __name__ == '__main__':
    app.run()
