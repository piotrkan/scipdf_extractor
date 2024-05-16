'''script for calling API'''
import os
import json
import argparse
from gradio_client import Client


def get_args() -> argparse.Namespace:
    """
    Argument parser.
    """
    parser = argparse.ArgumentParser(
        prog='API call for scipdf extractor',
        description='Provide a path to scientific paper (PDF) to extract entities'
    )
    parser.add_argument(
        "--data_dir",
        type=str,
        default='data',
        help="Path to dir where pdfs are present"
    )
    parser.add_argument(
        "--name",
        type=str,
        help="Name of the file to be used"
    )
    parser.add_argument(
        "--save_path",
        type=str,
        default='results',
        help="Path to save json output"
    )
    args = parser.parse_args()
    return args


def call_api(input_path: str) -> dict:
    """
    Function to initialize and call gradio api
    Args:
        input_path - path to input pdf for inference
    Outs:
        dict json
    """
    # initiate connection with the client
    client = Client("http://127.0.0.1:7860/")

    # run extraction
    result = client.predict(input_pdf=input_path, api_name="/predict")
    return result


def save_json(json_file: dict, save_dir: str, save_name: str) -> None:
    """
    Function to save json file from API endpoint
    Args:
        json_file - output of API endpoint, json file
        save_dir - string depicting pathway to saving directory
        save_name - string, depicting name under which file should be saved
    Outs:
        None, file is saved to specified pathway
    """
    # create dir if not present
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    # save
    json_pathway = os.path.join(save_dir, f'{save_name}.json')
    with open(json_pathway, 'w') as file:
        file.write(json.dumps(json_file))


def main():
    '''call api endpoint for inference and save output'''
    args = get_args()
    pdf_pathway = os.path.join(args.data_dir, f'{args.name}.pdf')
    json_output = call_api(pdf_pathway)
    save_json(json_output, args.save_path, args.name)
    print('Entities Extracted Successfully')


if __name__ == '__main__':
    main()