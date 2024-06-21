from setuptools import setup, find_packages

setup(
    name="md2docx",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "python-docx",
        "markdown2",
        "beautifulsoup4"
    ],
    entry_points={
        'console_scripts': [
            'md2docx=md2docx.converter:convert_markdown_to_docx',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A library to convert Markdown files to DOCX format",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/md2docx",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
