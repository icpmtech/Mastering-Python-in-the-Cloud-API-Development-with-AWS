class LoaderDto:
    def __init__(self, path):
        self.path = path

    def get_template(self):
        return self.path
   