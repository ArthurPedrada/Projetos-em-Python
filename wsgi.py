from app import create_app, db
#from flask_migrate import upgrade

app = create_app()

# Rodar migrations automaticamente no deploy
# Adicionar variável RAILWAY_ENVIRONMENT=production para que o bloco de migrations seja executado somente no deploy.

# Cria tabelas automaticamente no deploy
# if os.getenv("RAILWAY_ENVIRONMENT"):  # variável definir no Railway
with app.app_context():
    db.create_all()
#   upgrade()  # aplica as migrations pendentes
       