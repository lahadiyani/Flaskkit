from setuptools import setup, find_packages

setup(
    name="flaskkits-boilerplate",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask",
        "Flask-SQLAlchemy",
        "pymysql",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "flaskkit=flaskkit.cli:main",
        ],
    },
)
