from download_file import download_file_from_url,save_to_file
from text_extraction import read_file,count_words,count_letters



def convert_dict_to_list(dictionary):

   return [(k,v) for k,v in dictionary.items()]

def report(total_words,total_letters):
    print()
    print(f"{total_words} words found in the document")
    print()
    total_letters.sort(key= lambda x:x[1],reverse=True)
    for letter,counter in total_letters:
        print(f'The {letter} character was found {counter} times')


if __name__ == "__main__":
    gen = download_file_from_url()
    filename = 'download_file.txt'
    save_to_file(filename,gen)
    text = list(read_file(filename))

    total_words = count_words(text)
    total_letters = count_letters(text)
    list_of_dict_letters = convert_dict_to_list(total_letters)
    report(total_words,list_of_dict_letters)
    
