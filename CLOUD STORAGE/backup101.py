import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(),file_to)
def main():
    access_token ="sl.BKZCfizkPmyPUjARrIY81osUfNRCsjRdTpUSyu3SzGo6SbVmG0KvoODHWM00UPArlvxJ5wFxfM57mIHiOf0bcJrWBH76S2NB0B1hP1smE5W0guKLZP8ig8CWF_ErnmXVd-uS9fHOGByU"           
    transferdata = TransferData(access_token)
    file_from = "test.txt"
    file_to = "/Dropbox/test.txt"
    transferdata.upload_file(file_from, file_to)
if __name__ == "__main__":
    main()    