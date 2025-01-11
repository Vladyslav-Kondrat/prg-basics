import webbrowser

def search_google_play():
    # Prompt user for the program name
    program_name = input("Enter the name of the program you want to search for: ")

    # Construct the Google Play search URL
    base_url = "https://play.google.com/store/search?q="
    search_url = f"{base_url}{program_name.replace(' ', '+')}"

    # Open the URL in the default web browser
    print(f"Searching for '{program_name}' on Google Play...")
    webbrowser.open(search_url)

# Run the function
if __name__ == "__main__":
    search_google_play()