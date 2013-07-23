"""
Dropbox file that can access your dropbox folder,
as well as download and upload files to dropbox
"""
# Include the Dropbox SDK
import dropbox
from pip.backwardcompat import raw_input


class Connectdropbox:

# Get your app key and secret from the Dropbox developer website
    app_key = 'zvgozr44fggmmn7'
    app_secret = 'a6po4mgso0xcs3l'

    def auth_dropbox(self, app_key, app_secret):

        flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
        print(flow)
        authorize_url = flow.start()
        # Have the user sign in and authorize this token
        print ('1. Go to: ' + authorize_url)
        print ('2. Click "Allow" (you might have to log in first)')
        print ('3. Copy the authorization code.')
        code = raw_input("Enter the authorization code here: ").strip()
        print(code)
        self.access_token, self.user_id = flow.finish(code)
        print(self.access_token, self.user_id)
        #2VACX8KizYYAAAAAAAAAAc1_aQWJlzlbo2Y-bX3N4Zs45WyJcJuwDhdgLb6wzBYp 47045342
        #self.client = dropbox.client.DropboxClient(self.access_token)
        #print ('linked account: ', self.client.account_info())

    def upload_to_db(self):
        self.connect()
        print ('linked account: ', self.client.account_info())
        f = open('workingdraft.txt', 'rb')
        print('here')
        response = self.client.put_file('/magnum-opus.txt', f)
        print ("uploaded:", response)

    def download_from_db(self):
        self.connect()
        f, metadata = self.client.get_file_and_metadata('/magnum-opus.txt')
        out = open('magnum-opus.txt', 'wb')
        out.write(f.read())
        out.close()
        print (metadata)

    def get_data(self):
        self.connect()
        print ('linked account: ', self.client.account_info())
        folder_metadata = self.client.metadata('/')
        print ("metadata:", folder_metadata)

    def connect(self):
        self.access_token = 'dXlCga7-8fYAAAAAAAAAAZNXpmVWVwoECHc_sHNLlWnrw0mB7HLWulTOzp-VJRsW'
        print(self.access_token)
        self.client = dropbox.client.DropboxClient(self.access_token)

if __name__ == "__main__":
    # Get your app key and secret from the Dropbox developer website
    app_key = 'zvgozr44fggmmn7'
    app_secret = 'a6po4mgso0xcs3l'
    cdb = Connectdropbox()
    #cdb.auth_dropbox(app_key, app_secret)
    #cdb.upload_to_db()
    #cdb.get_data()
    cdb.download_from_db()
