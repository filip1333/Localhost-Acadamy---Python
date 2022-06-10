# Create function that returns elements of list that shold be on selected page
# list should be at least 100 objects long
# functiong takes as parameters: list, max elements on page, page_number
alphabet = [x for x in 'abcdefghijklmnoprstuwxyzabcdefghijklmnoprstuwxyzabcdefghijklmnoprstuwxyzabcdefghijklmnoprstuwxyzabcdefghijklmnoprstuwxyz']

def paginate(_list, max_elements_on_page, searh_page):
    a = searh_page*max_elements_on_page
    b = (searh_page+1)*max_elements_on_page
    list_of_elements_on_page = _list[a:b]
    return list_of_elements_on_page

print(paginate(alphabet, 5, 1))
