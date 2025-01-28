from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for flashing messages

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        username = request.form.get("username")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        gender = request.form.get("gender")

        # Validation
        if not full_name or not username or not email or not phone or not password or not confirm_password or not gender:
            flash("All fields are required!")
            return redirect(url_for("register"))
        if len(password) < 6:
            flash("Password must be at least 6 characters long!")
            return redirect(url_for("register"))
        if password != confirm_password:
            flash("Passwords do not match!")
            return redirect(url_for("register"))
        if len(phone) != 10 or not phone.isdigit():
            flash("Enter a valid 10-digit phone number!")
            return redirect(url_for("register"))

        # Success
        flash("Registration Successful!")
        return redirect(url_for("register"))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
