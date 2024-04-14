from bs4 import BeautifulSoup
import os

def generate_url(current_number):
    return f'_ HackerGuide{current_number}.html'

def process_html_file(input_path, output_path, current_number):
    with open(input_path, 'r') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')

    for link in soup.find_all('a', href=True):
        link_text = link.get_text()
        if 'Click here to continue to' in link_text or 'Click to continue to' in link_text:
            new_url = generate_url(current_number)
            link['href'] = new_url

    with open(output_path, 'w') as file:
        file.write(str(soup))

def main():
    input_directory = 'C:/Users/Matt/Desktop/hackerguidetest'
    output_directory = 'C:/Users/Matt/Desktop/hackerguideoutput'
    current_number = 1
    for filename in sorted(os.listdir(input_directory)):
        if filename.startswith('_ HackerGuide') and filename.endswith('.html'):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)
            process_html_file(input_path, output_path, current_number)
            current_number += 1

if __name__ == '__main__':
    main()