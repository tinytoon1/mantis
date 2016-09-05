
class Project:
    def __init__(self, name=None, status=1, inherit_global=False, view_state=1, description=None):
        self.name = name
        self.status = status
        self.inherit_global = inherit_global
        self.view_state = view_state
        self.description = description

    def __repr__(self):
        return "%s" % self.name

    def __eq__(self, other):
        return self.name == other.name

    def get_name(self):
        return self.name
