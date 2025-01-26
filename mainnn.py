from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database location
LOCATION = 'C:\\Users\\dakku\\Downloads'

def get_best_plans(data_usage, plan_duration):
    # Connect to the database
    conn = sqlite3.connect(LOCATION)
    cursor = conn.cursor()

    # Query to fetch plans based on user input
    query = """
    SELECT * FROM plans
    WHERE data_limit >= ? AND duration = ?
    ORDER BY price ASC
    """
    cursor.execute(query, (data_usage, plan_duration))
    plans = cursor.fetchall()
    
    conn.close()
    
    # Convert the plans to a list of dictionaries for JSON response
    plan_list = []
    for plan in plans:
        plan_dict = {
            'id': plan[0],  # Assuming the first column is the ID
            'name': plan[1],  # Assuming the second column is the name
            'data_limit': plan[2],  # Assuming the third column is the data limit
            'duration': plan[3],  # Assuming the fourth column is the duration
            'price': plan[4]  # Assuming the fifth column is the price
        }
        plan_list.append(plan_dict)

    return plan_list

@app.route('/api/best_plans', methods=['GET'])
def api_best_plans():
    # Get parameters from the query string
    data_usage = request.args.get('data_usage', type=int)
    plan_duration = request.args.get('plan_duration', type=str)

    if data_usage is None or plan_duration is None:
        return jsonify({'error': 'Missing data_usage or plan_duration parameter'}), 400

    best_plans = get_best_plans(data_usage, plan_duration)
    return jsonify(best_plans)

if __name__ == '__main__':
    app.run(debug=True)
    from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database location
LOCATION = 'C:\\Users\\dakku\\Desktop'  # Update this with your actual database path

def get_best_plans(data_usage, plan_duration):
    # Connect to the database
    conn = sqlite3.connect(LOCATION)
    cursor = conn.cursor()

    # Query to fetch plans based on user input
    query = """
    SELECT * FROM plans
    WHERE data_limit >= ? AND duration = ?
    ORDER BY price ASC
    """
    cursor.execute(query, (data_usage, plan_duration))
    plans = cursor.fetchall()
    
    conn.close()
    
    # Convert the plans to a list of dictionaries for JSON response
    plan_list = []
    for plan in plans:
        plan_dict = {
            'id': plan[0],  # Assuming the first column is the ID
            'name': plan[1],  # Assuming the second column is the name
            'data_limit': plan[2],  # Assuming the third column is the data limit
            'duration': plan[3],  # Assuming the fourth column is the duration
            'price': plan[4]  # Assuming the fifth column is the price
        }
        plan_list.append(plan_dict)

    return plan_list

@app.route('/api/best_plans', methods=['GET'])
def api_best_plans():
    # Get parameters from the query string
    data_usage = request.args.get('data_usage', type=int)
    plan_duration = request.args.get('plan_duration', type=str)

    if data_usage is None or plan_duration is None:
        return jsonify({'error': 'Missing data_usage or plan_duration parameter'}), 400

    best_plans = get_best_plans(data_usage, plan_duration)
    return jsonify(best_plans)

if __name__ == '__main__':
    app.run(debug=True)