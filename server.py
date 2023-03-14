from app import app
from app.controllers import users  # acá estoy llamando el init


if __name__ == "__main__":
    app.run(debug=True)
