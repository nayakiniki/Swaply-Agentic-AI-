import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def get_supabase_client():
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("Missing Supabase credentials")
    return create_client(SUPABASE_URL, SUPABASE_KEY)



