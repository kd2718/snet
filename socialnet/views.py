from allaccess.views import OAuthCallback

#User allacess callbacks to define what I need to do.
class NewCallback(OAuthCallback):
    #"Override OAuthCallback.get_login_redirect"
    
    def get_login_redirect(self, provider, user, access, new=False):
        "Return url to redirect authenticated users."
        return '/chekcmeout/'
        #return settings.LOGIN_REDIRECT_URL'

def profile(request):
	pass