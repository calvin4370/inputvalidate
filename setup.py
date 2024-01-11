from setuptools import setup, find_packages

setup(
    packages=['src/inputvalidate']
)

'''Below was the setup.cfg'''
# [metadata]
# name = inputvalidate
# version = 0.1.0
# author = Calvin Chan
# author_email = calvinchan4370z@gmail.com
# description = A Python Library with various functions to validate user input
# long_description = file: README.md
# long_description_content_type = text/markdown
# url = https://github.com/calvin4370/inputvalidate
# project_urls =
#     Bug Tracker = https://github.com/calvin4370/inputvalidate/issues
# classifiers =
#     Programming Language :: Python :: 3
#     License :: OSI Approved :: MIT License
#     Operating System :: OS Independent

# [options]
# packages = find: # OR `find_namespace:` if you want to use namespaces

# [options.packages.find]  # (always `find` even if `find_namespace:` was used before)
# # This section is optional as well as each of the following options:
# where=src  # . by default