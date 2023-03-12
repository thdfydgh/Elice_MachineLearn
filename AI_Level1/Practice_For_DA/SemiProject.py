import csv
import json 

books = 'books.csv'
jsons = 'books.json'

#제목의 리스트를 리턴
def get_titles(books_csv):
    with open(books_csv) as books:
        reader = csv.reader(books, delimiter=',')
        # 함수를 완성하세요.
        get_title = lambda row: row[0]
        titles = map(get_title,reader )
        
        return list(titles)


#페이지 수가 250이 넘는 책들의 제목을 리스트로 리턴하는 함수
def get_titles_of_long_books(books_csv):
    with open(books_csv) as books:
        reader = csv.reader(books, delimiter=',')
        # 함수를 완성하세요.
        is_long = lambda row: int(row[3])>250
        get_title = lambda row: row[0]
        
        long_books = filter(is_long, reader)
        long_book_titles = map(get_title, long_books)
        
        return list(long_book_titles)

    
#책 데이터를 JSON 형식으로 변환하여 저장하는 함수
def books_to_json(src_file, dst_file):
    # 아래 함수를 완성하세요.
    books = []
    with open(src_file) as src:
        reader = csv.reader(src, delimiter=",")
        
        # 각 줄 별로 대응되는 book 딕셔너리를 만듭니다.
        for row in reader:
            # 책 정보를 저장하는 딕셔너리를 생성합니다.
            book = {
                    "title": row[0],
                    "author": row[1],
                    "genre": row[2],
                    "pages": int(row[3]),
                    "publisher": row[4]
                }
            books.append(book)
    
    with open(dst_file, 'w') as dst:
        # JSON 형식으로 dst_file에 저장(loads(), dumps())
        json_string = json.dumps(books)
        dst.write(json_string)

get_titles(books)
get_titles_of_long_books(books)
books_to_json(books, jsons)