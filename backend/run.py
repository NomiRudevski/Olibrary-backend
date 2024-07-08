from .app import app
from flask_cors import CORS
from .routes.books import books_bp
from .routes.users import users_bp
from .routes.auth import auth_bp
from .routes.loans import loans_bp

# Enable CORS
CORS(app, supports_credentials=True)

@app.after_request
def after_request(response):
    # Print all response headers
    print("Response Headers:")
    for header, value in response.headers:
        print(f"{header}: {value}")

    # Modify the Set-Cookie header if it exists
    if 'Set-Cookie' in response.headers:
        cookies = response.headers.getlist('Set-Cookie')
        updated_cookies = []
        for cookie in cookies:
            if not cookie.endswith("Partitioned"):
                cookie += "; Partitioned"
            updated_cookies.append(cookie)
        
        # Remove the old Set-Cookie headers
        response.headers.pop('Set-Cookie')
        
        # Add the updated Set-Cookie headers
        for cookie in updated_cookies:
            response.headers.add('Set-Cookie', cookie)

    return response
# Register blueprints
app.register_blueprint(books_bp)
app.register_blueprint(users_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(loans_bp)

if __name__ == "__main__":
    app.run(debug=True)
