# This is only created for unit tests

from services.apache.business import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)