from setuptools import setup, find_packages

setup(
    name='Automated_Question_Generator',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'nltk==3.6.3',
        'spacy==3.1.0',
        'scikit-learn==0.24.2',
        'flask==2.0.1',
        'pandas==1.2.5',
        'numpy==1.21.0',
        'pytest==6.2.4',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='An automated question generator using NLP techniques.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/Automated_Question_Generator',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
