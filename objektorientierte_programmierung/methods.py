import pandas as pd

# Load the CSV file into a DataFrame
def load_todos():
    try:
        df = pd.read_csv('data/todos.csv')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['ID', 'Name', 'Completed'])
    return df

# Save the DataFrame to a CSV file
def save_todos(df):
    df.to_csv('data/todos.csv', index=False)

# Get all todos
def get_all_todos():
    return load_todos()

# Add a new todo
def add_todo(name):
    df = load_todos()
    new_id = df['ID'].max() + 1 if not df.empty else 1
    new_todo = pd.DataFrame([{'ID': new_id, 'Name': name, 'Completed': False}])
    df = pd.concat([df, new_todo], ignore_index=True)
    save_todos(df)

# Delete a todo by ID
def delete_todo(todo_id):
    df = load_todos()
    df = df[df['ID'] != todo_id]
    save_todos(df)

# Update a todo by ID
def update_todo(todo_id, name=None, completed=None):
    df = load_todos()
    index = df[df['ID'] == todo_id].index
    if not index.empty:
        if name is not None:
            df.at[index[0], 'Name'] = name
        if completed is not None:
            df.at[index[0], 'Completed'] = completed
        save_todos(df)
