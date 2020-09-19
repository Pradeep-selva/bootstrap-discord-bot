from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

setup( 
        name='bootstrap-discord-bot',
        version='1.0.7', 
        author='pradeep-selva', 
        author_email='pradeep.selva8833@gmail.com', 
        url='https://github.com/Pradeep-selva/bootstrap-discord-bot', 
        description='An opinionated discord.py bot code bootstrapper', 
        long_description=open("README.md").read(), 
        long_description_content_type="text/markdown", 
        license='MIT', 
        packages=find_packages(), 
        entry_points={ 
            'console_scripts': [ 
                'bootstrap-discord-bot = create_discord_bot.main:main'
            ] 
        }, 
        classifiers=( 
            "Programming Language :: Python :: 3",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8", 
            "License :: OSI Approved :: MIT License", 
            "Operating System :: OS Independent", 
        ), 
        keywords='discord.py cli-tool bootstrapper boilerplate genrator discord bot', 
        install_requires=requirements, 
        zip_safe=False
) 