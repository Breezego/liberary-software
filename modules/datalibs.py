from json import load, dump


class Get:
    def __init__(self):
        pass

    @staticmethod
    def book(isbn=None, title=None, authors=None):
        if (isbn is None) and (title is None) and (authors is None):
            return 0

        results = []

        with open("../data/books.json", "r") as file:
            books = load(file)

        if isbn:
            try:
                for book in books:
                    if isbn == book["isbn"]:
                        results.append(book)
                return results
            except KeyError:
                return 0

        elif title:
            try:
                for book in books:
                    if title.lower() == book["title"].lower():
                        results.append(book)
                        return results
            except KeyError:
                pass
            if len(results) < 10:
                for book in books:
                    for word in title.lower():
                        if word in book["title"].lower():
                            if book not in results:
                                results.append(book)
                if results:
                    return results
                else:
                    return 0

        elif authors:
            for book in books:
                for authors_ in book["authors"]:
                    if authors.lower() in authors_.lower():
                        results.append(book)
            return results

        if title and authors:
            for book in results:
                if authors in book["authors"]:
                    results.index(0, results.pop(book))

    @staticmethod
    def account(id_=None, name=None):
        if (id_ is None) and (name is None):
            return 0

        results = []

        with open("../data/accounts.json", "r") as file:
            accounts = load(file)

        if id_:
            try:
                for account in accounts:
                    if id_ == account["id"]:
                        results.append(account)
                return results
            except KeyError:
                return 0

        if name:
            print(name)
            try:
                for account in accounts:
                    if name == account["name"]:
                        results.append(account)
                return results
            except KeyError:
                pass
            if len(results) < 10:
                for account in accounts:
                    for n in account["name"]:
                        print(n, name)
                        if name == n:
                            results.append(account)
                    if results:
                        return results
                    else:
                        return 0


class Enter:

    def __init__(self):
        pass

    @staticmethod
    def add_book(data: dict):
        with open("../data/books.json", "r") as file:
            books = load(file)
            file.close()
        books.append(data)
        with open("../data/books.json", "w") as file:
            dump(books, file)

    @staticmethod
    def add_account(data: dict):
        with open("../data/accounts.json", "r") as file:
            books = load(file)
            file.close()
        books.append(data)
        with open("../data/accounts.json", "w") as file:
            dump(books, file)

    @staticmethod
    def edit_book(key, data):
        with open("../data/books.json", "r") as file:
            books = load(file)
            file.close()

        for book in books:
            if book["isbn"] == key:
                for d in data:
                    if d["cost"]:
                        book["cost"] = d["cost"]
                    if d["issues"]:
                        book["issues"] = d["issues"]
                break

        with open("../data/books.json", "w") as file:
            dump(books, file)

    @staticmethod
    def edit_accounts(key, data):
        with open("../data/accounts.json", "r") as file:
            accounts = load(file)
            file.close()

        for account in accounts:
            if account["key"] == key:
                for d in data:
                    if d["tally"]:
                        account["tally"] = d["tally"]
                    if d["issues"]:
                        account["issues"] = d["issues"]
                break

        with open("../data/accountss.json", "w") as file:
            dump(accounts, file)

    @staticmethod
    def log():
        pass





if __name__ == "__main__":
    pass
