from setuptools import setup, find_packages

setup(
    name="twitter-data-analyzer",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "tweepy>=4.14.0",
        "duckdb>=0.10.0",
        "google-generativeai>=0.3.0",
        "typer>=0.9.0",
        "rich>=13.0.0",
        "python-dotenv>=1.0.0",
        "pydantic>=2.0.0",
        "pydantic-settings>=2.0.0",
    ],
    entry_points={
        "console_scripts": [
            "twitter-analyzer=twitter_analyzer.cli:app",
        ],
    },
    python_requires=">=3.9",
    author="",
    description="CLI tool to download and analyze Twitter data using DuckDB and Gemini",
    long_description=open("README.md").read() if __file__ else "",
    long_description_content_type="text/markdown",
)
