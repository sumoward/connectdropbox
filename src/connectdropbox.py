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
        access_token, user_id = flow.finish(code)
        print(access_token, user_id)
        #2VACX8KizYYAAAAAAAAAAc1_aQWJlzlbo2Y-bX3N4Zs45WyJcJuwDhdgLb6wzBYp 47045342
        client = dropbox.client.DropboxClient(access_token)
        print ('linked account: ', client.account_info())

if __name__ == "__main__":
    # Get your app key and secret from the Dropbox developer website
    app_key = 'zvgozr44fggmmn7'
    app_secret = 'a6po4mgso0xcs3l'
    cdb = Connectdropbox()
    cdb.auth_dropbox(app_key, app_secret)
