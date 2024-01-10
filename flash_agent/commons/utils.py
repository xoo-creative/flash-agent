import pkg_resources
from flash.commons.prompt import Prompt

import logging


def load_text(path: str) -> str:
    """
    Load the text content from a file.

    Args:
        path (str): The path to the file.

    Returns:
        str: The content of the file.
    """
    logging.info(f"Reading from path {path}")
    with open(path, "r") as fp:
        return fp.read()
    
def load_prompt(prompt: Prompt) -> str:

    prompt_path = pkg_resources.resource_filename(package_or_requirement="flash", 
                                                  resource_name=f"prompts/{prompt.value}.txt")

    return load_text(prompt_path)


def escape_markdown(content: str) -> str:
    """
    Returns format-safe markdown str that can be passed into the taipy.Gui.Markdown function.
    """
    to_replace = {
        ">" : "\>",
        # "}" : "\}"
    }

    for old, new in to_replace.items():
        content = content.replace(old, new)
    
    return content


def _write_flash(content: str, path: str) -> str:

    """
    Writes `content` to a file in subfolder `/<project_root>/flash/{path}` 
    """

    flash_folder_path = pkg_resources.resource_filename("flash", "")

    file_path = f"{flash_folder_path}/{path}"

    logging.info(f"Writing content to {file_path}")

    with open(file_path, "w") as fp:
        fp.write(content)

    
