import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

# kayıtlı env dosyasından gerekli url ve key 
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

# supabase clienti başlatılıyor
def get_supabase() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_KEY)
