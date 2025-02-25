from setuptools import setup


def readme():
    with open("README.md", "r") as fh:
        long_description = fh.read()
        return long_description


setup(
    name='gemini_cli_simulation_game',
    version='1',
    packages=['gemini_cli_simulation_game'],
    url='https://github.com/GlobalCreativeApkDev/gemini_cli_simulation_game',
    license='MIT',
    author='GlobalCreativeApkDev',
    author_email='globalcreativeapkdev2022@gmail.com',
    description='This package contains implementation of a simulation game on command-line interface with '
                'Google Gemini AI integrated into it.',
    long_description=readme(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ],
    entry_points={
        "console_scripts": [
            "gemini_cli_simulation_game=gemini_cli_simulation_game.gemini_cli_simulation_game:main",
        ]
    }
)