from flask import Flask, render_template, request

from src.constants.parts_of_speech import PartsOfSpeech
from src.constants.word_types import RegistrationTypes
from src.repositories.children_repository import ChildrenRepository
from src.repositories.parents_repository import ParentRepository


app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html',
        page_title='Home'
    )


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    return render_template(
        'registration.html',
        page_title='Registration',
        parts_of_speech=PartsOfSpeech,
        registration_result_parents="",
        registration_result_children=""
    )


@app.route('/parents_registration', methods=['GET', 'POST'])
def parents_registration():
    input_word = request.form.get("word")
    input_part_of_speech = request.form.get("part_of_speech", default=PartsOfSpeech.NOUN.value)
    registration_result_parents = ""

    ParentRepository.insert([input_word, input_part_of_speech])
    registration_result_parents = "Success"

    return render_template(
        'registration.html',
        page_title='Parents Registration',
        registration_result_parents=registration_result_parents,
        parts_of_speech=PartsOfSpeech
    )


if __name__ == '__main__':
    app.run(debug=True)