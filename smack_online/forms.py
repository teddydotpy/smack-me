from django import forms
from django.forms import ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Submit, Row

class SmackForm(forms.Form):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Row(
                    HTML(
                    """
                        <a href={% url "smack:forgot" %} class='btn btn-success col-6'>
                            Forgot
                        </a>
                    """,
                    ),
                    HTML(
                    """
                        <a href={% url "smack:click" %} class='btn btn-warning col-6'>
                            Click Me
                        </a>
                    """,
                    ),
                    Submit('submit', 'Smack', css_class='col-6'),
                    css_class='justify-content-center'
                ),
        )
        