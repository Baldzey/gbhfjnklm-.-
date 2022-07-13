import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BLTd9HzRAM1fNtQxwc7ueKGeVps95PmyXwVBhwSt2MvzRSr6MWe20OpWMCt5xJxfy_niIgHsXDznDnTKXrEPjGgz3ro6rblw0zx4XW3HaOpIxQaZtoDC8jyQQ_p2y-r6F0M316nndF2a'
    transferData = TransferData(access_token)

    file_from = input("Enter path to transfer: -")
    file_to = input("Enter full path to upload: - ")  

    transferData.upload_file(file_from, file_to)
    print("Your file has been moved")


main()