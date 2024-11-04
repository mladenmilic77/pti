from setuptools import setup, find_packages

setup(
    name='pti',  # Naziv vašeg paketa
    version='0.0.1',  # Verzija vašeg paketa
    description='Opis vašeg paketa',
    long_description=open('README.md').read(),  # Opis koji se uzima iz README.md fajla
    long_description_content_type='text/markdown',
    author='Mladen Milic',
    author_email='mladen180577@gmail.com',
    url='https://github.com/mladen180577/pti',  # URL ka vašem projektu
    packages=find_packages(),  # Automatski pronalazi sve pakete unutar projekta
    install_requires=[
        # Ovde dodajte zavisnosti vašeg paketa, npr:
        # 'requests>=2.0.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
