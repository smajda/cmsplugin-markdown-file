from setuptools import setup

setup(
    name='cmsplugin-markdown-file',
    author='Jon Smajda',
    author_email='jon@smajda.com',
    version=__import__('cmsplugin_markdown_file').__version__,
    packages=['cmsplugin_markdown_file'],
    description='Django CMS plugin that pulls content from markdown files.',
    long_description=open('readme.markdown').read(),
    install_requires=[
        'markdown',
        'mdx-smartypants',
    ],
)
