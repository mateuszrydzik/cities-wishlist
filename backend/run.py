from api.app import create_app

if __name__ == '__main__':
    app = create_app('testing')
    app.run(debug=True, host="0.0.0.0")
