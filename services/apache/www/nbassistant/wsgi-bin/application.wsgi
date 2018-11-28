import sys
sys.path.insert(0, '/workdir')


from business import create_app

application = create_app()