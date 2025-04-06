from setuptools import setup

setup(
    name='countrygen',
    version='1.0.0',
    description='Country & Locale Configuration Generator',
    author='YourName',
    packages=['countrygen'],
    install_requires=[
        'pandas',
        'openpyxl'
    ],
    entry_points={
        'console_scripts': [
            'countrygen=countrygen.__main__:main'
        ]
    },
    python_requires='>=3.6'
)
