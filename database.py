#%%
from adapter import Adapter
import json
import psycopg2
from psycopg2.extras import Json

database = Adapter()

#%%
def insert_hints_solution(id, hints, solution):
    pool = database.get_pool_connection()
    with pool.connection() as conn:
        try:
            with conn.cursor() as cur:
                query = """
                INSERT INTO practice_module (id, hints, solution) 
                VALUES (%s, %s, %s)"""
                
                cur.execute(query, (id, hints, json.dumps(solution)))
                conn.commit()
                cur.close()
        except Exception as e:
            print(f"Error inserting message: {e}")
            conn.rollback()

def get_hints_solution(id):
    pool = database.get_pool_connection()
    with pool.connection() as conn:
        result = None  # Ensure 'result' is always defined
        try:
            with conn.cursor() as cur:
                query = "SELECT hints, solution FROM practice_module WHERE id = %s;"
                cur.execute(query, (id,))
                result = cur.fetchone()
        except Exception as e:
            print(f"Error retrieving: {e}")
            conn.rollback()
        
        if result:
            return result[0], result[1]  # hints as list, solution as JSON
    return None
