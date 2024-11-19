from flask import Flask, jsonify, request

app = Flask(__name__)

# Global variable containing tasks
todos = [
    {"label": "My first task", "done": False}
]

@app.route('/todos', methods=['GET'])
def get_todos():
    # Return the JSON representation of the global todos variable
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    # Parse the incoming JSON data
    new_task = request.get_json()
    if new_task:  # Ensure the request body contains valid data
        todos.append(new_task)  # Add the new task to the global todos list
    return jsonify(todos)  # Return the updated list

# Route to delete a todo item at a specific position
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    # Remove the item at the specified position in the todos list
    todos.pop(position)
    
    # Return the updated todos list as a JSON response
    json_text = jsonify(todos)
    return json_text
# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)