from wtforms import Form


class FormBase(Form):
    def errors_str(self):
        error = ""
        for k, v in self.errors.items():
            error += v[0] + '\n'

        return error