from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, EmailField, SubmitField, DateField, RadioField, SelectField, \
    IntegerField, FloatField
from wtforms.validators import DataRequired, length, equal_to, ValidationError
from string import ascii_uppercase, ascii_lowercase, ascii_letters, digits, punctuation
from flask_wtf.file import FileField, FileSize, FileAllowed, FileRequired


class RegisterForm(FlaskForm):
    username = StringField("Enter username", validators=[DataRequired(message='Please enter your username')])
    email = EmailField("Enter email", validators=[DataRequired(message='Please enter your email')])
    password = PasswordField("Enter password",
                             validators=[DataRequired(message='Please enter your password'), length(min=8, max=64)])
    repeat_password = PasswordField("Repeat password", validators=[DataRequired(message='Please confirm your password'),
                                                                   equal_to("password",
                                                                            message="Passwords must match.")])
    birthday = DateField("Enter birthday", validators=[DataRequired(message='Please enter your birthday')])
    gender = RadioField("Choose gender", choices=[(0, "Male"), (1, "Female")],
                        validators=[DataRequired(message='Please choose your gender')])
    country = SelectField(
        "Choose country",
        choices=[
            ("us", "United States"),
            ("ca", "Canada"),
            ("gb", "United Kingdom"),
            ("au", "Australia"),
            ("de", "Germany"),
            ("fr", "France"),
            ("it", "Italy"),
            ("es", "Spain"),
            ("jp", "Japan"),
            ("cn", "China"),
            ("in", "India"),
            ("br", "Brazil"),
            ("mx", "Mexico"),
            ("ru", "Russia"),
            ("za", "South Africa"),
            ("ng", "Nigeria"),
            ("eg", "Egypt")
        ],
        validators=[DataRequired()])
    profile_image = FileField("Upload Profile Image",
                              validators=[FileSize(1024 * 1024), FileAllowed(["jpg", "png", "jpeg"])])
    submit = SubmitField("Sign Up")

    def validate_password(self, field):
        contains_uppercase = False
        contains_lowercase = False
        contains_digits = False
        contains_symbols = False

        for char in field.data:
            if char in ascii_uppercase:
                contains_uppercase = True
            if char in ascii_lowercase:
                contains_lowercase = True
            if char in digits:
                contains_digits = True
            if char in punctuation:
                contains_symbols = True

        if not contains_uppercase:
            raise ValidationError("Password must contain at least one uppercase letter")
        if not contains_lowercase:
            raise ValidationError("Password must contain at least one lowercase letter")
        if not contains_digits:
            raise ValidationError("Password must contain at least one digit (0-9)")
        if not contains_symbols:
            raise ValidationError("Password must contain at least one special character (e.g., !, @, #, etc.)")


class AddTourForm(FlaskForm):
    title = StringField("Tour Title", validators=[DataRequired(message="Please enter a title"), length(max=100)])
    country = SelectField(
        "Country",
        choices=[
            ('', 'Select a country'),
            ('AF', 'Afghanistan'),
            ('AL', 'Albania'),
            ('DZ', 'Algeria'),
            ('AR', 'Argentina'),
            ('AU', 'Australia'),
            ('AT', 'Austria'),
            ('BD', 'Bangladesh'),
            ('BE', 'Belgium'),
            ('BR', 'Brazil'),
            ('BG', 'Bulgaria'),
            ('CA', 'Canada'),
            ('CL', 'Chile'),
            ('CN', 'China'),
            ('CO', 'Colombia'),
            ('HR', 'Croatia'),
            ('CZ', 'Czech Republic'),
            ('DK', 'Denmark'),
            ('EG', 'Egypt'),
            ('EE', 'Estonia'),
            ('FI', 'Finland'),
            ('FR', 'France'),
            ('DE', 'Germany'),
            ('GR', 'Greece'),
            ('HU', 'Hungary'),
            ('IS', 'Iceland'),
            ('IN', 'India'),
            ('ID', 'Indonesia'),
            ('IR', 'Iran'),
            ('IQ', 'Iraq'),
            ('IE', 'Ireland'),
            ('IL', 'Israel'),
            ('IT', 'Italy'),
            ('JP', 'Japan'),
            ('JO', 'Jordan'),
            ('KZ', 'Kazakhstan'),
            ('KE', 'Kenya'),
            ('KR', 'South Korea'),
            ('KW', 'Kuwait'),
            ('LV', 'Latvia'),
            ('LB', 'Lebanon'),
            ('LT', 'Lithuania'),
            ('MY', 'Malaysia'),
            ('MX', 'Mexico'),
            ('MA', 'Morocco'),
            ('NL', 'Netherlands'),
            ('NZ', 'New Zealand'),
            ('NG', 'Nigeria'),
            ('NO', 'Norway'),
            ('PK', 'Pakistan'),
            ('PE', 'Peru'),
            ('PH', 'Philippines'),
            ('PL', 'Poland'),
            ('PT', 'Portugal'),
            ('QA', 'Qatar'),
            ('RO', 'Romania'),
            ('RU', 'Russia'),
            ('SA', 'Saudi Arabia'),
            ('RS', 'Serbia'),
            ('SG', 'Singapore'),
            ('SK', 'Slovakia'),
            ('SI', 'Slovenia'),
            ('ZA', 'South Africa'),
            ('ES', 'Spain'),
            ('SE', 'Sweden'),
            ('CH', 'Switzerland'),
            ('SY', 'Syria'),
            ('TH', 'Thailand'),
            ('TR', 'Turkey'),
            ('UA', 'Ukraine'),
            ('AE', 'United Arab Emirates'),
            ('GB', 'United Kingdom'),
            ('US', 'United States'),
            ('VN', 'Vietnam'),
            ('YE', 'Yemen'),
            ('ZW', 'Zimbabwe'),
        ],
        validators=[DataRequired(message="Please select a country")]
    )
    description = StringField("Description", validators=[DataRequired(message="Please enter a description")])
    price = FloatField("Current Price",
                         validators=[DataRequired(message="Please enter the price")])
    currency = SelectField(
        "Currency",
        choices=[
            ("USD", "USD"),
            ("EUR", "EUR"),
            ("AUD", "AUD"),
            ("GBP", "GBP"),
            ("JPY", "JPY")
        ],
        validators=[DataRequired(message="Please select a currency")]
    )
    image = FileField("Upload Image",
                      validators=[FileSize(1024 * 1024), FileAllowed(["jpg", "png", "jpeg"])])
    duration = StringField("Duration (e.g. 4 days)", validators=[DataRequired(message="Please enter duration")])
    submit = SubmitField("Add Tour")