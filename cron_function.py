from neon_connector.neon_connector import NeonConnector
from dotenv import load_dotenv
import os
import argparse

def main():
    # Load environment variables from .env file
    load_dotenv()
    connection_string = os.getenv('NEON_DATABASE_URL')

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Execute a function from NeonConnector")
    parser.add_argument('--name', type=str, required=True, help='The name of the function to execute')
    parser.add_argument('--args', nargs='*', default=[], help='The arguments for the function')

    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Create an instance of NeonConnector
    nc = NeonConnector(connection_string)
    
    # Execute the specified function with the provided arguments
    function_name = args.name
    function_args = args.args

    # Call the function on the NeonConnector instance
    nc.execute_function(function_name, function_args)
    
if __name__ == "__main__":
    main()
