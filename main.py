import os
from datetime import datetime
from typing import List, Dict, Any, Optional
import psycopg2
from psycopg2.extras import RealDictCursor
from fastmcp import FastMCP

mcp = FastMCP('connection')
mcp.title= "Primer Mcp "

#Conección a la base de datos
def get_conection ():
    conn = psycopg2.connect(
        host = os.environ.get("DB_HOST"),
        port = os.environ.get("DB_PORT"),
        user= os.environ.get("DB_USER"),
        passoword= os. environ.get("DB_PASSWORD"),
        database = os.environ.get("DB_DATABASE"),
        cursor_factory = RealDictCursor
    )
    return conn
