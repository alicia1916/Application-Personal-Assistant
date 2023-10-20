from setuptools import setup

setup(
    name="Application-Personal-Assistant",
    version="1",
    description="Address book and notebook",
    url="https://github.com/alicia1916/Application-Personal-Assistant.git",
    author="group_2",
    author_email="alicja.barylski@gmail.com",
    license="MIT",
    packages=["Gotowy-szkielet-mozna-wklejac-swoje-kody"],
    install_requires=["python-Levenshtein"],
    entry_points={
        "console_scripts": ["assistant = application_personal_assistant.main:main"]
    },
)
