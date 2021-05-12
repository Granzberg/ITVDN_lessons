import shelve


def make_data(my_new_name, my_url):
    with shelve.open('data.txt', 'n') as db:
        db[my_new_name] = [my_url]
        db.close()
