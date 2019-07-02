# Save requirements.txt
pip freeze > requirements.txt

# Run Server
waitress-serve --listen=*:8000 startup:application