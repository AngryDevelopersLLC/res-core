from setuptools import setup
import os


def parse_requirements():
    path = os.path.join(os.path.dirname(__file__), "res", "core",
                        "requirements", "base.txt")
    reqs = []
    with open(path, "r") as fin:
        for r in fin.read().split("\n"):
            r = r.strip()
            if r.startswith("#") or not r:
                continue
            if r.startswith("git+"):
                print("Warning: git dependencies cannot be used in setuptools "
                      "(%s)" % r)
                continue
            if not r.startswith("-r"):
                reqs.append(r)
    return reqs


setup(
    name="res-core",
    description="RESystem common service package",
    version="1.0.0",
    license="Proprietary",
    author="Angry Developers",
    author_email="gmarkhor@gmail.com",
    url="http://dev.res-it.net/gerrit/#/q/project:res-service-core",
    download_url='http://dev.res-it.net/gerrit/#/q/project:res-service-core',
    packages=["res", "res.core"],
    install_requires=parse_requirements(),
    package_data={"": ["res/core/requirements/base.txt"]},
    classifiers=[
        "Development Status :: 5 - Stable",
        "Environment :: Console",
        "License :: Proprietary",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.4"
    ]
)