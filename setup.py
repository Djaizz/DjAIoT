import json
from setuptools import find_namespace_packages, setup
from types import SimpleNamespace


metadata = SimpleNamespace(**json.load(open('src/djai/metadata.json')))


doc_requirements = open('requirements-doc.txt').readlines()
lint_requirements = open('requirements-lint.txt').readlines()
pkg_requirements = open('requirements-pkg.txt').readlines()


# setuptools.readthedocs.io/en/latest/references/keywords.html
setup(
    name=metadata.PACKAGE,
    version=metadata.VERSION,
    description=metadata.DESCRIPTION,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author=metadata.AUTHOR,
    author_email=metadata.AUTHOR_EMAIL,
    maintainer=metadata.AUTHOR,
    maintainer_email=metadata.AUTHOR_EMAIL,
    url=metadata.URL,
    download_url=metadata.DOWNLOAD_URL,
    packages=find_namespace_packages(where='src', exclude=(), include=['*']),
    py_modules=[],
    scripts=['src/djai/util/cli/djai',
             'src/djai/util/cli/aws-eb/djai-aws'],
    classifiers=metadata.CLASSIFIERS,
    license='MIT',
    keywords=metadata.KEYWORDS,
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=open('src/requirements.txt').readlines(),
    entry_points={},
    extras_require={
        'all': [],

        'doc': doc_requirements,
        'lint': lint_requirements,
        'pkg': pkg_requirements,
        'dev': doc_requirements + lint_requirements + pkg_requirements
    },
    python_requires='>= 3.8',
    setup_requires=[],
    namespace_packages=[]
)
