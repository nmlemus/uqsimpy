

class CreateModel(object):

    def __init__(self, st):
        self.st = st

        self.st.title("Create Model")

        with self.st.expander("Help"):
            self.st.markdown('The UQSim hierarchy start with the model creation')