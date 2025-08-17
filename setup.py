from setuptools import setup, find_packages

setup(
    name="flaskkits-boilerplate",
    version="0.1.0",
    summary="Starter kit Flask modern dengan struktur rapi, integrasi Tailwind CSS, dan perintah CLI sederhana.",
    home_page="https://github.com/lahadiyani/flaskkit",
    author="Hadiani",
    author_email="lahadiyani@gmail.com",
    license="MIT",
    
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