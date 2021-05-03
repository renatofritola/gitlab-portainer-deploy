from setuptools import setup

setup(
    name="gitlab-portainer-deploy",
    version="0.1",
    packages=["deploy"],
    zip_safe=False,
    install_requires=[
        "requests",
        "typer",
        "yarl",
    ],
    entry_points="""
        [console_scripts]
        deploy=deploy.cli:app
    """
)
