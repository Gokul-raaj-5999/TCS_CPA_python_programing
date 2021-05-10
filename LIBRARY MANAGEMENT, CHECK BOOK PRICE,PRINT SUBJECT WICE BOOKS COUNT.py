class Book:
  def __init__(self,bid,bn,sub,bprice):
      self.bookId = bid
      self.bookName = bn
      self.subject = sub
      self.bookPrice = bprice

class Library:
  def __init__(self,libn,bl):
      self.libraryName = libn
      self.bookList = bl

  def findSubjectWiseBooks(self):
    d={}
    for i in self.bookList:
      if i.subject in d:
        d[i.subject]=d[i.subject]+1
      else:
        d[i.subject]=1

    return d

  def checkBookCategoryByPrice(self,no):
    for i in self.bookList:
      if(i.bookId == no):
        if(i.bookPrice>=1000):
          return 'High Price'
        elif(i.bookPrice>=750 and i.bookPrice<1000):
          return 'Medium Price'
        elif(i.bookPrice>=500 and i.bookPrice<750):
          return 'Average Price'
        else:
          return 'Low Price'
      return None

if __name__=='__main__':
  n = int(input())
  book1 = []

  for i in range(n):
    bookId = int(input())
    bookName = input()
    subject = input()
    bookPrice = int(input())
    book1.append(Book(bookId,bookName,subject,bookPrice))
    print(book1)

  libobj = Library("Univeristy",book1)
  res1 = libobj.findSubjectWiseBooks()
  ninput = int(input())
  res2 = libobj.checkBookCategoryByPrice(ninput)
  for i,j in res1.items():
    print(i,j)
  print(res2)
