
"""
Configuration for local and deploy environments
"""

class Config:
    def __init__(self, base_url):
        self.base_url = base_url

# Update each URL to your local and deploy URLs
development = Config('file:///home/user/Documents/testVault/public/')
deploy = Config('https://fugohan.github.io/testVault/')
