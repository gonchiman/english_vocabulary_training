from flask import Flask, render_template, request

from src.constants.word_types import RegistrationTypes
from src.repositories.children_repository import ChildrenRepository
from src.repositories.parents_repository import ParentRepository


app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html',
        page_title='English Vocabulary Training'
    )


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    selected_registration_type = request.form.get("registration_type", None)
    input_word = request.form.get("word")
    input_parent = request.form.get("parent", None)
    registration_result = ""

    if selected_registration_type == RegistrationTypes.PARENT:
        ParentRepository.insert([input_word])
        registration_result = "Success"
    elif selected_registration_type == RegistrationTypes.CHILD:
        if not input_parent:
            registration_result = "Failed"
        else:
            ChildrenRepository.insert([input_word, input_parent])
            registration_result = "Success"

    return render_template(
        'registration.html',
        page_title='Register Word',
        registration_result=registration_result
    )


if __name__ == '__main__':
    app.run(debug=True)