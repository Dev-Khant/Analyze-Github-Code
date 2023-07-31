from langchain.chat_models import ChatOpenAI

exclude_extensions = ["png", "jpg", "jpeg", "svg"] # exclude files with these extensions
no_decode_extensions = ["md", "html"] # No ASCII decoding

def summarize_code(llm_token, file_content):
    extension = file_content.path.split(".")[-1]
    if extension in exclude_extensions:
        return ""
    elif extension in no_decode_extensions:
        text = file_content.decoded_content.decode()
    else:
        text = file_content.decoded_content.decode("ASCII")
    
    return text

def response_repo(llm_token, summarize_list):
    pass
