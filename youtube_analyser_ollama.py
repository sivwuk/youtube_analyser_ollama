import ollama

# used test connection to Ollama, Unprompt when needed 
# prompt = "What is YouTube?"

# stream = ollama.chat(
#     model='llama2',
#     messages=[{'role': 'user', 'content': prompt}],
#     stream=True
# )
# for chunk in stream:
#     print(chunk['message']['content'], end='', flush=True)




 
# Read the .csv file 
import pandas as pd
df = pd.read_csv("Table data.csv")
df.head()




#Convert to row in csv file to a string
def row_to_string(row):
    """
    Converts a DataFrame row to a string format with each column's heading name
    followed by an equal sign, then the value, and a comma.
    """
    # Ensure row is a Series, which is the case when accessing a DataFrame row
    if isinstance(row, pd.Series):
        # Use items() to iterate over (column, value) pairs
        return ', '.join(f"{col}={val}" for col, val in row.items()) + ','
    else:
        raise ValueError("Input must be a pandas Series.")

# Example usage
row_index = 0  # Change this to the index of the row you want to convert
row_string = row_to_string(df.iloc[row_index])
print(row_string)
  
  
def comment_content(row_string):
    prompt = "As a youtube expert, analyse this YouTube analytics data and provide commentary on the video performance:" + row_string

    stream = ollama.chat(
        model='llama2',
        messages=[{'role': 'user', 'content': prompt}],
        stream=True
    )
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)


comment_content(row_string)
