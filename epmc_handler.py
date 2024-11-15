import requests
import json
import os
import argparse

tools = [
    {
        'name': 'myFirstTool', #example for delly
        'query': 'DELLY AND variants'
    },
]

def fetch_and_save_data(tool_name, query_input, file_name):
    # Define the base URL with the input query
    base_url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
    
    # Parameters for the request
    params = {
        'query': query_input,
        'resultType': 'core',
        'format': 'json'
    }
    
    # Send the GET request
    response = requests.get(base_url, params=params)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve data. HTTP Status Code: {response.status_code}")
        return
    
    # Parse the JSON response
    new_data = response.json()
    

    # Save the updated JSON data back to the file
    with open(file_name, 'w') as file:
        json.dump(new_data, file, indent=4)
    
    print(f"Data for tool '{tool_name}' successfully retrieved and saved to {file_name}.")

def main():
    parser = argparse.ArgumentParser(description='Data retrieval and management script.')
    subparsers = parser.add_subparsers(dest='command', required=True)
    
    # Parser for get_tools
    parser_get_tools = subparsers.add_parser('get_tools', help='Retrieve and save tool data.')
    
    # Parser for show_tool_information
    parser_show_info = subparsers.add_parser('show_tool_information', help='Show information stored in a specific tool file.')
    parser_show_info.add_argument('tool_name', help='Name of the tool whose information to display.')
    
    args = parser.parse_args()
    if args.command == 'get_tools':
        get_tool_information()
    elif args.command == 'show_tool_information':
        show_tool_information(args.tool_name)

def show_tool_information(tool_name):
    # Check if a file named TOOLNAME.json exists
    file_name = f"{tool_name}.json"
    
    if os.path.exists(file_name):
        print(f"File {file_name} exists. Proceeding with operations...")
        # Dummy code: Here you can define operations you want to perform on the file
        # For example, you might read the file and output some data, modify it, etc.
        with open(file_name, 'r') as file:
            data = json.load(file)
            # Implement any processing or viewing code here
            print(f"{len(data['resultList']['result'])} entries") # Example of printing the content
    else:
        print(f"File {file_name} does not exist.")


def get_tool_information():
    for tool in tools:
        name = tool['name']
        query = tool['query']
        f_name = f"{name}.json"
        fetch_and_save_data(name, query, f_name)
        




if __name__ == '__main__':
    main()