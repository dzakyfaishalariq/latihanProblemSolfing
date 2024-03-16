# menghapus tanda (#) sesudah ini akan dihapus
def remove_url_anchor(url):
    url = url.split("#")
    return url[0]


print(remove_url_anchor("www.codewars.com#about"))
print(remove_url_anchor("www.codewars.com?page=1"))
