from flask import Flask, render_template, request

from src.constants.parts_of_speech import PartsOfSpeech
from src.constants.word_types import RegistrationTypes
from src.repositories.children_repository import ChildrenRepository
from src.repositories.parents_repository import ParentRepository
from src.services.word_registration_service import WordRegistrationService


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
        parents=ParentRepository.find_values_by_column("word"),
        registration_result_parents="Nothing registered yet.",
        registration_result_children="Nothing registered yet."
    )


@app.route('/parents_registration', methods=['GET', 'POST'])
def parents_registration():
    input_word = request.form.get("word")
    input_part_of_speech = request.form.get("part_of_speech", default=PartsOfSpeech.NOUN.value)
    registration_result_parents = ""

    WordRegistrationService.register_multiple_words_to_parents(input_word, input_part_of_speech)

    registered_words = ', '.join(input_word.replace(' ', '').split(','))
    registration_result_parents = f"Successfully registered words: {registered_words}"

    return render_template(
        'registration.html',
        page_title='Registration',
        parts_of_speech=PartsOfSpeech,
        parents=ParentRepository.find_values_by_column("word"),
        registration_result_parents=registration_result_parents,
        registration_result_children="Nothing registered yet."
    )


@app.route('/children_registration', methods=['GET', 'POST'])
def children_registration():
    input_word = request.form.get("word")
    input_parent = request.form.get("parent")
    registration_result_children = ""

    WordRegistrationService.register_multiple_words_to_children(input_word, input_parent)

    registered_words = ', '.join(input_word.replace(' ', '').split(','))
    registration_result_children = f"Successfully registered words: {registered_words}"

    return render_template(
        'registration.html',
        page_title='Registration',
        parts_of_speech=PartsOfSpeech,
        parents=ParentRepository.find_values_by_column("word"),
        registration_result_children=registration_result_children,
        registration_result_parents="Nothing registered yet."
    )


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    return render_template(
        'edit.html',
        page_title='Edit',
        parts_of_speech=PartsOfSpeech,
        parents=[parent["word"] for parent in ParentRepository.find_by_condition("part_of_speech", PartsOfSpeech.NOUN.value)],
        children=[]
    )
    

@app.route('/show_children_list', methods=['GET', 'POST'])
def show_children_list():
    selected_part_of_speech = request.form.get(
        "part_of_speech",
        default=PartsOfSpeech.NOUN.value
    )

    parents = [
        parent["word"]
        for parent in ParentRepository.find_by_condition(
            "part_of_speech",
            selected_part_of_speech
        )
    ]

    selected_parent = request.form.get("parent")

    if selected_parent not in parents:
        if parents:
            selected_parent = parents[0]
        else:
            selected_parent = None

    if selected_parent is None:
        children = []
    else:
        children = [
            child["word"]
            for child in ChildrenRepository.find_by_condition(
                "parent",
                selected_parent
            )
        ]

    return render_template(
        'edit.html',
        page_title='Edit',
        selected_part_of_speech=selected_part_of_speech,
        selected_parent=selected_parent,
        parts_of_speech=PartsOfSpeech,
        parents=parents,
        children=children
    )


if __name__ == '__main__':
    app.run(debug=True)