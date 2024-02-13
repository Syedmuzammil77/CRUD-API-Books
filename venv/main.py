from flask import Flask, jsonify, request

app = Flask(__name__)

books=[
    {"id":1, "title":"book 1", "author":"author 1"},
    {"id":2, "title":"book 2", "author":"author 2"},
    {"id":3, "title":"book 3", "author":"author 3"},

]

#get all books
@app.route('/books', methods=['GET'])
def get_books():
    return books

#get a specific book by id
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id']==book_id:
            return book
        
    return {'error':'Book not found'}

#creat a book
@app.route('/books', methods=['POST'])
def create_book():
    new_book={'id':len(books)+1, 'title':request.json['title'], 'author':request.json['author']}
    books.append(new_book)
    return new_book

#update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def upadte_book(book_id):
    for book in books:
        if book['id']==book_id:
            book['title']=request.json['title']
            book['author']=request.json['author']
            return book
    return {'error':'Book not found'}

#delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id']==book_id:
            books.remove(book)
            return {"data":"Book Deleted Successfully"}
        
    return {'error':'Book not found'}

#run app
if __name__=='__main__':
    app.run(debug=True)