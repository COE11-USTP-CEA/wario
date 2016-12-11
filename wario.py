
from github import Github

class Wario(object):

    def_outfile = "wario_result.txt"

    def __init__(self, username=None, password=None, outfile=None, outdir=None):
        self.github_instance = Github(username, password)        
        if outfile:
            self.outfile = outfile
        else:
            self.outfile = self.def_outfile

    def get_org_members(self, org=None):
        members = self.github_instance.get_organization(org).get_members()
        return members

    def get_org_repos(self, org=None):
        repos = self.github_instance.get_organization(org).get_repos()
        return repos
