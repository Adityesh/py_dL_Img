import urllib.request


url = input("Enter the url of the image to be downloaded: ")


def dlImg(url,path_name):
    
    file_name = input("Enter the name to be saved as : ")
    full_path = path_name + file_name + ".jpg"
    urllib.request.urlretrieve(url,full_path)


dlImg(url,'images/')