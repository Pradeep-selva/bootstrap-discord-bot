from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

long_description = 'A python cli-tool to generate a boilerplate folder structure for your discord.py bot code'
setup( 
        name='create-discordpy-bot',
        version='1.0.0', 
        author='pradeep-selva', 
        author_email='pradeep.selva8833@gmail.com', 
        url='https://github.com/Pradeep-selva/create-discord-bot', 
        description='An opinionated discord.py bot code bootstrapper', 
        long_description= long_description, 
        long_description_content_type="text/markdown", 
        license='MIT', 
        packages=find_packages(), 
        entry_points={ 
            'console_scripts': [ 
                'create-discordpy-bot = create_discord_bot.main:main'
            ] 
        }, 
        classifiers=( 
            "Programming Language :: Python :: 3", 
            "License :: OSI Approved :: MIT License", 
            "Operating System :: OS Independent", 
        ), 
        keywords='discord.py cli-tool bootstrapper boilerplate genrator discord bot', 
        install_requires=requirements, 
        zip_safe=False
) 