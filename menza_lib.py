import requests

def save_webpage_to_html(url, filename):
    """
    Save the content of a webpage to an HTML file.

    Parameters:
    - url (str): The URL of the webpage.
    - filename (str): The name of the file to save the content to.

    Returns:
    - bool: True if the operation was successful, False otherwise.
    """
    try:
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            return True
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False