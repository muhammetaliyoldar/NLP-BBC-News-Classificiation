import nltk
import os

def download_nltk_resources():
    """Download all NLTK resources required for the application."""
    print("Downloading NLTK resources...")
    
    # Create user's nltk_data directory if it doesn't exist
    nltk_data_dir = os.path.join(os.path.expanduser('~'), 'nltk_data')
    os.makedirs(nltk_data_dir, exist_ok=True)
    
    # Download required resources
    resources = [
        'punkt',
        'stopwords',
        'wordnet'
    ]
    
    for resource in resources:
        print(f"Downloading {resource}...")
        nltk.download(resource, download_dir=nltk_data_dir, quiet=False)
    
    # Make sure the punkt tokenizer is available
    punkt_dir = os.path.join(nltk_data_dir, 'tokenizers', 'punkt')
    if os.path.exists(punkt_dir):
        print("Punkt tokenizer files found at:", punkt_dir)
    else:
        print("WARNING: Punkt tokenizer files not found in expected location")
        print("Trying alternate download method...")
        nltk.download('punkt', download_dir=nltk_data_dir, quiet=False)
    
    print("NLTK resources downloaded.")

if __name__ == "__main__":
    download_nltk_resources() 